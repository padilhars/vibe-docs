#!/usr/bin/env python3
"""
find_references.py — Análise de impacto por ID de rastreabilidade.

Busca todas as ocorrências de um ID (ex.: BR-04, UC-02, ENT-01) nos arquivos
.md de uma pasta de projeto, para saber quais documentos são afetados antes
de alterar uma decisão já consolidada no PROJECT.md.

Uso:
    python find_references.py <pasta-do-projeto> <ID>

Exemplo:
    python find_references.py projects/sistema-gestao-salas BR-04
"""

import sys
from pathlib import Path


def find_references(project_dir: Path, target_id: str):
    """Retorna uma lista de (arquivo, num_linha, texto_da_linha) para cada ocorrência do ID."""
    matches = []
    md_files = sorted(project_dir.rglob("*.md"))

    if not md_files:
        return matches, []

    for md_file in md_files:
        try:
            lines = md_file.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception as e:
            print(f"⚠️  Não foi possível ler {md_file}: {e}", file=sys.stderr)
            continue

        for i, line in enumerate(lines, start=1):
            if target_id in line:
                matches.append((md_file, i, line.strip()))

    return matches, md_files


def main():
    if len(sys.argv) != 3:
        print("Uso: python find_references.py <pasta-do-projeto> <ID>")
        print("Exemplo: python find_references.py projects/sistema-gestao-salas BR-04")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    target_id = sys.argv[2].strip()

    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    matches, md_files = find_references(project_dir, target_id)

    if not md_files:
        print(f"❌ Nenhum arquivo .md encontrado em {project_dir}")
        sys.exit(1)

    if not matches:
        print(f"Nenhuma ocorrência de '{target_id}' encontrada em {len(md_files)} arquivo(s) .md em {project_dir}.")
        print("Isso pode significar que o ID não existe, foi digitado de forma diferente, ou de fato não é referenciado em nenhum documento derivado ainda.")
        sys.exit(0)

    files_affected = sorted({m[0] for m in matches})
    print(f"'{target_id}' encontrado em {len(files_affected)} arquivo(s), {len(matches)} ocorrência(s) no total:\n")

    current_file = None
    for file_path, line_num, line_text in matches:
        if file_path != current_file:
            current_file = file_path
            print(f"\n📄 {file_path.relative_to(project_dir.parent) if project_dir.parent in file_path.parents else file_path}")
        print(f"   L{line_num}: {line_text}")

    print(f"\n→ {len(files_affected)} arquivo(s) provavelmente precisam de revisão antes de finalizar esta alteração.")


if __name__ == "__main__":
    main()
