# Contribuindo

## Fluxo de alteração

1. Crie um branch: `git checkout -b ajuste-backlog-atomico`.
2. Altere os arquivos em `vibe-docs/`. Para entender onde cada coisa vive, veja [docs/arquitetura-da-skill.md](docs/arquitetura-da-skill.md).
3. Valide e empacote localmente:
   ```bash
   python3 tools/validate_skill.py vibe-docs
   python3 tools/build_skill.py
   ```
4. Teste o `dist/vibe-docs.skill` no Claude.ai com pelo menos um caso real (um projeto novo do zero e, se a mudança tocar Files-Gen, a geração do documento afetado).
5. Adicione uma entrada no [CHANGELOG.md](CHANGELOG.md) explicando **o que mudou e por quê** — de preferência com o caso real que motivou a mudança.
6. Abra um Pull Request. O CI valida a estrutura, roda os scripts e checa os links da documentação.

## Princípios para editar a skill

- **Explique o porquê.** Uma regra com a razão por trás generaliza melhor que um "NUNCA" em maiúsculas.
- **Mantenha o `SKILL.md` como orquestrador.** Conteúdo detalhado vai para `references/`, carregado sob demanda.
- **O que é determinístico vira script.** Se uma verificação pode ser feita por código, não dependa da memória do modelo.
- **A documentação também encolhe.** Remover regra que não muda comportamento é uma contribuição válida.
- **Sincronize as superfícies.** Mudou um script ou um tipo de documento? Atualize `SKILL.md`, `docs/` e README juntos.

## Publicando uma versão

1. Adicione no topo do `CHANGELOG.md` uma seção `## vX.Y` com as mudanças.
2. Envie para a `main` (direto ou pelo merge do Pull Request).
3. O workflow **Release** percebe que essa versão ainda não tem release, cria a tag, valida, empacota e publica `vibe-docs.skill`, usando a seção do CHANGELOG como notas.

Enviar uma tag `vX.Y` à mão também funciona, e o workflow pode ser disparado manualmente na aba Actions.

Versionamento: incremente o **menor** (`v3.2 → v3.3`) para ajustes e novos documentos, e o **maior** (`v3.x → v4.0`) quando mudar a estrutura do `PROJECT.md` ou o comportamento de forma que projetos em andamento precisem de adaptação.

## Reportando problemas

Use os templates de issue. O mais útil é um trecho da conversa mostrando o comportamento e o que você esperava — sem dados pessoais de clientes ou pacientes.
