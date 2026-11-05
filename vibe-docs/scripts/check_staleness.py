#!/usr/bin/env python3
"""
check_staleness.py — Detecta documentos desatualizados em relação ao Blueprint.

Cada documento derivado registra, no frontmatter, a versão do PROJECT.md que
serviu de fonte. Quando o Blueprint evolui, quem foi gerado antes pode ter
ficado para trás sem que nada avise. Este script compara as duas versões e
aponta o que precisa ser regenerado ou revisado.

Uso:
    python check_staleness.py <pasta-do-projeto>

Saída: código 0 se tudo estiver em dia, 1 se houver documento desatualizado.
"""

import re
import sys
from pathlib import Path

PROJECT_FILENAME = "PROJECT.md"
VERSION_PATTERN = re.compile(r'^\s*version\s*:\s*["\']?([^"\'\n]+)["\']?\s*$', re.MULTILINE)

# CLAUDE.md não leva frontmatter por definição (ver references/documents/claude-md.md),
# então não tem versão a comparar — mas é o documento que o agente lê primeiro, o que
# torna a desatualização dele especialmente cara.
NO_FRONTMATTER = {"CLAUDE.md"}


def parse_version(text):
    """Extrai o campo version do frontmatter (primeiras ~15 linhas)."""
    head = "\n".join(text.splitlines()[:15])
    m = VERSION_PATTERN.search(head)
    return m.group(1).strip() if m else None


def version_tuple(v):
    """Converte '1.10' em (1, 10) para comparar numericamente quando possível."""
    try:
        return tuple(int(x) for x in re.split(r"[.\-]", v))
    except (ValueError, AttributeError):
        return None


def main():
    if len(sys.argv) != 2:
        print("Uso: python check_staleness.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    project_md = project_dir / PROJECT_FILENAME
    if not project_md.exists():
        print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}.")
        sys.exit(1)

    current = parse_version(project_md.read_text(encoding="utf-8", errors="replace"))
    if not current:
        print(f"❌ {PROJECT_FILENAME} não declara 'version' no frontmatter — sem isso não há como comparar.")
        sys.exit(1)

    print(f"📁 Projeto: {project_dir}")
    print(f"Versão atual do Blueprint: {current}\n")

    stale, ok, unknown = [], [], []
    cur_t = version_tuple(current)

    for doc in sorted(project_dir.glob("*.md")):
        if doc.name == PROJECT_FILENAME:
            continue

        if doc.name in NO_FRONTMATTER:
            unknown.append((doc.name, "sem frontmatter por definição — revise manualmente após qualquer mudança no Blueprint"))
            continue

        v = parse_version(doc.read_text(encoding="utf-8", errors="replace"))
        if not v:
            unknown.append((doc.name, "não declara 'version' no frontmatter"))
            continue

        if v == current:
            ok.append((doc.name, v))
            continue

        v_t = version_tuple(v)
        if cur_t and v_t and v_t > cur_t:
            unknown.append((doc.name, f"declara versão {v}, mais recente que o Blueprint ({current}) — verifique se o Blueprint deixou de ser atualizado"))
        else:
            stale.append((doc.name, v))

    if stale:
        print(f"🔴 {len(stale)} documento(s) desatualizado(s):\n")
        for name, v in stale:
            print(f"  • {name} — gerado da versão {v}")
        print("\n→ Regenere ou revise cada um. Ao regenerar, preserve o que ainda é válido")
        print("  e destaque o que mudou (ver references/documents/_shared-rules.md).")

    if unknown:
        print(f"\n🟡 {len(unknown)} documento(s) sem comparação possível:\n")
        for name, why in unknown:
            print(f"  • {name} — {why}")

    if ok:
        print(f"\n🟢 {len(ok)} documento(s) em dia com a versão {current}.")

    if not stale and not unknown and not ok:
        print("Nenhum documento derivado encontrado.")

    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
