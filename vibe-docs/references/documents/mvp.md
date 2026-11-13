# MVP — Definição de Escopo Mínimo

## Propósito
Definir qual subconjunto das funcionalidades já definidas compõe a primeira versão funcional do sistema — não é "a menor quantidade possível de funcionalidades", é a menor versão que ainda resolve o problema central de ponta a ponta.

## Insumos necessários do Blueprint
Funcionalidades (com IDs), objetivos, problema, casos de uso principais. Idealmente o PRD já existe, mas não é pré-requisito.

## Estrutura obrigatória

```markdown
# MVP — [Nome do Projeto]

## Objetivo do MVP
[o que esta versão precisa provar ou resolver]

## Incluído
[lista de FUN-xx que compõem o MVP]

## Fora do MVP
[lista de FUN-xx explicitamente adiadas, com uma frase de justificativa cada]

## Justificativa da Divisão
[por que esse corte específico — que critério foi usado]

## Dependências entre Funcionalidades Incluídas
[o que precisa existir antes do quê]

## Limitações Conhecidas desta Versão
[o que o usuário final vai perceber como ausente]

## Critérios de Conclusão
[como saber que o MVP está pronto para lançar]
```

## Simule antes de cortar

Se o Blueprint ainda não passou por uma simulação de uso real (ver `blueprint/simulation.md`), este é o melhor momento para rodar uma — e vale oferecer ao usuário antes de propor o corte.

O motivo é prático: a simulação do dia 1 e da primeira semana mostra o que é de fato indispensável para o sistema funcionar de ponta a ponta, e isso é um argumento mais forte para incluir ou excluir uma funcionalidade do que a avaliação de importância relativa. Funcionalidade sem a qual a semana 1 não acontece está no MVP, independentemente de parecer secundária.

## O corte volta para o Blueprint

Este é o único documento que legitimamente **estreita** algo que o Blueprint já afirmava — e por isso tem uma obrigação que os outros não têm: depois de definir o recorte, escreva-o de volta no `PROJECT.md`, em dois lugares:

- **Seção 4**, campo "Recorte do MVP": as `FUN-xx` incluídas.
- **Seção 22** (Fase Atual): "Objetivo desta fase" com o objetivo do MVP e "Funcionalidades desta fase" com as mesmas `FUN-xx`. É desta seção que o Backlog e o `CLAUDE.md` tiram o que "desta fase" quer dizer, e ninguém mais a preenche.

Isso não sobe a versão do Blueprint: é o primeiro preenchimento de campos que estavam `PENDENTE` (ver "Quando a versão sobe" em `blueprint/schema.md`).

Sem a seção 4, o Blueprint continua listando como escopo o que o MVP acabou de excluir, e o `CLAUDE.md` — que lê o Blueprint — vai mandar o agente não implementar exatamente aquilo que o Blueprint diz estar no escopo. O agente segue o CLAUDE.md, mas quem lê o Blueprint entende o contrário, e a divergência só aparece quando alguém compara os dois.

Escrever o corte de volta não é atualizar o escopo do projeto: o que estava no escopo continua lá. É registrar, lado a lado, o que fica para a primeira versão.

## Verificação obrigatória ao terminar

Rode `scripts/check_coverage.py <pasta-do-projeto>` antes de entregar. Este é um documento agregador: ele precisa refletir decisões tomadas ao longo de todo o projeto, e uma ausência aqui não aparece na leitura — o documento parece completo justamente porque o que falta não está nele. Resolva o que o script apontar (incluindo declarar exclusões deliberadas) antes de considerar o documento pronto.

## Regras específicas
- Nunca invente uma funcionalidade nova aqui — classifique somente as que já existem no Blueprint (`FUN-xx`). Se o Blueprint não tem funcionalidade suficiente para resolver o problema central mesmo num recorte mínimo, isso é uma lacuna do Blueprint, não algo para preencher no MVP.
- Classifique cada funcionalidade considerando: ela é necessária para o fluxo principal funcionar de ponta a ponta? Alguma outra funcionalidade incluída depende dela? Qual a complexidade de implementar comparada ao valor que entrega sozinha?
- "Fora do MVP" deve ser tão explícito quanto "Incluído" — omitir isso é a causa mais comum de escopo do MVP crescer sem controle depois.
