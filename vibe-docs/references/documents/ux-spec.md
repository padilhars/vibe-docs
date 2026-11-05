# UX Specification

## Propósito
Descrever a experiência do usuário derivada dos atores, casos de uso e fluxos já definidos. Este arquivo cobre em conjunto o que às vezes é pedido separadamente como "jornada do usuário", "arquitetura de informação", "especificação de tela" ou "especificação de interação" — se o usuário pedir só uma dessas partes, gere apenas a seção correspondente da estrutura abaixo.

## Insumos necessários do Blueprint
Atores, casos de uso, fluxos, entidades (para saber que informação cada tela precisa mostrar).

## Estrutura obrigatória

```markdown
# UX Spec — [Nome do Projeto]

## Jornadas de Usuário
[uma por ator relevante: sequência de telas/passos que ele percorre para atingir seu objetivo principal — deriva dos UC-xx daquele ator]

## Arquitetura de Informação
[como as telas se organizam entre si — hierarquia de navegação, não o design visual de cada uma]

## Especificação de Telas
### Tela: [nome]
- **Objetivo:** [o que o usuário realiza aqui]
- **Usuário:** [ator(es) que acessam]
- **Informações exibidas:** [dados que a tela mostra, derivados das entidades]
- **Ações disponíveis:** [o que o usuário pode fazer aqui]
- **Estados:** [vazio, carregando, erro, sucesso — o que muda visualmente em cada um]
- **Navegação:** [para onde cada ação leva]

## Especificação de Interação
[padrões de interação que se repetem entre telas — confirmação antes de ação destrutiva, feedback de ação concluída, etc.]

## Acessibilidade
[requisitos básicos aplicáveis, quando o Blueprint tiver informação suficiente para isso — senão, registrar como pendência]
```

## Regras específicas
- Não desenhe uma tela só para preencher espaço — cada tela listada deve corresponder a um caso de uso ou funcionalidade real do Blueprint.
- Estados de erro e vazio de cada tela devem remeter aos casos de borda já registrados (Blueprint seção 10 / `edge-cases.md`) em vez de inventar um comportamento novo aqui.
