# Development Plan — Plano de Desenvolvimento

## Propósito
Transformar o conjunto de requisitos já definido numa sequência lógica de implementação, respeitando dependências reais — não a ordem em que os itens apareceram no PRD ou na conversa.

## Insumos necessários do Blueprint
Funcionalidades, entidades, arquitetura (se já gerada) — dependências técnicas ficam mais claras com a arquitetura definida, então prefira gerar este documento depois dela quando possível.

## Estrutura obrigatória

```markdown
# Plano de Desenvolvimento — [Nome do Projeto]

## Ondas

### Onda 1 — Esqueleto funcional
[uma fatia vertical fina que atravessa o sistema inteiro de ponta a ponta e já roda: o setup mínimo, a autenticação, **uma** funcionalidade simples completa (da interface ao banco), os testes dela e o deploy. Não é a camada de infraestrutura inteira — é o caminho mais curto até algo que funciona de verdade em produção]

### Onda 2 — Domínio Central
[entidades e regras de negócio centrais, sem UI ainda se fizer sentido separar]

### Onda 3 — Funcionalidades Core
[FUN-xx da fase atual (seção 22 do Blueprint), em ordem de dependência]

### Onda 4 — Integrações
[o que depende de serviço externo]

### Onda 5 — UX e Refinamento
[telas finais, estados de erro, polimento]

### Onda 6 — Observabilidade e Endurecimento
[logging, monitoramento, testes ponta a ponta dos fluxos críticos — os testes de cada funcionalidade nascem junto com ela, nas ondas anteriores, não aqui]

## Dependências Entre Ondas
[o que bloqueia o quê, de forma explícita]

## Marcos
[pontos de verificação intermediários que valem a pena demonstrar]
```

## Por que a Onda 1 é uma fatia vertical, não a infraestrutura inteira

Esta é a diferença mais importante entre um plano para um time humano e um plano para implementação assistida por IA.

Construir "toda a fundação" primeiro — modelo de dados completo, todas as camadas, nenhuma funcionalidade pronta — deixa o agente sem nenhum exemplo real de como este projeto faz as coisas. Ele então inventa os padrões: nomeia do jeito que acha melhor, estrutura o tratamento de erro à sua maneira, escolhe um formato de teste. Cada funcionalidade seguinte inventa de novo, e o resultado é um código coerente em cada parte e inconsistente no todo.

Uma fatia vertical fina resolve isso: depois dela existe, no próprio repositório, um exemplo funcionando de endpoint, de validação, de acesso a dados, de teste e de deploy. A partir daí o agente copia padrões reais em vez de inventá-los — e divergir passa a ser visível na revisão, porque há um padrão com que comparar.

Escolha para essa fatia a funcionalidade mais simples que ainda atravesse todas as camadas. A mais importante costuma ser a mais complexa, e complexidade aqui atrapalha: o objetivo desta onda é estabelecer o padrão, não entregar valor.

## Onda não é fase

Este plano organiza a construção **dentro de uma fase de produto**. Fase é o que a seção 22 do Blueprint registra (MVP, Fase 2...); onda é a subdivisão de construção dentro dela. O plano cobre só as funcionalidades da fase atual — quando a fase mudar, gera-se um plano novo para ela.

## Regras específicas
- Organize por dependência real, não por ordem de aparição no PRD ou no MVP — uma funcionalidade "importante" que depende de outra "menor" vem depois dela no plano, mesmo que pareça contraintuitivo.
- Se o Domain Model ou a Arquitetura ainda não foram gerados, este plano pode ficar mais genérico nas ondas iniciais — registre isso como limitação do documento em vez de inventar decisões técnicas só para completar o plano.
