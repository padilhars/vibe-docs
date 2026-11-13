# Changelog — Vibe-Docs

## v3.2
Revisão completa da skill (leitura de todos os arquivos, execução dos scripts e simulação de uso de ponta a ponta num projeto fictício), mais três funcionalidades novas.

**Correções críticas**
- **`CLAUDE.md` deixa de importar a documentação inteira.** O template usava `@ARQUIVO.md` para sete documentos e para o Blueprint, supondo que o agente os abriria quando precisasse; no Claude Code, arquivo importado com `@` é carregado inteiro em toda sessão. Agora só `STATE.md` e `LEARNINGS.md` são importados; os demais são citados pelo caminho, com a situação em que devem ser lidos. `handoff_check.py` avisa sobre import indevido.
- **Comparação de IDs pelo ID inteiro.** `check_coverage.py` dava "cobertura completa" com a BR-10 ausente se o documento citasse BR-100, e `find_references.py` devolvia TASK-010 na busca por TASK-01.
- **A seção 22 (Fase Atual) ganhou quem a preencha**: nasce na consolidação, é completada pelo `MVP.md` e muda pelo procedimento "Encerrar uma fase". Antes tinha três leitores e nenhum escritor, e `handoff_check.py` não a verificava.
- **Regra de quando a versão do Blueprint sobe**: só ao alterar ou acrescentar decisão, não ao preencher o que estava PENDENTE. Antes, gerar o terceiro documento já marcava os dois primeiros como desatualizados.
- **Layout do projeto definido**, antes e depois do handoff (`CLAUDE.md` na raiz, o restante em `docs/`), com os scripts funcionando nos dois.

**Correções médias**
- `schema.md`: bloco de código mal fechado deixava as seções 20 e 21 dentro de um bloco.
- Fim da contradição sobre o `PROJECT.md` durante o Concept: o arquivo só nasce na consolidação, como versão 1.0.
- Marcadores do template (`- BR-01: PENDENTE`) não contam mais como IDs definidos.
- Pendências críticas lidas em qualquer formato de lista; `schema.md` e template passaram a usar o mesmo formato.
- `STATE.md` e `LEARNINGS.md` fora da comparação de versões.
- Os scripts funcionam também em modo isolado (`python -I`, usado no CI), em que a pasta do script não entra no caminho de importação e o módulo comum não seria encontrado.
- Fluxo "Alterar uma decisão" reescrito em passos na ordem certa; checkpoint completo fica só para consolidação.
- `check_traceability.py` passou a ter gatilho na rotina obrigatória; `check_staleness.py`, no fim de toda alteração e na retomada.
- "Fase" (de produto, seção 22) e "onda" (de construção, plano e backlog) deixaram de ser o mesmo termo.
- Nova seção "Entrega e retomada": entregar cada arquivo assim que fica pronto e como continuar um projeto em outra conversa.

**Correções menores**
- Exemplo de pasta, contagens de tipos de documento, "Duas verificações" que eram três, referência a seção inexistente, termo "Modo 3", categorias de maturidade divergentes entre template e `maturity.md`, Data Model tratado como essencial no texto e recomendado no script, padrões de ID diferentes entre scripts (agora em `scripts/_common.py`), bloco de código aninhado no template do runbook, simulação anterior ao primeiro Blueprint sem versão a registrar.

**Funcionalidades novas**
- **Rotina de fim de tarefa e protocolo de bug**, fixos em todo `CLAUDE.md`: verificar, conferir a Definition of Done, marcar no backlog, atualizar estado e aprendizados, commit — a cada tarefa, não ao fim da sessão; e, para bugs, teste que reproduz antes da correção, mantido na suíte. O Test Strategy ganhou a seção de testes de regressão e o runbook, a orientação de garantir a verificação por gancho ou CI.
- **`LEARNINGS.md`** (`references/documents/learnings.md`): aprendizados da implementação versionados no repositório, curados e limitados a 100 linhas, complementares à memória automática do Claude Code.
- **`SKILLS-RECOMENDADAS.md`** (`references/documents/skills-recommendation.md`): até cinco skills gratuitas verificadas por pesquisa, com origem, licença, o que acessam, sobreposição com o `CLAUDE.md` e o pedido de instalação pronto. Nada é instalado sem aprovação do usuário, e o documento não é gerado de memória.

## v3.1
Calibração da simulação contra o primeiro uso real (sistema financeiro pessoal com bot, importação de fatura e integração de agenda). Dos 14 achados daquela sessão, os 7 cenários da v3.0 cobriam 1 bem e 2 parcialmente — estavam enviesados para CRUD com atores humanos em tela, que é o que os três projetos de referência anteriores eram.
- **Cenários reorganizados em duas camadas**: universais (agora 8, com "a mesma realidade entrando por dois caminhos", que pega dupla contagem) e condicionais por característica do sistema. As condicionais cobrem o que faltava: entrada em linguagem livre (ambígua, incompleta, múltipla, referencial), importação de dado externo (linha que o modelo não previu, reenvio, extração parcial, entidade desconhecida), dependência de serviço externo (falha silenciosa e indisponibilidade), acúmulo ao longo do tempo (proliferação de dado mestre), período de competência e efeito agregado de notificações.
- **O cenário do dia 0 ganhou a parte que mais rendeu no teste**: todo cálculo que depende de histórico precisa ter resposta para antes de existir histórico.
- **Formato de relato**, copiado do que funcionou: agrupar por natureza em vez de listar solto, separar o que exige decisão do que é correção direta, exemplo concreto em cada achado, correção proposta junto do apontamento, alternativa quando há outro caminho razoável, e fechar com o próximo passo.
- **Achado de simulação não entra automaticamente no MVP** — passa pelo corte como qualquer funcionalidade, senão a primeira versão fica grande por acúmulo de correção.
- **Gatilhos em linguagem real**: o pedido raramente usa a palavra "simulação"; no uso real veio como "problemas que podem ocorrer no uso diário".

## v3.0
- **Simulação de uso real** (`blueprint/simulation.md`), rodada depois do checkpoint e antes de consolidar o Blueprint, antes de definir o MVP, e sob demanda. Primeira verificação **dinâmica** da skill: todas as outras são estáticas (categorizar o que foi discutido, conferir presença de ID, reler cada documento por dentro), e nenhuma delas executa o sistema no tempo. Narrar atores concretos agindo em sequência pega a classe de defeito que leitura não pega — sistema vazio no dia 1, ator que faz na ordem errada, abandono no meio, operação do administrador que ninguém previu. A falha mais custosa dos nossos testes era exatamente dessa classe: "não existe caminho para criar a conta da secretária" só apareceu com o Backlog sendo escrito, depois de API Spec e User Stories prontos.
- **Postura adversarial obrigatória**: simulação que narra o caminho feliz e conclui "funciona bem" cria confiança falsa, então a instrução exige simular procurando quebrar — e relatar explicitamente quando não achou nada, porque silêncio depois de uma simulação é ambíguo.
- **Quatro destinos para os achados**, separando o que é lacuna real (vira pendência ou regra), comportamento indefinido (vira pergunta agora), risco operacional (§14) e mera preferência (🔵 §17) — sem essa separação a simulação viraria máquina de inflar escopo.
- **Gatilho estreito de re-simulação**: só quando a alteração mexe em regra, fluxo, permissão ou estado, isto é, quando muda a sequência do que um ator faz. Mudança de nome de campo ou número de NFR não dispara — verificação que dispara sempre vira ruído que se aprende a pular.
- Cada simulação é registrada na seção 18 com a versão sobre a qual rodou; nenhum arquivo novo é gerado, porque um registro narrativo ficaria obsoleto na primeira mudança de regra.

## v2.9
- **Pesquisa de sistemas existentes no Concept** (`concept/prior-art.md`), nas rodadas do meio. Enquadrada deliberadamente como descoberta de **problemas que o domínio exige resolver** — no-show, webhook que não chega, limite de janela de API, exigência regulatória — e não como catálogo de funcionalidades de concorrente: o resultado vira pergunta, nunca funcionalidade adicionada por conta própria. Achado não decidido explicitamente pelo usuário entra como 🔵 Sugestão futura no checkpoint.
- Três guardrails junto: a pesquisa nunca vira avaliação de mercado ou de viabilidade (`propositions.md`); respeita a proporcionalidade, pulando projetos pequenos; e distingue sempre "encontrei pesquisando agora" de "é conhecimento meu, que pode estar desatualizado" — distinção motivada por um caso real em que a skill afirmou que não existia API oficial de consulta a registro profissional e o usuário mostrou que existia.

## v2.8
Incorporações de uma proposta independente de metodologia para vibe coding, filtrada pelo que a skill ainda não cobria:
- **Regra de precedência no `CLAUDE.md`**: o que fazer quando os documentos se contradizem, com a regra dura de que conflito envolvendo regra de negócio, permissão ou dado pessoal faz o agente parar e perguntar, nunca escolher. A skill não dizia nada sobre isso, e nossas próprias auditorias provaram que contradição acontece.
- **Seção "Nunca faça" no `CLAUDE.md`**, com os modos de falha típicos de código gerado por IA: enfraquecer teste para passar, dependência nova sem aprovação (incluindo pacote inexistente ou com nome parecido com um legítimo, que é vetor de ataque), erro engolido em `try/catch`, refatoração fora de escopo, validação só no cliente. Os três primeiros também entraram na Definition of Done da seção 21.
- **Fase 1 reenquadrada como esqueleto funcional**: uma fatia vertical fina de ponta a ponta em vez da infraestrutura inteira, para que o agente copie padrões reais do repositório em vez de inventá-los a cada funcionalidade.
- **Novo documento `STATE.md`** (21º tipo): estado da implementação entre sessões — tarefa em andamento, bloqueios, questões. É o único documento que a skill cria para o agente de implementação manter, e o `CLAUDE.md` passa a mandar lê-lo no início e sobrescrevê-lo no fim de cada sessão.
- **Garantias determinísticas no `SETUP-RUNBOOK`**: para cada princípio inviolável e item da Definition of Done, preferir verificação automática a instrução — o que o agente *não consegue* violar vale mais que o que ele *deve* lembrar.
- **A documentação também deve encolher**: cortar vira parte legítima da revisão, como contrapeso ao viés de só acrescentar.

## v2.7
- **`check_coverage.py` ganhou gatilho concreto**: passa a ser passo obrigatório ao terminar qualquer documento agregador (`BUSINESS-RULES`, `TEST-STRATEGY`, `MVP`, `CLAUDE.md`), registrado tanto na rotina de `_shared-rules.md` quanto nos quatro geradores. Antes estava só listado e amarrado a "quando o usuário pedir" — a mesma posição do `handoff_check.py`, que atravessou um projeto real inteiro sem ser chamado nenhuma vez.

## v2.6
Ajuste derivado da primeira execução dos scripts contra um projeto real completo (21 documentos):
- **`check_coverage.py` passa a exigir prestação de contas, não cobertura cega.** Na primeira execução ele acusou 6 BRs ausentes do `TEST-STRATEGY.md` — mas 4 delas eram legitimamente de Fase 2. O problema não era o recorte, era o recorte ser silencioso: exclusão não declarada é indistinguível de esquecimento. Agora o relatório separa as duas causas possíveis e diz como resolver cada uma.
- **`test-strategy.md`**: toda `BR-xx` do Blueprint precisa aparecer no documento — com cenário de teste ou citada em "O que NÃO testar" com a justificativa.

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
