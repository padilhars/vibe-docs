# LEARNINGS.md — Aprendizados da implementação

## Propósito
Guardar o que a implementação ensinou e que não está em nenhum outro documento: a armadilha do ambiente que custou uma hora, o padrão que o projeto adotou e onde está o exemplo, a abordagem que foi tentada e não funcionou. É o que permite encerrar uma sessão, abrir outra dias depois e não reaprender tudo.

O `STATE.md` responde "onde estamos". Este responde "o que já sabemos sobre construir este sistema".

## Por que um arquivo no repositório, se o Claude Code já tem memória

O Claude Code mantém uma memória automática própria, mas ela fica na máquina de quem está rodando, fora do repositório: não é versionada, não acompanha o projeto para outro computador e não é vista por outra pessoa da equipe. Este arquivo é o complemento versionado — vai junto com o código, aparece no histórico do git e pode ser revisado. Os dois convivem; o que importa para o projeto, e não só para aquela máquina, vem para cá.

## O risco, e as regras que o evitam

Um arquivo de aprendizados sem disciplina vira diário: cresce a cada sessão, ninguém lê, e passa a contradizer os documentos. Como ele é importado com `@` pelo `CLAUDE.md` — carregado inteiro em toda sessão — crescer sem limite custa contexto em todas elas. As regras abaixo vão escritas no topo do próprio arquivo, porque quem o mantém é o agente de implementação, que não lê esta skill.

## Estrutura obrigatória

```markdown
# Aprendizados — [Nome do Projeto]

<!-- Regras deste arquivo (para quem o mantém):
- Registre só o que uma próxima sessão precisaria saber e não descobriria lendo o código ou os documentos de docs/.
- Uma linha por aprendizado, na seção certa. Sem data, sem narrativa de como foi descoberto.
- Antes de acrescentar, veja se já existe um item sobre o assunto: atualize-o em vez de criar outro.
- Limite: 100 linhas. Ao chegar perto, corte o que deixou de valer e junte o que se repete.
- Decisão de negócio não entra aqui: pergunte ao usuário, e a resposta vai para docs/PROJECT.md.
- Onde a implementação está não entra aqui: é docs/STATE.md.
- Se um item contradiz um documento de docs/, o documento vence; avise o usuário sobre a divergência.
-->

## Armadilhas do ambiente
[o que falha de forma não óbvia e como contornar. Ex.: "A suíte de integração exige o banco de teste no ar: `docker compose up db-test` antes de `npm test`."]

## Padrões estabelecidos
[como este projeto faz as coisas, com o arquivo que serve de exemplo. Ex.: "Validação de entrada: schema zod ao lado da rota — ver `src/rotas/emprestimos.ts`."]

## O que não funcionou
[abordagem tentada e abandonada, com o motivo em uma frase — para não ser tentada de novo.]

## Decisões técnicas de implementação
[escolhas pequenas feitas durante o código que a arquitetura não cobre. Ex.: "Datas trafegam em ISO-8601 UTC; conversão para horário local só na interface."]
```

## Versão inicial

As quatro seções vazias, com o bloco de regras no topo. Como no `STATE.md`, a convenção precisa existir antes de ser útil.

Se o projeto parte de código já existente (ver `concept/existing-codebase.md`), a versão inicial pode já trazer em "Padrões estabelecidos" o que foi observado no repositório — com o arquivo de exemplo, não de memória.

## Regras específicas

- **Não leva frontmatter nem versão**, pelo mesmo motivo do `STATE.md`: é mantido pelo agente, não derivado de uma versão do Blueprint.
- **Gere junto com o `CLAUDE.md` e o `STATE.md`.** A rotina de fim de tarefa do `CLAUDE.md` manda atualizar este arquivo; ele precisa existir desde a primeira sessão. No layout final, vive em `docs/LEARNINGS.md`.
- **Aprendizado que virou regra permanente sobe para o `CLAUDE.md`.** Se um item de "Padrões estabelecidos" passou a valer para todo o projeto, o lugar dele é a seção de Convenções — proponha a mudança ao usuário em vez de manter nos dois lugares.
- **Decisão técnica que muda a arquitetura não fica só aqui.** Trocar de biblioteca, mudar a forma de persistência ou alterar um contrato de API é alteração de decisão: volta para o Blueprint pelo fluxo normal.
