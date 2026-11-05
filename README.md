# Vibe-Docs

[![CI](https://github.com/padilhars/vibe-docs/actions/workflows/ci.yml/badge.svg)](https://github.com/padilhars/vibe-docs/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/padilhars/vibe-docs)](https://github.com/padilhars/vibe-docs/releases/latest)

Skill do Claude que transforma uma ideia de sistema em documentação estruturada e rastreável, pronta para orientar desenvolvimento assistido por IA (*vibe coding*) no Claude Code.

> Você traz o problema e a ideia. A skill conduz a descoberta, consolida tudo num `PROJECT.md` — a fonte única de verdade — e projeta dele até 21 documentos especializados, terminando num `CLAUDE.md` que o Claude Code carrega sozinho.

## Por que existe

A maioria das conversas sobre "criar um sistema" pula para *como construir* antes de *o que exatamente estamos construindo* estar claro. O resultado é documentação que parece completa mas esconde decisões nunca tomadas — lacunas que só aparecem no meio do código. A Vibe-Docs separa essas responsabilidades em três etapas e mantém tudo amarrado por IDs verificáveis por script.

## Início rápido

1. Baixe `vibe-docs.skill` do [último release](https://github.com/padilhars/vibe-docs/releases/latest).
2. No Claude.ai: **Customize → Skills → + → Upload a skill** e envie o arquivo.
3. Comece uma conversa: *"quero iniciar um novo projeto: tenho um consultório e perco horas confirmando agendamento por WhatsApp"*.

Não há comando: a skill dispara ao reconhecer a intenção. Detalhes e alternativas em [docs/instalacao.md](docs/instalacao.md).

## Como funciona

| Etapa | O que acontece | Saída |
|---|---|---|
| **1. Concept** | Conversa investigativa — perguntas e propostas, sempre com um palpite embutido para você reagir | Nenhum arquivo |
| **2. Blueprint** | Checkpoint obrigatório 🟢🟡🔵🔴, depois consolidação | `PROJECT.md` |
| **3. Files-Gen** | Projeção do Blueprint em documentos especializados | Até 21 documentos |

A transição entre etapas é sempre sua. Guia completo em [docs/guia-de-uso.md](docs/guia-de-uso.md).

## Documentos gerados

| Grupo | Documentos |
|---|---|
| Produto | PRD, MVP, Feature Spec |
| Funcional | Use Case Spec, Business Rules, User Stories, Process Spec |
| UX | UX Spec |
| Técnico | Architecture, Domain Model, Data Model, API Spec, Integration Spec, Security Spec, NFR |
| Desenvolvimento | Development Plan, Backlog, Test Strategy, Setup & Runbook, STATE.md, CLAUDE.md |

Catálogo com o propósito de cada um e a ordem recomendada: [docs/documentos.md](docs/documentos.md).

## Documentação

| Página | Para quê |
|---|---|
| [Instalação](docs/instalacao.md) | Claude.ai, Claude Code e a partir do código-fonte |
| [Guia de uso](docs/guia-de-uso.md) | As três etapas na prática, com exemplos de pedidos |
| [Conceitos](docs/conceitos.md) | Blueprint, IDs, rastreabilidade, checkpoint, versionamento |
| [Documentos](docs/documentos.md) | Os 21 tipos e quando pedir cada um |
| [Scripts](docs/scripts.md) | Referência dos 6 scripts de verificação |
| [Do blueprint ao Claude Code](docs/handoff-claude-code.md) | Como levar o projeto para implementação |
| [Arquitetura da skill](docs/arquitetura-da-skill.md) | Como os arquivos se organizam e são carregados |
| [FAQ](docs/faq.md) | Dúvidas e problemas comuns |
| [Contribuindo](CONTRIBUTING.md) | Como alterar a skill e publicar versões |
| [Changelog](CHANGELOG.md) | Histórico de versões |

## Estrutura do repositório

```
.
├── vibe-docs/            ← a skill em si (é isto que vai para o .skill)
│   ├── SKILL.md
│   ├── references/       concept/ · blueprint/ · documents/
│   ├── scripts/          6 verificadores em Python (sem dependências)
│   └── assets/           project-template.md
├── docs/                 documentação para pessoas (não vai no pacote)
├── tools/                validação e empacotamento
└── .github/              CI, release automático e templates de issue
```

## Requisitos

Funciona melhor com terminal e sistema de arquivos (Claude.ai com execução de código, ou Claude Code) — é o que permite persistir o `PROJECT.md` e rodar os scripts. Sem isso, roda em modo conversacional, com as verificações passando a ser manuais. Os scripts usam apenas a biblioteca padrão do Python 3.8+.

## Licença

A definir. Até um arquivo `LICENSE` ser adicionado, todos os direitos ficam reservados ao autor.
