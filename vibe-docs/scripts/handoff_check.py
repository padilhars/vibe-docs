#!/usr/bin/env python3
"""
handoff_check.py — Verificação pré-entrega para implementação autônoma.

Checa se um projeto tem o mínimo necessário para ser entregue a uma ferramenta
de desenvolvimento assistido por IA (Claude Code) sem que ela precise adivinhar
o que falta: documentos essenciais presentes, CLAUDE.md válido, imports que
apontam para arquivos existentes, e nenhuma pendência crítica em aberto.

Uso:
    python handoff_check.py <pasta-do-projeto>

Saída: código 0 se pronto, 1 se houver bloqueio.
"""

import re
import sys
from pathlib import Path

PROJECT_FILENAME = "PROJECT.md"
CLAUDE_MD = "CLAUDE.md"

# Documentos considerados essenciais para implementação autônoma.
ESSENTIAL = {
    "CLAUDE.md": "contrato de comportamento carregado automaticamente pelo Claude Code",
    "ARCHITECTURE.md": "stack e componentes — sem isso o agente escolhe tecnologia sozinho",
    "BACKLOG.md": "o que implementar, em tarefas acionáveis",
    "TEST-STRATEGY.md": "como o agente verifica o próprio trabalho",
    "SETUP-RUNBOOK.md": "como rodar, testar e buildar o projeto",
    "STATE.md": "ponte entre sessões de implementação — sem ele cada sessão começa cega",
}

# Recomendados, não bloqueantes.
RECOMMENDED = {
    "DATA-MODEL.md": "estrutura de dados concreta",
    "BUSINESS-RULES.md": "regras consolidadas para consulta",
    "API-SPEC.md": "contrato dos endpoints",
    "DEVELOPMENT-PLAN.md": "ordem de implementação",
}

# Documento -> subseção correspondente na seção 19 (Aprofundamento por Área).
# Documento que existe com a área ainda PENDENTE significa que decisões foram
# tomadas durante a geração e não voltaram para o Blueprint.
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

# Seções do Blueprint que, vazias/PENDENTE, comprometem o handoff.
BLUEPRINT_SECTIONS = {
    20: "Princípios Não-Negociáveis",
    21: "Definition of Done e Convenções de Trabalho",
}

IMPORT_PATTERN = re.compile(r"@([A-Za-z0-9_\-./]+\.md)")


def section_body(lines, number):
    start = None
    pattern = re.compile(rf"^##\s*{number}\.")
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
    return "\n".join(lines[start + 1:end]).strip()


def main():
    if len(sys.argv) != 2:
        print("Uso: python handoff_check.py <pasta-do-projeto>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    if not project_dir.exists() or not project_dir.is_dir():
        print(f"❌ Pasta de projeto não encontrada: {project_dir}")
        sys.exit(1)

    blockers = []
    warnings = []

    present = {p.name: p for p in project_dir.glob("*.md")}

    # 1. Documentos essenciais
    for name, why in ESSENTIAL.items():
        if name not in present:
            blockers.append(f"{name} não existe — {why}")

    for name, why in RECOMMENDED.items():
        if name not in present:
            warnings.append(f"{name} não existe — {why}")

    # 2. Blueprint: pendências críticas e seções-chave
    project_md = present.get(PROJECT_FILENAME)
    if not project_md:
        blockers.append(f"{PROJECT_FILENAME} não existe — não há fonte de verdade para o projeto")
    else:
        lines = project_md.read_text(encoding="utf-8", errors="replace").splitlines()

        pend = section_body(lines, 16)
        if pend:
            critical_block = pend.split("**Menores")[0]
            items = [
                l.strip("- ").strip()
                for l in critical_block.splitlines()
                if l.strip().startswith("-") and "nenhuma" not in l.lower()
            ]
            if items:
                blockers.append(
                    f"{len(items)} pendência(s) crítica(s) em aberto no Blueprint: "
                    + "; ".join(items[:3])
                    + ("..." if len(items) > 3 else "")
                )

        # Recorte do MVP: se MVP.md existe, a seção 4 precisa refletir o corte
        escopo = section_body(lines, 4) or ""
        if "MVP.md" in present:
            recorte = ""
            for chunk in escopo.split("**"):
                if chunk.lower().startswith("recorte do mvp"):
                    recorte = chunk
            if not recorte:
                blockers.append(
                    "MVP.md existe, mas a seção 4 do Blueprint não tem o campo 'Recorte do MVP' — "
                    "o CLAUDE.md pode acabar proibindo o que o Blueprint diz estar no escopo"
                )
            elif "PENDENTE" in recorte.upper():
                blockers.append(
                    "MVP.md existe, mas 'Recorte do MVP' na seção 4 está PENDENTE — "
                    "o corte do MVP não voltou para o Blueprint"
                )

        # Aprofundamento: documento gerado com a área correspondente ainda vazia
        area_body = section_body(lines, 19) or ""
        for doc, area in DOC_TO_AREA.items():
            if doc not in present:
                continue
            trecho = ""
            for bloco in area_body.split("### "):
                if bloco.startswith(area):
                    trecho = bloco
                    break
            if not trecho or "PENDENTE" in trecho.upper():
                warnings.append(
                    f"{doc} existe, mas a área '{area}' da seção 19 segue PENDENTE — "
                    "decisões tomadas ao gerar o documento podem não ter voltado ao Blueprint"
                )

        for num, label in BLUEPRINT_SECTIONS.items():
            body = section_body(lines, num)
            if body is None:
                warnings.append(f"Seção {num} ({label}) não existe no Blueprint")
            elif not body or "PENDENTE" in body.upper():
                blockers.append(
                    f"Seção {num} ({label}) está PENDENTE — o agente não terá {'regras invioláveis' if num == 20 else 'critério para saber quando parar'}"
                )

    # 3. CLAUDE.md: tamanho e imports
    claude_md = present.get(CLAUDE_MD)
    if claude_md:
        content = claude_md.read_text(encoding="utf-8", errors="replace")
        line_count = len(content.splitlines())
        if line_count > 200:
            warnings.append(
                f"{CLAUDE_MD} tem {line_count} linhas — acima de ~200 ele consome context window demais; considere mover detalhe para os documentos importados"
            )
        for imported in IMPORT_PATTERN.findall(content):
            target = (project_dir / Path(imported).name)
            if not target.exists():
                blockers.append(
                    f"{CLAUDE_MD} importa @{imported}, que não existe na pasta do projeto"
                )

    # Relatório
    print(f"📁 Projeto: {project_dir}\n")
    print(f"Documentos presentes: {len(present)}")

    if blockers:
        print(f"\n🔴 {len(blockers)} bloqueio(s) para implementação autônoma:\n")
        for b in blockers:
            print(f"  • {b}")

    if warnings:
        print(f"\n🟡 {len(warnings)} aviso(s) — não impedem, mas reduzem a autonomia do agente:\n")
        for w in warnings:
            print(f"  • {w}")

    if not blockers and not warnings:
        print("\n🟢 Pronto para handoff — nenhum bloqueio ou aviso encontrado.")
    elif not blockers:
        print("\n🟢 Sem bloqueios. Os avisos acima são opcionais.")
    else:
        print("\n→ Resolva os bloqueios antes de entregar o projeto ao Claude Code.")

    sys.exit(1 if blockers else 0)


if __name__ == "__main__":
    main()
