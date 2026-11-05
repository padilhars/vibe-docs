#!/usr/bin/env python3
"""
check_traceability.py — Checagem automática da regra "não invente".

Lê o PROJECT.md de uma pasta de projeto para montar o registro de IDs
válidos (BR-xx, UC-xx, ENT-xx, FUN-xx, OBJ-xx, REQ-xx, US-xxx, API-xx...),
depois varre todos os outros documentos .md da pasta procurando por IDs
citados que NÃO existem no PROJECT.md — um sinal de possível invenção ou
de drift entre um documento derivado e o Blueprint atual.

Uso:
    python check_traceability.py <pasta-do-projeto>

Exemplo:
    python check_traceability.py projects/sistema-gestao-salas
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# IDs no formato PREFIXO-NUMERO, ex.: BR-04, UC-12, ENT-01, US-001, API-3.
# Aceita prefixo de 1 letra para conseguir detectar (e avisar sobre) IDs fora
# do padrão, como "P-01" em vez de "PRINC-01" — antes eles eram invisíveis.
ID_PATTERN = re.compile(r"\b([A-Z]{1,6}-\d{1,4})\b")

# Prefixos oficiais (ver references/documents/_shared-rules.md)
STANDARD_PREFIXES = {"OBJ", "FUN", "UC", "BR", "ENT", "REQ", "PRINC", "US", "TASK", "API"}

# Tokens técnicos que casam com o padrão PREFIXO-NUMERO sem serem ID de rastreabilidade.
# Sem esta lista, "AES-256" num documento de segurança vira ruído em toda execução.
TECH_TOKENS = {
    "AES-256", "SHA-256", "SHA-1", "SHA-512", "HMAC-256", "RSA-2048",
    "UTF-8", "ISO-8601", "RFC-2119", "RFC-5545", "SPF-1", "BASE-64",
    "HTTP-2", "TLS-1", "OAUTH-2", "ARGON-2", "P-256",
}

PROJECT_FILENAME = "PROJECT.md"

# Prefixos que legitimamente nascem em documentos derivados, não no Blueprint
# (ver references/documents/_shared-rules.md). Não são invenção; só precisam
# apontar para um ID de origem, o que este script não consegue verificar sozinho.
DOCUMENT_LOCAL_PREFIXES = {"US", "TASK", "API"}


def extract_ids(text: str):
    return {i for i in ID_PATTERN.findall(text) if i not in TECH_TOKENS}


def main():
    if len(sys.argv) != 2:
        print("Uso: python check_traceability.py <pasta-do-projeto>")
        print("Exemplo: python check_traceability.py projects/sistema-gestao-salas")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    project_md = project_dir / PROJECT_FILENAME
    if not project_md.exists():
        # Busca case-insensitive como fallback, caso o arquivo tenha sido salvo com outro nome de caixa.
        candidates = [p for p in project_dir.glob("*.md") if p.name.lower() == PROJECT_FILENAME.lower()]
        if candidates:
            project_md = candidates[0]
        else:
            print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}. Este script precisa do Blueprint consolidado para saber quais IDs são válidos.")
            sys.exit(1)

    valid_ids = extract_ids(project_md.read_text(encoding="utf-8", errors="replace"))

    nonstandard = {i for i in valid_ids if i.split("-")[0] not in STANDARD_PREFIXES}

    if not valid_ids:
        print(f"⚠️  Nenhum ID no formato PREFIXO-NUMERO foi encontrado em {project_md.name}. Verifique se o Blueprint usa o padrão de rastreabilidade (ex.: BR-01, UC-02) antes de confiar neste relatório.")

    other_files = sorted(p for p in project_dir.rglob("*.md") if p.resolve() != project_md.resolve())

    unknown_by_id = defaultdict(list)  # id -> [(arquivo, linha)]
    local_ids = set()  # IDs que nascem legitimamente em documentos derivados
    referenced_valid_ids = set()

    for md_file in other_files:
        try:
            lines = md_file.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception as e:
            print(f"⚠️  Não foi possível ler {md_file}: {e}", file=sys.stderr)
            continue

        for i, line in enumerate(lines, start=1):
            for found_id in extract_ids(line):
                if found_id in valid_ids:
                    referenced_valid_ids.add(found_id)
                elif found_id.split("-")[0] in DOCUMENT_LOCAL_PREFIXES:
                    local_ids.add(found_id)
                else:
                    unknown_by_id[found_id].append((md_file, i))

    print(f"Blueprint: {project_md}")
    print(f"IDs válidos registrados: {len(valid_ids)}")

    if nonstandard:
        print(f"\n🟡 {len(nonstandard)} ID(s) com prefixo fora do padrão no Blueprint:")
        print("   " + ", ".join(sorted(nonstandard)))
        print("   Prefixos oficiais: " + ", ".join(sorted(STANDARD_PREFIXES)))
        print("   (ex.: um princípio deve ser PRINC-01, não P-01. Prefixo não padronizado dificulta rastrear entre projetos —")
        print("    e se algum item acima não for um ID de verdade, é falso positivo da detecção e pode ser ignorado.)")
    print(f"Documentos derivados analisados: {len(other_files)}\n")

    if unknown_by_id:
        print(f"🔴 {len(unknown_by_id)} ID(s) citados em documentos derivados mas ausentes do Blueprint:\n")
        for found_id, locations in sorted(unknown_by_id.items()):
            print(f"  {found_id}")
            for file_path, line_num in locations:
                print(f"    - {file_path} (linha {line_num})")
        print("\n→ Cada um desses é ou uma invenção a corrigir, ou uma decisão real que ainda não foi levada de volta ao PROJECT.md.")
    else:
        print("🟢 Nenhum ID órfão encontrado — todo ID citado nos documentos derivados existe no Blueprint.")

    if local_ids:
        print(f"\nℹ️  {len(local_ids)} ID(s) locais de documento (US/TASK/API), que nascem fora do Blueprint por definição — confira manualmente se cada um aponta para uma origem válida:")
        print("   " + ", ".join(sorted(local_ids)))

    unused_ids = valid_ids - referenced_valid_ids
    if unused_ids:
        print(f"\nℹ️  {len(unused_ids)} ID(s) definidos no Blueprint mas ainda não referenciados em nenhum documento derivado (informativo, não é um erro):")
        print("   " + ", ".join(sorted(unused_ids)))

    sys.exit(1 if unknown_by_id else 0)


if __name__ == "__main__":
    main()
