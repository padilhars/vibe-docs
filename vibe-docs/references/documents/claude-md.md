# CLAUDE.md — Contrato de comportamento para o Claude Code

## Propósito
Este é o artefato final do pipeline. Diferente de todos os outros documentos, ele não existe pra ser lido por uma pessoa que quer entender o projeto — existe porque o Claude Code carrega automaticamente o arquivo `CLAUDE.md` da raiz do repositório no início de toda sessão. É o único documento do pipeline que chega ao agente sem ninguém precisar apontar pra ele.

Isso muda completamente como ele deve ser escrito.

## A regra que define este documento

**CLAUDE.md não é documentação — é um contrato de comportamento.** Cada linha precisa mudar o que o agente faz. Se uma linha não muda nenhuma decisão de implementação, ela está gastando context window à toa e deve sair.

Consequência prática: mantenha abaixo de ~200 linhas. Não resuma a arquitetura inteira aqui, não repita o modelo de dados, não reconte os casos de uso. Aponte pros documentos que já têm isso (ver "Imports" abaixo) e reserve o espaço deste arquivo pro que o agente precisa saber *sempre*, em toda tarefa, sem exceção.

Se você se pegar escrevendo um parágrafo explicativo, provavelmente ele pertence a outro documento e aqui deveria virar uma linha imperativa mais um import.

## Onde este arquivo vive

Diferente dos outros documentos, que ficam na pasta do projeto de documentação, o `CLAUDE.md` precisa ficar **na raiz do repositório de código** pra ser carregado automaticamente. Gere na pasta do projeto normalmente, mas diga isso ao usuário explicitamente ao entregar: o arquivo deve ser copiado pra raiz do repo, e os caminhos dos imports precisam ser relativos a esse destino final, não à pasta de documentação.

Se os documentos derivados forem ficar numa subpasta do repo (ex.: `docs/`), os imports devem refletir isso: `@docs/ARCHITECTURE.md`.

## Antes de gerar: feche as seções 20 e 21

O `CLAUDE.md` é normalmente o último documento do pipeline, e é quando as seções 20 (Princípios) e 21 (Definition of Done e Convenções) precisam estar resolvidas — elas entram inline aqui, e um contrato que diz `PENDENTE` onde deveria dizer o que fazer é quase inútil para o agente. Se ainda estiverem em aberto, resolva-as antes (ver `deepening.md`), com o mesmo mecanismo de palpite embutido de sempre.

## Gere o STATE.md junto

O `CLAUDE.md` manda ler e atualizar o `STATE.md` em toda sessão, então os dois nascem juntos no fim do pipeline — um import apontando para um arquivo inexistente é pior que não ter a instrução. Ver `state.md`.

## Insumos necessários
Idealmente todos os documentos já gerados. Se faltar algum dos essenciais pra implementação autônoma (Architecture, Data Model, Backlog, Test Strategy, Setup & Runbook), avise antes de gerar — um CLAUDE.md que importa arquivo inexistente é pior que um curto, porque o agente segue um ponteiro que não leva a lugar nenhum.

## Sem frontmatter

Diferente de todos os outros documentos, o `CLAUDE.md` **não leva bloco de metadados YAML**. Ele começa direto no título. Metadados servem para uma pessoa rastrear a origem de um documento; aqui, cada linha que não muda o comportamento do agente é context window gasta à toa em um arquivo carregado em toda sessão.

## Estrutura obrigatória

```markdown
# [Nome do Projeto]

[Uma frase: o que é o sistema e pra quem.]

## Comandos

| Ação | Comando |
|---|---|
| Instalar dependências | `[comando]` |
| Rodar em desenvolvimento | `[comando]` |
| Rodar testes | `[comando]` |
| Lint / formatação | `[comando]` |
| Build | `[comando]` |

## Regras invioláveis

[Os Princípios Não-Negociáveis da seção 20 do Blueprint, cada um em uma linha imperativa, começando pelo ID: `- (PRINC-01) Nenhum tenant acessa dado de outro tenant...`. O ID é o que permite ir do agente de volta ao Blueprint, e é o que os scripts de rastreabilidade conseguem verificar. Se um princípio precisa de explicação pra ser entendido, ele está mal escrito no Blueprint — corrija lá, não aqui.]

## Convenções

[Nomenclatura, estrutura de pastas, padrão de commit — só o que o agente precisa seguir ao escrever código. Da seção 21 do Blueprint.]

## Definition of Done

[O que precisa ser verdade antes de considerar qualquer tarefa concluída. Da seção 21 do Blueprint.]

## Início e fim de sessão

No início: leia @STATE.md para saber em que ponto a implementação está — qual tarefa ficou em andamento, o que travou, o que vem a seguir. Não reconstrua isso lendo o backlog inteiro.

No fim: sobrescreva @STATE.md com a situação nova (tarefa atual, concluídas recentes, próximas, bloqueios, questões em aberto). Sobrescreva, não acrescente — o histórico fica no git.

Essas duas linhas são o que faz uma sessão se conectar à seguinte sem depender da conversa anterior.

## Quando os documentos discordam

Precedência, da mais forte para a mais fraca:
1. Uma decisão que o usuário acabou de tomar nesta sessão.
2. @PROJECT.md (o Blueprint) — fonte primária de verdade.
3. Os demais documentos, que são derivações dele.
4. O código e os testes existentes, que mandam sobre *como* algo já foi feito.

O @STATE.md fica fora dessa escala: ele registra onde a implementação está, não o que o sistema deve ser. Se o estado contradisser um documento, o documento vence e o estado está desatualizado.

**Em qualquer conflito que envolva regra de negócio, permissão ou dado pessoal: pare e pergunte. Não escolha.** Uma contradição nesses temas significa que uma das duas versões nunca foi decidida, e escolher sozinho transforma um documento desatualizado em comportamento implementado.

Para contradição que não toca regra de negócio (uma convenção de nome divergente, por exemplo), siga a precedência acima e diga em uma linha qual você seguiu e por quê.

## Limites de escopo

[O que NÃO implementar: funcionalidades fora do MVP ou da fase atual, tecnologias descartadas. Sem isso explícito, um agente tende a implementar "de brinde" o que parece faltar.

Tire isso da seção 22 do Blueprint (Fase Atual) combinada com o campo "Recorte do MVP" da seção 4 — não do `MVP.md` diretamente. Se o projeto já passou da primeira fase, é a seção 22 que manda: o que ficou para trás no MVP pode ter entrado na fase corrente. Se os dois divergirem, ou se o campo ainda estiver PENDENTE apesar de o MVP existir, pare e sinalize: escrever aqui um limite que o Blueprint não confirma cria a pior contradição possível do projeto, porque este arquivo é o que o agente lê primeiro e obedece.]

## Nunca faça

- Enfraquecer, remover ou "ajustar" um teste para ele passar. Teste que falha é informação — se o teste está errado, diga qual e por quê, e espere resposta.
- Adicionar dependência nova sem aprovação explícita. Confirme que o pacote existe e é o que você pensa: nomes parecidos com pacotes legítimos são um vetor de ataque conhecido, e um pacote inventado com nome plausível é um erro frequente de código gerado por IA.
- Capturar exceção sem tratá-la, nem engolir erro em `try/catch` silencioso.
- Refatorar o que a tarefa não pediu, ainda que o código pareça melhorável — proponha separadamente.
- Validar só no cliente. Toda regra de negócio é verificada no servidor, mesmo quando a interface já impede.

## Documentação de referência

Arquitetura e decisões técnicas: @ARCHITECTURE.md
Modelo de dados: @DATA-MODEL.md
Regras de negócio completas: @BUSINESS-RULES.md
Tarefas desta fase: @BACKLOG.md
Estratégia de testes: @TEST-STRATEGY.md
Estado da implementação: @STATE.md — leia no início e atualize no fim de toda sessão.
Setup e ambiente: @SETUP-RUNBOOK.md

[Ajuste a lista ao que realmente existe. Cada linha deve dizer quando vale abrir aquele arquivo, não só nomeá-lo.]
```


## Verificação obrigatória ao terminar

Rode `scripts/check_coverage.py <pasta-do-projeto>` antes de entregar. Este é um documento agregador: ele precisa refletir decisões tomadas ao longo de todo o projeto, e uma ausência aqui não aparece na leitura — o documento parece completo justamente porque o que falta não está nele. Resolva o que o script apontar (incluindo declarar exclusões deliberadas) antes de considerar o documento pronto.
## Regras específicas

- **Corte sem dó.** Se estiver na dúvida se uma linha merece estar aqui, pergunte: "sem esta linha, o agente faria algo diferente?" Se a resposta for não, tire.
- **Comandos são a seção mais valiosa e a mais frequentemente esquecida.** Um agente que não sabe rodar os testes não consegue verificar o próprio trabalho. Se o Setup & Runbook ainda não existe e ninguém decidiu esses comandos, isso é uma lacuna a resolver antes de gerar (ver `deepening.md`), não algo pra deixar em branco.
- **Nunca invente comando.** Se a stack ainda não foi decidida, o comando não existe — registre como pendência em vez de escrever um `npm test` genérico que pode nem se aplicar.
- **Imports não substituem as regras invioláveis.** Princípio de segurança e limite de escopo ficam inline, mesmo ocupando espaço: são o que mais previne dano quando o agente decide sozinho.
- Este documento nunca implementa nada — produz só o contrato. Se o usuário pedir pra "já começar a implementar" junto, gere o CLAUDE.md primeiro, deixe claro que está pronto, e trate a implementação como pedido separado (fora do escopo desta skill).
