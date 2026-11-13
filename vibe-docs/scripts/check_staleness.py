#!/usr/bin/env python3
"""
check_staleness.py — Detecta documentos desatualizados em relação ao Blueprint.

Cada documento derivado registra, no frontmatter, a versão do PROJECT.md contra
a qual foi conferido. A versão do Blueprint só sobe quando uma decisão muda ou
é acrescentada (ver "Quando a versão sobe" em references/blueprint/schema.md),
então um documento atrás da versão atual pode de fato estar sem uma decisão.

Ficam fora da comparação os arquivos mantidos pelo agente de implementação
(STATE.md, LEARNINGS.md), que não têm versão, e o CLAUDE.md, que não leva
frontmatter e por isso é sempre apontado para revisão manual.

Uso:
    python check_staleness.py <pasta-do-projeto>

Saída: código 0 se tudo estiver em dia, 1 se houver documento desatualizado.
"""

import re
import sys
from pathlib import Path

# Garante o import de _common mesmo em modo isolado (python -I), que tira a
# pasta do script do sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import AGENT_MAINTAINED, CLAUDE_MD, PROJECT_FILENAME, project_files, read

VERSION_PATTERN = re.compile(r'^\s*version\s*:\s*["\']?([^"\'\n]+?)["\']?\s*$', re.MULTILINE)


def parse_version(text):
    """Campo version do frontmatter (primeiras 15 linhas)."""
    head = "\n".join(text.splitlines()[:15])
    m = VERSION_PATTERN.search(head)
    return m.group(1).strip() if m else None


def version_tuple(v):
    """'1.10' -> (1, 10), para comparar numericamente quando possível."""
    try:
        return tuple(int(x) for x in re.split(r"[.\-]", v))
    except (ValueError, AttributeError):
        return None


def main():
    if len(sys.argv) != 2:
        print("Uso: python check_staleness.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    files = project_files(project_dir) if project_dir.is_dir() else {}
    if PROJECT_FILENAME not in files:
        print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}.")
        sys.exit(1)

    current = parse_version(read(files[PROJECT_FILENAME]))
    if not current:
        print(f"❌ {PROJECT_FILENAME} não declara 'version' no frontmatter — sem isso não há como comparar.")
        sys.exit(1)

    print(f"📁 Projeto: {project_dir}")
    print(f"Versão atual do Blueprint: {current}\n")

    stale, ok, unknown = [], [], []
    cur_t = version_tuple(current)

    for name in sorted(files):
        if name == PROJECT_FILENAME or name in AGENT_MAINTAINED:
            continue
        if name == CLAUDE_MD:
            unknown.append((name, "não leva versão — reconfira à mão sempre que o Blueprint mudar"))
            continue

        v = parse_version(read(files[name]))
        if not v:
            unknown.append((name, "não declara 'version' no frontmatter"))
        elif v == current:
            ok.append(name)
        else:
            v_t = version_tuple(v)
            if cur_t and v_t and v_t > cur_t:
                unknown.append((name, f"declara versão {v}, à frente do Blueprint ({current}) — o Blueprint deixou de ser atualizado?"))
            else:
                stale.append((name, v))

    if stale:
        print(f"🔴 {len(stale)} documento(s) atrás da versão atual:\n")
        for name, v in stale:
            print(f"  • {name} — conferido contra a versão {v}")
        print("\n→ Reconfira cada um contra as decisões que entraram desde então (seção 18 do Blueprint).")
        print("  Só suba a versão do documento depois de conferir o conteúdo — subir sem conferir esconde o problema.")

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
