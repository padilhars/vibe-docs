#!/usr/bin/env python3
"""
project_status.py — Visão geral rápida de um projeto.

Mostra quais dos tipos de documento já foram gerados na pasta do projeto, e
extrai diretamente do PROJECT.md as seções de Estado do Projeto, Pendências,
Sugestões Futuras, Aprofundamento por Área, Princípios Não-Negociáveis e
Definition of Done — sem precisar reler o Blueprint inteiro à mão.

Uso:
    python project_status.py <pasta-do-projeto>
"""

import re
import sys
from pathlib import Path

PROJECT_FILENAME = "PROJECT.md"

# padrão de arquivo esperado -> rótulo de exibição
# "*" no padrão indica que múltiplas instâncias são normais (ex.: uma Feature
# Spec por funcionalidade), então contamos quantas em vez de checar 1 arquivo.
DOCUMENT_TYPES = {
    "PRD.md": "PRD",
    "MVP.md": "MVP",
    "FEATURE-SPEC*.md": "Feature Spec",
    "USE-CASE-SPEC.md": "Use Case Spec",
    "BUSINESS-RULES.md": "Business Rules",
    "USER-STORIES.md": "User Stories",
    "PROCESS-SPEC*.md": "Process Spec",
    "UX-SPEC.md": "UX Spec",
    "ARCHITECTURE.md": "Architecture",
    "DOMAIN-MODEL.md": "Domain Model",
    "DATA-MODEL.md": "Data Model",
    "API-SPEC.md": "API Spec",
    "INTEGRATION-SPEC.md": "Integration Spec",
    "SECURITY-SPEC.md": "Security Spec",
    "NFR.md": "NFR",
    "DEVELOPMENT-PLAN.md": "Development Plan",
    "BACKLOG.md": "Backlog",
    "TEST-STRATEGY.md": "Test Strategy",
    "SETUP-RUNBOOK.md": "Setup & Runbook",
    "STATE.md": "STATE.md (estado da implementação)",
    "CLAUDE.md": "CLAUDE.md (contrato do agente)",
}

# número da seção -> rótulo (usado só se o título exato não for encontrado)
SECTIONS_TO_SHOW = [
    (15, "Estado do Projeto"),
    (16, "Pendências"),
    (17, "Sugestões Futuras"),
    (19, "Aprofundamento por Área"),
    (20, "Princípios Não-Negociáveis"),
    (21, "Definition of Done e Convenções"),
]


def find_section(lines, number):
    """Acha uma seção '## <number>. ...' e retorna (início, fim) em índices de linha."""
    pattern = re.compile(rf"^##\s*{number}\.")
    start = None
    for i, line in enumerate(lines):
        if pattern.match(line.strip()):
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^##\s", lines[i].strip()):
            end = i
            break
    return start, end


def main():
    if len(sys.argv) != 2:
        print("Uso: python project_status.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    project_md = project_dir / PROJECT_FILENAME
    if not project_md.exists():
        print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}. Sem Blueprint consolidado, não há o que reportar.")
        sys.exit(1)

    print(f"📁 Projeto: {project_dir}")

    existing = {p.name.upper(): p for p in project_dir.glob("*.md") if p.name.upper() != PROJECT_FILENAME}

    print("\nDocumentos gerados:")
    for pattern, label in DOCUMENT_TYPES.items():
        if pattern.endswith("*.md"):
            prefix = pattern[:-4].upper()
            matches = [name for name in existing if name.startswith(prefix)]
            mark = "✅" if matches else "⬜"
            extra = f" ({len(matches)})" if matches else ""
            print(f"  {mark} {label}{extra}")
        else:
            mark = "✅" if pattern.upper() in existing else "⬜"
            print(f"  {mark} {label}")

    text = project_md.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    print(f"\n{'-' * 40}")
    for number, fallback_label in SECTIONS_TO_SHOW:
        found = find_section(lines, number)
        if found:
            start, end = found
            print("\n" + "\n".join(lines[start:end]).strip())
        else:
            print(f"\n## {number}. {fallback_label} — não encontrado no PROJECT.md")


if __name__ == "__main__":
    main()
