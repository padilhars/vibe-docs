---
name: vibe-docs
description: Conduz um processo estruturado de descoberta e documentação de sistemas/produtos de software, para uso antes de desenvolvimento assistido por IA (vibe coding). Use sempre que o usuário apresentar um problema real com uma ideia de solução de sistema, app ou produto digital; pedir para iniciar, discutir ou refinar um projeto de software; pedir para consolidar um "blueprint" ou PROJECT.md; ou solicitar a geração de um documento de projeto — PRD, MVP, user stories, regras de negócio, casos de uso, UX spec, arquitetura, domain/data model, API, integrações, segurança, requisitos não-funcionais, plano de desenvolvimento, backlog ou contexto para Claude Code — a partir de um projeto já definido. Dispara mesmo sem esses termos exatos, como em "me ajuda a pensar num sistema pra X" ou "documenta isso pra eu jogar no Claude Code". Use também para alterar uma decisão já tomada e avaliar o impacto nos documentos existentes, e para simular o uso real do sistema em busca de falhas.
compatibility: Funciona melhor com acesso a terminal (bash) e sistema de arquivos, usados pelos scripts de rastreabilidade em scripts/ e para persistir o PROJECT.md e os documentos derivados como arquivos reais. Sem isso, a skill ainda funciona em modo conversacional, mas a análise de impacto e a checagem de consistência ficam manuais.
---

# Vibe-Docs

## Por que este processo existe

A maioria das conversas sobre "criar um sistema" pula direto pra "como construir" antes de "o que exatamente estamos construindo" estar claro. Isso produz documentação que parece completa mas esconde decisões nunca tomadas — e essas lacunas só aparecem depois, no meio do código.

Este processo separa três responsabilidades que normalmente ficam misturadas numa única conversa:

1. **Concept** — descobrir o que o sistema precisa ser (conversa, sem gerar documento).
2. **Blueprint** — consolidar isso numa fonte única de verdade (`PROJECT.md`).
3. **Files-Gen** — projetar essa fonte de verdade em documentos especializados (PRD, arquitetura, etc.), sem reabrir o Concept.

A regra mais importante do processo inteiro: **o Blueprint é a única fonte primária de verdade.** PRD, MVP, arquitetura e todo o resto são derivações — nunca o contrário. Se um documento derivado e o Blueprint discordarem, o Blueprint vence, a menos que o usuário decida explicitamente atualizar o Blueprint primeiro.

## As três etapas

| Etapa | Disparado por | O que fazer | O que NÃO fazer | Saída |
|---|---|---|---|---|
| **1. Concept** | Usuário apresenta um problema + ideia de solução, ou pede para iniciar/continuar um projeto | Investigar, questionar, propor — ver `references/concept/` | Gerar qualquer documento; presumir respostas para perguntas em aberto | Nenhum arquivo — só conversa |
| **2. Blueprint** | Usuário sinaliza que quer consolidar ("vamos fechar", "gere o blueprint", "temos o suficiente") | Checkpoint de revisão obrigatório, depois gerar/atualizar `PROJECT.md` — ver `references/blueprint/` | Pular o checkpoint; consolidar com pendência crítica sem avisar | `PROJECT.md` (arquivo real) |
| **3. Files-Gen** | Usuário pede um documento específico (PRD, arquitetura, etc.) ou uma alteração num projeto já consolidado | Ler o `PROJECT.md` atual, checar consistência, projetar no formato pedido — ver `references/documents/` | Inventar informação ausente; reabrir o Concept do zero | O documento pedido, como arquivo |

Não pule etapas automaticamente. Se não estiver claro em qual etapa você está, pergunte-se: "existe um Blueprint definido para este projeto?" Se não, você está em Concept. Se existe e o usuário quer um artefato específico, você está em Files-Gen. Consolidação só acontece quando o usuário pede.

## Etapa 1 — Concept

O Concept é uma discussão, não um interrogatório — questionar e propor têm o mesmo peso, e a reação do usuário a uma proposição (concordar, discordar, contrapor) é conteúdo tão importante quanto a resposta a uma pergunta de levantamento. Ao identificar que o usuário está trazendo uma ideia nova (ou continuando um Concept em andamento), leia:
- `references/concept/methodology.md` — como conduzir a conversa como troca real, e quando sugerir consolidar
- `references/concept/questioning.md` — como fazer boas perguntas de levantamento, sempre com um palpite embutido
- `references/concept/propositions.md` — como propor, e como conduzir a discussão que vem depois de cada proposição
- `references/concept/edge-cases.md` — checklist de casos de borda a explorar
- `references/concept/existing-codebase.md` — como verificar um código já existente antes de perguntar o que já dá pra descobrir sozinho
- `references/concept/prior-art.md` — como pesquisar o que sistemas do mesmo domínio tiveram que resolver, e transformar isso em pergunta em vez de funcionalidade

Nunca gere `PROJECT.md` ou qualquer outro documento nesta etapa. O objetivo é amadurecer o entendimento através de troca genuína, não produzir artefato nem só coletar respostas.

## Etapa 2 — Blueprint

Quando o usuário sinalizar que quer consolidar, leia:
- `references/blueprint/review-checklist.md` — o checkpoint 🟢🟡🔵🔴 (**obrigatório**, não pule mesmo se o usuário parecer com pressa — leva um parágrafo e evita retrabalho grande depois)
- `references/blueprint/schema.md` — a estrutura exata do `PROJECT.md`
- `references/blueprint/simulation.md` — simulação de uso real, rodada depois do checkpoint confirmado e antes de escrever o arquivo
- `references/blueprint/maturity.md` — como reportar o estado do projeto (checklist qualitativo, não percentual)

A ordem é: checkpoint → confirmação do usuário → simulação de uso real → escrever o `PROJECT.md`. Na primeira consolidação, parta de `assets/project-template.md` e grave como versão `1.0` na pasta do projeto (ver "Layout do projeto"). Se o arquivo já existe, edite as seções que mudaram em vez de regenerar tudo — preserva histórico e reduz o risco de perder algo que ainda era válido. Ao terminar, entregue o arquivo (ver "Entrega e retomada").

## Etapa 3 — Files-Gen

Sempre leia `references/documents/_shared-rules.md` e `references/documents/deepening.md` primeiro. O primeiro traz as regras que valem para todo documento derivado (rastreabilidade, o que fazer com lacunas, formato de metadados, como lidar com inconsistências); o segundo traz a ordem certa de checagem antes de escrever — se algo que falta já foi decidido em outro documento ou no Blueprint, e o que fazer quando for uma lacuna pequena (resolve na hora) ou grande (para e oferece escolha). Depois leia o arquivo específico do documento pedido, usando esta tabela de roteamento:

| Quando pedirem... | Leia também |
|---|---|
| PRD, "documento de produto", visão e escopo do produto | `references/documents/prd.md` |
| MVP, "versão mínima", "o que entra e o que fica de fora" | `references/documents/mvp.md` |
| Especificação de uma funcionalidade específica | `references/documents/feature-spec.md` |
| Especificação formal de casos de uso | `references/documents/use-case-spec.md` |
| Documento de regras de negócio | `references/documents/business-rules.md` |
| User stories, histórias de usuário, critérios de aceitação | `references/documents/user-stories.md` |
| Especificação de processo / fluxo operacional mais amplo | `references/documents/process-spec.md` |
| UX spec, jornadas de usuário, arquitetura de informação, telas, interação | `references/documents/ux-spec.md` |
| Arquitetura de software, especificação técnica | `references/documents/architecture.md` |
| Modelo de domínio (conceitual) | `references/documents/domain-model.md` |
| Modelo de dados (lógico/físico) | `references/documents/data-model.md` |
| Especificação de API | `references/documents/api-spec.md` |
| Especificação de integrações externas | `references/documents/integration-spec.md` |
| Especificação de segurança | `references/documents/security-spec.md` |
| Requisitos não-funcionais (performance, disponibilidade...) | `references/documents/nfr.md` |
| Plano de desenvolvimento / roadmap de implementação | `references/documents/development-plan.md` |
| Backlog, tarefas de desenvolvimento, implementação | `references/documents/backlog.md` |
| Estratégia de testes, plano de QA, "como testar isso" | `references/documents/test-strategy.md` |
| Setup, ambiente, comandos, "como rodar o projeto" | `references/documents/setup-runbook.md` |
| Skills que podem ajudar na implementação, "que skills instalar" | `references/documents/skills-recommendation.md` |
| Estado da implementação, "onde paramos", retomar entre sessões | `references/documents/state.md` |
| Aprendizados da implementação, memória entre sessões | `references/documents/learnings.md` |
| CLAUDE.md, contexto para Claude Code, "IA de desenvolvimento", coding guidelines | `references/documents/claude-md.md` |

`CLAUDE.md`, `STATE.md` e `LEARNINGS.md` são gerados juntos: o primeiro importa os outros dois e manda mantê-los a cada tarefa. Pedido de qualquer um dos três gera o trio.

Se o pedido não bater claramente com uma linha da tabela, pergunte qual desses tipos mais se aproxima em vez de inventar uma estrutura nova — a lista já é ampla o suficiente pra cobrir a grande maioria dos pedidos reais.

### Aprofundar antecipadamente

O usuário pode pedir o mesmo mecanismo de `deepening.md` de forma proativa, antes de pedir qualquer documento específico — por exemplo, "vamos aprofundar arquitetura e UX antes de eu pedir os documentos". Trate como uma rodada de aprofundamento focada nas áreas pedidas, gravando o resultado na seção 19 do `PROJECT.md`, sem gerar nenhum documento ainda. Diferente dos comandos de consulta abaixo, isso escreve no Blueprint — não é operação só de leitura.

### Alterar uma decisão já tomada

É uma reabertura pontual do Blueprint, não um novo Concept: não questione de novo decisões que não foram tocadas. Nesta ordem:

1. **Identifique** o(s) ID(s) afetado(s) e rode `scripts/find_references.py <pasta> <ID>` para cada um.
2. **Escreva o plano de propagação** — os documentos e seções afetados — e mostre ao usuário antes de editar qualquer arquivo. Uma alteração num projeto maduro costuma atravessar dez ou mais documentos, e uma cascata feita de cabeça pode ser interrompida no meio, deixando metade dos arquivos numa versão e metade na outra. A lista é o que permite retomar.
3. **Simule de novo, se a alteração mudar a sequência do que um ator faz ou quem pode fazer o quê** — regra de negócio, fluxo, permissão ou estado (ver `references/blueprint/simulation.md`). Mudança que não altera sequência (nome de campo, número de NFR, redação) não precisa.
4. **Atualize o `PROJECT.md`**: a decisão, uma linha na seção 18 e a versão, conforme "Quando a versão sobe" em `references/blueprint/schema.md`. Alterar o que estava decidido sobe; preencher o que estava `PENDENTE` não.
5. **Propague** seguindo o plano e marcando cada item. Cada documento tocado passa pela rotina obrigatória de `_shared-rules.md`, e só recebe a versão nova depois de conferido.
6. **Confira** com `scripts/check_staleness.py` e `scripts/check_coverage.py`: o primeiro mostra o que ficou para trás, o segundo o que nunca recebeu a decisão.

### Encerrar uma fase

Quando o usuário disser que a fase atual terminou (o MVP está pronto, vamos para a fase 2): na seção 22 do `PROJECT.md`, mova a fase atual para "Fases concluídas" com a data, defina a nova fase, seu objetivo e suas funcionalidades com o usuário, e registre a transição na seção 18. Depois regenere o que depende da fase: Plano de Desenvolvimento, Backlog (as tarefas concluídas ficam; entram as ondas da fase nova, com IDs novos), os limites de escopo do `CLAUDE.md` e o cabeçalho do `STATE.md`. Mudar de fase muda o que o agente deve implementar, então sobe a versão.

### Simular sob demanda

O usuário pode pedir uma simulação a qualquer momento depois de o Blueprint existir — "que problemas podem ocorrer no uso diário", "o que pode dar errado no dia a dia", "simule o uso real", "como seria a primeira semana" — raramente com a palavra "simulação". Conduza seguindo `references/blueprint/simulation.md`, com a mesma postura de procurar quebrar em vez de narrar o caminho feliz. Diferente dos comandos de consulta abaixo, isso escreve no Blueprint: lacuna real e comportamento indefinido viram pendência ou regra, e a simulação é registrada na seção 18.

## Comandos de consulta

Além de conduzir as três etapas, a skill responde a pedidos de consulta a qualquer momento, em qualquer etapa — são só leitura, nunca alteram o Blueprint nem geram documento:

| Pedido | O que fazer |
|---|---|
| "Qual o estado do projeto?" / "o que falta?" | Ler `references/blueprint/maturity.md` e reportar o checklist qualitativo, ou rodar `scripts/project_status.py <pasta>` pra um resumo já pronto |
| "Onde a BR-04 é usada?" / "o que depende disso?" | Rodar `scripts/find_references.py <pasta> <ID>` — vale mesmo sem intenção de mudar nada, não é exclusivo do fluxo de alteração |
| "Tá tudo rastreável?" / "tem algum ID inventado?" | Rodar `scripts/check_traceability.py <pasta>` sob demanda, não só depois de gerar um documento novo |
| "Quais documentos já existem?" / "o que já foi gerado?" | Rodar `scripts/project_status.py <pasta>` |
| "Mostra o blueprint" / "resume o projeto" | Ler e apresentar o `PROJECT.md` atual — o arquivo inteiro, ou um resumo, dependendo do que o usuário pedir |
| "Quais são as pendências?" | Ler a seção 16 do `PROJECT.md` (ou usar `project_status.py`, que já traz isso) |
| "O que ficou de fora? Sugestões futuras?" | Ler a seção 17 (🔵) do `PROJECT.md` (ou usar `project_status.py`) |
| "O que já foi aprofundado tecnicamente?" / "quais decisões técnicas já existem?" | Ler a seção 19 do `PROJECT.md` (ou usar `project_status.py`) |
| "Quais são os princípios do projeto?" / "o que nunca pode acontecer?" | Ler a seção 20 do `PROJECT.md` (ou usar `project_status.py`) |
| "Quando uma tarefa está pronta?" / "quais as convenções?" | Ler a seção 21 do `PROJECT.md` (ou usar `project_status.py`) |
| "Revise tudo" / "está tudo coerente?" / "tem divergência entre os documentos?" | Rodar os quatro scripts de verificação (`check_coverage`, `check_traceability`, `check_staleness`, `handoff_check`), depois revisar manualmente o que eles não alcançam: seções 15 e 19 do Blueprint ainda marcando como pendente algo já resolvido, pendência resolvida cujo texto antigo não foi removido, e afirmação escrita como fato sem decisão por trás |
| "Está pronto pro Claude Code?" / "posso começar a implementar?" | Rodar `scripts/handoff_check.py <pasta>` e reportar bloqueios e avisos |
| "Que documentos estão desatualizados?" | Rodar `scripts/check_staleness.py <pasta>` |
| "Em que fase o projeto está?" | Ler a seção 22 do `PROJECT.md` (ou usar `project_status.py`) |
| "Histórico de decisões?" | Ler a seção 18 do `PROJECT.md` |

## Comportamento de fallback

- **Pedido de documento sem Blueprint disponível** (ex.: chat novo, "gera o PRD do sistema X" sem `PROJECT.md` em contexto ou enviado): peça o arquivo primeiro. Só ofereça um Concept expresso se o usuário disser explicitamente que quer pular a etapa — e, nesse caso, avise que o documento vai sair com várias seções marcadas como PENDENTE.
- **Contradição durante o Concept**: se algo que o usuário disser conflitar com o que foi estabelecido antes na mesma conversa, sinalize na hora ("isso conflita com o que você disse sobre X — qual das duas deve valer?"), em vez de carregar as duas versões até o checkpoint final.
- **Pedido de documento fora da tabela de roteamento**: pergunte qual tipo mais se aproxima antes de criar uma estrutura ad-hoc.

## Regras universais

- **Calibre a profundidade ao tamanho do projeto.** A estrutura é a mesma para todo projeto; a quantidade de detalhe não deveria ser. Num sistema pequeno, seções curtas e algumas pendências legítimas são o resultado certo — insistir na mesma profundidade de um sistema grande vira cerimônia sem retorno. Ver a nota de proporcionalidade em `references/blueprint/schema.md`.
- **IDs só nascem no Blueprint.** Documentos derivados podem referenciar IDs (`BR-04`, `UC-02`, `ENT-01`...) mas nunca criar um novo — se um documento precisa de um identificador que não existe, isso é sinal de que falta algo no Blueprint, não uma oportunidade de inventar um ID ali mesmo. Exceção: identificadores específicos do próprio tipo de documento (ex.: `US-001` para uma user story) podem nascer no documento, mas devem sempre referenciar o(s) ID(s) de origem no Blueprint.
- **Idioma é configuração do Blueprint, não suposição.** O `PROJECT.md` tem um campo para isso (ver `references/blueprint/schema.md`). Documentos derivados seguem o que estiver definido ali; se não estiver definido, pergunte antes da primeira geração.
- **Use os scripts para análise de impacto, não a memória da conversa.** Ver seção seguinte.
- **Nunca trate um documento derivado como fonte de verdade.** Se notar uma inconsistência entre um documento antigo e o Blueprint atual, avise — não corrija silenciosamente nenhum dos dois lados.

## Scripts

Todos recebem a pasta que contém o `PROJECT.md` e funcionam nos dois momentos do layout (ver abaixo). `scripts/_common.py` é o módulo que eles compartilham, não um comando.

| Script | O que faz | Quando rodar |
|---|---|---|
| `check_traceability.py <pasta>` | Aponta ID citado num documento derivado que o Blueprint não define | Depois de gerar ou editar qualquer documento (passo 5 da rotina) |
| `check_coverage.py <pasta>` | Aponta `BR-xx`/`PRINC-xx` do Blueprint ausente de onde deveria constar, e funcionalidade do recorte ausente do `MVP.md` | Ao terminar um documento agregador (passo 5 da rotina) e ao fim de toda alteração de decisão |
| `find_references.py <pasta> <ID>` | Lista onde um ID é citado, pelo ID inteiro | Antes de qualquer alteração de decisão, e sob consulta |
| `check_staleness.py <pasta>` | Compara a versão do Blueprint com a de cada documento | Ao fim de toda alteração de decisão, e ao retomar um projeto |
| `handoff_check.py <pasta>` | Verifica se o pacote está pronto para o Claude Code | Ao terminar o `CLAUDE.md`, e antes de o usuário levar o projeto para implementação |
| `project_status.py <pasta>` | Mostra os documentos gerados e as seções de estado do Blueprint | Ao retomar um projeto, e em qualquer pedido de "como está o projeto" |

## Layout do projeto

**Durante a documentação**, tudo fica numa pasta só — é onde os scripts rodam:

```
projects/<nome-do-projeto>/
├── PROJECT.md
├── PRD.md, MVP.md, ARCHITECTURE.md, ...
├── STATE.md
├── LEARNINGS.md
└── CLAUDE.md
```

**No handoff**, o conteúdo vai para o repositório de código assim:

```
<repositório>/
├── CLAUDE.md          ← raiz: é onde o Claude Code o carrega
└── docs/
    ├── PROJECT.md
    ├── ...todos os outros documentos
    ├── STATE.md
    └── LEARNINGS.md
```

O `CLAUDE.md` já é gerado com os caminhos finais (`docs/...`). Depois do handoff, os scripts são rodados sobre `docs/` e encontram o `CLAUDE.md` na pasta acima. Ao entregar, diga ao usuário onde cada coisa vai — é o único passo manual do processo.

## Entrega e retomada

O ambiente em que a skill roda pode ser temporário: arquivos que só existem na pasta de trabalho podem não estar lá na conversa seguinte, ou sumir no meio de uma conversa longa.

- **Entregue cada arquivo assim que ele ficar pronto**, não em lote no fim. A partir do terceiro documento, entregue também a pasta do projeto compactada a cada rodada que mudar mais de um arquivo — é o que o usuário guarda e o que ele devolve para continuar.
- **Para retomar um projeto** em outra conversa, peça a pasta inteira (ou o arquivo compactado), não só o `PROJECT.md`: os scripts e a propagação de alterações precisam de todos os documentos. Com a pasta em mãos, rode `project_status.py` e `check_staleness.py` antes de qualquer outra coisa e diga ao usuário o que encontrou.
- **Se o usuário trouxer só o `PROJECT.md`**, dá para gerar documentos novos, mas avise que os já existentes não serão conferidos nem atualizados.
