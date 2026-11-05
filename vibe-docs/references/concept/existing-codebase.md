# Verificando código existente antes de perguntar

## Por que isso importa

Se o usuário está descrevendo um sistema que já existe — uma evolução, uma funcionalidade nova num projeto em andamento — muita coisa que normalmente seria pergunta de levantamento já está escrita no código: entidades, campos, rotas, convenções de nome. Perguntar o que já dá pra ler é o tipo de atrito que faz a sessão parecer burocrática à toa. Prefira ler a perguntar sempre que a resposta já existe em algum lugar acessível.

## Quando verificar

Verifique um código existente quando:
- o usuário mencionar explicitamente que já existe um projeto ou repositório (ex.: "isso é uma funcionalidade nova pro sistema que já tenho", "olha o código em X");
- houver uma pasta de projeto ou código disponível no ambiente atual que pareça relacionada ao que está sendo discutido;
- o usuário enviar ou referenciar arquivos de código como parte do pedido inicial.

Se não houver nenhum sinal de código existente, não vá procurar por conta própria — presuma que é um projeto novo e siga o Concept normalmente. Vasculhar um sistema de arquivos sem motivo é ruído, não investigação.

## O que procurar

Antes da primeira rodada de perguntas fundamentais, faça uma varredura rápida (listar estrutura de pastas, buscar por palavras-chave) atrás de:

- **Modelos e entidades**: arquivos de schema, migrations, modelos de ORM, definições de tipo — costumam revelar entidades e campos já decididos.
- **Rotas e endpoints**: arquivos de rota ou controller — revelam ações e casos de uso já implementados.
- **Autenticação e autorização**: middleware ou configuração de auth, se existir — revela quem já pode fazer o quê.
- **Documentação existente**: README, comentários de topo de arquivo, um glossário ou `CONTEXT.md` se houver — revela terminologia e decisões já tomadas.
- **Configuração e stack**: `package.json`, `requirements.txt`, arquivos de configuração — revela tecnologia já escolhida, o que evita perguntar de novo na etapa de arquitetura.

Não é necessário ler o código inteiro. Uma varredura de estrutura de pastas e alguns arquivos-chave costuma bastar para responder as perguntas fundamentais sem precisar perguntar tudo do zero.

## Como usar o que foi encontrado

Não pergunte o que já foi encontrado — confirme:

- Fraco: "Quais entidades o sistema vai ter?"
- Bom: "Vi no código que já existem `Room`, `Booking` e `Professional` como entidades — é essa a base, ou você quer mudar algo aqui?"

Isso segue o mesmo princípio de `questioning.md` (toda pergunta vem com um palpite) — só que aqui o palpite vem de ter lido o código, não de um padrão genérico de sistemas parecidos. É um palpite mais forte que o de costume, então trate a confirmação como praticamente automática a menos que o usuário aponte uma mudança.

## Quando o código contradiz o que o usuário disse

Se a leitura do código revelar algo que conflita com o que o usuário acabou de descrever — por exemplo, o usuário diz que "qualquer profissional pode cancelar", mas o código atual só permite pra quem criou a reserva — trate isso como uma contradição, com o mesmo tratamento descrito em `methodology.md`: aponte na hora, não decida sozinho qual versão vale. Pode ser que o usuário esteja pedindo justamente para mudar esse comportamento, e é importante saber qual dos dois casos é esse antes de registrar qualquer coisa no Blueprint.

## Registrando no Blueprint

Quando o projeto partir de código existente, registre isso na seção 13 do `PROJECT.md` (Requisitos Técnicos Iniciais) — a stack, as convenções e as entidades já existentes não são escolha do projeto novo, são restrição herdada. Isso também evita que a etapa de Files-Gen (em especial `architecture.md` e `data-model.md`) proponha uma tecnologia ou modelagem diferente da que já está em uso: ambos os arquivos já dão prioridade ao que a seção 13 do Blueprint declarar.
