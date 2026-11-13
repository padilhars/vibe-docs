# Test Strategy — Estratégia de Testes

## Propósito
Definir como o sistema será verificado. Este documento existe por um motivo específico do fluxo de implementação autônoma: um agente que não sabe verificar o próprio trabalho produz código que *parece* pronto. Critério de aceitação numa user story diz o que deveria acontecer; este documento diz como provar que acontece.

Tem também um papel que nenhum outro documento cumpre: os Princípios Não-Negociáveis (seção 20 do Blueprint) são contexto para o agente, não imposição — nada impede que sejam violados por descuido. Um teste que falha quando o princípio é violado é o que os torna garantia de verdade.

## Insumos necessários do Blueprint
Regras de negócio (`BR-xx`), princípios não-negociáveis (seção 20), fluxos principais, casos de uso, critérios de aceitação das User Stories (se já geradas), arquitetura (para saber o que é testável em qual nível).

## Estrutura obrigatória

```markdown
# Estratégia de Testes — [Nome do Projeto]

## Níveis de Teste

### Unitário
[o que é testado isoladamente — normalmente regra de negócio pura, validação, cálculo]

### Integração
[o que é testado com dependências reais — persistência, comunicação entre componentes]

### Ponta a ponta
[quais fluxos completos precisam de teste que atravessa todo o sistema — normalmente só os fluxos principais do Blueprint, não todos]

## Ferramentas
[framework de teste, runner, biblioteca de asserção — se ainda não decidido, registre como pendência em vez de assumir]

## O que Testar por Prioridade

| Prioridade | O que | Por quê |
|---|---|---|
| Crítica | [princípios não-negociáveis, regras de conflito, permissões] | falha aqui causa dano real |
| Alta | [fluxo principal ponta a ponta, BR-xx centrais] | falha aqui quebra o propósito do sistema |
| Média | [casos alternativos e de erro] | falha aqui degrada a experiência |

## Cobertura de Princípios Não-Negociáveis

| Princípio | Teste que o garante | Nível |
|---|---|---|
| [princípio da seção 20] | [descrição do teste que falha se ele for violado] | [unitário/integração/e2e] |

## Cobertura de Regras de Negócio

| BR-xx | Cenário de teste | Resultado esperado |
|---|---|---|

## Testes de Regressão
[onde ficam e como são nomeados os testes que nascem de bugs. Todo bug corrigido deixa um teste que o reproduzia — escrito antes da correção, mantido na suíte para sempre. Convenção sugerida: o nome ou um comentário do teste diz qual era o bug]

## Dados de Teste
[que fixtures/seeds o sistema precisa pra testes rodarem — usuários de exemplo, estados iniciais. Dados sensíveis nunca devem vir de produção; se o domínio envolve dado pessoal, isso precisa ser dito explicitamente]

## O que NÃO testar
[decisão consciente sobre onde não vale investir — evita que um agente gere centenas de testes triviais de getter/setter]

## Comando de Verificação
[o comando único que roda tudo e diz se está passando — é o que o agente executa antes de considerar uma tarefa concluída]
```

## Verificação obrigatória ao terminar

Rode `scripts/check_coverage.py <pasta-do-projeto>` antes de entregar. Este é um documento agregador: ele precisa refletir decisões tomadas ao longo de todo o projeto, e uma ausência aqui não aparece na leitura — o documento parece completo justamente porque o que falta não está nele. Resolva o que o script apontar (incluindo declarar exclusões deliberadas) antes de considerar o documento pronto.

## Regras específicas

- **Toda linha da tabela de Princípios Não-Negociáveis precisa existir.** Se um princípio da seção 20 do Blueprint não tem teste correspondente, ou o princípio é vago demais pra ser verificável (corrija no Blueprint), ou falta um teste (registre como pendência) — não deixe a linha em branco silenciosamente.
- **Derive cenários dos critérios de aceitação já escritos**, quando as User Stories existirem. Um critério no formato dado/quando/então já é praticamente um caso de teste — reaproveite em vez de inventar cenário novo, e mantenha a rastreabilidade até a `US-xxx`.
- **Não proponha meta de cobertura percentual** ("80% de cobertura") a menos que o usuário tenha decidido isso. Percentual de cobertura mede linhas executadas, não comportamento verificado — é o tipo de meta que um agente satisfaz gerando testes inúteis. Prefira definir o que precisa estar coberto, não quanto.
- **Toda `BR-xx` do Blueprint precisa aparecer no documento — com teste ou com justificativa.** Regra de fase futura, ou que não é testável automaticamente, vai para a seção "O que NÃO testar" citando o ID e o motivo. Deixar a regra simplesmente de fora é indistinguível de tê-la esquecido: quem lê não sabe se foi decisão ou falha, e `scripts/check_coverage.py` acusa como ausência. Declarar a exclusão custa uma linha e transforma um buraco numa decisão registrada.
- **A seção de Testes de Regressão é o lado deste documento do protocolo de bug do `CLAUDE.md`** (teste que falha → correção → teste que passa). Defina aqui só a convenção — pasta, nome, marcação. O protocolo em si é fixo e não precisa ser repetido.
- **"O que NÃO testar" não é opcional.** Sem esse limite explícito, implementação autônoma tende a gerar teste pra tudo, inflando a suíte e o tempo de execução sem ganho real de confiança.
