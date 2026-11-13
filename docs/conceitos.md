# Conceitos

## Blueprint (`PROJECT.md`)

O único documento primário do projeto. Todo o resto é derivação. Se um documento derivado e o Blueprint discordarem, o Blueprint vence — a menos que você decida explicitamente atualizá-lo primeiro.

### Metadados

```yaml
---
project: "Clínica Ressignificar"
version: "1.3"                  # sobe quando uma decisão muda ou entra
status: "em evolução"           # consolidado | em evolução
idioma_documentacao: "pt-BR"    # vale para todos os documentos derivados
last_updated: "2026-11-05"
---
```

### As 22 seções

| # | Seção | # | Seção |
|---|---|---|---|
| 1 | Resumo do Negócio | 12 | Permissões |
| 2 | O Problema | 13 | Requisitos Técnicos Iniciais |
| 3 | Objetivos | 14 | Riscos e Pontos de Atenção |
| 4 | Escopo (inclui o recorte do MVP) | 15 | Estado do Projeto |
| 5 | Atores | 16 | Pendências |
| 6 | Entidades | 17 | Sugestões Futuras 🔵 |
| 7 | Estados | 18 | Histórico de Decisões |
| 8 | Funcionalidades | 19 | Aprofundamento por Área |
| 9 | Casos de Uso | 20 | Princípios Não-Negociáveis |
| 10 | Regras de Negócio | 21 | Definition of Done e Convenções |
| 11 | Fluxos | 22 | Fase Atual |

O esqueleto vazio está em [`vibe-docs/assets/project-template.md`](../vibe-docs/assets/project-template.md); a especificação completa, em [`references/blueprint/schema.md`](../vibe-docs/references/blueprint/schema.md).

## IDs de rastreabilidade

Cada decisão relevante ganha um ID no Blueprint: `OBJ-01` (objetivo), `ENT-03` (entidade), `FUN-05` (funcionalidade), `UC-02` (caso de uso), `BR-04` (regra de negócio), `REQ-02` (requisito técnico), `PRINC-01` (princípio). Um ID nunca é reaproveitado nem renumerado.

A regra: **IDs só nascem no Blueprint.** Um documento derivado que precisa de um ID inexistente está sinalizando que falta algo no Blueprint — não é oportunidade de inventar. A única exceção são identificadores próprios do tipo de documento (`US-001` numa user story, `TASK-012` no backlog, `API-03` na especificação de API), que sempre apontam para o ID de origem.

É isso que torna os scripts possíveis: com IDs estáveis, dá para perguntar "onde a `BR-04` aparece?" e obter uma resposta exata, não uma lembrança.

## DEFINIDO / DERIVADO / PENDENTE

Todo conteúdo de um documento derivado é uma destas três coisas:

- **DEFINIDO** — está explicitamente no Blueprint.
- **DERIVADO** — segue logicamente de algo definido (se `BR-04` diz que só o criador cancela, o endpoint de cancelamento precisa checar isso).
- **PENDENTE** — ainda não foi decidido, e aparece marcado como tal.

Nunca se escreve algo pendente como se fosse definido. Um documento com pendências honestas vale mais que um documento completo de mentira.

## Checkpoint 🟢🟡🔵🔴

Aplicado antes de toda consolidação. Ver [guia de uso](guia-de-uso.md#2-blueprint--consolidar). Dois detalhes que costumam passar batido: só entra em 🟢 o que você afirmou ou aceitou (não o que "parecia boa ideia"), e nada é descartado em silêncio — o que não foi decidido vira 🔵.

## Simulação de uso real

Checkpoint, scripts e revisão são verificações estáticas: leem o que foi escrito. A simulação **executa** o sistema no tempo: narra atores concretos agindo em sequência, procurando quebrar. Ela pega a classe de defeito que só existe na ordem dos acontecimentos: o sistema vazio no primeiro dia, alguém que faz as coisas fora da ordem prevista, uma operação abandonada no meio, a mesma realidade entrando por dois caminhos.

Roda depois do checkpoint confirmado e antes de o `PROJECT.md` ser escrito, antes do corte do MVP, quando uma alteração muda a sequência do que um ator faz (regra, fluxo, permissão ou estado) e sempre que você pedir. Há oito cenários universais e cenários condicionais por característica do sistema (entrada em linguagem livre, importação de dado externo, dependência de serviço externo, acúmulo ao longo do tempo, entre outros).

Cada achado tem um de quatro destinos: lacuna real vira pendência ou regra, comportamento indefinido vira pergunta na hora, risco operacional vai para a seção 14 e preferência vai para 🔵. Achado de simulação não entra sozinho no MVP: passa pelo corte como qualquer funcionalidade. Detalhes em [`references/blueprint/simulation.md`](../vibe-docs/references/blueprint/simulation.md).

## Maturidade, não percentual

O estado do projeto é um checklist qualitativo por categoria (problema, atores, regras, fluxos…), não "73% pronto". Percentual sugere precisão que não existe e esconde *qual* lacuna importa.

## Versionamento e documentos desatualizados

Cada documento derivado guarda, no frontmatter, a versão do Blueprint que o originou:

```yaml
---
document_type: "PRD"
project: "Clínica Ressignificar"
version: "1.2"           # versão do PROJECT.md usada como fonte
status: "completo com pendências"
source: "PROJECT.md"
generated_at: "2026-10-20"
---
```

O Blueprint nasce como versão `1.0` na primeira consolidação. A partir daí:

| Sobe a versão | Não sobe |
|---|---|
| Alterar ou acrescentar uma decisão: regra, funcionalidade, ator, entidade, estado, permissão, princípio | Preencher o que estava PENDENTE (uma área da seção 19, a seção 21, o recorte do MVP, a seção 22) |
| Encerrar uma fase e abrir a seguinte | Atualizar as seções de acompanhamento (15 a 18) |

Sem essa distinção, gerar o terceiro documento já marcaria os dois primeiros como desatualizados sem que nenhuma decisão tivesse mudado.

Quando o Blueprint sobe de versão, `check_staleness.py` aponta quem ficou para trás. Ele não pega um caso: documento gerado **antes** de uma regra existir, que nunca a recebeu. Para isso existe `check_coverage.py`. `STATE.md` e `LEARNINGS.md` ficam fora dessa comparação: são mantidos pelo agente de implementação e não têm versão.

## Fase e onda

Dois termos que não se confundem:

- **Fase** é de produto: o que esta entrega inclui (MVP, fase 2…). Vive na seção 22 do Blueprint, que nasce na consolidação, é completada pelo `MVP.md` e muda quando você encerra uma fase.
- **Onda** é de construção: a ordem em que as tarefas de uma fase são implementadas. Vive no Development Plan e no Backlog.

## Proporcionalidade

A estrutura é igual para todo projeto; a profundidade não. Insistir no nível de detalhe de um sistema grande num sistema pequeno vira cerimônia sem retorno.

## Princípios e Definition of Done

As seções 20 e 21 do Blueprint são o que o agente de implementação precisa saber **sempre**: o que nunca pode acontecer e quando uma tarefa está pronta. Elas entram inline no `CLAUDE.md`, por isso precisam estar fechadas antes dele, junto com a seção 22, de onde saem os limites de escopo. Veja [handoff-claude-code.md](handoff-claude-code.md).
