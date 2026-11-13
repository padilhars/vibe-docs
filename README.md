# Vibe-Docs

[![CI](https://github.com/padilhars/vibe-docs/actions/workflows/ci.yml/badge.svg)](https://github.com/padilhars/vibe-docs/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/padilhars/vibe-docs)](https://github.com/padilhars/vibe-docs/releases/latest)

**[padilhars.github.io/vibe-docs](https://padilhars.github.io/vibe-docs/)**

Skill do Claude que transforma uma ideia de sistema em documentação estruturada e rastreável, pronta para orientar desenvolvimento assistido por IA (*vibe coding*) no Claude Code.

> Você traz o problema e a ideia. A skill conduz a descoberta, consolida tudo num `PROJECT.md` — a fonte única de verdade — e projeta dele até 23 documentos especializados, terminando num `CLAUDE.md` que o Claude Code carrega sozinho e que já traz a rotina de fim de tarefa e o protocolo de bug.

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
| **2. Blueprint** | Checkpoint obrigatório 🟢🟡🔵🔴, simulação de uso real, depois consolidação | `PROJECT.md` |
| **3. Files-Gen** | Projeção do Blueprint em documentos especializados | Até 23 documentos |

A transição entre etapas é sempre sua. Guia completo em [docs/guia-de-uso.md](docs/guia-de-uso.md).

## Documentos gerados

| Grupo | Documentos |
|---|---|
| Produto | PRD, MVP, Feature Spec |
| Funcional | Use Case Spec, Business Rules, User Stories, Process Spec |
| UX | UX Spec |
| Técnico | Architecture, Domain Model, Data Model, API Spec, Integration Spec, Security Spec, NFR |
| Desenvolvimento | Development Plan, Backlog, Test Strategy, Setup & Runbook, Skills recomendadas |
| Para o agente de implementação | CLAUDE.md, STATE.md, LEARNINGS.md |

Catálogo com o propósito de cada um e a ordem recomendada: [docs/documentos.md](docs/documentos.md).

## Documentação

Também publicada em [padilhars.github.io/vibe-docs/docs](https://padilhars.github.io/vibe-docs/docs/).

**Manual do usuário:** [Instalação](docs/instalacao.md) · [Guia de uso](docs/guia-de-uso.md) · [Conceitos](docs/conceitos.md) · [Documentos](docs/documentos.md) · [Do Blueprint ao Claude Code](docs/handoff-claude-code.md) · [FAQ](docs/faq.md)

**Guia do administrador:** [Distribuição, versões e dados](docs/guia-do-admin.md)

**Documentação técnica:** [Arquitetura da skill](docs/arquitetura-da-skill.md) · [Scripts](docs/scripts.md) · [Validação, release e site](docs/ci-e-release.md) · [Contribuindo](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## Estrutura do repositório

```
.
├── vibe-docs/            ← a skill em si (é isto que vai para o .skill)
│   ├── SKILL.md
│   ├── references/       concept/ · blueprint/ · documents/
│   ├── scripts/          6 verificadores em Python + módulo comum (sem dependências)
│   └── assets/           project-template.md
├── docs/                 documentação (fonte do site; não vai no pacote)
├── site/                 página inicial e estilos do site
├── tools/                validação e empacotamento
└── .github/              CI, release automático e templates de issue
```

## Requisitos

No Claude.ai, a execução de código e criação de arquivos precisa estar ligada (skills não rodam sem ela). No Claude Code, nada além dele. Os scripts usam apenas a biblioteca padrão do Python 3.8+.

## Licença

A definir. Até um arquivo `LICENSE` ser adicionado, todos os direitos ficam reservados ao autor.
