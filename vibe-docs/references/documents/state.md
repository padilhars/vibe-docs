# STATE.md — Estado da implementação

## Propósito
Todos os outros documentos descrevem o que o sistema **deve ser**. Este descreve onde a implementação **está agora**: qual tarefa está em andamento, o que acabou de ser concluído, o que travou.

Ele existe porque implementação assistida por IA acontece em sessões curtas e independentes. Sem um estado escrito, cada sessão nova começa cega — relê o backlog inteiro, não sabe se a TASK-012 ficou pela metade, não sabe que a TASK-015 está bloqueada esperando uma credencial. O histórico da conversa anterior não está disponível, e não deveria ser a ponte mesmo quando está.

## O que torna este documento diferente

Junto com o `LEARNINGS.md`, é um dos dois arquivos que a vibe-docs cria para **o agente de implementação manter**. A skill gera a versão inicial e a convenção; a partir daí quem escreve nele é o agente, ao fim de cada tarefa (ver a rotina em `claude-md.md`).

Três consequências:
- **É sobrescrito, nunca acumulado.** Estado é o agora. O histórico fica no git — se este arquivo virar um diário, ninguém lê e ele para de cumprir a função.
- **Cabe numa tela.** Ele é importado com `@` pelo `CLAUDE.md`, ou seja, carregado inteiro em toda sessão. Se não couber numa tela, virou relatório: corte.
- **Não leva frontmatter nem versão.** Não é derivado de uma versão do Blueprint, e os scripts o deixam fora da comparação de versões.

## Insumos necessários
Backlog (primeira tarefa da fase atual) e seção 22 do Blueprint. Gere junto com o `CLAUDE.md` e o `LEARNINGS.md`, no fim do pipeline. No layout final, vive em `docs/STATE.md`.

## Estrutura obrigatória

```markdown
# Estado — [Nome do Projeto]

**Atualizado em:** [data] · **Fase:** [da seção 22 do Blueprint] · **Onda:** [do Backlog]

## Em andamento
[a tarefa sendo implementada agora, com o ID, e em que ponto ela está. "Nenhuma" se a última tarefa fechou limpa.]

## Concluídas recentemente
[as 3 a 5 últimas, com ID. As antigas saem daqui — o backlog guarda o status completo.]

## Próximas
[as 2 ou 3 seguintes, na ordem do backlog]

## Bloqueios
[o que impede o avanço e de quem depende. Vazio é o estado normal.]

## Questões em aberto
[dúvidas que surgiram implementando e precisam de decisão humana.]
```

## Versão inicial

Antes da primeira linha de código, o arquivo registra que o projeto está documentado e não iniciado: "Em andamento: nenhuma", a primeira tarefa do backlog em "Próximas", e as demais seções vazias. Parece trivial, e é exatamente o ponto — a convenção precisa existir antes de ser útil, senão a primeira sessão de implementação nunca a cria.

## Regras específicas

- **Não duplique o backlog.** O backlog tem todas as tarefas e o status de cada uma, e a rotina de fim de tarefa manda marcá-lo antes de atualizar este arquivo. Aqui fica só o recorte do momento. Se os dois divergirem, o backlog vence.
- **Não registre decisão de negócio aqui.** Decisão vai para o Blueprint; aqui fica, no máximo, a pergunta ainda não respondida. Uma questão em aberto que seja decisão de negócio deve ser levada ao usuário, e a resposta entra no `PROJECT.md` pelo fluxo de alteração de decisão.
- **Não registre aprendizado aqui.** O que a implementação ensinou vai para o `LEARNINGS.md`, que acumula; este arquivo é sobrescrito e perderia.
