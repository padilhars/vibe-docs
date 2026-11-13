# Documentos

23 tipos, todos derivados do `PROJECT.md`. Peça pelo nome ou pela intenção ("o que entra e o que fica de fora" → MVP). Cada um tem um gerador em [`vibe-docs/references/documents/`](../vibe-docs/references/documents/).

## Produto

| Documento | Para quê | Gerador |
|---|---|---|
| **PRD** | Visão, escopo e requisitos para quem decide e prioriza. Não é técnico. | `prd.md` |
| **MVP** | A menor versão que ainda resolve o problema — não a menor lista de funcionalidades. Grava o corte de volta nas seções 4 e 22 do Blueprint. | `mvp.md` |
| **Feature Spec** | Uma única funcionalidade (`FUN-xx`) em todo o detalhe comportamental. | `feature-spec.md` |

## Funcional

| Documento | Para quê | Gerador |
|---|---|---|
| **Use Case Spec** | Cada caso de uso com pré-condições, fluxos principal e alternativos, pós-condições. | `use-case-spec.md` |
| **Business Rules** | Todas as regras num só lugar — revisão de negócio e checklist de implementação. | `business-rules.md` |
| **User Stories** | Funcionalidades em histórias com critérios de aceitação. | `user-stories.md` |
| **Process Spec** | Processo ponta a ponta que atravessa vários casos de uso e atores. | `process-spec.md` |

## UX

| Documento | Para quê | Gerador |
|---|---|---|
| **UX Spec** | Jornadas, arquitetura de informação, telas e interação, num só documento. | `ux-spec.md` |

## Técnico

| Documento | Para quê | Gerador |
|---|---|---|
| **Architecture** | Como o sistema será construído; onde as decisões de tecnologia entram. | `architecture.md` |
| **Domain Model** | Entidades conceituais, relacionamentos, estados e invariantes — sem banco. | `domain-model.md` |
| **Data Model** | Representação lógica pronta para virar schema. | `data-model.md` |
| **API Spec** | Só os endpoints que algum caso de uso exige. | `api-spec.md` |
| **Integration Spec** | Cada sistema externo (pagamento, e-mail, calendário…) em detalhe. | `integration-spec.md` |
| **Security Spec** | Autenticação, autorização e proteção de dado sensível. | `security-spec.md` |
| **NFR** | Performance, disponibilidade, escala, manutenibilidade. | `nfr.md` |

## Desenvolvimento

| Documento | Para quê | Gerador |
|---|---|---|
| **Development Plan** | Sequência de implementação pelas dependências reais, em ondas. A onda 1 é um esqueleto funcional ponta a ponta. | `development-plan.md` |
| **Backlog** | Tarefas atômicas, agrupadas por onda, prontas para pegar e implementar. O agente marca cada uma ao concluir. | `backlog.md` |
| **Test Strategy** | Como o sistema será verificado — o que permite ao agente checar o próprio trabalho. Inclui a política de testes de regressão. | `test-strategy.md` |
| **Setup & Runbook** | Do clone ao sistema rodando com testes passando; garantias automáticas por gancho ou CI. | `setup-runbook.md` |
| **Skills recomendadas** (opcional) | Até cinco skills gratuitas que ajudam a implementar este projeto, com origem, licença, o que acessam e o pedido de instalação pronto. | `skills-recommendation.md` |

## Para o agente de implementação

Os três nascem juntos: pedir qualquer um gera o trio.

| Documento | Para quê | Gerador |
|---|---|---|
| **CLAUDE.md** | Contrato de comportamento que o Claude Code carrega sozinho, com a rotina de fim de tarefa e o protocolo de bug. | `claude-md.md` |
| **STATE.md** | Onde a implementação está agora. Sobrescrito pelo agente a cada tarefa concluída. | `state.md` |
| **LEARNINGS.md** | O que a implementação ensinou e a próxima sessão precisa saber: armadilhas do ambiente, padrões estabelecidos, o que não funcionou, decisões técnicas. Limitado a 100 linhas. | `learnings.md` |

### Sobre as skills recomendadas

O documento é montado por pesquisa feita na hora, nunca de memória, começando pelas fontes oficiais. Cada skill entra com o motivo de servir a **este** projeto e com o que se sobrepõe ao `CLAUDE.md`. Nada é instalado sem a sua aprovação: o documento traz o pedido de instalação pronto para você usar, depois de revisar o que cada skill acessa.

## Ordem sugerida

Qualquer ordem funciona, porque tudo sai do Blueprint. Mas algumas dependências tornam certos documentos melhores quando gerados depois de outros:

```
PRD → MVP ─┬─► Domain Model → Data Model → API Spec
           ├─► Architecture → Integration / Security / NFR
           └─► User Stories → Development Plan → Backlog
                                   Test Strategy, Setup & Runbook
                                          ↓
                       CLAUDE.md + STATE.md + LEARNINGS.md   (sempre por último)
```

**Mínimo para vibe coding:** PRD, MVP, Architecture, Backlog, Test Strategy, Setup & Runbook e o trio CLAUDE.md, STATE.md, LEARNINGS.md. Data Model, Business Rules, API Spec e Development Plan são recomendados.

## Regras comuns a todos

Definidas em [`_shared-rules.md`](../vibe-docs/references/documents/_shared-rules.md): frontmatter com a versão de origem (exceto `CLAUDE.md`, `STATE.md` e `LEARNINGS.md`, que não levam metadados), rastreabilidade por ID, marcação de PENDENTE, como tratar inconsistências e a rotina de fechamento em sete passos (devolver ao Blueprint o que foi decidido, rodar `check_traceability.py` sempre e `check_coverage.py` nos documentos agregadores, entregar o arquivo). Antes de escrever, a skill segue a ordem de checagem de [`deepening.md`](../vibe-docs/references/documents/deepening.md): ver se o que falta já foi decidido em outro lugar antes de perguntar.
