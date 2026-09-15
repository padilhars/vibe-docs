# Changelog — Vibe-Docs

## v2.5
Correções derivadas do terceiro teste real (sistema de agendamento de salas), o primeiro em que os 21 documentos foram gerados numa sessão só:
- **Rotina obrigatória ao terminar um documento** (`_shared-rules.md`): revisão crítica antes de entregar, atualização das seções 15 e 19 do Blueprint, remoção do texto antigo de pendência resolvida, e conferência das listas de pendências. No teste, a revisão só acontecia quando o usuário perguntava — e encontrava algo real em quase toda vez que ele perguntou.
- **"Sincronizar versão não é revisar"**: subir o campo `version` sem reconferir conteúdo fazia o `check_staleness.py` reportar tudo em dia enquanto regras inteiras (BR-19, BR-20) nunca chegavam a documentos criados antes delas.
- **Novo script `check_coverage.py`**: verifica se toda `BR-xx`/`PRINC-xx` do Blueprint aparece onde é obrigatória, e se as funcionalidades do recorte do MVP constam no `MVP.md`. Pega exatamente o caso que o `check_staleness` não pega.
- **IDs são append-only**: renumerar `TASK-xxx` para manter ordem quebrou referências cruzadas três vezes no teste. A ordem vem da posição e da onda, nunca do número.
- **Tokens técnicos excluídos da detecção de ID**: `AES-256` aparecia como falso positivo em toda execução do `check_traceability.py` desde a v2.3.
- **Plano de propagação escrito antes da cascata**: uma alteração atravessou 12 documentos e foi interrompida no meio, sem registro do que faltava aplicar.
- **Comando de auditoria global** ("revise tudo", "está tudo coerente?"), combinando os quatro scripts com o que eles não alcançam.
- **Todo ator precisa de caminho de criação** (checkpoint): a falta de como criar conta de secretária/admin só apareceu no Backlog, depois de API Spec e User Stories prontos.
- **Seções 20 e 21 fechadas antes do `CLAUDE.md`**, já que entram inline nele.

## v2.4
- Novo script `check_staleness.py`: compara a versão do Blueprint com a declarada por cada documento derivado e aponta o que ficou para trás. Fecha o ciclo da análise de impacto — `find_references.py` diz o que *seria* afetado, este diz o que *ficou* desatualizado.
- Seção 22 do Blueprint: **Fase Atual**. Antes, "funcionalidades desta fase" aparecia no Backlog e no `CLAUDE.md` sem nada definir qual era a fase, e o agente decidia sozinho. Backlog e CLAUDE.md agora leem dela.
- Alterar uma decisão passa a exigir incrementar a versão do `PROJECT.md`, sem o que a detecção de desatualização não funciona.

## v2.3
Correções derivadas do segundo teste real (SaaS multi-tenant de conteúdo educacional), o primeiro em que os 20 documentos foram gerados:
- **Seção 4 separa escopo do projeto do recorte do MVP.** Antes chamava-se "Dentro do escopo (MVP)", misturando os dois: o `MVP.md` estreitou o escopo corretamente, mas o corte nunca voltou ao Blueprint, e o `CLAUDE.md` acabou proibindo o que o Blueprint afirmava estar no escopo. O `MVP.md` agora escreve o corte de volta, e o `CLAUDE.md` lê os limites do Blueprint em vez do MVP.
- **Regra geral de refinamento legítimo**: quando um documento derivado estreita ou detalha algo do Blueprint, o refinamento volta para lá e é registrado no histórico.
- **Vazamento do aprofundamento fechado**: gerar um documento sem preencher (ou justificar explicitamente) a área correspondente da seção 19 fazia decisões sumirem do Blueprint. `handoff_check.py` passa a avisar quando um documento existe com a área ainda PENDENTE.
- **Consistência interna do Blueprint**: registrar algo na seção 19 exige verificar se aquilo resolve um PENDENTE de outra seção — no teste, a seção 13 dizia "stack não definida" enquanto a 19 listava a stack completa.
- **`CLAUDE.md` sem frontmatter YAML** — metadados são ruído num arquivo carregado em toda sessão, onde cada linha deve mudar o comportamento do agente.
- **Princípios citados por ID no `CLAUDE.md`**, preservando o caminho de volta ao Blueprint.
- **`check_traceability.py` enxerga prefixo de uma letra** e avisa sobre prefixo fora do padrão: `P-01` era completamente invisível ao script antes.

## v2.2
Correções derivadas do primeiro teste com um projeto real (bot de agendamento de barbearia):
- Prefixo `PRINC-` padronizado no schema — antes era improvisado a cada projeto. `TASK-` também entrou na lista oficial.
- Cada funcionalidade passa a referenciar o objetivo que atende (`FUN-03 (OBJ-02)`) — sem isso, um corte de MVP vira preferência em vez de argumento.
- Nova categoria de pergunta no Concept: **identidade** — como o sistema sabe quem é cada ator. Toda permissão depende disso e quase nunca é dito em voz alta.
- Decisões sobre identidade e autorização passam a virar nota obrigatória na seção 14, mesmo quando a decisão é sensata: no teste real, "a conta do Telegram identifica o admin, sem senha" foi registrado como regra de negócio sem que a consequência (conta comprometida = acesso total) fosse notada.
- Checkpoint de revisão ganhou duas verificações rápidas antes de consolidar: toda permissão tem identidade que a sustente, e toda funcionalidade serve a algum objetivo.

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
