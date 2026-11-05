# Guia do administrador

Para quem distribui a Vibe-Docs para uma equipe ou organização, mantém a versão em uso e responde por onde ficam os dados dos projetos.

## Pré-requisitos

| Ambiente | O que precisa estar ligado |
|---|---|
| Claude.ai (qualquer plano) | **Execução de código e criação de arquivos**. Skills não rodam sem isso. |
| Claude Code | Nada além do Claude Code. Os scripts usam Python 3.8+ da máquina, sem dependências. |

No Claude.ai, a execução de código também é o que permite à skill gravar o `PROJECT.md` como arquivo e rodar os seis verificadores.

## Distribuindo na organização (Team e Enterprise)

Os **Owners** da organização podem provisionar skills para todos os membros a partir das configurações de administração. Uma skill provisionada aparece automaticamente na lista de cada pessoa. O Owner define se ela fica ligada ou desligada por padrão, e cada pessoa ainda pode desligá-la para si.

1. Baixe `vibe-docs.skill` do [release](https://github.com/padilhars/vibe-docs/releases/latest) que vai adotar.
2. Nas configurações de administração, adicione-a como skill da organização.
3. Decida o padrão: ligada para todos, ou desligada para que cada um ative quando precisar.
4. Avise a equipe que não há comando: a skill dispara ao reconhecer um pedido de projeto (ver [Guia de uso](guia-de-uso.md)).

No Enterprise, se a varredura de skills estiver ativa, o pacote passa por ela no upload. A Vibe-Docs só contém Markdown e seis scripts Python que leem arquivos `.md` locais. Nenhum deles acessa rede.

O passo a passo atualizado das telas está na central de ajuda: [Provision and manage skills for your organization](https://support.claude.com/en/articles/12512176-what-are-skills).

## Distribuindo para uma equipe no Claude Code

Para todos que clonarem um repositório, versione a skill nele:

```bash
mkdir -p .claude/skills
cp -r /caminho/do/clone/vibe-docs/vibe-docs .claude/skills/
git add .claude/skills/vibe-docs && git commit -m "Adiciona skill vibe-docs v2.9"
```

Fixar a skill no repositório fixa também a versão: todos usam a mesma até alguém atualizar a pasta.

## Escolhendo e atualizando a versão

- Cada release traz as notas extraídas do [CHANGELOG](https://github.com/padilhars/vibe-docs/blob/main/CHANGELOG.md). Leia antes de atualizar: mudanças de comportamento estão descritas com o motivo.
- **Versão menor** (`v2.9 → v2.10`): ajustes e novos documentos. Blueprints existentes continuam válidos.
- **Versão maior** (`v2.x → v3.0`): mudança na estrutura do `PROJECT.md`. As notas dizem o que adaptar nos projetos em andamento.
- Para atualizar no Claude.ai, envie o `.skill` novo pelo mesmo caminho. A versão anterior é substituída.
- Para acompanhar lançamentos, use **Watch → Custom → Releases** no repositório do GitHub.

## Onde ficam os dados dos projetos

A skill não envia nada a lugar nenhum. O `PROJECT.md` e os documentos ficam onde a conversa grava arquivos:

| Ambiente | Onde os arquivos vivem |
|---|---|
| Claude.ai | Nos arquivos da conversa, ou no conhecimento de um Projeto, se a pessoa os salvar lá |
| Claude Code | Na pasta do repositório, versionados com o código |

Projetos que envolvem dado pessoal (saúde, CPF, endereço) tendem a gerar documentos que **descrevem** esses dados, não que os contêm. Ainda assim, oriente a equipe a não colar dados reais de clientes durante o Concept: exemplos fictícios bastam para a skill fazer as perguntas certas.

## Política sugerida para a equipe

- **Um Projeto do Claude.ai por sistema**, com o `PROJECT.md` no conhecimento. Assim qualquer pessoa retoma sem reexplicar.
- **Blueprint versionado junto com o código** quando a implementação começar (pasta `docs/` do repositório).
- **Mudança de decisão passa pela skill**, não por edição direta no código, para que o plano de propagação liste todos os documentos afetados.
- **`handoff_check.py` como portão** antes de entregar um projeto ao Claude Code.

## Problemas comuns

| Sintoma | Causa provável |
|---|---|
| A skill não aparece para ninguém | Execução de código desligada na organização, ou skill provisionada como desligada por padrão |
| Aparece, mas não dispara | Pedido genérico demais. Peça explicitamente: "use a vibe-docs para iniciar um projeto" |
| Pessoas com versões diferentes | Uploads individuais antigos convivendo com a versão da organização. Peça para removerem a cópia pessoal |
| Upload recusado | Varredura de skills, política da organização, ou o arquivo não é o `.skill` do release (o zip do código-fonte não serve) |
