# Schema do Project Blueprint (PROJECT.md)

## Papel deste documento

Esta é a estrutura obrigatória do `PROJECT.md`. Ela existe para que qualquer documento derivado (Modo 3) saiba exatamente onde procurar cada tipo de informação, sem depender de reler a conversa de Concept inteira. Preencha cada seção com o que foi decidido; quando algo ficar em aberto, escreva `PENDENTE` explicitamente em vez de omitir a seção.

## Proporcionalidade

A estrutura é a mesma para todo projeto, mas a profundidade de cada seção não deveria ser. Um CRUD de três telas e um sistema com dez atores merecem o mesmo esqueleto e quantidades de detalhe muito diferentes — para o primeiro, uma seção de duas linhas pode estar completa, e insistir em mais é cerimônia sem retorno.

Calibre pelo tamanho real do projeto: em algo pequeno, várias seções vão ser curtas e algumas continuarão `PENDENTE` legitimamente, porque a decisão ainda não importa. Isso não é um Blueprint mal feito. As únicas seções que sempre merecem esforço, mesmo num projeto minúsculo, são as que impedem dano ou retrabalho caro: regras de negócio (10), princípios não-negociáveis (20) e escopo (4).

## Metadados (topo do arquivo)

```yaml
---
project: "[nome do projeto]"
version: "[incrementa a cada consolidação relevante]"
status: "[em concept | consolidado | em evolução]"
idioma_documentacao: "[pt-BR | en | outro — usado por todos os documentos derivados]"
last_updated: "[data]"
---
```

## 1. Resumo do Negócio
1-2 parágrafos: o que é o sistema e para quem, em linguagem simples.

## 2. O Problema
A dor real que motivou o projeto, descrita de forma concreta (não "processos ineficientes", e sim o que exatamente é ineficiente e por quê).

## 3. Objetivos
Lista curta do que o sistema deve alcançar, com ID (`OBJ-01`, `OBJ-02`...). Cada objetivo deve ser algo verificável, não uma aspiração vaga.

## 4. Escopo
Duas coisas diferentes que não podem ser confundidas — a confusão entre elas é a forma mais comum de o Blueprint acabar contradizendo o `CLAUDE.md` e mandar o agente construir o que não devia:

```
**Dentro do escopo do projeto:** [tudo que o sistema faz quando estiver pronto]
**Fora do escopo:** [o que ele explicitamente não faz, nem depois]
**Recorte do MVP:** PENDENTE — preenchido quando o MVP for definido
```

O escopo do projeto é o destino; o recorte do MVP é a primeira parada, sempre mais estreito. Uma funcionalidade pode estar dentro do escopo do projeto e fora do MVP ao mesmo tempo, e isso precisa ficar visível aqui, lado a lado. Quando o `MVP.md` for gerado, o corte dele volta para cá (ver `references/documents/mvp.md`) — sem isso, esta seção segue afirmando um escopo que o MVP já contradisse.

## 5. Atores
Cada ator com uma frase sobre seu papel no sistema.

## 6. Entidades
Lista das entidades centrais com ID (`ENT-01`...), sem entrar em modelo de dados físico — isso é papel de `references/documents/data-model.md` quando gerado.

## 7. Estados
Para cada entidade que tem ciclo de vida relevante, as transições possíveis:
```
Reserva
├── Solicitada → Confirmada
├── Confirmada → Concluída
└── Confirmada → Cancelada
```

## 8. Funcionalidades
Lista com ID (`FUN-01`...), incluindo tanto as que o usuário trouxe quanto as que surgiram durante o Concept — sem distinguir origem aqui (a origem já não importa depois que algo vira 🟢 Definido).

Cada funcionalidade deve indicar qual objetivo ela atende:
```
- FUN-03 (OBJ-02): Sugestão de horário alternativo quando o pedido original está ocupado.
```
Isso é o que permite, mais tarde, justificar um corte de MVP com critério — sem essa ligação, decidir o que fica de fora vira preferência em vez de argumento. Se uma funcionalidade não serve a nenhum objetivo, isso é sinal de escopo esticado ou de um objetivo que ficou faltando: levante o ponto em vez de deixar sem referência.

## 9. Casos de Uso
Para cada caso de uso relevante, com ID (`UC-01`...): ator principal, objetivo, resumo do fluxo.

## 10. Regras de Negócio
Cada regra com ID (`BR-01`...), descrita como uma afirmação verificável:
```
BR-04
O criador de uma reserva pode cancelá-la. A secretária pode cancelar qualquer reserva.
```

## 11. Fluxos
O passo a passo do(s) fluxo(s) principal(is), ponta a ponta. Diagramas Mermaid são bem-vindos quando ajudam a clarear.

## 12. Permissões
Uma matriz simples: ator × ação × permitido/negado, para as ações mais relevantes.

## 13. Requisitos Técnicos Iniciais (se já mencionados)
Qualquer restrição ou preferência técnica que o usuário já tenha declarado (ex.: "precisa rodar num navegador comum", "já uso Postgres em outros projetos"), ou identificada a partir de um código já existente (ver `references/concept/existing-codebase.md`). Não é a arquitetura em si — é só o que já é fato conhecido ou herdado.

## 14. Riscos e Pontos de Atenção
Riscos técnicos, de segurança ou de dado sensível identificados durante o Concept (ver `references/concept/propositions.md` sobre a diferença entre isso e questionar viabilidade). Não é uma seção de SWOT de negócio — é uma lista prática do tipo "dado de paciente aqui provavelmente é dado sensível pela LGPD; considerar isso na modelagem de acesso".

## 15. Estado do Projeto
Preenchido seguindo `references/blueprint/maturity.md` — checklist qualitativo, não percentual.

## 16. Pendências
- **Críticas**: bloqueiam a geração confiável da maioria dos documentos.
- **Menores**: não bloqueiam, mas devem aparecer marcadas como PENDENTE nos documentos que dependerem delas.

## 17. Sugestões Futuras (🔵)
Ideias que surgiram no Concept mas não foram aceitas nem rejeitadas — fora do escopo atual, mas registradas para não se perder.

## 18. Histórico de Decisões
Um log curto de mudanças relevantes pós-consolidação inicial, útil para quando `scripts/find_references.py` apontar algo que precisa de contexto:
```
[data] — BR-04 alterada: profissionais deixaram de poder cancelar reservas próprias; só a secretária pode.
```

## 19. Aprofundamento por Área

**Ao registrar algo aqui, verifique se isso resolve um PENDENTE de outra seção.** É comum uma decisão de arquitetura resolver o que a seção 13 (Requisitos Técnicos) marcava como indefinido, ou um aprofundamento de segurança responder um risco da seção 14. Quando isso acontecer, atualize a outra seção também — um Blueprint que diz "stack ainda não definida" na seção 13 e lista a stack completa aqui está se contradizendo, e quem lê primeiro decide errado.

Preenchida progressivamente durante Files-Gen, conforme `references/documents/deepening.md` — nunca durante o Concept. Cada subseção começa PENDENTE e recebe uma decisão de cada vez, sempre que um documento precisar de algo que ainda não estava aqui nem em nenhum outro documento já gerado.

```
### Arquitetura
PENDENTE

### UX/UI
PENDENTE

### Dados
PENDENTE

### API
PENDENTE

### Segurança
PENDENTE

### Performance e Escala (NFR)
PENDENTE

### Integrações
PENDENTE

### Testes e Qualidade
PENDENTE

## 20. Princípios Não-Negociáveis
Cada princípio recebe ID no formato `PRINC-01`, `PRINC-02`... Regras que valem para o projeto inteiro, sempre, e que nenhum documento gerado — nem nenhuma regra de negócio específica — pode contradizer. Diferente da seção 10 (Regras de Negócio, que descreve comportamento funcional específico) e da seção 14 (Riscos, que sinaliza pontos de atenção a considerar), aqui só entra restrição já decidida como inegociável: se um princípio está registrado aqui e um documento gerado o violaria, isso é uma inconsistência a sinalizar, não uma decisão a tomar.

Exemplos do tipo de conteúdo: "Dado de paciente nunca é compartilhado com terceiros sem consentimento explícito", "Toda ação financeira exige autenticação de dois fatores", "Nunca armazenar senha em texto plano".

## 21. Definition of Done e Convenções de Trabalho
Decisões que valem pra toda tarefa de implementação, não pra uma funcionalidade específica. São a base das seções de Convenções e Definition of Done do `CLAUDE.md`, e o que permite a um agente saber quando parar em vez de considerar concluído o que só está escrito.

**Definition of Done** — o que precisa ser verdade antes de qualquer tarefa ser considerada concluída. Cada item precisa ser verificável, não uma intenção:
```
- Testes da funcionalidade passam
- Suíte completa continua passando
- Lint/formatação sem erro
- Nenhum princípio da seção 20 violado
- Nenhum teste foi enfraquecido ou removido para fazer a tarefa passar
- Nenhuma dependência nova foi adicionada sem aprovação
- Nenhum segredo ou dado pessoal aparece em log
- [outros itens decididos pelo projeto]
```

Os três itens do meio não são burocracia: são os modos de falha mais comuns de código gerado por IA, e os três passam despercebidos numa revisão rápida porque a suíte fica verde em todos eles.

**Convenções de código** — nomenclatura, estrutura de pastas, estilo. Se o projeto parte de código existente, isso é herdado, não escolhido (ver `references/concept/existing-codebase.md`).

**Convenções de commit e branch** — padrão de mensagem, granularidade esperada, nomenclatura de branch. Importa especialmente em implementação autônoma, que gera muitos commits sem revisão humana a cada passo.

Quando qualquer um dos três ainda não foi decidido, mantenha PENDENTE — um agente seguindo uma convenção inventada é pior que um agente perguntando qual usar.
```
## 22. Fase Atual
Um projeto real não acontece de uma vez. Esta seção registra em que ponto ele está, e é o que dá sentido à expressão "desta fase" que aparece no Backlog e no `CLAUDE.md` — sem ela, "implemente as funcionalidades desta fase" não tem referente e o agente decide sozinho o que isso significa.

```
**Fase atual:** [ex.: MVP | Fase 2 — Colaboração | Manutenção]
**Objetivo desta fase:** [o que precisa estar funcionando ao fim dela]
**Funcionalidades desta fase:** [FUN-xx incluídas]
**Fases concluídas:** [histórico curto, com data]
**Próxima fase (provável):** [o que vem depois, se já se sabe]
```

Enquanto o projeto estiver na primeira fase, "Fase atual" é o MVP e esta seção repete o recorte da seção 4 — o que é aceitável e esperado. Ela passa a ganhar valor quando a primeira fase termina: aí o recorte do MVP vira histórico, e o que o agente deve implementar muda sem que o escopo do projeto mude.

Ao encerrar uma fase, não apague o que foi feito: mova para "Fases concluídas" e registre a transição na seção 18. Um agente que lê "Funcionalidades desta fase" precisa receber só a fase corrente, mas quem revisa o projeto precisa enxergar o caminho inteiro.

