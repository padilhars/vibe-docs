# API Specification

## Propósito
Definir os endpoints necessários para os comportamentos já identificados no Blueprint — não é uma oportunidade de desenhar uma API "completa e genérica"; cada endpoint deve existir porque um caso de uso ou funcionalidade real precisa dele.

## Insumos necessários do Blueprint
Casos de uso, funcionalidades, entidades, permissões (seção 12), modelo de dados (se já gerado).

## Estrutura obrigatória (por endpoint)

```markdown
### [MÉTODO] /caminho/do/recurso

**Objetivo:** [o que este endpoint faz]
**Caso de uso relacionado:** UC-xx
**Autenticação:** [obrigatória / opcional / nenhuma]
**Autorização:** [quais atores podem chamar — deriva da matriz de permissões do Blueprint]

**Parâmetros / Request:**
| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|

**Response (sucesso):**
| Campo | Tipo | Descrição |
|---|---|---|

**Erros possíveis:**
| Código | Condição | BR-xx relacionada (se houver) |
|---|---|---|
```

## Regras específicas
- Não crie endpoint para funcionalidade que não existe no Blueprint. Se notar uma necessidade óbvia de endpoint auxiliar (ex.: listar salas antes de poder reservar uma), isso é DERIVADO de uma funcionalidade existente, não uma invenção — mas diga explicitamente que é derivado, não que veio direto do Blueprint.
- Erros possíveis devem, sempre que fizer sentido, remeter à regra de negócio que os motiva — um erro "409 Conflito" numa reserva, por exemplo, normalmente existe por causa de uma `BR-xx` específica sobre conflito de horário.
- Agrupe endpoints por recurso/entidade para facilitar leitura quando a API tiver muitos endpoints.
