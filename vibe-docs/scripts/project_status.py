#!/usr/bin/env python3
"""
project_status.py — Visão geral rápida de um projeto.

Mostra quais dos tipos de documento já foram gerados na pasta do projeto, e
extrai diretamente do PROJECT.md as seções de Estado do Projeto, Pendências,
Sugestões Futuras, Aprofundamento por Área, Princípios Não-Negociáveis,
Definition of Done e Fase Atual — sem precisar reler o Blueprint inteiro à mão.

Uso:
    python project_status.py <pasta-do-projeto>
"""

import sys
from pathlib import Path

# Garante o import de _common mesmo em modo isolado (python -I), que tira a
# pasta do script do sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import PROJECT_FILENAME, project_files, read, section_body

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
    "SKILLS-RECOMENDADAS.md": "Skills recomendadas (opcional)",
    "STATE.md": "STATE.md (estado da implementação)",
    "LEARNINGS.md": "LEARNINGS.md (aprendizados da implementação)",
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
    (22, "Fase Atual"),
]


def main():
    if len(sys.argv) != 2:
        print("Uso: python project_status.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    files = project_files(project_dir)
    if PROJECT_FILENAME not in files:
        print(f"❌ {PROJECT_FILENAME} não encontrado em {project_dir}. Sem Blueprint consolidado, não há o que reportar.")
        sys.exit(1)

    print(f"📁 Projeto: {project_dir}")

    existing = {name.upper() for name in files if name != PROJECT_FILENAME}

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

    lines = read(files[PROJECT_FILENAME]).splitlines()

    print(f"\n{'-' * 40}")
    for number, fallback_label in SECTIONS_TO_SHOW:
        body = section_body(lines, number)
        if body is not None:
            print(f"\n## {number}. {fallback_label}\n{body}")
        else:
            print(f"\n## {number}. {fallback_label} — não encontrado no PROJECT.md")


if __name__ == "__main__":
    main()
