# Arquitetura da skill

Para quem vai manter ou estender a Vibe-Docs.

## Carregamento progressivo

Uma skill é carregada em três níveis, e a organização dos arquivos segue isso:

| Nível | O que | Quando entra no contexto |
|---|---|---|
| 1 | `name` + `description` do frontmatter | Sempre — é o que decide se a skill dispara |
| 2 | Corpo do `SKILL.md` | Quando a skill dispara |
| 3 | Arquivos de `references/` | Só quando o `SKILL.md` manda ler |

Por isso o `SKILL.md` é um **orquestrador** enxuto (bem abaixo das 500 linhas recomendadas): define as etapas, a tabela de roteamento e as regras universais, e aponta para o arquivo certo. Gerar um PRD carrega `_shared-rules.md`, `deepening.md` e `prd.md` — não os outros 22 geradores.

## Mapa dos arquivos

```
vibe-docs/
├── SKILL.md
├── references/
│   ├── concept/
│   │   ├── methodology.md        condução da conversa, quando sugerir consolidar
│   │   ├── questioning.md        perguntas com palpite embutido
│   │   ├── propositions.md       como propor sem inventar; limite de viabilidade
│   │   ├── edge-cases.md         checklist de casos de borda
│   │   ├── existing-codebase.md  ler código antes de perguntar
│   │   └── prior-art.md          pesquisa do domínio → pergunta, nunca funcionalidade
│   ├── blueprint/
│   │   ├── review-checklist.md   checkpoint 🟢🟡🔵🔴
│   │   ├── schema.md             as 22 seções do PROJECT.md e a regra de versão
│   │   ├── simulation.md         simulação de uso real
│   │   └── maturity.md           estado qualitativo
│   └── documents/
│       ├── _shared-rules.md      regras de todo derivado
│       ├── deepening.md          ordem de checagem e lacunas
│       └── <tipo>.md × 23        um gerador por documento
├── scripts/                      6 verificadores + _common.py (módulo compartilhado)
└── assets/
    └── project-template.md       esqueleto do PROJECT.md
```

## Decisões de projeto

- **Raciocínio explicado em vez de "NUNCA".** Os arquivos de referência dizem *por que* cada regra existe; o modelo generaliza melhor para casos não previstos.
- **Scripts para o que é determinístico.** Rastreabilidade, versão e cobertura não dependem da memória da conversa.
- **Toda verificação presa a um momento do fluxo.** Um script que ninguém manda rodar não roda. Cada um tem gatilho na rotina de fechamento de documento, no fluxo de alteração ou na retomada.
- **Uma verificação dinâmica além das estáticas.** A simulação de uso real narra o sistema no tempo e pega o que leitura de documento não pega.
- **Um só lugar para o que os scripts compartilham.** Padrão de ID, leitura de seção e localização do `CLAUDE.md` vivem em `scripts/_common.py`.
- **Um gerador por tipo, regras comuns separadas.** Evita repetir as mesmas regras 23 vezes e mantém cada arquivo pequeno.
- **Tipos parecidos mesclados.** Vision e Scope estão no PRD; Journeys, IA e telas, no UX Spec; Dev Tasks, no Backlog.

## Adicionando um tipo de documento

1. Crie `references/documents/<tipo>.md` seguindo a estrutura dos outros: Propósito, Insumos necessários do Blueprint, Estrutura obrigatória, Regras específicas.
2. Adicione a linha na tabela de roteamento do `SKILL.md`.
3. Se o tipo tiver nome de arquivo próprio, inclua-o na lista de tipos conhecidos de `project_status.py` (e, se for essencial, de `handoff_check.py`). Se ele criar um prefixo de ID próprio ou não levar frontmatter, registre isso em `scripts/_common.py`.
4. Atualize [documentos.md](documentos.md), o README e o CHANGELOG.
5. Rode `python3 tools/validate_skill.py vibe-docs`.

## Limite da descrição

O campo `description` tem no máximo 1024 caracteres. Ele é o único texto que decide o disparo, então é deliberadamente específico e "insistente" (lista os tipos de documento e frases como "me ajuda a pensar num sistema pra X"). O validador do CI falha se passar do limite.
