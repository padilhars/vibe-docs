# Do Blueprint ao Claude Code

O fim do pipeline é um repositório de código onde o Claude Code implementa sem precisar adivinhar. Três peças fazem isso funcionar.

## 1. `CLAUDE.md` — o contrato

Não é documentação: é um contrato de comportamento, com menos de ~200 linhas, em que cada linha muda alguma decisão do agente. Contém:

- **Comandos** (instalar, rodar, testar), tirados do Setup & Runbook;
- **Regras invioláveis** e **Definition of Done**, inline, das seções 20 e 21 do Blueprint;
- **Início e fim de sessão**: ler o `STATE.md` ao começar, sobrescrevê-lo ao terminar;
- **Precedência quando os documentos discordam**: decisão do usuário na sessão → `PROJECT.md` → derivados → código existente. Em conflito que envolva regra de negócio, permissão ou dado pessoal, o agente **para e pergunta**;
- **Limites de escopo**: o que não implementar nesta fase;
- **Nunca faça**: enfraquecer teste, adicionar dependência sem aprovação, engolir erro, refatorar fora de escopo, validar só no cliente;
- **Imports** (`@ARCHITECTURE.md`, `@BACKLOG.md`…) para os documentos profundos, carregados sob demanda.

## 2. `STATE.md` — a memória entre sessões

Diz onde a implementação está: tarefa em andamento, concluídas recentes, próximas, bloqueios, questões em aberto. É o único documento que o agente mantém. Nasce junto com o `CLAUDE.md`.

## 3. `handoff_check.py` — o portão

Peça *"está pronto pro Claude Code?"* antes de começar. Bloqueios comuns: pendência crítica aberta, seções 20/21 vazias, import apontando para arquivo inexistente.

## Montando o repositório

O `CLAUDE.md` precisa ficar **na raiz do repositório de código**. Os imports são relativos a esse destino:

```
meu-sistema/
├── CLAUDE.md          ← imports apontam para docs/
├── STATE.md
├── docs/
│   ├── PROJECT.md
│   ├── ARCHITECTURE.md
│   ├── DATA-MODEL.md
│   ├── BACKLOG.md
│   └── ...
└── src/
```

Se a documentação for para `docs/`, avise a skill ao gerar o `CLAUDE.md` para que os imports saiam como `@docs/ARCHITECTURE.md`.

## Durante a implementação

- Mudou uma decisão? Volte à skill (ou peça ao próprio Claude Code com a skill instalada) para alterar o Blueprint e propagar — não edite só o código.
- Uma skill de guardrails específica do projeto, com os princípios que nunca podem ser violados, complementa bem o `CLAUDE.md` para tarefas sensíveis (pagamento, dado pessoal, permissões).
- Rode `check_staleness.py` periodicamente: documento desatualizado é o que leva o agente a implementar a versão antiga de uma regra.
