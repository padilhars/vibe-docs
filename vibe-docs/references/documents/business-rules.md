# Business Rules — Documento de Regras de Negócio

## Propósito
Reunir todas as regras de negócio do projeto num único documento de referência rápida — útil tanto para revisão de negócio quanto como checklist de validação durante a implementação.

## Insumos necessários do Blueprint
Todas as `BR-xx` da seção 10, mais as entidades e casos de uso que cada uma referencia.

## Estrutura obrigatória

```markdown
# Regras de Negócio — [Nome do Projeto]

| ID | Regra | Entidades Afetadas | Casos de Uso Relacionados | Origem |
|---|---|---|---|---|
| BR-01 | [descrição verificável] | ENT-xx | UC-xx | Concept / Alteração em [data] |

## Detalhamento por Regra

### BR-01 — [título curto]
[descrição completa, incluindo exceções conhecidas]

**Validação esperada:** [como testar se a regra está sendo respeitada, em termos de comportamento observável]
```


## Verificação obrigatória ao terminar

Rode `scripts/check_coverage.py <pasta-do-projeto>` antes de entregar. Este é um documento agregador: ele precisa refletir decisões tomadas ao longo de todo o projeto, e uma ausência aqui não aparece na leitura — o documento parece completo justamente porque o que falta não está nele. Resolva o que o script apontar (incluindo declarar exclusões deliberadas) antes de considerar o documento pronto.
## Regras específicas
- A tabela é o resumo navegável; o detalhamento abaixo dela é o texto completo — não deixe as duas seções divergirem.
- "Validação esperada" deve ser concreto o suficiente para virar um teste, mas isso não é o mesmo que um Critério de Aceitação formal (esses ficam em `user-stories.md`, ligados a uma história específica) — aqui é validação da regra em si, independente de qual fluxo a aciona.
- Regras que mudaram (ver histórico de decisões do Blueprint) devem indicar isso na coluna "Origem", não só a regra atual — perder esse rastro é o tipo de coisa que `scripts/check_traceability.py` não consegue pegar sozinho.
