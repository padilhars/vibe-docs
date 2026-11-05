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

## O corte volta para o Blueprint

Este é o único documento que legitimamente **estreita** algo que o Blueprint já afirmava — e por isso tem uma obrigação que os outros não têm: depois de definir o recorte, escreva-o de volta na seção 4 do `PROJECT.md`, no campo "Recorte do MVP".

Sem isso, a seção 4 continua listando como escopo o que o MVP acabou de excluir, e o `CLAUDE.md` — que lê o Blueprint — vai mandar o agente não implementar exatamente aquilo que o Blueprint diz estar no escopo. O agente segue o CLAUDE.md, mas quem lê o Blueprint entende o contrário, e a divergência só aparece quando alguém compara os dois.

Escrever o corte de volta não é atualizar o escopo do projeto: o que estava no escopo continua lá. É registrar, lado a lado, o que fica para a primeira versão.


## Verificação obrigatória ao terminar

Rode `scripts/check_coverage.py <pasta-do-projeto>` antes de entregar. Este é um documento agregador: ele precisa refletir decisões tomadas ao longo de todo o projeto, e uma ausência aqui não aparece na leitura — o documento parece completo justamente porque o que falta não está nele. Resolva o que o script apontar (incluindo declarar exclusões deliberadas) antes de considerar o documento pronto.
## Regras específicas
- Nunca invente uma funcionalidade nova aqui — classifique somente as que já existem no Blueprint (`FUN-xx`). Se o Blueprint não tem funcionalidade suficiente para resolver o problema central mesmo num recorte mínimo, isso é uma lacuna do Blueprint, não algo para preencher no MVP.
- Classifique cada funcionalidade considerando: ela é necessária para o fluxo principal funcionar de ponta a ponta? Alguma outra funcionalidade incluída depende dela? Qual a complexidade de implementar comparada ao valor que entrega sozinha?
- "Fora do MVP" deve ser tão explícito quanto "Incluído" — omitir isso é a causa mais comum de escopo do MVP crescer sem controle depois.
