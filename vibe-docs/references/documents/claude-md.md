# CLAUDE.md — Contrato de comportamento para o Claude Code

## Propósito
Este é o artefato final do pipeline. Diferente de todos os outros documentos, ele não existe pra ser lido por uma pessoa que quer entender o projeto — existe porque o Claude Code carrega automaticamente o arquivo `CLAUDE.md` da raiz do repositório no início de toda sessão. É o único documento do pipeline que chega ao agente sem ninguém precisar apontar pra ele.

Isso muda completamente como ele deve ser escrito.

## A regra que define este documento

**CLAUDE.md não é documentação — é um contrato de comportamento.** Cada linha precisa mudar o que o agente faz. Se uma linha não muda nenhuma decisão de implementação, ela está gastando contexto à toa e deve sair.

Consequência prática: mantenha abaixo de ~200 linhas. Não resuma a arquitetura inteira aqui, não repita o modelo de dados, não reconte os casos de uso. Aponte pros documentos que já têm isso (seção "Documentação de referência" do template) e reserve o espaço deste arquivo pro que o agente precisa saber *sempre*, em toda tarefa, sem exceção.

Se você se pegar escrevendo um parágrafo explicativo, provavelmente ele pertence a outro documento e aqui deveria virar uma linha imperativa mais uma referência.

## `@` carrega o arquivo inteiro em toda sessão

No Claude Code, escrever `@caminho/arquivo.md` dentro do `CLAUDE.md` **não** cria um ponteiro que o agente segue quando precisa: o arquivo importado é expandido e carregado no início de toda sessão, junto com o próprio `CLAUDE.md`. Dividir em imports organiza, mas não economiza contexto.

Por isso há duas formas de citar um documento, e elas não são intercambiáveis:

| Forma | O que acontece | Use para |
|---|---|---|
| `@docs/STATE.md` | Carregado inteiro em toda sessão | Só o que é curto e necessário sempre: `STATE.md` e `LEARNINGS.md` |
| `docs/ARCHITECTURE.md` (sem `@`) | Nada é carregado; o agente abre quando a instrução ao lado mandar | Todo o resto, sempre acompanhado de **quando** ler |

Importar com `@` a arquitetura, o modelo de dados, as regras e o Blueprint colocaria milhares de linhas em toda sessão e anularia o limite de 200 linhas que este arquivo existe para respeitar. `scripts/handoff_check.py` avisa quando isso acontece.

Este é um comportamento do produto, que pode mudar. Se houver busca disponível, confirme na documentação atual do Claude Code antes de gerar; se o comportamento tiver mudado, diga ao usuário em vez de seguir esta seção às cegas.

## Onde este arquivo vive

O layout final de um projeto está em "Layout do projeto" no `SKILL.md`: `CLAUDE.md` na raiz do repositório de código e todos os outros documentos em `docs/`. Gere o `CLAUDE.md` na pasta do projeto, junto com os demais, **já escrevendo os caminhos como ficarão depois** (`docs/ARCHITECTURE.md`, `@docs/STATE.md`), e diga ao usuário, ao entregar, que este arquivo vai para a raiz e o restante para `docs/`.

Os scripts aceitam os dois momentos: antes de mover, encontram os documentos na mesma pasta; depois, encontram o `CLAUDE.md` na pasta acima de `docs/`.

## Antes de gerar: feche as seções 20, 21 e 22

O `CLAUDE.md` é normalmente o último documento do pipeline, e é quando as seções 20 (Princípios), 21 (Definition of Done e Convenções) e 22 (Fase Atual) precisam estar resolvidas — elas entram aqui por extenso, e um contrato que diz `PENDENTE` onde deveria dizer o que fazer é quase inútil para o agente. Se ainda estiverem em aberto, resolva-as antes (ver `deepening.md`), com o mesmo mecanismo de palpite embutido de sempre.

## Gere o STATE.md e o LEARNINGS.md junto

O `CLAUDE.md` importa os dois e manda atualizá-los a cada tarefa, então os três nascem juntos no fim do pipeline — apontar para um arquivo inexistente é pior que não ter a instrução. Ver `state.md` e `learnings.md`.

## Insumos necessários
Idealmente todos os documentos já gerados. Os essenciais pra implementação autônoma são Architecture, Backlog, Test Strategy e Setup & Runbook; se faltar algum, avise antes de gerar. Data Model, Business Rules, API Spec e Development Plan são recomendados — cite só os que existem.

## Sem frontmatter

Diferente dos documentos derivados, o `CLAUDE.md` **não leva bloco de metadados YAML**. Ele começa direto no título. Metadados servem para uma pessoa rastrear a origem de um documento; aqui, cada linha que não muda o comportamento do agente é contexto gasto à toa em um arquivo carregado em toda sessão.

## Estrutura obrigatória

```markdown
# [Nome do Projeto]

[Uma frase: o que é o sistema e pra quem.]

## Comandos

| Ação | Comando |
|---|---|
| Instalar dependências | `[comando]` |
| Rodar em desenvolvimento | `[comando]` |
| Verificar tudo (testes + lint) | `[comando único de verificação do TEST-STRATEGY]` |
| Rodar um teste específico | `[comando]` |
| Build | `[comando]` |

## Regras invioláveis

[Os Princípios Não-Negociáveis da seção 20 do Blueprint, cada um em uma linha imperativa, começando pelo ID: `- (PRINC-01) Nenhum tenant acessa dado de outro tenant...`. O ID é o que permite ir do agente de volta ao Blueprint, e é o que `check_coverage.py` verifica. Se um princípio precisa de explicação pra ser entendido, ele está mal escrito no Blueprint — corrija lá, não aqui.]

## Convenções

[Nomenclatura, estrutura de pastas, padrão de commit e branch — só o que o agente precisa seguir ao escrever código. Da seção 21 do Blueprint.]

## Definition of Done

[O que precisa ser verdade antes de considerar qualquer tarefa concluída. Da seção 21 do Blueprint.]

## Ao começar uma sessão

O estado da implementação e os aprendizados das sessões anteriores estão abaixo e já foram carregados. Leia os dois antes de qualquer ação.

@docs/STATE.md
@docs/LEARNINGS.md

Retome pela tarefa em "Em andamento". Se não houver, pegue a primeira de "Próximas". Uma tarefa por vez.

## Ao terminar cada tarefa

Nesta ordem, antes de começar a próxima:

1. Rode o comando de verificação e leia a saída. Tarefa com verificação falhando não está terminada.
2. Confira a Definition of Done item a item.
3. Marque a tarefa como concluída em `docs/BACKLOG.md`.
4. Sobrescreva `docs/STATE.md` com a situação nova: tarefa em andamento, concluídas recentes, próximas, bloqueios, questões em aberto.
5. Registre em `docs/LEARNINGS.md` o que esta tarefa ensinou e que a próxima sessão precisaria saber — ou nada, se nada. Siga as regras no topo daquele arquivo.
6. Faça o commit, na convenção acima.

Faça isso ao fim de cada tarefa, não ao fim da sessão: a sessão pode acabar sem aviso, e o que não foi gravado se perde.

## Ao encontrar um bug

1. Antes de alterar o código, escreva um teste que reproduz o bug e veja-o falhar pelo motivo certo.
2. Corrija.
3. Veja o teste passar e a verificação completa continuar passando.
4. Mantenha o teste na suíte — é ele que impede o bug de voltar.
5. Se a causa for uma armadilha que pode se repetir, registre em `docs/LEARNINGS.md`.

Se não for possível reproduzir o bug em teste automatizado, diga por quê e descreva a verificação manual feita. Se o bug revelar uma regra de negócio errada ou nunca decidida, pare e pergunte: isso não é bug de código.

## Quando os documentos discordam

Precedência, da mais forte para a mais fraca:
1. Uma decisão que o usuário acabou de tomar nesta sessão.
2. `docs/PROJECT.md` (o Blueprint) — fonte primária de verdade.
3. Os demais documentos de `docs/`, que são derivações dele.
4. O código e os testes existentes, que mandam sobre *como* algo já foi feito.

`docs/STATE.md` e `docs/LEARNINGS.md` ficam fora dessa escala: registram onde a implementação está e o que ela ensinou, não o que o sistema deve ser. Se contradisserem um documento, o documento vence.

**Em qualquer conflito que envolva regra de negócio, permissão ou dado pessoal: pare e pergunte. Não escolha.** Uma contradição nesses temas significa que uma das duas versões nunca foi decidida, e escolher sozinho transforma um documento desatualizado em comportamento implementado.

Para contradição que não toca regra de negócio (uma convenção de nome divergente, por exemplo), siga a precedência acima e diga em uma linha qual você seguiu e por quê.

## Limites de escopo

[O que NÃO implementar: funcionalidades fora da fase atual, tecnologias descartadas. Sem isso explícito, um agente tende a implementar "de brinde" o que parece faltar.]

## Nunca faça

- Enfraquecer, remover ou "ajustar" um teste para ele passar. Teste que falha é informação — se o teste está errado, diga qual e por quê, e espere resposta.
- Corrigir um bug sem antes ter o teste que o reproduz.
- Adicionar dependência nova sem aprovação explícita. Confirme que o pacote existe e é o que você pensa: nomes parecidos com pacotes legítimos são um vetor de ataque conhecido.
- Capturar exceção sem tratá-la, nem engolir erro em silêncio.
- Refatorar o que a tarefa não pediu, ainda que o código pareça melhorável — proponha separadamente.
- Validar só no cliente. Toda regra de negócio é verificada no servidor, mesmo quando a interface já impede.
- Instalar skill, plugin ou ferramenta que o usuário não aprovou.

## Documentação de referência

Nenhum destes é carregado automaticamente. Abra quando a situação ao lado acontecer:

- `docs/BACKLOG.md` — para saber o que fazer a seguir e o critério de pronto de cada tarefa.
- `docs/ARCHITECTURE.md` — antes de criar um componente novo, escolher biblioteca ou mexer em [pontos sensíveis deste projeto].
- `docs/DATA-MODEL.md` — antes de criar ou alterar qualquer tabela ou campo.
- `docs/BUSINESS-RULES.md` — ao implementar qualquer validação ou comportamento condicional.
- `docs/API-SPEC.md` — antes de criar ou alterar um endpoint.
- `docs/TEST-STRATEGY.md` — antes de escrever um teste, pra saber o nível certo e o que não vale testar.
- `docs/SETUP-RUNBOOK.md` — se algo no ambiente não funcionar como esperado.
- `docs/PROJECT.md` — quando dois documentos discordarem, ou faltar uma decisão.
- `docs/SKILLS-RECOMENDADAS.md` — skills opcionais para este projeto; instale só as que o usuário aprovar.

[Liste só o que existe, e troque o gatilho genérico pelo específico deste projeto sempre que houver um.]
```

## De onde vem cada seção

| Seção do `CLAUDE.md` | Origem |
|---|---|
| Comandos | `SETUP-RUNBOOK.md` e o comando de verificação do `TEST-STRATEGY.md` |
| Regras invioláveis | Seção 20 do Blueprint |
| Convenções, Definition of Done | Seção 21 do Blueprint |
| Limites de escopo | Seção 22 (Fase Atual) e o campo "Recorte do MVP" da seção 4 — nunca o `MVP.md` diretamente |
| Ao começar uma sessão, Ao terminar cada tarefa, Ao encontrar um bug, Quando os documentos discordam, Nunca faça | Fixas — entram em todo projeto como estão no template, ajustando só comandos e caminhos |

Sobre os limites de escopo: se o projeto já passou da primeira fase, é a seção 22 que manda — o que ficou fora do MVP pode ter entrado na fase corrente. Se a seção 22 e a seção 4 divergirem, ou se alguma estiver `PENDENTE` apesar de o MVP existir, pare e sinalize. Escrever aqui um limite que o Blueprint não confirma cria a pior contradição possível do projeto, porque este é o arquivo que o agente lê primeiro e obedece.

## Por que as rotinas são fixas

As seções "Ao terminar cada tarefa" e "Ao encontrar um bug" não dependem de decisão do projeto, e não devem ser encurtadas para economizar linhas.

A rotina de fim de tarefa existe porque uma sessão de implementação pode terminar sem aviso — limite de contexto, queda, o usuário fechando a janela. Tudo que só seria gravado "no fim da sessão" se perde nesses casos, e a sessão seguinte recomeça sem saber o que foi feito. Gravar a cada tarefa limita a perda a uma tarefa.

O protocolo de bug existe porque corrigir sem teste deixa duas coisas sem resposta: se a correção atacou a causa certa, e o que impede o bug de voltar. O teste que falha antes e passa depois responde as duas.

Lembre que o `CLAUDE.md` é contexto, não imposição: o agente pode deixar de seguir uma instrução. O que precisa ser garantido — a suíte rodar antes de uma tarefa ser dada como concluída — deve também existir como verificação automática (ver "Garantias que não dependem de alguém lembrar" em `setup-runbook.md`).

## Verificação obrigatória ao terminar

Rode `scripts/check_coverage.py <pasta-do-projeto>` e `scripts/handoff_check.py <pasta-do-projeto>` antes de entregar. O primeiro confere se todo princípio do Blueprint está escrito aqui; o segundo confere tamanho, rotinas, imports com `@` indevidos e referências a arquivos que não existem. Resolva o que apontarem antes de considerar o documento pronto.

## Regras específicas

- **Corte sem dó.** Se estiver na dúvida se uma linha merece estar aqui, pergunte: "sem esta linha, o agente faria algo diferente?" Se a resposta for não, tire.
- **Comandos são a seção mais valiosa e a mais frequentemente esquecida.** Um agente que não sabe rodar a verificação não consegue conferir o próprio trabalho. Se o Setup & Runbook ainda não existe e ninguém decidiu esses comandos, isso é uma lacuna a resolver antes de gerar (ver `deepening.md`), não algo pra deixar em branco.
- **Nunca invente comando.** Se a stack ainda não foi decidida, o comando não existe — registre como pendência em vez de escrever um `npm test` genérico que pode nem se aplicar.
- **Regras invioláveis e limites de escopo ficam escritos aqui**, mesmo ocupando espaço: são o que mais previne dano quando o agente decide sozinho, e não podem depender de ele abrir outro arquivo.
- Este documento nunca implementa nada — produz só o contrato. Se o usuário pedir pra "já começar a implementar" junto, gere o `CLAUDE.md` primeiro, deixe claro que está pronto, e trate a implementação como pedido separado (fora do escopo desta skill).
