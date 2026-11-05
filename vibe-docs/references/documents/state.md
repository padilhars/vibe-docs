# STATE.md — Estado da implementação

## Propósito
Todos os outros documentos descrevem o que o sistema **deve ser**. Este descreve onde a implementação **está agora**: qual tarefa está em andamento, o que acabou de ser concluído, o que travou.

Ele existe porque implementação assistida por IA acontece em sessões curtas e independentes. Sem um estado escrito, cada sessão nova começa cega — relê o backlog inteiro, não sabe se a TASK-012 ficou pela metade, não sabe que a TASK-015 está bloqueada esperando uma credencial. O histórico da conversa anterior não está disponível, e não deveria ser a ponte mesmo quando está.

## O que torna este documento diferente de todos os outros

É o único que a vibe-docs cria para **outra pessoa manter**. A skill gera a versão inicial e a convenção; a partir daí quem escreve nele é o agente de implementação, ao fim de cada sessão.

Duas consequências:
- **É sobrescrito, nunca acumulado.** Estado é o agora. O histórico fica no git e no `PROJECT.md` (seção 18) — se este arquivo virar um diário, ninguém lê e ele para de cumprir a função.
- **Cabe numa tela.** Se não couber, é porque virou relatório. Corte.

## Insumos necessários
Backlog (primeira tarefa da fase atual) e seção 22 do Blueprint (fase atual). Gere junto com o `CLAUDE.md`, no fim do pipeline — os dois formam o par que uma sessão de implementação lê para se situar.

## Estrutura obrigatória

```markdown
# Estado — [Nome do Projeto]

**Atualizado em:** [data] · **Fase:** [da seção 22 do Blueprint]

## Em andamento
[a tarefa sendo implementada agora, com o ID. "Nenhuma" se a última sessão fechou limpa.]

## Concluídas recentemente
[as 3 a 5 últimas, com ID. As antigas saem daqui — o backlog guarda o status completo.]

## Próximas
[as 2 ou 3 seguintes, na ordem do backlog]

## Bloqueios
[o que impede o avanço e de quem depende. Vazio é o estado normal — bloqueio aqui é exceção, não lista de desejos.]

## Questões em aberto
[dúvidas que surgiram implementando e precisam de decisão humana. Cada uma vira pendência no Blueprint se for decisão de negócio.]
```

## Versão inicial

Antes da primeira linha de código, o arquivo registra que o projeto está documentado e não iniciado: "Em andamento: nenhuma", a primeira tarefa do backlog em "Próximas", e as demais seções vazias. Parece trivial, e é exatamente o ponto — a convenção precisa existir antes de ser útil, senão a primeira sessão de implementação nunca a cria.

## Regras específicas

- **Não duplique o backlog.** O backlog tem todas as tarefas e o status de cada uma; este arquivo tem só o recorte do momento. Se os dois divergirem, o backlog vence.
- **Não registre decisão de negócio aqui.** Decisão vai para o Blueprint, que é a fonte de verdade; aqui fica, no máximo, a pergunta ainda não respondida.
- **O `CLAUDE.md` precisa mandar ler este arquivo no início da sessão e atualizá-lo no fim.** Sem essas duas instruções, o arquivo nasce e morre na versão inicial (ver `claude-md.md`).
