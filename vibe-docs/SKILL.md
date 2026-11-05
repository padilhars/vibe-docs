---
name: "vibe-docs"
description: Conduz um processo estruturado de descoberta e documentação de sistemas/produtos de software, para uso antes de desenvolvimento assistido por IA (vibe coding). Use sempre que o usuário apresentar um problema real com uma ideia de solução de sistema, app ou produto digital; pedir para iniciar, discutir ou refinar um projeto de software; pedir para consolidar um "blueprint" ou PROJECT.md; ou solicitar a geração de um documento de projeto — PRD, MVP, user stories, regras de negócio, casos de uso, UX spec, arquitetura, domain/data model, API, integrações, segurança, requisitos não-funcionais, plano de desenvolvimento, backlog ou contexto para Claude Code — a partir de um projeto já definido. Dispara mesmo sem esses termos exatos, como em "me ajuda a pensar num sistema pra X" ou "documenta isso pra eu jogar no Claude Code". Use também para alterar uma decisão já tomada e avaliar o impacto da mudança nos documentos existentes.
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
- `references/blueprint/maturity.md` — como reportar o estado do projeto (checklist qualitativo, não percentual)

Depois do checkpoint, crie ou atualize o `PROJECT.md` na pasta do projeto (ver convenção de pastas no fim deste arquivo). Se o arquivo já existe, prefira editar as seções que mudaram a regenerar tudo — preserva histórico e reduz risco de perder algo que ainda era válido.

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
| Estado da implementação, "onde paramos", retomar entre sessões | `references/documents/state.md` |
| CLAUDE.md, contexto para Claude Code, "IA de desenvolvimento", coding guidelines | `references/documents/claude-md.md` |

Se o pedido não bater claramente com uma linha da tabela, pergunte qual desses tipos mais se aproxima em vez de inventar uma estrutura nova — a lista já é ampla o suficiente pra cobrir a grande maioria dos pedidos reais.

### Aprofundar antecipadamente

O usuário pode pedir o mesmo mecanismo de `deepening.md` de forma proativa, antes de pedir qualquer documento específico — por exemplo, "vamos aprofundar arquitetura e UX antes de eu pedir os documentos". Trate como uma rodada de aprofundamento focada nas áreas pedidas, gravando o resultado na seção 19 do `PROJECT.md`, sem gerar nenhum documento ainda. Diferente dos comandos de consulta abaixo, isso escreve no Blueprint — não é operação só de leitura.

### Alterar uma decisão já tomada

Ao concluir uma alteração, incremente a versão no frontmatter do `PROJECT.md` — é ela que o `check_staleness.py` usa para saber o que ficou para trás. Sem incrementar, documentos desatualizados passam por atuais.

**Escreva o plano de propagação antes de editar o primeiro arquivo.** Uma alteração de decisão num projeto maduro costuma atravessar dez ou mais documentos, e uma cascata feita de cabeça pode ser interrompida no meio — deixando metade dos arquivos numa versão e metade na outra, sem registro do que faltou. Liste os documentos e as seções afetadas (a partir do `find_references.py`), mostre a lista ao usuário, e vá marcando conforme aplica. A lista é o que permite retomar com segurança se algo interromper.

Quando o usuário pedir para mudar algo já definido: identifique o(s) ID(s) afetado(s), rode `scripts/find_references.py` (ver seção de scripts abaixo) para localizar todos os documentos que citam esse ID, mostre o impacto ao usuário antes de editar qualquer coisa, e só depois atualize o `PROJECT.md` e ofereça atualizar os documentos derivados afetados. Isso é uma reabertura pontual do Blueprint, não um novo Concept completo — não questione novamente decisões que não foram tocadas.

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
| "Em que fase o projeto está?" | Ler a seção 22 do `PROJECT.md` |
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

- `scripts/find_references.py <pasta-do-projeto> <ID>` — busca todas as ocorrências de um ID (ex.: `BR-04`) nos arquivos `.md` da pasta do projeto. Use antes de qualquer alteração de decisão, para saber o que será afetado.
- `scripts/check_traceability.py <pasta-do-projeto>` — lê o `PROJECT.md` para montar o registro de IDs válidos, depois varre os demais documentos e aponta qualquer ID citado que não existe no Blueprint (possível invenção ou drift). Rode depois de gerar ou editar qualquer documento derivado, ou sob demanda quando o usuário pedir uma checagem.
- `scripts/project_status.py <pasta-do-projeto>` — mostra quais documentos já foram gerados (comparando com os 20 tipos possíveis) e extrai as seções de Estado do Projeto, Pendências, Sugestões Futuras, Aprofundamento por Área, Princípios Não-Negociáveis e Definition of Done direto do `PROJECT.md`. Use para qualquer pedido de "como está o projeto".
- `scripts/check_staleness.py <pasta-do-projeto>` — compara a versão do Blueprint com a que cada documento derivado declara no frontmatter e aponta o que ficou para trás. Rode depois de qualquer alteração de decisão, junto com `find_references.py`: um diz o que seria afetado, o outro diz o que de fato ficou desatualizado.
- `scripts/check_coverage.py <pasta-do-projeto>` — verifica se toda `BR-xx` e `PRINC-xx` do Blueprint aparece nos documentos onde é obrigatória, e se toda funcionalidade do recorte do MVP consta no `MVP.md`. Pega o caso que o `check_staleness.py` não pega: documento gerado antes de uma decisão existir, que nenhuma cascata posterior alcançou.
- `scripts/handoff_check.py <pasta-do-projeto>` — verificação pré-entrega: checa documentos essenciais, pendências críticas, seções 20 e 21 do Blueprint, e se os `@imports` do `CLAUDE.md` apontam para arquivos que existem. Rode sempre antes de o usuário levar o projeto para o Claude Code.

## Convenção de pastas de um projeto

Cada projeto vive na sua própria pasta, com o Blueprint e os documentos derivados como arquivos reais lado a lado:

```
projects/<nome-do-projeto>/
├── PROJECT.md
├── PRD.md
├── MVP.md
├── ...
└── CLAUDE-CODE-CONTEXT.md
```

Ao iniciar um projeto novo em Concept, use `assets/project-template.md` como esqueleto inicial do `PROJECT.md` em vez de montar a estrutura do zero.
