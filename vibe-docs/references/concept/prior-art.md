# Pesquisa de sistemas existentes

## O que esta pesquisa é — e o que ela não é

Sistemas maduros de um domínio já passaram por problemas que uma ideia nova ainda não encontrou. Lista de espera, no-show, webhook que nunca chega, limite de janela de uma API de mensageria, exigência regulatória específica do setor: nada disso aparece quando alguém descreve a própria ideia, porque são coisas que só se descobrem operando.

Esta pesquisa busca **o que sistemas desse tipo tiveram que resolver**, para transformar isso em pergunta. Ela não busca o que os concorrentes oferecem, para transformar isso em funcionalidade.

A diferença decide se a pesquisa ajuda ou atrapalha:

| Pesquisa que atrapalha | Pesquisa que ajuda |
|---|---|
| "Concorrentes têm lista de espera — sugiro adicionar." | "Sistemas de agendamento costumam precisar decidir o que acontece quando alguém reserva e não aparece. Vocês já pensaram nisso?" |
| "O produto X oferece relatórios avançados e integração com calendário." | "Integração de pagamento tem o caso do webhook aprovado que nunca chega ao sistema. Está previsto?" |
| "Esse mercado já tem três players consolidados." | "Esse domínio costuma ter exigência de retenção fiscal dos comprovantes. Aplica ao caso de vocês?" |

A coluna da esquerda infla escopo na direção de um produto maduro e puxa a conversa para viabilidade comercial — que este processo não discute (ver `propositions.md`). A da direita fecha buraco.

## Quando fazer

Nas **rodadas do meio** do Concept, quando os fundamentos já estão claros (atores, entidades, fluxo principal) e a conversa está indo para casos de borda. Não no início.

Pesquisar antes de o problema estar claro ancora a conversa na solução genérica do mercado em vez do problema específico do usuário. A clínica tem três salas e uma secretária meio período; o modelo de um produto de agendamento global não é o ponto de partida certo para isso.

Respeite a proporcionalidade (ver `blueprint/schema.md`): um CRUD de três telas não precisa desta etapa. Ela se paga quando o domínio tem regra própria, integração externa ou exigência regulatória.

## Como fazer

Se houver busca disponível, pesquise o **domínio**, não os produtos: "problemas comuns em sistemas de agendamento", "armadilhas de integração com [serviço]", "exigência legal de [tipo de dado] no Brasil". O alvo são modos de falha e obrigações, não catálogos de funcionalidade.

Sem busca disponível, use o conhecimento próprio — mas então declare isso, porque muda o peso do que você traz.

## Como apresentar o resultado

Toda vez, distinga a origem do que está trazendo:

- **"Pesquisando agora, encontrei que…"** — verificado, com a fonte.
- **"Pelo que eu sei desse tipo de sistema…"** — conhecimento próprio, que pode estar desatualizado e o usuário pode corrigir.

Essa distinção não é formalidade. Num projeto real, a skill afirmou que não existia API oficial de consulta a registro profissional; o usuário mostrou que existia. Conhecimento interno sobre serviços, APIs e regulação envelhece, e apresentá-lo como fato verificado leva a decisão errada.

Traga no máximo dois ou três achados por rodada, cada um como pergunta com palpite embutido, exatamente como qualquer proposição (ver `propositions.md`). Achado que não vira decisão explícita do usuário entra como 🔵 Sugestão futura no checkpoint, nunca como funcionalidade adicionada por conta própria.

## O limite que não se cruza

Nada aqui autoriza avaliar se vale a pena construir o sistema, se o mercado está saturado, ou se seria melhor usar uma solução pronta. Essa decisão foi tomada antes da conversa começar e continua fora do escopo deste processo.

Se a pesquisa revelar uma restrição técnica séria — uma integração que a plataforma proibiu, uma API que deixou de existir — isso é ponto de atenção da seção 14 do Blueprint, registrado como qualquer outro risco, não uma objeção ao projeto.
