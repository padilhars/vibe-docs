# Como fazer boas perguntas no Concept

## O que torna uma pergunta boa aqui

Uma boa pergunta do Concept força uma decisão que muda o sistema de forma visível — não é uma pergunta retórica nem uma que qualquer resposta serve. Compare:

- Fraca: "Você quer que o sistema seja fácil de usar?" (a resposta não muda nada concreto)
- Boa: "Se duas pessoas tentarem reservar a mesma sala no mesmo horário, o que deve acontecer — a segunda tentativa é bloqueada na hora, ou entra numa fila de espera?" (cada resposta leva a uma regra de negócio diferente)

## Toda pergunta vem com um palpite

Uma pergunta em branco ("quem pode reservar uma sala?") exige que o usuário escreva a resposta do zero. A mesma pergunta com um palpite razoável embutido ("imagino que só profissionais e a secretária possam reservar, sendo a secretária capaz de reservar em nome de outra pessoa — é isso, ou você via diferente?") exige só reagir: confirmar, corrigir, ou dizer que não sabe. A segunda forma responde mais rápido e capta a mesma informação — é o mesmo ganho que uma proposição traz (ver `propositions.md`), só que aplicado à pergunta de levantamento em vez de a uma ideia nova.

Use como palpite o padrão mais comum para sistemas parecidos, sempre que existir um razoável. Isso não é inventar decisão — inventar seria apresentar o palpite como fato já definido; aqui ele nasce explicitamente como sugestão a confirmar, o que é bem diferente. Quando não houver base nenhuma para um palpite razoável (a resposta depende de algo específico do negócio do usuário, sem padrão comparável), tudo bem perguntar em aberto — mas isso deve ser a exceção, não o padrão. Se houver código já existente disponível, o palpite pode vir de lá em vez de um padrão genérico — ver `existing-codebase.md`.

## Categorias de perguntas a cobrir ao longo do Concept

Não precisa passar por todas em toda rodada — use como checklist mental ao longo da conversa inteira:

- **Atores**: quem interage com o sistema, e o que cada um pode e não pode fazer.
- **Fluxo principal**: o caminho feliz, passo a passo, de ponta a ponta.
- **Conflitos e concorrência**: o que acontece quando duas ações colidem (ver também `edge-cases.md`).
- **Estados**: quais estados uma entidade central pode assumir, e o que dispara cada transição.
- **Permissões**: quem pode criar, ler, editar, cancelar, administrar — para cada ação relevante.
- **Identidade**: como o sistema sabe quem é cada ator. Parece óbvio e quase nunca é dito em voz alta — mas toda permissão do item anterior depende disso. Se a resposta for "pelo login", pergunte como o login funciona; se for por um canal externo (conta do Telegram, número de telefone), registre a consequência disso na seção 14 do Blueprint (ver `propositions.md`).
- **Dados sensíveis**: o sistema lida com dado pessoal, financeiro ou de saúde? Isso não é pergunta sobre viabilidade — é levantamento de requisito, e normalmente implica em tratamento especial mais adiante (ver nota em `propositions.md` sobre a diferença entre questionar viabilidade e sinalizar risco).
- **Volume e frequência**: o sistema lida com dezenas ou milhares de registros? Isso muda decisões de arquitetura mais à frente, mas vale capturar a expectativa aqui.
- **Restrições inegociáveis**: existe algo que nunca pode acontecer nesse sistema, não importa a situação? (ex.: nunca guardar senha em texto puro, sempre exigir dois fatores pra ação financeira, nunca compartilhar dado de paciente sem consentimento). Isso é diferente de uma regra de negócio comum — vira um Princípio Não-Negociável (seção 20 do Blueprint), não uma `BR-xx` normal.

## Quantas perguntas por rodada

2 a 3 perguntas por mensagem é o ponto de equilíbrio. Menos que isso, o Concept anda devagar demais; mais que isso, vira formulário. Priorize as perguntas que mais mudam o entendimento do sistema, não as mais fáceis de responder.

Essa contagem é sobre perguntas de levantamento — as que buscam uma informação ainda não discutida. Perguntas que já vêm embutidas numa proposição (ver `propositions.md`) não entram nessa conta: uma rodada pode ter só 1 pergunta de levantamento e 2 proposições bem discutidas, e isso está certo. Não empilhe as duas coisas até bater um número fixo — o equilíbrio importa mais que a contagem.

## Como reagir à resposta do palpite

Como toda pergunta já chega com um palpite, a resposta do usuário normalmente é uma reação a ele, não uma decisão construída do zero:

- **Concordância** ("é isso mesmo", "pode ser") → registre como decisão tomada, mas mantenha claro nos seus próprios registros que partiu de um palpite aceito, não de algo que o usuário definiu de forma independente — isso importa quando o Blueprint for revisado depois.
- **Correção** ("não, é diferente porque...") → é exatamente pra isso que o palpite serve: corrigir uma sugestão específica é mais rápido do que preencher um campo em branco, e a correção em si costuma revelar mais contexto do que uma resposta do zero revelaria.
- **"Não sei mesmo"** → não force uma decisão que o usuário genuinamente não tem opinião formada. Tudo bem manter o palpite como sugestão registrada, mas marcado como pendência de confirmação, não como decisão fechada.

## Perguntas de fechamento antes de sugerir consolidação

Perto do fim do Concept, vale uma rodada específica de "o que eu não perguntei ainda":
- Existe algum papel/ator que ainda não apareceu na conversa?
- Existe alguma integração externa (pagamento, e-mail, calendário, autenticação de terceiros) que o sistema vai precisar?
- Existe algum requisito legal ou de compliance relevante para este domínio?
