# Validação, release e site

Como o repositório garante que o que chega aos usuários está íntegro, e como cada artefato é produzido.

## Ferramentas locais

| Comando | O que faz |
|---|---|
| `python3 tools/validate_skill.py vibe-docs` | Valida a estrutura da skill |
| `python3 tools/build_skill.py` | Gera `dist/vibe-docs.skill` |
| `python3 tools/build_site.py` | Gera o site em `_site/` a partir de `site/` e `docs/` (requer `pip install markdown`) |

### O que o validador confere

- `SKILL.md` com frontmatter contendo `name` e `description`
- `name` em kebab-case, até 64 caracteres, igual ao nome da pasta
- `description` com até 1024 caracteres e sem `<` ou `>`
- corpo do `SKILL.md` abaixo de 500 linhas
- todo caminho `references/…`, `scripts/…` ou `assets/…` citado em qualquer `.md` existe
- todo script de `scripts/` compila
- nenhum arquivo que não deve ir no pacote (README, CHANGELOG, caches)

Sai com código 1 no primeiro problema encontrado, listando todos.

### O pacote `.skill`

Um zip cuja raiz é a pasta `vibe-docs/`. O build é determinístico (datas fixas, ordem alfabética, arquivos ocultos excluídos), então o mesmo conteúdo gera sempre o mesmo arquivo.

## Workflows do GitHub Actions

| Workflow | Quando roda | O que faz |
|---|---|---|
| **CI** (`ci.yml`) | Push na `main` e Pull Requests | Valida a skill em Python 3.8 e 3.12, roda os seis scripts contra o template, confere os links internos da documentação e empacota. O `.skill` fica disponível como artefato da execução |
| **Release** (`release.yml`) | Push na `main` que toca `CHANGELOG.md` ou `vibe-docs/`, push de tag `v*`, ou manual | Lê a versão do topo do CHANGELOG. Se ainda não existe release com essa tag, valida, empacota, cria a tag e publica o release com o `.skill` e as notas da versão |
| **Página** (`pages.yml`) | Push na `main` que toca `site/`, `docs/` ou `tools/build_site.py`, ou manual | Gera o site e publica no GitHub Pages |

### Smoke test dos scripts

O CI copia `assets/project-template.md` como `PROJECT.md` de um projeto vazio e roda cada script contra ele. Códigos 0 e 1 são resultados válidos (sem problema / problema encontrado). Qualquer outro código, ou uma exceção, falha o CI.

## Publicando uma versão

1. Adicione `## vX.Y` no topo do `CHANGELOG.md`, com o que mudou e por quê.
2. Envie para a `main`.
3. O workflow Release cria a tag `vX.Y` e o release. O link "último release" do README e do site passa a apontar para ele.

Se o release falhar, corrija e envie de novo. Ele só é criado quando todas as etapas passam, então não sobra release pela metade.

## O site

O site é gerado, não escrito à mão:

- `site/index.html` é a página inicial.
- Cada arquivo de `docs/` vira uma página HTML, organizada em três trilhas: manual do usuário, guia do administrador e documentação técnica.
- Links entre arquivos de `docs/` viram links entre páginas. Links para a skill ou para arquivos da raiz apontam para o GitHub.

Para mudar a documentação, edite o Markdown em `docs/`. O site se atualiza no próximo push. Para mudar a ordem ou a trilha de uma página, edite a lista `NAV` em `tools/build_site.py`.

Ativação, feita uma vez: **Settings → Pages → Source: GitHub Actions**.
