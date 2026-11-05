# Domain Model — Modelo de Domínio

## Propósito
Representar as entidades do domínio de forma conceitual — atributos, relacionamentos, estados, invariantes — sem entrar em decisão de banco de dados. Isso é frequentemente confundido com o modelo de dados físico; são documentos diferentes, gerados a partir do mesmo Blueprint mas com propósitos distintos (ver `data-model.md`).

## Insumos necessários do Blueprint
Entidades (seção 6), estados (seção 7), regras de negócio que restringem entidades.

## Estrutura obrigatória

```markdown
# Modelo de Domínio — [Nome do Projeto]

## Entidades
### ENT-xx — [Nome]
- **Atributos conceituais:** [nome do atributo e o que representa, sem tipo de banco]
- **Invariantes:** [o que sempre precisa ser verdade sobre esta entidade — deriva das BR-xx aplicáveis]
- **Estados possíveis:** [se houver ciclo de vida]

## Relacionamentos
[ENT-xx relaciona-se com ENT-yy de que forma — um-para-um, um-para-muitos, muitos-para-muitos — e por qual regra de negócio essa relação existe]

## Agregados
[quando fizer sentido: quais entidades formam uma unidade consistente que deveria ser tratada em conjunto]

## Eventos de Domínio
[mudanças de estado relevantes que outras partes do sistema podem precisar reagir — ex.: "reserva cancelada"]
```

## Regras específicas
- Atributo conceitual é "o que essa entidade precisa guardar sobre si", não "coluna de banco com tipo SQL" — isso é `data-model.md`. Se o usuário pedir os dois, gere este primeiro e derive o outro a partir dele, deixando explícito o que foi herdado.
- Invariantes devem estar ligadas a uma `BR-xx` sempre que possível — um invariante sem regra de negócio correspondente é sinal de que ou falta registrar essa regra no Blueprint, ou o invariante é uma suposição sua que não deveria estar aqui.
