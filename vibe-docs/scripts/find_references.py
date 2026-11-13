#!/usr/bin/env python3
"""
find_references.py — Análise de impacto por ID de rastreabilidade.

Busca todas as ocorrências de um ID (ex.: BR-04, UC-02, ENT-01) nos documentos
de um projeto, para saber quais são afetados antes de alterar uma decisão já
consolidada no PROJECT.md. A busca é pelo ID inteiro: TASK-01 não devolve
ocorrências de TASK-010.

Uso:
    python find_references.py <pasta-do-projeto> <ID>

Exemplo:
    python find_references.py projects/sistema-gestao-salas BR-04
"""

import re
import sys
from pathlib import Path

# Garante o import de _common mesmo em modo isolado (python -I), que tira a
# pasta do script do sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import project_files, read


def find_references(project_dir: Path, target_id: str):
    """Lista de (arquivo, num_linha, texto_da_linha) para cada ocorrência do ID inteiro."""
    whole = re.compile(rf"(?<![A-Za-z0-9-]){re.escape(target_id)}(?!\d)")
    files = project_files(project_dir)
    matches = []
    for name in sorted(files):
        for i, line in enumerate(read(files[name]).splitlines(), start=1):
            if whole.search(line):
                matches.append((name, i, line.strip()))
    return matches, files


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

    matches, files = find_references(project_dir, target_id)

    if not files:
        print(f"❌ Nenhum documento .md encontrado em {project_dir}")
        sys.exit(1)

    if not matches:
        print(f"Nenhuma ocorrência de '{target_id}' em {len(files)} documento(s) de {project_dir}.")
        print("O ID pode não existir, ter sido digitado de forma diferente, ou ainda não ser citado em nenhum documento.")
        sys.exit(0)

    affected = sorted({m[0] for m in matches})
    print(f"'{target_id}' encontrado em {len(affected)} documento(s), {len(matches)} ocorrência(s) no total:")

    current = None
    for name, line_num, line_text in matches:
        if name != current:
            current = name
            print(f"\n📄 {name}")
        print(f"   L{line_num}: {line_text}")

    print(f"\n→ {len(affected)} documento(s) entram no plano de propagação desta alteração.")


if __name__ == "__main__":
    main()
