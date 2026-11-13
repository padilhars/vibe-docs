# Simulação de uso real

## Por que simular, tendo checkpoint e revisão

Todas as outras verificações da skill são estáticas: o checkpoint categoriza o que foi discutido, os scripts conferem presença de ID, a revisão crítica lê cada documento por dentro. Nenhuma delas **executa** o sistema.

Simular é narrar o sistema funcionando no tempo, com atores concretos fazendo coisas em sequência. Isso encontra uma classe de defeito que leitura não encontra — a que só existe na ordem dos acontecimentos:

- O sistema começa vazio, e alguém tem que entrar nele antes de existir qualquer dado.
- Um ator faz as coisas na ordem que faz sentido para ele, não na ordem que o fluxo previu.
- Alguém começa uma operação e não termina.
- Duas pessoas agem ao mesmo tempo, de verdade, não em tese.
- Alguém precisa corrigir o erro de outro.

Um exemplo real do que isso pega: num projeto de agendamento, todo o cadastro de clientes estava bem desenhado, mas não existia caminho nenhum para criar a conta da secretária — a falta só apareceu quando o backlog estava sendo escrito, depois da API e das user stories prontas. Uma simulação do dia 1 pegaria na primeira frase, porque o dia 1 começa com o sistema vazio e alguém tendo que entrar.

Note que `concept/edge-cases.md` já lista "estado vazio" como categoria de pergunta, e isso não impediu a falha. Perguntar sobre estado vazio em abstrato é diferente de narrar o primeiro dia.

## Como o usuário pede isso

Raramente com a palavra "simulação". No uso real, o pedido veio como *"revise e busque por possíveis problemas que podem ocorrer no uso diário do sistema e quais melhorias implementar pra resolver"*. Reconheça também: "o que pode dar errado no dia a dia", "quais problemas podem aparecer", "testa isso antes de eu fechar o MVP", "como seria a primeira semana", "simule o uso".

## Quando simular

- **Depois do checkpoint e antes de consolidar o Blueprint** (ver `review-checklist.md`). É o momento de maior retorno: o entendimento está completo o suficiente para a simulação fazer sentido, e nada derivado foi gerado ainda, então corrigir é barato.
- **Antes de definir o MVP**, quando o usuário for pedir o corte. A simulação revela o que é de fato indispensável para a primeira semana funcionar, e isso é um argumento melhor para o corte do que preferência.
- **Quando uma decisão já consolidada mudar** — mas só no gatilho abaixo.

### O gatilho da re-simulação

Simule de novo quando a alteração mexer em **regra de negócio, fluxo, permissão ou estado** — ou seja, quando ela muda *a sequência do que um ator faz* ou *quem pode fazer o quê*. É aí que a ordem dos acontecimentos pode quebrar sem que nenhum documento pareça errado isoladamente.

Não simule por mudança que não altera sequência: renomear um campo, ajustar um número de NFR, acrescentar uma pendência, corrigir redação. Uma verificação que dispara em toda mudança vira ruído e se aprende a pular — e uma que nunca dispara não serve para nada.

Respeite a proporcionalidade (ver `schema.md`): num CRUD de três telas, uma simulação curta do dia 1 basta. O retorno cresce com o número de atores e com a quantidade de estado que o sistema carrega.

## Como simular

Escolha um horizonte concreto e narre em ordem cronológica, com nomes. "A Duilia abre o sistema na segunda-feira" funciona; "o usuário realiza o cadastro" não — a segunda formulação é a do fluxo que você está justamente tentando testar, então ela não testa nada.

A cada passo, faça uma pergunta só: **o sistema, como está definido agora, permite isso? Por qual regra?** Quando a resposta for não, decida entre duas coisas (ver a seção seguinte).

### Cenários universais

Valem para qualquer sistema. Os três primeiros são obrigatórios; os demais entram conforme a complexidade justificar:

1. **Dia 0 — sistema vazio.** Ninguém cadastrado, nada configurado. Quem entra primeiro, e como essa conta passa a existir? O que cada tela mostra sem dado nenhum? E, principalmente: **todo cálculo que depende de histórico roda com o quê, antes de existir histórico?** Uma média de três meses não tem o que calcular na primeira semana, e o resultado é uma tela vazia que ninguém previu.
2. **Primeira semana de operação normal.** O fluxo principal acontecendo várias vezes, com atores diferentes, acumulando dado.
3. **Alguém faz na ordem errada.** Tenta a ação principal antes de existir o pré-requisito dela.
4. **Abandono no meio.** Começa a operação, fecha o navegador, volta depois. O que ficou gravado? Retoma de onde parou ou recomeça?
5. **Dois atores ao mesmo tempo**, no mesmo registro.
6. **A operação do administrador.** Corrigir o erro de outra pessoa, intervir manualmente, desfazer algo. Quase nunca é discutido na Discovery e aparece na primeira semana real.
7. **Fim de ciclo.** Fechamento do dia, da semana ou do mês — relatório, cobrança, limpeza, arquivamento.
8. **A mesma realidade entrando por dois caminhos.** Se um fato pode ser registrado de duas formas diferentes, ele é contado duas vezes? Num sistema financeiro, a compra entra pelo lançamento e pela importação da fatura, e o pagamento da fatura pode entrar como uma terceira despesa do mesmo dinheiro. Dupla contagem é invisível na leitura de cada regra isolada.

### Cenários por característica do sistema

Os universais acima nascem de sistemas com atores humanos operando telas. Um sistema com outras características tem classes de problema que eles não alcançam. Para cada pergunta abaixo, quando a resposta for sim, simule os cenários correspondentes:

**O usuário escreve em linguagem livre?** (bot, busca, campo de texto aberto, comando por voz)
- **Entrada ambígua**: a mesma frase significa duas coisas plausíveis. "Almoço com a Ana sexta, 50 reais" é um gasto, um compromisso, ou os dois?
- **Entrada incompleta**: falta um dado que o sistema precisa e o usuário não disse. "Gastei 40 na farmácia" — em qual forma de pagamento?
- **Entrada múltipla**: várias coisas numa mensagem só. "Uber 25, mercado 180 e farmácia 40."
- **Entrada referencial**: uma correção que aponta para algo anterior. Depois de três registros, "é mercado, não farmácia" vale para qual deles?

**O sistema importa dado de fora?** (arquivo, planilha, extrato, API de terceiro)
- **O dado real tem linha que o modelo não previu.** Numa fatura de cartão: estorno com valor negativo, linha de pagamento recebido, anuidade, juros, IOF. Nada disso é uma compra, e tratar como compra corrompe todo o cálculo.
- **O mesmo arquivo enviado duas vezes.** Duplica tudo, ou o sistema reconhece e oferece substituir?
- **A extração saiu incompleta ou errada.** Se a soma do que foi lido não bate com o total que o próprio documento declara, o que acontece — importa errado em silêncio, ou para e avisa?
- **Referência a entidade que não existe no sistema.** A fatura é de um cartão não cadastrado.

**Depende de serviço externo?** (integração, autenticação de terceiro, IA, gateway)
- **Falha silenciosa**: a credencial expira ou o acesso é revogado, e nada para de funcionar visivelmente — só deixa de acontecer. Quem descobre, e quando?
- **Indisponibilidade no momento da ação**: alguém age enquanto o serviço está fora. O pedido se perde, ou fica guardado para processar depois?

**Acumula dado ao longo do tempo?**
- **Mês 6**: o que proliferou? Categorias quase idênticas ("Farmácia", "Farmácias", "Drogaria"), registros duplicados, lixo que ninguém limpa. Um sistema que deixa qualquer ator criar dado mestre livremente degrada com o uso.

**Tem período de competência?** (mês fiscal, ciclo de cobrança, safra, semestre letivo)
- **A mesma transação pertence a qual período?** Uma compra de 28 de outubro numa fatura que vence em 10 de dezembro conta em outubro ou em dezembro? A resposta pode ser *as duas*, dependendo da pergunta que se faz — e isso precisa estar decidido explicitamente, não emergir de como cada tela consulta.

**Notifica o usuário?**
- **Efeito agregado**: somando todos os avisos de todas as funcionalidades, quantas mensagens por dia? Cada notificação é defensável sozinha e o conjunto vira spam que a pessoa aprende a ignorar — inclusive os avisos que importam.

### Postura

Simulação que narra o caminho feliz e conclui "funciona bem" é pior que simulação nenhuma: cria confiança falsa sobre um projeto que não foi testado. O valor está inteiramente em achar coisa, então simule procurando quebrar — quem erra a ordem, quem desiste, quem faz duas coisas ao mesmo tempo.

Se de fato não encontrar nada, **diga isso explicitamente**, junto com os cenários que cobriu. Silêncio depois de uma simulação é ambíguo: quem lê não sabe se não havia problema ou se a simulação foi superficial.

## O que fazer com cada achado

Separe duas coisas que a simulação mistura com facilidade:

| Tipo | Exemplo | Para onde vai |
|---|---|---|
| **Lacuna real** — o fluxo exige algo que não existe em lugar nenhum | "Não existe caminho para criar a conta da secretária" | Pendência (§16), ou nova `BR-xx`/`FUN-xx` quando o usuário decidir ali mesmo |
| **Comportamento indefinido** — a situação acontece e ninguém decidiu o que o sistema faz | "Se ela fechar o navegador no meio, não está dito se a reserva fica pendente ou é descartada" | Pergunta ao usuário agora; a resposta vira `BR-xx` |
| **Risco operacional** — funciona como definido, mas vai doer na prática | "A secretária teria que repetir isso 40 vezes por dia" | Ponto de atenção (§14) |
| **Preferência** — seria melhor com, mas nada no fluxo exige | "Seria bom ter filtro na lista" | 🔵 Sugestão futura (§17) |

As três primeiras linhas são o motivo de a simulação existir. A última é a que infla escopo se tratada como as outras — achado de simulação não vira funcionalidade por iniciativa própria, exatamente como em `concept/prior-art.md`.

Toda lacuna real ou comportamento indefinido que o usuário decidir na hora precisa **voltar para o Blueprint** antes de consolidar, não ficar só no texto da simulação. Registre também uma linha no histórico (§18) dizendo que a simulação rodou e sobre qual versão ("pré-consolidação" quando for a que antecede o primeiro `PROJECT.md`) — é o que permite, mais tarde, saber se a versão atual do Blueprint já foi submetida a ela.

## Como relatar

Uma simulação produtiva encontra muita coisa — dez, quinze achados não é incomum num sistema com várias integrações. Um número grande só é digerível com estrutura, então:

**Agrupe por natureza, não por ordem de descoberta.** Grupos que funcionam: decisões que mudam o sistema, entendimento da entrada do usuário, importação de dado externo, funcionamento e falhas. Quinze itens soltos cansam; quinze em quatro grupos nomeados se leem.

**Separe o que exige decisão do que é correção direta.** Normalmente dois ou três achados são escolhas reais de produto, com mais de um caminho defensável, e o resto é correção que só precisa de confirmação. Diga isso na abertura — "três exigem uma decisão sua, os outros são correções diretas" — e o usuário sabe onde gastar atenção.

**Cada achado leva três coisas:**
- O problema com **exemplo concreto**, não em abstrato. "Um jantar de 28 de outubro numa fatura que vence em 10 de dezembro conta em qual mês?" funciona; "há ambiguidade na competência temporal" não.
- A **correção que você proporia**, não só o apontamento. Achado sem proposta transfere todo o trabalho de volta ao usuário.
- A **alternativa**, quando a decisão é relevante e há outro caminho razoável — com o trade-off em uma linha.

**Feche dizendo o próximo passo.** Peça a decisão nos que precisam, a confirmação nos demais, e diga o que vem depois (consolidar, cortar o MVP).

## Achado de simulação não entra automaticamente no MVP

Uma simulação com catorze achados aceitos aumenta o escopo do projeto antes de o MVP existir — e isso é saudável, porque é melhor descobrir agora. Mas as funcionalidades e regras que nasceram aqui passam pelo corte do MVP como qualquer outra: entram na primeira versão só as que a semana 1 exige de fato.

O contrário disso é o modo mais fácil de a simulação inflar escopo: catorze problemas reais viram catorze itens de MVP, e a primeira versão fica grande por acúmulo de correção, não por decisão.

## O que a simulação não produz

Nenhum arquivo. Ela não gera um `SIMULATION.md`: um registro narrativo ficaria obsoleto na primeira alteração de regra e passaria a contradizer o Blueprint, que é o problema que a skill inteira existe para evitar. O produto da simulação são as correções no Blueprint e a linha no histórico.
