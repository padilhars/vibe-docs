#!/usr/bin/env python3
"""
check_coverage.py — Detecta decisão do Blueprint que nunca chegou a um documento.

O check_staleness compara versões; este compara conteúdo. Ele existe para um
caso específico e traiçoeiro: documento gerado ANTES de uma regra existir nunca
a recebeu, porque não existia quando a decisão foi tomada — e como a versão dele
vai sendo sincronizada a cada rodada, nada acusa a ausência.

Para cada BR-xx / FUN-xx / PRINC-xx do Blueprint, verifica se o ID aparece nos
documentos onde ele deveria obrigatoriamente constar.

Uso:
    python check_coverage.py <pasta-do-projeto>

Saída: código 0 se a cobertura estiver completa, 1 se houver ausência.
"""

import re
import sys
from pathlib import Path

PROJECT_FILENAME = "PROJECT.md"

# Onde cada tipo de ID precisa obrigatoriamente aparecer, quando o documento existir.
# (documento, descrição do porquê)
COVERAGE_RULES = {
    "BR": [
        ("BUSINESS-RULES.md", "documento consolida TODAS as regras de negócio"),
        ("TEST-STRATEGY.md", "toda regra precisa de cenário de teste que a verifique"),
    ],
    "PRINC": [
        ("TEST-STRATEGY.md", "princípio sem teste é intenção, não garantia"),
        ("CLAUDE.md", "princípios ficam inline no contrato do agente"),
    ],
}

ID_PATTERN = re.compile(r"\b([A-Z]{2,6}-\d{1,4})\b")

# Tokens técnicos que casam com o padrão de ID sem serem ID.
TECH_TOKENS = {
    "AES-256", "SHA-256", "SHA-1", "SHA-512", "HMAC-256", "RSA-2048",
    "UTF-8", "ISO-8601", "RFC-2119", "RFC-5545", "SPF-1", "BASE-64",
    "HTTP-2", "TLS-1", "OAUTH-2", "ARGON-2", "P-256",
}


def extract_ids(text, prefix=None):
    found = {i for i in ID_PATTERN.findall(text) if i not in TECH_TOKENS}
    if prefix:
        found = {i for i in found if i.split("-")[0] == prefix}
    return found


def mvp_functionalities(project_text):
    """Extrai as FUN-xx citadas no campo 'Recorte do MVP' da seção 4."""
    m = re.search(r"\*\*Recorte do MVP:\*\*(.+?)(?=\n##|\Z)", project_text, re.DOTALL)
    if not m:
        return set()
    return extract_ids(m.group(1), "FUN")


def main():
    if len(sys.argv) != 2:
        print("Uso: python check_coverage.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    project_md = project_dir / PROJECT_FILENAME
    if not project_md.exists():
        print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}.")
        sys.exit(1)

    blueprint = project_md.read_text(encoding="utf-8", errors="replace")
    present = {p.name: p.read_text(encoding="utf-8", errors="replace")
               for p in project_dir.glob("*.md") if p.name != PROJECT_FILENAME}

    print(f"📁 Projeto: {project_dir}")
    gaps = []
    skipped = []

    # Cobertura por prefixo
    for prefix, targets in COVERAGE_RULES.items():
        ids = extract_ids(blueprint, prefix)
        if not ids:
            continue
        print(f"{prefix}: {len(ids)} no Blueprint")
        for doc, why in targets:
            if doc not in present:
                skipped.append(f"{doc} (ainda não gerado)")
                continue
            missing = sorted(i for i in ids if i not in present[doc])
            if missing:
                gaps.append((doc, why, missing))

    # Funcionalidades do MVP precisam constar no MVP.md
    mvp_funs = mvp_functionalities(blueprint)
    if mvp_funs and "MVP.md" in present:
        missing = sorted(f for f in mvp_funs if f not in present["MVP.md"])
        if missing:
            gaps.append(("MVP.md", "funcionalidade listada no recorte do MVP da seção 4", missing))

    print()
    if gaps:
        total = sum(len(m) for _, _, m in gaps)
        print(f"🔴 {total} ID(s) sem prestação de contas:\n")
        for doc, why, missing in gaps:
            print(f"  {doc} — {why}")
            print(f"    faltando: {', '.join(missing)}")
        print("\n→ Cada ID acima não aparece em lugar nenhum do documento.")
        print("  Duas causas possíveis, e as duas exigem ação:")
        print("  1. O documento foi gerado antes da decisão existir e nenhuma cascata o alcançou.")
        print("  2. A exclusão é deliberada (ex.: regra de uma fase futura) mas não foi declarada.")
        print("  No caso 2, cite o ID na seção de exclusões do documento com a justificativa")
        print("  (em TEST-STRATEGY.md, a seção \"O que NÃO testar\") — exclusão silenciosa é")
        print("  indistinguível de esquecimento, tanto para quem lê quanto para este script.")
    else:
        print("🟢 Cobertura completa — toda regra e princípio do Blueprint aparece onde deveria.")

    if skipped:
        print(f"\nℹ️  Não verificado (documento ausente): {', '.join(sorted(set(skipped)))}")

    sys.exit(1 if gaps else 0)


if __name__ == "__main__":
    main()
