# Como propor, sem inventar

## A diferença entre Concept e Files-Gen nisso

No Concept, propor livremente é parte do valor que você agrega — um usuário trazendo uma ideia inicial normalmente não pensou em tudo, e sugestões bem colocadas (histórico de ações, estados intermediários, papéis adicionais) costumam amadurecer o projeto de verdade. Isso muda completamente na etapa 3 (Files-Gen): lá, inventar é o principal risco a evitar, porque o documento precisa refletir fielmente o que foi decidido, não o que pareceria uma boa ideia. As regras são diferentes de propósito, não uma contradição — ver `references/documents/_shared-rules.md`.

## Como propor bem

Uma proposição forte é específica, traz o motivo, e já vem com o convite a reagir embutido — não é um item de lista, é o começo de uma troca:

- Fraco: "Podíamos ter notificações. O que acha?"
- Bom: "Vale considerar enviar uma notificação quando uma reserva for cancelada por outra pessoa — sem isso, o profissional só descobre olhando a agenda de novo. Faz sentido pro seu caso, ou você prefere deixar isso de fora por agora?"

A segunda versão funciona melhor porque a pergunta final é específica o suficiente pra gerar uma resposta real (concordar, discordar com motivo, ou propor uma variação), em vez de um "o que acha?" que é fácil de responder com um "ok, pode ser" sem pensar muito.

Limite-se a 1-2 proposições por rodada, do mesmo jeito que com perguntas — mais que isso dilui a atenção do usuário.

## Depois de propor: o que fazer com a reação do usuário

Uma proposição não é uma entrega — é o início de uma troca, e o que você faz com a resposta do usuário importa tanto quanto a proposição em si. É aqui que a conversa vira discussão de verdade, ou continua parecendo formulário:

- **Se o usuário concordar**, reconheça brevemente antes de seguir ("faz sentido, registro isso como decisão") — não trate como uma caixa marcada e emende direto na próxima pergunta sem esse instante de reconhecimento.
- **Se o usuário discordar**, pergunte o motivo antes de descartar a ideia. "Não quero isso" é uma resposta válida, mas entender o porquê às vezes revela uma restrição real que muda outras partes do sistema — "não quero histórico de reservas" pode ser preferência simples, ou pode ser porque o usuário já sabe que não vai ter capacidade de armazenamento pra isso, e esses dois motivos levam a lugares bem diferentes do Blueprint.
- **Se o usuário propuser uma alternativa**, trate com o mesmo peso que uma proposição sua — não é só "aceito a correção". É uma ideia nova que merece uma pergunta de acompanhamento se algo nela ainda não estiver claro, do mesmo jeito que você faria com a sua própria proposição.
- **Se o usuário trouxer uma ideia sem você ter perguntado nada relacionado**, isso é o sinal de que a conversa está funcionando como discussão de verdade — construa em cima na hora, não apenas anote e volte pro seu roteiro de perguntas planejado.
- **A cada poucas rodadas, convide isso ativamente** em vez de só esperar que aconteça: "tem alguma coisa que você já tinha pensado sobre o sistema que eu ainda não perguntei?" costuma trazer a informação mais valiosa da conversa, porque é o que o usuário já sabia ser importante antes mesmo de você perguntar.

## O que fazer com uma proposição que o usuário não aceitou nem rejeitou

Isso acontece com frequência — o usuário segue a conversa sem responder diretamente a uma sugestão. Não trate isso como aceite silencioso. No checkpoint de revisão (`references/blueprint/review-checklist.md`), toda proposição sem decisão explícita vai para o bucket 🔵 Sugestão futura, nunca para 🟢 Definido. Se o padrão se repetir (o usuário ignora proposições seguidas), vale perguntar diretamente se prefere que você pare de propor e foque só em levantamento — algumas pessoas realmente preferem esse modo, e insistir em propor contra a preferência explícita do usuário não agrega.

## Viabilidade vs. risco — a distinção que evita confusão

Este processo não questiona se vale a pena construir o sistema (isso já foi decidido antes da conversa começar). Mas isso é diferente de sinalizar que uma escolha específica de implementação carrega um risco técnico, de segurança ou de dado sensível — isso continua sendo parte do seu trabalho.

Exemplo concreto: numa ideia de sistema de clínica, dado de paciente costuma receber tratamento como dado sensível pela LGPD. Isso não é uma objeção a construir o sistema — é uma informação que muda decisões reais mais adiante (como o dado é armazenado, quem pode acessar, se precisa de consentimento explícito). Vale mencionar como ponto de atenção no momento em que aparecer, do mesmo jeito que uma proposição de funcionalidade — e registrar como pendência ou nota no Blueprint, não como recomendação de negócio.

## Decisões de identidade e autorização sempre viram nota na seção 14

Há uma categoria de risco que passa batido com facilidade, porque a decisão que a cria costuma ser perfeitamente sensata: como o sistema sabe quem é quem, e o que essa identidade autoriza.

Exemplo real: num bot de agendamento, decidir que a conta do Telegram já identifica o administrador, sem senha adicional, é uma escolha razoável para o contexto — mas significa que uma conta comprometida vira acesso administrativo total. A decisão pode continuar de pé; o que não pode é ela ficar registrada só como regra de negócio, sem que ninguém tenha notado a consequência.

Sempre que uma decisão estabelecer **como um ator é identificado** ou **o que essa identidade autoriza**, registre a consequência na seção 14 do Blueprint (Riscos e Pontos de Atenção), mesmo que a decisão seja boa. Isso não é questionar a escolha do usuário — é garantir que a etapa de segurança (`references/documents/security-spec.md`) receba o ponto em vez de precisar redescobri-lo.

Vale também a pergunta inversa, que é a que mais escapa: se a matriz de permissões diz que um ator **não pode** fazer algo com o registro de outro (um cliente não cancela o agendamento de outro cliente), o sistema precisa de alguma forma de distinguir um do outro. Se essa forma nunca foi discutida, ela é uma lacuna — pergunte antes de consolidar, porque a permissão inteira depende dela.

## Pesquisa não é avaliação de mercado

Quando a conversa incluir pesquisa de sistemas existentes (`prior-art.md`), o limite é o mesmo da seção anterior, e vale repetir porque a tentação é maior: o que o mercado oferece é informação sobre **problemas a resolver**, nunca argumento sobre **se vale a pena construir**.

Na prática, três coisas ficam fora, mesmo que apareçam na pesquisa: quantos concorrentes existem, se algum deles resolve melhor, e se seria mais barato contratar um produto pronto. Se o usuário puxar esse assunto por conta própria, responda e siga — mas não traga por iniciativa própria.

## Integrações e tecnologia

É comum surgir a tentação de sugerir uma tecnologia específica ("usa Stripe pra pagamento", "hospeda na AWS"). Proponha a necessidade funcional ("o sistema vai precisar processar pagamentos online"), não a tecnologia — a escolha de fornecedor/stack é uma decisão técnica que pertence à etapa de arquitetura (`references/documents/architecture.md`), a menos que o usuário já tenha uma preferência definida, caso em que isso deve ser registrado no Blueprint como decisão tomada.
