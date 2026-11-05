# Use Case Specification — Especificação de Casos de Uso

## Propósito
Formalizar cada caso de uso do Blueprint (que ali é só um resumo) em uma especificação completa, com pré-condições, fluxo principal, fluxos alternativos e pós-condições — o nível de detalhe que costuma faltar quando alguém tenta implementar um caso de uso a partir só do resumo do PROJECT.md.

## Insumos necessários do Blueprint
Os casos de uso (`UC-xx`), os atores envolvidos, as regras de negócio e os estados relacionados a cada um.

## Estrutura obrigatória (por caso de uso)

```markdown
### UC-xx — [Nome do Caso de Uso]

**Ator principal:** [ator]
**Objetivo:** [o que o ator quer alcançar]
**Pré-condições:** [o que precisa ser verdade antes de começar]

**Fluxo principal:**
1. [passo]
2. [passo]
...

**Fluxos alternativos:**
- A1 — [condição]: [o que muda no fluxo]

**Fluxos de exceção:**
- E1 — [condição de erro]: [o que o sistema faz]

**Pós-condições:** [o que é verdade depois do caso de uso concluído com sucesso]

**Regras de negócio aplicáveis:** [BR-xx]
```

## Regras específicas
- Repita esta estrutura para cada caso de uso pedido — se o usuário pedir "os casos de uso do sistema", gere para todos os `UC-xx` do Blueprint; se pedir um específico, gere só esse.
- Fluxos alternativos e de exceção costumam não estar totalmente detalhados no Blueprint (que geralmente só tem o fluxo principal). Isso é esperado: use `references/concept/edge-cases.md` como checklist mental do que perguntar, mas não invente a resposta — se não tiver sido discutido, registre como pendência específica daquele caso de uso.
