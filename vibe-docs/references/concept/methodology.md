# Metodologia do Concept

## O objetivo desta etapa

Sair de "uma ideia de sistema" para "um entendimento maduro o suficiente para consolidar sem lacunas críticas". Isso normalmente significa várias rodadas de troca — não tem problema a conversa ter 20, 40 ou 60 mensagens. O tempo gasto aqui é o que evita retrabalho na implementação, então não force uma consolidação cedo demais só para parecer produtivo.

## Isto é uma discussão, não um formulário

O erro mais fácil de cair aqui é transformar o Concept numa sequência de "você pergunta, o usuário responde". Isso produz um Blueprint tecnicamente completo, mas raso: você só recebe de volta o que perguntou, nunca o que não pensou em perguntar. O valor real desta etapa vem de troca genuína — você propõe, o usuário reage (concorda, discorda, ou traz uma ideia própria), e essa reação vira o próximo passo da conversa, não só um item marcado como resolvido.

Isso muda como cada rodada deve ser montada:

- **Toda proposição termina com um convite real a discordar**, não um "o que acha?" genérico e fácil de ignorar. Pergunte algo específico o suficiente pra ser respondido de verdade: "isso faz sentido pro seu caso, ou tem uma razão pra não fazer assim?"
- **Perguntas e proposições não são dois blocos separados.** Uma proposição já carrega a pergunta que a testa — não empilhe "aqui vão minhas perguntas" e depois "aqui vão minhas ideias" como se fossem seções de formulário preenchidas em paralelo.
- **Quando o usuário discordar de uma proposição, explore o motivo antes de seguir em frente.** "Não quero isso" é resposta válida, mas "por quê?" às vezes revela uma restrição real que muda outras partes do sistema — não trate a discordância como um "ok, descartado" e pule pra próxima pergunta.
- **Quando o usuário concordar, isso ainda é uma decisão a reconhecer, não um sinal pra emendar direto na próxima pergunta.** Um instante de reconhecimento antes de seguir já resolve.
- **Convide o usuário a trazer o que ele já pensou e você não perguntou.** A cada poucas rodadas, pergunte diretamente: "tem alguma coisa que você já tinha em mente e que eu ainda não perguntei?" — a melhor ideia da conversa pode não estar na sua lista de perguntas. Ver `propositions.md` para o detalhamento completo de como conduzir essa troca.

## Como abrir a conversa

Antes da primeira rodada de perguntas, se houver algum sinal de código já existente relacionado ao que está sendo discutido, faça a verificação descrita em `existing-codebase.md` primeiro — isso muda o que você já sabe antes mesmo de perguntar, e evita repetir pro usuário o que já dá pra ler sozinho.

Quando o usuário apresentar um problema e uma ideia de solução, comece com um "entendimento inicial" curto (1 parágrafo) mostrando que você captou o essencial. A partir daí, misture, sem seções rígidas:

- o que já está claro a partir do que foi dito (ou do código, se houver);
- 1-2 proposições concretas — ideias novas que o usuário não trouxe, cada uma com o convite a reagir embutido (ver `propositions.md`);
- 1-2 perguntas de levantamento — lacunas que precisam ser preenchidas, cada uma já acompanhada do seu melhor palpite pra essa resposta (ver `questioning.md`).

Não abra com uma lista enorme de perguntas, e não termine toda mensagem com uma bateria delas empilhadas — isso sobrecarrega e faz a conversa parecer um formulário. Uma rodada pode, perfeitamente, ser majoritariamente sobre uma única proposição que gerou uma boa discussão — não force preencher uma cota de perguntas se a conversa está indo bem por outro caminho.

## Como a intensidade da investigação deve mudar ao longo da conversa

O Concept não deve manter o mesmo ritmo do início ao fim:

- **Rodadas iniciais**: foque em fundamentos — quem são os atores, quais as entidades centrais, qual é o fluxo principal de ponta a ponta. Sem isso definido, qualquer detalhe adicional é prematuro.
- **Rodadas do meio**: uma vez que o fluxo principal está claro, vá para casos de borda, conflitos, permissões e estados alternativos (ver `edge-cases.md`). É também o momento de pesquisar o que sistemas parecidos tiveram que resolver, para transformar isso em pergunta (ver `prior-art.md`) — antes disso a pesquisa ancora a conversa na solução genérica do mercado em vez do problema específico do usuário.
- **Rodadas finais**: foque só nas lacunas que restaram. Se uma área já está bem coberta, não volte a perguntar sobre ela "só para confirmar" — isso cansa o usuário sem agregar.

## Sinalizando quando o Concept parece maduro

Não espere passivamente o usuário dizer "chega". Quando perceber que os fundamentos, o fluxo principal, os casos de borda relevantes e as permissões já estão cobertos, diga isso explicitamente: "Acho que já temos uma base sólida — atores, entidades, fluxo principal e as regras de conflito estão claros. Ainda ficou em aberto [X e Y]. Quer aprofundar isso ou já podemos consolidar?" Isso transforma o Concept de uma investigação sem fim visível em um processo com direção.

## Contradições

Se o usuário disser algo que contradiz uma decisão anterior na mesma conversa, aponte na hora: "isso conflita com o que você disse sobre X — qual das duas deve valer daqui pra frente?". Não carregue as duas versões silenciosamente até o checkpoint de consolidação — nesse ponto já é tarde para uma correção barata.

## Por que não gerar nada nesta etapa

Gerar um documento no meio do Concept cria uma falsa sensação de conclusão e tende a "fixar" decisões que ainda estavam em aberto — o usuário passa a reagir ao documento em vez de continuar pensando livremente sobre o problema. É por isso que esta etapa produz só conversa, mesmo que o usuário peça um resumo: um resumo em prosa é aceitável, um documento estruturado não.
