# Changelog — Vibe-Docs

## v2.1
- Seções 20 (Princípios Não-Negociáveis) e 21 (Definition of Done e Convenções) ganharam dono explícito no mecanismo de aprofundamento — antes o `handoff_check.py` bloqueava por elas estarem pendentes sem que nenhuma etapa fosse responsável por preenchê-las.
- Nota de proporcionalidade: a profundidade de cada seção deve ser calibrada ao tamanho real do projeto, não tratada como formulário obrigatório.
- Categoria "Testes e qualidade" no checklist de maturidade.
- README e este changelog incluídos no pacote.

## v2.0
- `CLAUDE-CODE-CONTEXT.md` substituído por um gerador de `CLAUDE.md` real — curto, contrato de comportamento, com `@imports`, no nome que o Claude Code carrega automaticamente.
- Novos documentos: **Test Strategy** (loop de verificação, com cada princípio inviolável amarrado a um teste) e **Setup & Runbook** (comandos, ambiente, estrutura de pastas).
- Seção 21 do Blueprint: Definition of Done e convenções de código/commit/branch.
- Novo script `handoff_check.py`: documentos essenciais, pendências críticas, seções bloqueantes e imports quebrados.
- Área "Testes e Qualidade" no aprofundamento sob demanda.
- **Correção encontrada em teste ponta a ponta:** `check_traceability.py` acusava IDs locais de documento (`US-xxx`, `TASK-xxx`) como invenção; agora são reportados separadamente, sem falso positivo.

## v1.5
- Seção 20 do Blueprint: Princípios Não-Negociáveis, verificados antes de finalizar qualquer documento.
- Backlog com critério explícito de atomicidade — tarefa precisa ser verificável isoladamente.

## v1.4
- Aprofundamento sob demanda: quando um documento precisa de algo que o Concept não cobriu, a skill pergunta só o necessário e grava a resposta no Blueprint (seção 19).
- Tabela de dependência entre documentos — reaproveita decisão já tomada em outro documento antes de perguntar de novo.

## v1.3
- Toda pergunta de levantamento passa a vir com palpite embutido, não só as proposições.
- `existing-codebase.md`: verifica código já existente antes de perguntar o que dá pra descobrir sozinho.

## v1.2
- Comandos de consulta (estado, referências, rastreabilidade, documentos existentes).
- Novo script `project_status.py`.

## v1.1
- Concept reescrito como discussão bidirecional: proposições passam a convidar discordância, e há comportamento definido para concordância, discordância e contraproposta do usuário.

## v1.0
- Três etapas (Concept, Blueprint, Files-Gen), 18 tipos de documento, rastreabilidade por ID, scripts `find_references.py` e `check_traceability.py`.
