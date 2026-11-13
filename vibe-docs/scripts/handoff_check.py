#!/usr/bin/env python3
"""
handoff_check.py — Verificação pré-entrega para implementação autônoma.

Checa se um projeto tem o mínimo para ser entregue ao Claude Code sem que o
agente precise adivinhar o que falta:

  - documentos essenciais presentes;
  - nenhuma pendência crítica em aberto (seção 16);
  - recorte do MVP (seção 4) e fase atual (seção 22) preenchidos;
  - princípios (seção 20) e Definition of Done (seção 21) decididos;
  - CLAUDE.md enxuto, com as rotinas de fim de tarefa e de bug, apontando só
    para arquivos que existem e importando com @ apenas o que é pequeno.

Funciona nos dois layouts: tudo numa pasta só, ou CLAUDE.md na raiz do
repositório com o restante em docs/ (passe a pasta que contém o PROJECT.md).

Uso:
    python handoff_check.py <pasta-do-projeto>

Saída: código 0 se pronto, 1 se houver bloqueio.
"""

import re
import sys
from pathlib import Path

# Garante o import de _common mesmo em modo isolado (python -I), que tira a
# pasta do script do sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    AGENT_MAINTAINED,
    CLAUDE_MD,
    PROJECT_FILENAME,
    critical_pendencies,
    field_value,
    project_files,
    read,
    section_body,
)

ESSENTIAL = {
    "CLAUDE.md": "contrato de comportamento que o Claude Code carrega sozinho",
    "ARCHITECTURE.md": "stack e componentes — sem isso o agente escolhe tecnologia sozinho",
    "BACKLOG.md": "o que implementar, em tarefas acionáveis",
    "TEST-STRATEGY.md": "como o agente verifica o próprio trabalho",
    "SETUP-RUNBOOK.md": "como rodar, testar e buildar o projeto",
    "STATE.md": "onde a implementação está — sem ele cada sessão começa cega",
    "LEARNINGS.md": "o que as sessões anteriores aprenderam — sem ele cada sessão reaprende",
}

RECOMMENDED = {
    "DATA-MODEL.md": "estrutura de dados concreta",
    "BUSINESS-RULES.md": "regras consolidadas para consulta",
    "API-SPEC.md": "contrato dos endpoints",
    "DEVELOPMENT-PLAN.md": "ordem de implementação",
}

# Documento -> subseção da seção 19. Documento gerado com a área ainda PENDENTE
# indica decisão tomada na geração que não voltou para o Blueprint.
DOC_TO_AREA = {
    "ARCHITECTURE.md": "Arquitetura",
    "UX-SPEC.md": "UX/UI",
    "DATA-MODEL.md": "Dados",
    "API-SPEC.md": "API",
    "SECURITY-SPEC.md": "Segurança",
    "NFR.md": "Performance e Escala",
    "INTEGRATION-SPEC.md": "Integrações",
    "TEST-STRATEGY.md": "Testes e Qualidade",
}

BLUEPRINT_SECTIONS = {
    20: ("Princípios Não-Negociáveis", "regras invioláveis"),
    21: ("Definition of Done e Convenções de Trabalho", "critério para saber quando parar"),
}

# Rotinas que o CLAUDE.md precisa trazer (ver references/documents/claude-md.md).
REQUIRED_ROUTINES = {
    "terminar cada tarefa": "a rotina de fim de tarefa (verificar, marcar no backlog, atualizar estado e aprendizados)",
    "encontrar um bug": "o protocolo de bug (teste que reproduz antes da correção)",
}

# Menção a um documento do projeto dentro do CLAUDE.md, com ou sem @.
DOC_REFERENCE = re.compile(r"(@?)((?:[A-Za-z0-9_.-]+/)*[A-Z][A-Z0-9-]*\.md)\b")


def is_pending(value) -> bool:
    return value is None or not value.strip() or "PENDENTE" in value.upper()


def main():
    if len(sys.argv) != 2:
        print("Uso: python handoff_check.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    blockers, warnings = [], []
    files = project_files(project_dir)

    for name, why in ESSENTIAL.items():
        if name not in files:
            blockers.append(f"{name} não existe — {why}")
    for name, why in RECOMMENDED.items():
        if name not in files:
            warnings.append(f"{name} não existe — {why}")

    if PROJECT_FILENAME not in files:
        blockers.append(f"{PROJECT_FILENAME} não existe — não há fonte de verdade para o projeto")
    else:
        lines = read(files[PROJECT_FILENAME]).splitlines()

        pend = critical_pendencies(lines)
        if pend:
            blockers.append(
                f"{len(pend)} pendência(s) crítica(s) em aberto no Blueprint: "
                + "; ".join(pend[:3]) + ("..." if len(pend) > 3 else "")
            )

        if "MVP.md" in files:
            recorte = field_value(section_body(lines, 4) or "", "Recorte do MVP")
            if recorte is None:
                blockers.append("MVP.md existe, mas a seção 4 do Blueprint não tem o campo 'Recorte do MVP'")
            elif is_pending(recorte):
                blockers.append("MVP.md existe, mas 'Recorte do MVP' na seção 4 está PENDENTE — o corte não voltou para o Blueprint")

        fase = section_body(lines, 22)
        if fase is None:
            warnings.append("Seção 22 (Fase Atual) não existe no Blueprint")
        elif "BACKLOG.md" in files or "MVP.md" in files:
            if is_pending(field_value(fase, "Funcionalidades desta fase")):
                blockers.append(
                    "Seção 22: 'Funcionalidades desta fase' está PENDENTE — Backlog e CLAUDE.md "
                    "falam em 'desta fase' sem que nada diga quais funcionalidades ela inclui"
                )
            if is_pending(field_value(fase, "Objetivo desta fase")):
                warnings.append("Seção 22: 'Objetivo desta fase' está PENDENTE")

        area_body = section_body(lines, 19) or ""
        for doc, area in DOC_TO_AREA.items():
            if doc not in files:
                continue
            trecho = next((b for b in area_body.split("### ") if b.startswith(area)), "")
            if not trecho or "PENDENTE" in trecho.upper():
                warnings.append(
                    f"{doc} existe, mas a área '{area}' da seção 19 segue PENDENTE — "
                    "decisões tomadas ao gerar o documento podem não ter voltado ao Blueprint"
                )

        for num, (label, consequence) in BLUEPRINT_SECTIONS.items():
            body = section_body(lines, num)
            if body is None:
                warnings.append(f"Seção {num} ({label}) não existe no Blueprint")
            elif is_pending(body):
                blockers.append(f"Seção {num} ({label}) tem item PENDENTE — o agente não terá {consequence}")

    if CLAUDE_MD in files:
        claude_path = files[CLAUDE_MD]
        content = read(claude_path)
        line_count = len(content.splitlines())
        if line_count > 200:
            warnings.append(
                f"{CLAUDE_MD} tem {line_count} linhas — acima de ~200 a aderência cai; mova detalhe para os documentos referenciados"
            )
        if content.lstrip().startswith("---"):
            warnings.append(f"{CLAUDE_MD} começa com frontmatter — ele não leva metadados (cada linha ali é contexto de toda sessão)")

        low = content.lower()
        for marker, what in REQUIRED_ROUTINES.items():
            if marker not in low:
                blockers.append(f"{CLAUDE_MD} não traz {what}")

        seen = set()
        for at, ref in DOC_REFERENCE.findall(content):
            base = Path(ref).name
            if base == CLAUDE_MD or (at, ref) in seen:
                continue
            seen.add((at, ref))
            target = None
            for candidate in (claude_path.parent / ref, project_dir / base):
                if candidate.exists():
                    target = candidate
                    break
            if target is None:
                blockers.append(f"{CLAUDE_MD} aponta para {at}{ref}, que não existe")
            elif at and base not in AGENT_MAINTAINED:
                size = len(read(target).splitlines())
                warnings.append(
                    f"{CLAUDE_MD} importa @{ref} ({size} linhas) — arquivo importado com @ é carregado inteiro "
                    "em toda sessão; cite o caminho sem @ e diga quando lê-lo"
                )

    print(f"📁 Projeto: {project_dir}\n")
    print(f"Documentos presentes: {len(files)}")

    if blockers:
        print(f"\n🔴 {len(blockers)} bloqueio(s) para implementação autônoma:\n")
        for b in blockers:
            print(f"  • {b}")
    if warnings:
        print(f"\n🟡 {len(warnings)} aviso(s) — não impedem, mas reduzem a autonomia do agente:\n")
        for w in warnings:
            print(f"  • {w}")

    if not blockers and not warnings:
        print("\n🟢 Pronto para handoff — nenhum bloqueio ou aviso.")
    elif not blockers:
        print("\n🟢 Sem bloqueios. Os avisos acima são opcionais.")
    else:
        print("\n→ Resolva os bloqueios antes de entregar o projeto ao Claude Code.")

    sys.exit(1 if blockers else 0)


if __name__ == "__main__":
    main()
