# Data Model — Modelo de Dados

## Propósito
Derivar do Modelo de Domínio (ou diretamente das entidades do Blueprint, se o Domain Model ainda não foi gerado) uma representação lógica pronta para virar schema de banco de dados.

## Insumos necessários do Blueprint
Entidades, relacionamentos, regras de negócio que impliquem restrição de dado (unicidade, obrigatoriedade). `domain-model.md`, se já existir, deve ser a base direta.

## Estrutura obrigatória

```markdown
# Modelo de Dados — [Nome do Projeto]

## Entidades

### ENT-xx — [Nome] → tabela `[nome_tabela]`
| Campo | Tipo | Obrigatório | Restrições | Origem |
|---|---|---|---|---|
| id | uuid/serial | sim | chave primária | convenção |
| [campo] | [tipo] | [sim/não] | [unique, etc.] | [ENT-xx / BR-xx / convenção] |

## Relacionamentos e Chaves Estrangeiras
[ENT-xx.campo → ENT-yy.id, com cardinalidade]

## Índices
[só quando houver justificativa — ex.: campo usado com frequência em busca/filtro segundo os fluxos do Blueprint]

## Auditoria
[quando necessário: created_at, updated_at, e se o domínio exigir histórico de mudanças — ligar isso a uma BR-xx quando existir, ou à seção de riscos se for por exigência de dado sensível]
```

## Regras específicas
- Campos de convenção (id, `created_at`, `updated_at`) não precisam de justificativa explícita no Blueprint — são práticas padrão. Qualquer outro campo deve ser rastreável a uma entidade, atributo ou regra de negócio já definida; se não for, é invenção e deve ser evitada (ver `_shared-rules.md`).
- Tipo de dado é uma decisão técnica que pode não estar no Blueprint — é aceitável inferir tipos óbvios (texto curto, data, booleano) sem tratar isso como pendência, mas decisões menos óbvias (ex.: como representar dinheiro, timezone) devem ser explicitadas como decisão tomada aqui, não silenciosamente assumidas.
