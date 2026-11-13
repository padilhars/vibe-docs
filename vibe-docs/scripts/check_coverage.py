#!/usr/bin/env python3
"""
check_coverage.py — Detecta decisão do Blueprint que nunca chegou a um documento.

O check_staleness compara versões; este compara conteúdo. Ele existe para um
caso traiçoeiro: documento gerado ANTES de uma regra existir nunca a recebeu,
e nada acusa a ausência porque o documento, lido sozinho, parece completo.

Para cada BR-xx e PRINC-xx definido no Blueprint, verifica se o ID aparece nos
documentos onde deveria constar; e se toda funcionalidade do recorte do MVP
consta no MVP.md. A comparação é pelo ID inteiro: citar BR-100 não cobre BR-10.

Uso:
    python check_coverage.py <pasta-do-projeto>

Saída: código 0 se a cobertura estiver completa, 1 se houver ausência.
"""

import sys
from pathlib import Path

# Garante o import de _common mesmo em modo isolado (python -I), que tira a
# pasta do script do sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    PROJECT_FILENAME,
    blueprint_ids,
    extract_ids,
    field_value,
    prefix_of,
    project_files,
    read,
    section_body,
)

# prefixo -> [(documento, por que o ID precisa aparecer ali)]
COVERAGE_RULES = {
    "BR": [
        ("BUSINESS-RULES.md", "o documento consolida todas as regras de negócio"),
        ("TEST-STRATEGY.md", "toda regra precisa de cenário de teste ou de exclusão declarada"),
    ],
    "PRINC": [
        ("TEST-STRATEGY.md", "princípio sem teste é intenção, não garantia"),
        ("CLAUDE.md", "princípios ficam escritos no contrato do agente"),
    ],
}


def mvp_functionalities(blueprint_lines):
    """FUN-xx citadas no campo 'Recorte do MVP' da seção 4."""
    recorte = field_value(section_body(blueprint_lines, 4) or "", "Recorte do MVP")
    if not recorte:
        return set()
    return {i for i in extract_ids(recorte) if prefix_of(i) == "FUN"}


def main():
    if len(sys.argv) != 2:
        print("Uso: python check_coverage.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    files = project_files(project_dir) if project_dir.is_dir() else {}
    if PROJECT_FILENAME not in files:
        print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}.")
        sys.exit(1)

    blueprint = read(files[PROJECT_FILENAME])
    defined = blueprint_ids(blueprint)
    doc_ids = {n: extract_ids(read(p)) for n, p in files.items() if n != PROJECT_FILENAME}

    print(f"📁 Projeto: {project_dir}")
    gaps, skipped = [], set()

    for prefix, targets in COVERAGE_RULES.items():
        ids = {i for i in defined if prefix_of(i) == prefix}
        if not ids:
            continue
        print(f"{prefix}: {len(ids)} definido(s) no Blueprint")
        for doc, why in targets:
            if doc not in doc_ids:
                skipped.add(doc)
                continue
            missing = sorted(ids - doc_ids[doc])
            if missing:
                gaps.append((doc, why, missing))

    mvp_funs = mvp_functionalities(blueprint.splitlines())
    if mvp_funs and "MVP.md" in doc_ids:
        missing = sorted(mvp_funs - doc_ids["MVP.md"])
        if missing:
            gaps.append(("MVP.md", "funcionalidade listada no recorte do MVP da seção 4", missing))

    print()
    if gaps:
        total = sum(len(m) for _, _, m in gaps)
        print(f"🔴 {total} ID(s) sem prestação de contas:\n")
        for doc, why, missing in gaps:
            print(f"  {doc} — {why}")
            print(f"    faltando: {', '.join(missing)}")
        print("\n→ Cada ID acima não aparece no documento. Duas causas possíveis, e as duas pedem ação:")
        print("  1. O documento foi gerado antes de a decisão existir e nenhuma propagação o alcançou.")
        print("  2. A exclusão é deliberada (ex.: regra de fase futura) mas não foi declarada.")
        print("  No caso 2, cite o ID na seção de exclusões com a justificativa (no TEST-STRATEGY.md,")
        print('  a seção "O que NÃO testar") — exclusão silenciosa é indistinguível de esquecimento.')
    else:
        print("🟢 Cobertura completa — toda regra e princípio do Blueprint aparece onde deveria.")

    if skipped:
        print(f"\nℹ️  Não verificado (documento ainda não gerado): {', '.join(sorted(skipped))}")

    sys.exit(1 if gaps else 0)


if __name__ == "__main__":
    main()
