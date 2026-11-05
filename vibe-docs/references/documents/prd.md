# PRD — Product Requirements Document

## Propósito
Documento de referência para quem vai decidir e priorizar o que construir — não é um documento técnico. Cobre visão, escopo e requisitos do produto num nível que qualquer stakeholder de negócio deveria conseguir ler.

## Insumos necessários do Blueprint
Resumo do negócio, problema, objetivos, escopo, atores, funcionalidades, casos de uso principais, regras relevantes. Se `PENDENTE` no escopo (seção 4 do Blueprint), o PRD não deve ser finalizado sem isso — escopo mal definido é a lacuna mais cara de carregar adiante.

## Estrutura obrigatória

```markdown
# PRD — [Nome do Projeto]

## Visão do Produto
[o que é, para quem, por que importa — deriva do Resumo do Negócio + Objetivos]

## Problema
[a dor real — vem direto da seção 2 do Blueprint]

## Contexto
[situação atual, o que existe hoje que o produto substitui ou complementa]

## Objetivos
[lista com IDs OBJ-xx do Blueprint]

## Usuários e Necessidades
[para cada ator: quem é, o que precisa do sistema]

## Escopo
[o que está dentro / fora desta versão — direto da seção 4 do Blueprint]

## Funcionalidades
[lista com IDs FUN-xx, agrupadas por área quando fizer sentido]

## Requisitos
[requisitos funcionais relevantes derivados das funcionalidades e regras]

## Regras de Negócio Relevantes
[só as que afetam decisão de produto — não repita o documento de Business Rules inteiro]

## Fluxos Principais
[resumo do(s) fluxo(s) mais importantes — remeta ao Blueprint para o passo a passo completo]

## Critérios de Sucesso
[como saber se o produto está cumprindo o objetivo — deriva dos OBJ-xx]

## Dependências e Riscos
[da seção 14 do Blueprint]

## Pendências
[qualquer PENDENTE que afete decisão de produto]
```

## Regras específicas
- Não inclua detalhe técnico de implementação (isso é `architecture.md` e `data-model.md`) — se uma decisão técnica já foi tomada e afeta o produto (ex.: "vai funcionar offline"), mencione o efeito para o usuário, não a solução técnica.
- "Visão do Produto" e "Escopo" cobrem o que às vezes é pedido separadamente como "Product Vision" ou "Product Scope" — se o usuário pedir só uma dessas partes, gere apenas essa seção em vez do PRD inteiro.
