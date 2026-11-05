# Explorando casos de borda

## Por que isso merece um arquivo próprio

Casos de borda são a categoria de pergunta mais fácil de esquecer e mais cara de descobrir tarde — normalmente só aparecem quando alguém já está implementando e esbarra num caso que ninguém discutiu. Trazer isso para o Concept, mesmo que pareça um detalhe menor na hora, costuma ser o que mais separa um Blueprint sólido de um que parece completo mas não é.

## Checklist de categorias (use como guia, não como roteiro fixo)

- **Concorrência**: o que acontece quando duas ações conflitantes acontecem ao mesmo tempo (duas reservas na mesma sala, dois editores no mesmo registro)?
- **Estado vazio**: como o sistema se comporta quando não há nada ainda (nenhuma sala cadastrada, nenhum profissional ativo)?
- **Limites**: existe um número máximo/mínimo relevante (quantas ocorrências uma recorrência pode ter, quantos usuários um plano suporta)?
- **Cancelamento e reversão**: toda ação de criação tem uma contraparte de desfazer? O que acontece com o que já dependia dela?
- **Permissão negada**: o que o sistema mostra quando alguém tenta uma ação que não pode fazer — erro silencioso, mensagem clara, opção alternativa?
- **Falha parcial**: em uma operação com múltiplas partes (como uma reserva recorrente com várias ocorrências), o que acontece se só uma parte falhar? Tudo é desfeito, ou o que deu certo permanece?
- **Dado ausente ou inválido**: o que acontece quando uma informação esperada não veio ou veio em formato inesperado?
- **Expiração e tempo**: existe algo que deveria acontecer automaticamente após um tempo (reserva expira se não confirmada, sessão expira por inatividade)?

## Como trazer isso sem parecer um interrogatório

Não liste a checklist inteira para o usuário. Escolha 1-2 categorias mais relevantes para o que já foi discutido naquela rodada e pergunte de forma concreta, ancorada num cenário real do sistema — como no exemplo de `questioning.md` sobre duas reservas conflitantes.

## Registrando a resposta

Toda decisão de caso de borda vira uma regra de negócio candidata no Blueprint (ver `references/blueprint/schema.md`), com o mesmo tratamento de qualquer outra regra — não é uma categoria à parte, é conteúdo normal da seção de regras de negócio.
