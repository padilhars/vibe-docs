# Non-Functional Requirements — Requisitos Não-Funcionais

## Propósito
Registrar as expectativas de qualidade do sistema que não são uma funcionalidade em si — performance, disponibilidade, escalabilidade, usabilidade mensurável, manutenibilidade.

## Insumos necessários do Blueprint
Volume e frequência de uso esperados (se mencionados no Concept), qualquer expectativa explícita do usuário sobre desempenho ou disponibilidade.

## Estrutura obrigatória

```markdown
# Requisitos Não-Funcionais — [Nome do Projeto]

## Performance
[tempo de resposta esperado para as operações mais frequentes, se definido]

## Escalabilidade
[volume esperado de usuários/dados, e se há expectativa de crescimento relevante]

## Disponibilidade
[expectativa de uptime, se relevante para o domínio]

## Usabilidade
[só inclua critério mensurável — não "deve ser fácil de usar"]

## Manutenibilidade
[expectativas sobre facilidade de evoluir o sistema, se discutidas]

## Compatibilidade
[navegadores, dispositivos, integrações que precisam continuar funcionando]
```

## Regras específicas
- Este é o documento onde mais frequentemente vai faltar informação — a maioria das Discoveries foca em comportamento funcional, não em expectativa de performance. Isso é normal: gere as seções que têm base real e marque as demais como pendência, em vez de inventar números.
- Nunca escreva um NFR vago do tipo "deve ser rápido" ou "deve escalar bem" — se não há como tornar isso mensurável a partir do que foi discutido, é melhor deixar como pendência explícita do que preencher com uma frase sem valor de verificação.
