# Setup & Runbook — Ambiente e Operação

## Propósito
Reunir tudo que alguém (ou um agente) precisa pra sair de um repositório recém-clonado até o sistema rodando e os testes passando. É o documento que alimenta a seção de Comandos do `CLAUDE.md` — sem ele, um agente autônomo não consegue nem verificar se o que escreveu funciona.

## Insumos necessários do Blueprint
Arquitetura (stack, componentes, persistência), integrações externas (para saber quais credenciais são necessárias), Test Strategy (para o comando de teste). Se a stack ainda não foi decidida, este documento não deve ser gerado ainda — não há comando real a documentar, e inventar um genérico é pior que não ter.

## Estrutura obrigatória

```markdown
# Setup & Runbook — [Nome do Projeto]

## Pré-requisitos
[runtime e versão, banco de dados, ferramentas externas necessárias antes de qualquer coisa]

## Instalação
[passo a passo, em comandos executáveis, num bloco de código]

## Skills opcionais
[só se `SKILLS-RECOMENDADAS.md` existir: uma linha apontando para ele. Nenhuma skill é instalada como parte do setup — a instalação é decisão do usuário]

## Variáveis de Ambiente

| Variável | Obrigatória | Descrição | Exemplo (nunca um valor real) |
|---|---|---|---|

## Comandos do Dia a Dia

| Ação | Comando |
|---|---|
| Rodar em desenvolvimento | |
| Rodar todos os testes | |
| Rodar um teste específico | |
| Lint / formatação | |
| Migrations | |
| Build de produção | |

## Estrutura de Pastas
[o mapa do repositório, com uma linha sobre o que vive em cada pasta principal — é o que evita um agente criar arquivo no lugar errado]

## Dados Iniciais
[como popular o banco pra desenvolvimento — seeds, fixtures, usuário admin inicial]

## Problemas Conhecidos
[armadilhas de ambiente já identificadas, se houver — porta ocupada, dependência de sistema, passo que falha silenciosamente]
```

## Garantias que não dependem de alguém lembrar

Há uma diferença entre uma regra que o agente **deve** seguir e uma que ele **não consegue** violar. A primeira vive numa instrução e falha no dia em que o contexto está cheio ou a instrução não foi lida; a segunda vive numa verificação automática e falha nunca.

Para cada Princípio Não-Negociável (seção 20 do Blueprint) e para cada item da Definition of Done (seção 21), pergunte: isso dá para garantir mecanicamente? Quando der, especifique aqui o mecanismo em vez de confiar na instrução:

| O que proteger | Mecanismo |
|---|---|
| Suíte de testes verde antes de concluir | Comando único de verificação, rodando no CI a cada commit ou PR |
| Formatação e lint | Verificação automática ao salvar ou no CI, não revisão manual |
| Segredo nunca commitado | `.env` fora do versionamento e varredura de segredos no CI |
| Princípio inviolável que tem teste correspondente | Esse teste roda junto com a suíte, não separado |
| Tarefa só é dada como concluída com a verificação passando | Além da rotina de fim de tarefa do `CLAUDE.md`, um gancho do Claude Code que roda a verificação quando o agente termina de responder |
| Bug corrigido não volta | O teste de regressão fica na suíte, que roda no CI |

Sobre ganchos do Claude Code: eles são configurados em `.claude/settings.json` no repositório e disparam em eventos como o fim de uma resposta, o início de uma sessão ou depois de uma edição de arquivo. É o mecanismo certo para o que o `CLAUDE.md` só consegue pedir — mas o formato da configuração é do produto e muda. Se houver busca disponível, confira a documentação atual de hooks antes de escrever a configuração; sem busca, descreva o que o gancho deve fazer e deixe a configuração como pendência, em vez de escrever um formato de memória.

Registre o que for aplicável numa seção "Verificações automáticas" do documento, com o comando real de cada uma. O que não der para automatizar continua sendo instrução no `CLAUDE.md` — mas a escolha deve ser consciente, não o padrão por omissão.

## Regras específicas

- **Nunca escreva credencial, chave ou senha real neste documento**, nem como exemplo. A coluna de exemplo da tabela de variáveis existe pra mostrar o *formato* (`postgres://user:senha@localhost:5432/nome_do_banco`), não um valor que funciona.
- **Todo comando precisa ser copiável e executável como está.** "Rodar o servidor de desenvolvimento" não é comando; `npm run dev` é. Se o comando ainda não existe porque a stack não foi decidida, registre como pendência — ver `deepening.md`.
- **A estrutura de pastas aqui é a fonte da convenção**, e deve bater com o que a Arquitetura descreve. Se as duas divergirem, isso é inconsistência a sinalizar, não a resolver silenciosamente.
- Se o projeto parte de um código já existente (ver `concept/existing-codebase.md`), extraia os comandos reais do que está no repositório — `package.json`, `Makefile`, `README` — em vez de propor comandos que "deveriam" existir.
