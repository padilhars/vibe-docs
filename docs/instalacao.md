# Instalação

## Claude.ai (web, desktop ou app)

1. Baixe `vibe-docs.skill` da página de [Releases](https://github.com/padilhars/vibe-docs/releases/latest).
2. Em **Customize → Skills**, clique em **+ → Upload a skill** e envie o arquivo.
3. Confirme que a skill aparece ativada na lista.

A **execução de código e criação de arquivos** precisa estar ligada nas configurações: no Claude.ai, skills não rodam sem ela. É também o que permite à skill gravar o `PROJECT.md` e rodar os scripts.

Em contas Team e Enterprise, o administrador pode distribuir a skill para a organização inteira. Veja o [Guia do administrador](guia-do-admin.md).

## Claude Code

Skills do Claude Code são pastas com um `SKILL.md`. Copie a pasta `vibe-docs/` deste repositório para um destes lugares:

| Escopo | Caminho |
|---|---|
| Só para você, em todos os projetos | `~/.claude/skills/vibe-docs/` |
| Para todo mundo que clonar um repositório | `<repo>/.claude/skills/vibe-docs/` |

```bash
git clone https://github.com/padilhars/vibe-docs.git
mkdir -p ~/.claude/skills
cp -r vibe-docs/vibe-docs ~/.claude/skills/
```

Para manter atualizado, prefira um link simbólico para o clone e dê `git pull` quando sair versão nova:

```bash
ln -s "$(pwd)/vibe-docs/vibe-docs" ~/.claude/skills/vibe-docs
```

## A partir do código-fonte

O `.skill` é só um zip cuja raiz é a pasta da skill. Para gerar o seu:

```bash
python3 tools/validate_skill.py vibe-docs   # confere frontmatter e links internos
python3 tools/build_skill.py                # gera dist/vibe-docs.skill
```

## Verificando se funcionou

Numa conversa nova, escreva algo como *"me ajuda a pensar num sistema para controlar empréstimo de equipamentos do laboratório"*. A skill deve responder com perguntas de descoberta — cada uma com um palpite para você confirmar ou corrigir — e **não** gerar nenhum documento ainda. Se ela pular direto para um PRD, provavelmente não foi carregada.

## Atualizando

Baixe o `.skill` novo e envie de novo pelo mesmo caminho; a versão anterior é substituída. O que mudou em cada versão está no [CHANGELOG](../CHANGELOG.md). Projetos já em andamento continuam compatíveis: o `PROJECT.md` não depende da versão da skill que o gerou. Vindo de uma versão anterior à v3.2, regenere o `CLAUDE.md` dos projetos que já estão em implementação (o motivo está no [FAQ](faq.md)).
