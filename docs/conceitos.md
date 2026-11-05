# Conceitos

## Blueprint (`PROJECT.md`)

O único documento primário do projeto. Todo o resto é derivação. Se um documento derivado e o Blueprint discordarem, o Blueprint vence — a menos que você decida explicitamente atualizá-lo primeiro.

### Metadados

```yaml
---
project: "Clínica Ressignificar"
version: "1.3"                  # incrementa a cada consolidação relevante
status: "em evolução"           # em concept | consolidado | em evolução
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

Cada decisão relevante ganha um ID no Blueprint: `OBJ-01` (objetivo), `ENT-03` (entidade), `FUN-05` (funcionalidade), `UC-02` (caso de uso), `BR-04` (regra de negócio), `PRINC-01` (princípio), entre outros.

A regra: **IDs só nascem no Blueprint.** Um documento derivado que precisa de um ID inexistente está sinalizando que falta algo no Blueprint — não é oportunidade de inventar. A única exceção são identificadores próprios do tipo de documento (`US-001` numa user story), que sempre apontam para o ID de origem.

É isso que torna os scripts possíveis: com IDs estáveis, dá para perguntar "onde a `BR-04` aparece?" e obter uma resposta exata, não uma lembrança.

## DEFINIDO / DERIVADO / PENDENTE

Todo conteúdo de um documento derivado é uma destas três coisas:

- **DEFINIDO** — está explicitamente no Blueprint.
- **DERIVADO** — segue logicamente de algo definido (se `BR-04` diz que só o criador cancela, o endpoint de cancelamento precisa checar isso).
- **PENDENTE** — ainda não foi decidido, e aparece marcado como tal.

Nunca se escreve algo pendente como se fosse definido. Um documento com pendências honestas vale mais que um documento completo de mentira.

## Checkpoint 🟢🟡🔵🔴

Aplicado antes de toda consolidação. Ver [guia de uso](guia-de-uso.md#2-blueprint--consolidar). Dois detalhes que costumam passar batido: só entra em 🟢 o que você afirmou ou aceitou (não o que "parecia boa ideia"), e nada é descartado em silêncio — o que não foi decidido vira 🔵.

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

Quando o Blueprint sobe de versão, `check_staleness.py` aponta quem ficou para trás. Ele não pega um caso: documento gerado **antes** de uma regra existir, que nunca a recebeu. Para isso existe `check_coverage.py`.

## Proporcionalidade

A estrutura é igual para todo projeto; a profundidade não. Insistir no nível de detalhe de um sistema grande num sistema pequeno vira cerimônia sem retorno.

## Princípios e Definition of Done

As seções 20 e 21 do Blueprint são o que o agente de implementação precisa saber **sempre**: o que nunca pode acontecer e quando uma tarefa está pronta. Elas entram inline no `CLAUDE.md`, por isso precisam estar fechadas antes dele. Veja [handoff-claude-code.md](handoff-claude-code.md).
