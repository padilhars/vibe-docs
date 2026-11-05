# Checkpoint de Revisão (obrigatório)

## Por que isso não é opcional

Consolidar o Blueprint sem esse passo é o momento em que mais informação se perde silenciosamente — proposições que ninguém decidiu viram "definidas" por omissão, ou pendências reais somem porque a conversa seguiu em frente. O checkpoint custa um parágrafo e evita descobrir um buraco no meio da geração de um documento importante. Rode este checkpoint **antes de toda consolidação inicial e antes de toda alteração de decisão em um projeto já consolidado** — não só na primeira vez.

## O formato

Organize tudo que foi discutido em quatro categorias e apresente ao usuário antes de escrever o `PROJECT.md`:

```
🟢 Definido
[tudo que tem decisão clara e foi confirmado ou não contestado pelo usuário]

🟡 Pendente
[perguntas que ficaram sem resposta, com uma nota se são críticas ou não]

🔵 Sugestões futuras
[proposições feitas durante o Concept que não foram aceitas nem rejeitadas explicitamente]

🔴 Inconsistências
[qualquer contradição entre coisas ditas em momentos diferentes da conversa que não foi resolvida na hora]
```

## Regra para cada categoria

- **🟢 Definido**: só entra aqui o que o usuário afirmou diretamente ou aceitou explicitamente depois de uma proposição sua. Não promova algo de 🔵 para 🟢 só porque parecia uma boa ideia.
- **🟡 Pendente**: separe pendências **críticas** (bloqueiam a maioria dos documentos derivados) de **menores** (afetam só um documento específico). Isso já antecipa o que vai aparecer em `maturity.md`.
- **🔵 Sugestões futuras**: inclui todo achado de pesquisa (`concept/prior-art.md`) que o usuário não decidiu explicitamente — pesquisa revela possibilidade, não decisão. Nunca descarte silenciosamente — mesmo que pareça óbvio que o usuário não quis aquilo, registre para se decidir depois.
- **🔴 Inconsistências**: explique o conflito em uma frase e pergunte qual versão deve prevalecer. Não resolva por conta própria escolhendo a que parece mais razoável.

## Duas verificações rápidas antes de escrever o Blueprint

Independente das quatro categorias acima, confira estes dois pontos — são os que mais passam batido e os mais caros de corrigir depois:

1. **Toda permissão tem uma identidade que a sustente?** Se a matriz de permissões distingue o que um ator pode fazer com o próprio registro versus o de outro, mas nunca foi dito como o sistema diferencia um ator do outro, isso é uma lacuna a resolver agora (ver `references/concept/questioning.md`).
2. **Todo ator tem um caminho de criação definido?** Para cada ator da seção 5, pergunte como a conta dele passa a existir. É comum o ator principal ter um cadastro bem desenhado enquanto os internos (secretária, operador, admin) nunca ganham um — e a falta só aparece muito depois, quando alguém tenta montar o backlog e descobre que não há como criar o primeiro usuário. Isso vale também para o primeiro admin, que normalmente precisa de seed, não de tela.
3. **Toda funcionalidade serve a algum objetivo?** Se alguma `FUN-xx` não se liga a nenhum `OBJ-xx`, ou o escopo esticou, ou falta registrar um objetivo. Levante o ponto — é o que evita um MVP sem critério de corte depois.

## Depois de apresentar o checkpoint

Se houver pendência crítica ou inconsistência, pergunte diretamente se o usuário quer resolvê-la agora ou consolidar mesmo assim (nesse caso, ela vira uma pendência crítica registrada na seção 16 do `PROJECT.md`, não um vazio silencioso). Só escreva ou atualize o `PROJECT.md` depois que o usuário confirmar que o checkpoint está correto.
