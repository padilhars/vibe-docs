# Backlog — Tarefas de Desenvolvimento

## Propósito
Quebrar o Plano de Desenvolvimento (ou, na ausência dele, as User Stories) em itens de trabalho concretos, no nível de granularidade que alguém pega e implementa diretamente. Cobre o que às vezes é pedido separadamente como "backlog", "tarefas de desenvolvimento" ou "especificação de implementação" — são o mesmo tipo de artefato visto de ângulos ligeiramente diferentes.

## Insumos necessários do Blueprint
User Stories (se já geradas) ou funcionalidades diretamente, Plano de Desenvolvimento (se já gerado, para ordenação), arquitetura (para saber a granularidade técnica das tarefas), e a seção 22 (Fase Atual) — é ela que define quais funcionalidades entram neste backlog. Gerar um backlog com tudo que existe no Blueprint, ignorando a fase, entrega ao agente um escopo maior que o combinado.

## Estrutura obrigatória

```markdown
# Backlog — [Nome do Projeto]

## [Fase / Épico]

- [ ] **TASK-xxx** — [descrição da tarefa, específica o suficiente para implementar sem perguntar de novo]
  - Origem: US-xxx / FUN-xx
  - Componente: [onde no sistema isso se encaixa, se a arquitetura já existe]
  - Critério de pronto: [como verificar que está concluída, de forma isolada — ver "tamanho certo de uma tarefa" abaixo]
```

## Tamanho certo de uma tarefa

Uma tarefa boa é implementável e verificável isoladamente — dá pra saber que funcionou sem depender de nenhuma outra tarefa ainda não feita. Compare:

- Grande demais: "Implementar autenticação de usuários" — esconde várias tarefas dentro (cadastro, login, recuperação de senha, sessão), e não dá pra dizer objetivamente quando "está pronta".
- No tamanho certo: "Criar endpoint de cadastro que valida formato de e-mail e recusa e-mail duplicado" — implementável de uma vez, e o critério de pronto é óbvio: cadastra com e-mail válido e único, recusa o resto.

Se, ao escrever o critério de pronto de uma tarefa, você perceber que só dá pra testar depois que 2-3 outras tarefas também existirem, ela é grande demais — quebre antes de listar, não depois.

## Inserir tarefa num backlog existente

Tarefa nova recebe o próximo `TASK-xxx` livre e é posicionada na onda/fase correta do documento — **nunca renumere as existentes para manter a sequência visual**. É tentador achar que a numeração deve refletir a ordem de execução, mas ela não precisa: a ordem vem da posição no documento e da onda, e o ID serve só para referenciar. Renumerar quebra toda referência cruzada que aponta para os números antigos, inclusive em outros documentos (Development Plan, User Stories) que a renumeração não alcança — e o erro é silencioso, porque os números continuam existindo, só apontando para a tarefa errada.

## Regras específicas
- Uma tarefa deve ser implementável sem que quem a pega precise voltar ao Blueprint para entender o que fazer — se a descrição não é suficiente para isso, é sinal de que a tarefa está grande demais ou a informação de origem ainda é insuficiente.
- Mantenha a rastreabilidade até a origem (`US-xxx` ou `FUN-xx`) em toda tarefa — é o que permite, mais tarde, achar todas as tarefas afetadas quando uma decisão de negócio mudar.
- Ordene pela sequência do Plano de Desenvolvimento quando ele existir; sem ele, ordene pela dependência lógica mais evidente e diga que essa ordenação é provisória.
