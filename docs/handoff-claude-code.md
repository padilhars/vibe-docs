# Do Blueprint ao Claude Code

O fim do pipeline é um repositório de código onde o Claude Code implementa sem precisar adivinhar. Quatro peças fazem isso funcionar.

## 1. `CLAUDE.md` — o contrato

Não é documentação: é um contrato de comportamento, com menos de 200 linhas, em que cada linha muda alguma decisão do agente. Não leva frontmatter. Contém:

- **Comandos** (instalar, rodar, testar), tirados do Setup & Runbook;
- **Regras invioláveis** e **Definition of Done**, inline, das seções 20 e 21 do Blueprint;
- **Ao começar uma sessão**: o estado e os aprendizados, importados com `@docs/STATE.md` e `@docs/LEARNINGS.md`;
- **Ao terminar cada tarefa** e **Ao encontrar um bug**: as duas rotinas descritas abaixo;
- **Precedência quando os documentos discordam**: decisão do usuário na sessão → `PROJECT.md` → derivados → código existente. Em conflito que envolva regra de negócio, permissão ou dado pessoal, o agente **para e pergunta**;
- **Limites de escopo**: o que não implementar nesta fase, tirado da seção 22;
- **Nunca faça**: enfraquecer teste, adicionar dependência sem aprovação, engolir erro, refatorar fora de escopo, validar só no cliente;
- **Documentação de referência**: o caminho de cada documento profundo e a situação em que ele deve ser aberto.

### Por que só dois imports

No Claude Code, um arquivo importado com `@` é carregado **inteiro, em toda sessão**. Não é leitura sob demanda. Importar a arquitetura, o backlog e o Blueprint gastaria o contexto antes de a primeira tarefa começar. Por isso só o que é curto e necessário sempre é importado (`STATE.md` e `LEARNINGS.md`); os demais documentos são citados pelo caminho, sem `@`, com a indicação de quando abrir cada um.

### A rotina de fim de tarefa

Fixa em todo `CLAUDE.md`, executada a cada tarefa, não ao fim da sessão (uma sessão pode cair no meio):

1. rodar o comando de verificação e ler a saída;
2. conferir a Definition of Done item a item;
3. marcar a tarefa como concluída no `BACKLOG.md`;
4. sobrescrever o `STATE.md` com a situação nova;
5. registrar no `LEARNINGS.md` o que a tarefa ensinou, ou nada, se nada;
6. fazer o commit.

### O protocolo de bug

1. antes de alterar o código, escrever um teste que reproduz o bug e vê-lo falhar pelo motivo certo;
2. corrigir;
3. ver o teste passar e a verificação completa continuar passando;
4. manter o teste na suíte: é ele que impede o bug de voltar;
5. se a causa for uma armadilha que pode se repetir, registrar no `LEARNINGS.md`.

O `CLAUDE.md` é contexto, não imposição: o agente tende a segui-lo, mas nada o obriga. O Setup & Runbook orienta a garantir a verificação também por gancho do Claude Code ou CI, que é o que de fato impede um commit com teste falhando.

## 2. `STATE.md` — onde a implementação está

Tarefa em andamento, concluídas recentes, próximas, bloqueios, questões em aberto, onda atual. Curto, sobrescrito a cada tarefa. É o que permite fechar uma sessão e abrir outra sem perder o fio.

## 3. `LEARNINGS.md` — o que a implementação ensinou

O `STATE.md` diz *onde* o trabalho está; o `LEARNINGS.md` guarda *o que se aprendeu* fazendo: armadilhas do ambiente, padrões estabelecidos, o que não funcionou e decisões técnicas de implementação. É curado, não um diário: tem limite de 100 linhas e as regras de manutenção ficam no topo do próprio arquivo.

O Claude Code tem memória automática, mas ela fica na máquina de quem rodou a sessão. O `LEARNINGS.md` fica no repositório: é versionado, revisável e vale para qualquer pessoa ou máquina que continue o projeto. Os dois se complementam.

## 4. `handoff_check.py` — o portão

Peça *"está pronto pro Claude Code?"* antes de começar. A lista completa de bloqueios e avisos está em [Scripts](scripts.md#handoff_checkpy-pasta). Os mais comuns: pendência crítica aberta, seções 20/21 com item pendente, seção 22 sem as funcionalidades da fase, `CLAUDE.md` sem as rotinas ou apontando para arquivo que não existe.

## Montando o repositório

Durante a documentação, tudo fica numa pasta só. No handoff, o `CLAUDE.md` vai para a **raiz do repositório de código** e todo o resto para `docs/`:

```
meu-sistema/
├── CLAUDE.md          ← raiz: é onde o Claude Code o carrega
├── docs/
│   ├── PROJECT.md
│   ├── ARCHITECTURE.md
│   ├── BACKLOG.md
│   ├── ...
│   ├── STATE.md
│   └── LEARNINGS.md
└── src/
```

O `CLAUDE.md` já é gerado com os caminhos finais (`docs/...`), então não há nada para ajustar: mover os arquivos é o único passo manual. Depois disso, os scripts são rodados sobre `docs/` e encontram o `CLAUDE.md` na pasta acima.

## Skills que ajudam na implementação

Se quiser, peça *"que skills podem ajudar a implementar este projeto?"*. A skill pesquisa na hora, recomenda até cinco skills gratuitas e gera o `SKILLS-RECOMENDADAS.md` com origem, licença, o que cada uma acessa, onde se sobrepõe ao `CLAUDE.md` e o pedido de instalação pronto. Nada é instalado automaticamente: revise antes, porque uma skill instalada roda com as permissões que declara.

## Durante a implementação

- Mudou uma decisão? Volte à skill (ou peça ao próprio Claude Code com a skill instalada) para alterar o Blueprint e propagar — não edite só o código.
- Terminou a fase? Peça para encerrar a fase: o Backlog, os limites de escopo do `CLAUDE.md` e o `STATE.md` são regenerados para a fase seguinte.
- Uma skill de guardrails específica do projeto, com os princípios que nunca podem ser violados, complementa bem o `CLAUDE.md` para tarefas sensíveis (pagamento, dado pessoal, permissões).
- Rode `check_staleness.py` ao retomar o trabalho de documentação: documento desatualizado é o que leva o agente a implementar a versão antiga de uma regra.
