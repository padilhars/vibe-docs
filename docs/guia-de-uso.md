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

**O que não acontece:** nenhum arquivo é gerado. O Concept é só conversa.

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

Depois da sua revisão, ela grava o `PROJECT.md` (22 seções, do resumo do negócio à fase atual). Esse arquivo é a **fonte única de verdade**: tudo o que vem depois sai dele.

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

A skill identifica o ID afetado, roda `find_references.py` para listar **todos** os documentos que o citam, mostra o plano de propagação **antes** de editar e só então atualiza o `PROJECT.md` (incrementando a versão) e oferece atualizar os derivados. Decisões não tocadas não são rediscutidas.

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
| "Histórico de decisões?" | Lê a seção 18 |

## Retomando em outro chat

Envie o `PROJECT.md` (e os documentos já gerados, se for alterar algum) e diga o que quer. A skill não depende da conversa anterior — esse é o ponto do Blueprint. Num Projeto do Claude.ai, deixar os arquivos no conhecimento do projeto faz isso automaticamente.

## Dicas

- **Projeto pequeno, documentação pequena.** A estrutura é a mesma, a profundidade não. Algumas pendências legítimas num sistema simples são o resultado certo.
- **Não peça os 21 documentos.** Para *vibe coding*, PRD → MVP → Architecture → Data Model → Backlog → CLAUDE.md já leva longe.
- **Defina o idioma cedo.** O campo `idioma_documentacao` do Blueprint vale para todos os documentos derivados.
