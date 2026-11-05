# User Stories e Critérios de Aceitação

## Propósito
Traduzir funcionalidades e casos de uso já definidos em unidades de trabalho no formato que times ágeis costumam usar para planejar e implementar.

## Insumos necessários do Blueprint
Funcionalidades, casos de uso, atores, regras de negócio relacionadas. Prefira gerar a partir do MVP quando ele existir, para já vir com prioridade implícita.

## Estrutura obrigatória (por história)

```markdown
### US-xxx — [título curto]

**Como** [ator],
**quero** [ação],
**para** [objetivo].

**Contexto:** [quando essa história se aplica]

**Critérios de aceitação:**
- Dado que [contexto], quando [ação], então [resultado esperado]
- Dado que [contexto alternativo], quando [ação], então [resultado esperado]

**Regras de negócio relacionadas:** [BR-xx]
**Rastreabilidade:** US-xxx → FUN-xx → UC-xx → BR-xx
**Dependências:** [outras US que precisam existir antes, se houver]
**Casos alternativos relevantes:** [cenários de erro ou exceção que valem uma linha, sem duplicar `use-case-spec.md` inteiro]
```

## Regras específicas
- Uma história por funcionalidade concreta e testável — se uma funcionalidade é grande demais para uma história só, divida, mas mantenha a rastreabilidade para a mesma `FUN-xx` de origem em todas.
- Critérios de aceitação devem ser objetivos e verificáveis. Evite formulações como "funcionar corretamente" ou "ter boa usabilidade" — se a informação necessária para tornar um critério objetivo não estiver no Blueprint, registre isso como pendência daquela história específica em vez de escrever um critério vago só para preencher o espaço.
- Não crie história para funcionalidade que não existe como `FUN-xx` no Blueprint.
