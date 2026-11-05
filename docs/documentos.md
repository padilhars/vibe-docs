# Documentos

21 tipos, todos derivados do `PROJECT.md`. Peça pelo nome ou pela intenção ("o que entra e o que fica de fora" → MVP). Cada um tem um gerador em [`vibe-docs/references/documents/`](../vibe-docs/references/documents/).

## Produto

| Documento | Para quê | Gerador |
|---|---|---|
| **PRD** | Visão, escopo e requisitos para quem decide e prioriza. Não é técnico. | `prd.md` |
| **MVP** | A menor versão que ainda resolve o problema — não a menor lista de funcionalidades. | `mvp.md` |
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
| **Development Plan** | Sequência de implementação pelas dependências reais. A fase 1 é um esqueleto funcional ponta a ponta. | `development-plan.md` |
| **Backlog** | Tarefas atômicas, prontas para pegar e implementar. | `backlog.md` |
| **Test Strategy** | Como o sistema será verificado — o que permite ao agente checar o próprio trabalho. | `test-strategy.md` |
| **Setup & Runbook** | Do clone ao sistema rodando com testes passando; garantias automáticas. | `setup-runbook.md` |
| **STATE.md** | Onde a implementação está agora. Único documento mantido pelo agente. | `state.md` |
| **CLAUDE.md** | Contrato de comportamento que o Claude Code carrega sozinho. | `claude-md.md` |

## Ordem sugerida

Qualquer ordem funciona, porque tudo sai do Blueprint. Mas algumas dependências tornam certos documentos melhores quando gerados depois de outros:

```
PRD → MVP ─┬─► Domain Model → Data Model → API Spec
           ├─► Architecture → Integration / Security / NFR
           └─► User Stories → Development Plan → Backlog
                                   Test Strategy, Setup & Runbook
                                          ↓
                                 CLAUDE.md + STATE.md   (sempre por último)
```

**Mínimo para vibe coding:** PRD, MVP, Architecture, Data Model, Backlog, Test Strategy, Setup & Runbook, CLAUDE.md, STATE.md.

## Regras comuns a todos

Definidas em [`_shared-rules.md`](../vibe-docs/references/documents/_shared-rules.md): frontmatter com a versão de origem, rastreabilidade por ID, marcação de PENDENTE, como tratar inconsistências e a rotina de fechamento (atualizar as seções 15 e 19 do Blueprint e rodar os verificadores). Antes de escrever, a skill segue a ordem de checagem de [`deepening.md`](../vibe-docs/references/documents/deepening.md): ver se o que falta já foi decidido em outro lugar antes de perguntar.
