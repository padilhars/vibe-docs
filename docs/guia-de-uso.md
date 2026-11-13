# Guia de uso

A skill trabalha em três etapas. Você decide quando passar de uma para a outra; ela nunca avança sozinha.

```
 Concept ──(você: "vamos fechar")──► Blueprint ──(você: "gera o PRD")──► Files-Gen
 conversa                             PROJECT.md                          documentos
```

## 1. Concept — descobrir

**Como começar:** apresente o problema real e a ideia de solução. Quanto mais concreto o problema, melhor.

> Tenho uma clínica de psicologia com 6 profissionais. A secretária perde a manhã inteira confirmando consultas por WhatsApp e ainda temos 20% de falta. Queria um sistema de agendamento com confirmação automática.

**O que esperar:**

- Perguntas em rodadas curtas, cada uma com um **palpite embutido** ("imagino que o paciente possa remarcar até 24h antes — é isso?"). Reagir a um palpite é mais rápido que preencher campo em branco.
- **Proposições**: a skill sugere coisas que você talvez não tenha pensado. Concordar, recusar ou contrapor é tão útil quanto responder.
- Nas rodadas do meio, casos de borda (conflito de horário, cancelamento tardio, permissões) e uma pesquisa do que sistemas do mesmo domínio tiveram de resolver — que volta como pergunta, nunca como funcionalidade adicionada por conta própria.
- Se você contradisser algo dito antes, ela aponta na hora.

**O que não acontece:** nenhum arquivo é gerado. O Concept é só conversa, e o `PROJECT.md` só nasce na consolidação.

Se já existe código, avise ou aponte a pasta: a skill lê o que dá para descobrir sozinha antes de perguntar.

## 2. Blueprint — consolidar

**Como pedir:** *"temos o suficiente, vamos consolidar"*, *"gera o blueprint"*, *"vamos fechar"*.

Antes de escrever qualquer coisa, a skill apresenta o **checkpoint** — obrigatório mesmo com pressa:

| | Categoria | O que entra |
|---|---|---|
| 🟢 | Definido | O que você afirmou ou aceitou explicitamente |
| 🟡 | Pendente | Perguntas sem resposta, separadas em críticas e menores |
| 🔵 | Sugestão futura | Propostas nem aceitas nem recusadas, achados de pesquisa |
| 🔴 | Inconsistência | Contradições não resolvidas — você escolhe qual vale |

Com o checkpoint confirmado, vem a **simulação de uso real**: a skill narra o sistema funcionando nos primeiros dias, com atores concretos, procurando onde quebra (o sistema vazio no dia 1, alguém que faz fora de ordem, uma operação largada no meio). O relato separa o que exige decisão sua do que é correção direta, sempre com exemplo e correção proposta. Se não achar nada, ela diz isso explicitamente.

Só então ela grava o `PROJECT.md`, versão 1.0 (22 seções, do resumo do negócio à fase atual). Esse arquivo é a **fonte única de verdade**: tudo o que vem depois sai dele.

A sequência é sempre a mesma: checkpoint → sua confirmação → simulação → arquivo.

## 3. Files-Gen — gerar documentos

**Como pedir:** pelo nome, em qualquer ordem. *"Gera o PRD"*, *"agora o modelo de dados"*, *"quero as user stories do módulo de agendamento"*.

Cada documento:

- traz um frontmatter dizendo de qual versão do Blueprint saiu;
- só **cita** IDs do Blueprint (`BR-04`, `UC-02`…), nunca inventa;
- marca como **PENDENTE** o que não foi decidido, em vez de preencher com suposição.

Quando falta informação, a skill resolve na hora se a lacuna for pequena, ou para e oferece opções se for grande. Também dá para aprofundar antes: *"vamos aprofundar arquitetura e UX antes dos documentos"* — o resultado vai para a seção 19 do Blueprint.

Ordem sugerida e descrição de cada tipo: [documentos.md](documentos.md).

## Mudando uma decisão

> Mudou: agora o paciente só pode remarcar até 48h antes, não 24h.

A skill segue seis passos, nesta ordem:

1. identifica o ID afetado e roda `find_references.py` para listar **todos** os documentos que o citam;
2. mostra o plano de propagação **antes** de editar qualquer arquivo;
3. simula de novo, se a mudança altera a sequência do que um ator faz ou quem pode fazer o quê;
4. atualiza o `PROJECT.md`: a decisão, uma linha no histórico e a versão;
5. propaga pelos documentos do plano, marcando cada um;
6. confere com `check_staleness.py` e `check_coverage.py`.

Decisões não tocadas não são rediscutidas.

## Simulando sob demanda

A qualquer momento depois de o Blueprint existir: *"que problemas podem ocorrer no uso diário?"*, *"como seria a primeira semana?"*, *"testa isso antes de eu fechar o MVP"*. Diferente das consultas abaixo, a simulação escreve no Blueprint: lacuna vira pendência ou regra, e o registro vai para o histórico de decisões.

## Encerrando uma fase

> O MVP está pronto. Vamos para a fase 2.

A skill move a fase atual para "Fases concluídas" na seção 22, define com você o objetivo e as funcionalidades da nova fase e regenera o que depende dela: Development Plan, Backlog (as tarefas concluídas ficam), os limites de escopo do `CLAUDE.md` e o cabeçalho do `STATE.md`.

## Perguntas que você pode fazer a qualquer momento

São só leitura — não alteram nada.

| Pergunta | O que a skill faz |
|---|---|
| "Qual o estado do projeto?" / "o que falta?" | Checklist de maturidade, ou `project_status.py` |
| "Onde a BR-04 é usada?" | `find_references.py` |
| "Tem algum ID inventado?" | `check_traceability.py` |
| "Que documentos estão desatualizados?" | `check_staleness.py` |
| "Revise tudo" / "está coerente?" | Os quatro verificadores + revisão manual do que eles não alcançam |
| "Está pronto pro Claude Code?" | `handoff_check.py` |
| "Quais as pendências / sugestões / princípios?" | Lê as seções 16, 17 e 20 do Blueprint |
| "Em que fase o projeto está?" | Lê a seção 22 |
| "Histórico de decisões?" | Lê a seção 18 |

## Retomando em outro chat

Envie a **pasta inteira do projeto** (ou o arquivo compactado que a skill entrega a cada rodada) e diga o que quer. Com a pasta em mãos, a skill roda `project_status.py` e `check_staleness.py` antes de qualquer coisa e conta o que encontrou. Se você enviar só o `PROJECT.md`, dá para gerar documentos novos, mas os já existentes não serão conferidos nem atualizados. A skill não depende da conversa anterior — esse é o ponto do Blueprint. Num Projeto do Claude.ai, deixar os arquivos no conhecimento do projeto faz isso automaticamente.

Guarde cada arquivo assim que ele é entregue: o ambiente em que a skill roda pode ser temporário.

## Dicas

- **Projeto pequeno, documentação pequena.** A estrutura é a mesma, a profundidade não. Algumas pendências legítimas num sistema simples são o resultado certo.
- **Não peça os 23 documentos.** Para *vibe coding*, PRD → MVP → Architecture → Data Model → Backlog → Test Strategy → Setup & Runbook → CLAUDE.md já leva longe.
- **Defina o idioma cedo.** O campo `idioma_documentacao` do Blueprint vale para todos os documentos derivados.
