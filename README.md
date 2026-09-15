# Vibe-Docs

Skill do Claude que transforma uma ideia de sistema em documentação estruturada, pronta para orientar desenvolvimento assistido por IA (vibe coding).

## Instalação

**A partir de um release:** baixe o arquivo `vibe-docs.skill` na aba Releases. No Claude.ai, vá em **Customize → Skills → + → Create skill → Upload a skill** e envie o arquivo.

**A partir do código-fonte:** clone este repositório e gere o pacote você mesmo — o `.skill` é apenas um zip com a pasta da skill dentro:

```bash
git clone <url-do-repo> vibe-docs
zip -r vibe-docs.skill vibe-docs -x '*.git*'
```

Depois envie o `.skill` gerado pelo mesmo caminho acima.

Uma vez instalada, ela dispara sozinha ao reconhecer a intenção — não precisa de comando. Basta apresentar o problema e a ideia de solução, ou dizer "quero iniciar um novo projeto".

## Como funciona

Três etapas, com transição sempre controlada pelo usuário:

| Etapa | O que acontece | Saída |
|---|---|---|
| **Concept** | Conversa investigativa — perguntas e propostas, sempre com um palpite embutido para você reagir em vez de preencher campo em branco | Nenhum arquivo |
| **Blueprint** | Checkpoint 🟢🟡🔵🔴, depois consolidação | `PROJECT.md` — fonte única de verdade |
| **Files-Gen** | Projeção do Blueprint em documentos especializados | 20 tipos de documento |

O `PROJECT.md` é a única fonte primária de verdade. Todo documento derivado sai dele, nunca o contrário — é isso que permite pedir qualquer documento, em qualquer ordem, sem reexplicar o sistema.

## Documentos gerados

**Produto:** PRD, MVP, Feature Spec
**Funcional:** Use Case Spec, Business Rules, User Stories, Process Spec
**UX:** UX Spec
**Técnico:** Architecture, Domain Model, Data Model, API Spec, Integration Spec, Security Spec, NFR
**Desenvolvimento:** Development Plan, Backlog, Test Strategy, Setup & Runbook, CLAUDE.md

O `CLAUDE.md` é o artefato final: um contrato de comportamento curto que o Claude Code carrega automaticamente quando está na raiz do repositório, com imports apontando para os documentos profundos.

## Estrutura da skill

```
vibe-docs/
├── SKILL.md                      orquestrador: etapas, roteamento, regras universais
├── references/
│   ├── concept/                  como conduzir a conversa
│   ├── blueprint/                schema do PROJECT.md, checkpoint, maturidade
│   └── documents/                um gerador por tipo de documento + regras comuns
├── scripts/
│   ├── find_references.py        análise de impacto por ID
│   ├── check_traceability.py     detecta ID citado que não existe no Blueprint
│   ├── project_status.py         visão geral do projeto
│   ├── check_staleness.py        documentos gerados de uma versão antiga do Blueprint
│   ├── check_coverage.py         decisão do Blueprint que nunca chegou a um documento
│   └── handoff_check.py          verificação pré-entrega ao Claude Code
└── assets/
    └── project-template.md       esqueleto do PROJECT.md
```

## Requisitos

Funciona melhor com acesso a terminal e sistema de arquivos — é o que permite persistir o `PROJECT.md`, rodar os scripts de rastreabilidade e ler código já existente. Sem isso, roda em modo conversacional, com essas verificações passando a ser manuais.

## Estrutura do repositório

O que está versionado aqui é o código-fonte da skill. O arquivo `.skill` distribuído nos releases é apenas esta pasta compactada — se você editar qualquer arquivo, regenere o pacote com o comando da seção de instalação.

Ao alterar comportamento, vale atualizar o `CHANGELOG.md` junto.
