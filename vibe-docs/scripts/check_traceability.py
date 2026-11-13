#!/usr/bin/env python3
"""
check_traceability.py — Checagem automática da regra "não invente".

Monta o registro de IDs que o PROJECT.md define (BR-xx, UC-xx, ENT-xx, FUN-xx,
OBJ-xx, PRINC-xx...) e varre os demais documentos atrás de IDs citados que não
existem no Blueprint — sinal de invenção ou de divergência entre um documento
derivado e o Blueprint atual.

Marcadores do template ainda em PENDENTE ("- BR-01: PENDENTE") não contam como
ID definido. IDs locais de documento (US/TASK/API) nascem fora do Blueprint por
definição e são listados à parte.

Uso:
    python check_traceability.py <pasta-do-projeto>
"""

import sys
from collections import defaultdict
from pathlib import Path

# Garante o import de _common mesmo em modo isolado (python -I), que tira a
# pasta do script do sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    DOCUMENT_LOCAL_PREFIXES,
    PROJECT_FILENAME,
    STANDARD_PREFIXES,
    blueprint_ids,
    extract_ids,
    prefix_of,
    project_files,
    read,
)


def main():
    if len(sys.argv) != 2:
        print("Uso: python check_traceability.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    files = project_files(project_dir)
    if PROJECT_FILENAME not in files:
        print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}. Sem o Blueprint não há como saber quais IDs são válidos.")
        sys.exit(1)

    valid_ids = blueprint_ids(read(files[PROJECT_FILENAME]))
    nonstandard = {i for i in valid_ids if prefix_of(i) not in STANDARD_PREFIXES}
    others = {n: p for n, p in files.items() if n != PROJECT_FILENAME}

    unknown = defaultdict(list)  # id -> [(documento, linha)]
    local_ids, referenced = set(), set()

    for name in sorted(others):
        for i, line in enumerate(read(others[name]).splitlines(), start=1):
            for found in extract_ids(line):
                if prefix_of(found) in DOCUMENT_LOCAL_PREFIXES:
                    local_ids.add(found)
                elif found in valid_ids:
                    referenced.add(found)
                else:
                    unknown[found].append((name, i))

    print(f"Blueprint: {files[PROJECT_FILENAME]}")
    print(f"IDs definidos no Blueprint: {len(valid_ids)}")
    print(f"Documentos derivados analisados: {len(others)}")

    if not valid_ids:
        print("\n⚠️  Nenhum ID definido no Blueprint (só marcadores PENDENTE ou nenhum ID no padrão PREFIXO-NUMERO).")

    if nonstandard:
        print(f"\n🟡 {len(nonstandard)} ID(s) com prefixo fora do padrão no Blueprint: {', '.join(sorted(nonstandard))}")
        print("   Prefixos oficiais: " + ", ".join(sorted(STANDARD_PREFIXES)))
        print("   (um princípio é PRINC-01, não P-01; se algum item não for ID de verdade, ignore)")

    print()
    if unknown:
        print(f"🔴 {len(unknown)} ID(s) citados em documentos derivados mas não definidos no Blueprint:\n")
        for found, locations in sorted(unknown.items()):
            print(f"  {found}")
            for name, line_num in locations:
                print(f"    - {name} (linha {line_num})")
        print("\n→ Cada um é uma invenção a corrigir ou uma decisão real que ainda não voltou ao PROJECT.md.")
    else:
        print("🟢 Nenhum ID órfão — todo ID citado nos documentos derivados está definido no Blueprint.")

    if local_ids:
        print(f"\nℹ️  {len(local_ids)} ID(s) locais de documento (US/TASK/API), que nascem fora do Blueprint por definição.")

    unused = valid_ids - referenced
    if unused and others:
        print(f"\nℹ️  {len(unused)} ID(s) do Blueprint ainda não citados em nenhum documento derivado (informativo): {', '.join(sorted(unused))}")

    sys.exit(1 if unknown else 0)


if __name__ == "__main__":
    main()
