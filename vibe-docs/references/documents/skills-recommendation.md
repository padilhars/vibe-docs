# SKILLS-RECOMENDADAS.md — Skills que podem ajudar na implementação

## Propósito
Indicar um conjunto pequeno de skills de uso livre e gratuito que ajudariam a implementar **este** projeto — por causa da stack escolhida, do tipo de interface, das integrações — e deixar pronto o pedido de instalação para o usuário aprovar.

É um documento opcional. Só vale gerar depois que a Arquitetura existe, porque a recomendação depende da stack.

## O que este documento não é

Não é um catálogo. Catálogos comunitários listam dezenas de milhares de skills de qualidade muito desigual; copiar uma lista longa transfere ao usuário o trabalho de triagem, que é justamente o que ele pediu para não fazer. O valor está em poucas indicações, cada uma com o motivo de servir a este projeto.

## Pesquise agora, nunca de memória

Skills, repositórios e comandos de instalação mudam rápido, e uma skill lembrada de memória pode ter sido renomeada, abandonada ou nunca ter existido com aquele nome. Recomendar de memória é a forma mais provável de este documento mandar instalar algo que não existe.

- **Com busca disponível**: pesquise, abra a página de cada candidata e confirme que existe, o que faz e como se instala. Registre a data da verificação.
- **Sem busca disponível**: não gere o documento. Diga ao usuário que a recomendação exige pesquisa e ofereça gerar quando houver busca, ou a partir de links que ele trouxer.

## Onde procurar, nesta ordem

1. **Fontes oficiais da Anthropic** — o repositório oficial de skills e o marketplace oficial de plugins do Claude Code. Confirme os nomes atuais na documentação antes de citar.
2. **Projetos de código aberto estabelecidos** — repositório público, licença declarada, manutenção recente, uso amplo.
3. **Catálogos comunitários** — só como forma de achar candidatas; a avaliação é feita na página do repositório de origem, não no catálogo.

## Critérios para entrar na lista

Uma skill entra se **todas** as condições valem:

- É gratuita e tem licença que permite o uso (anote qual).
- Você abriu a origem e confirmou o que ela faz.
- Ela resolve uma necessidade concreta deste projeto, que você consegue nomear (a stack, um tipo de tarefa do backlog, uma integração).
- Você sabe dizer o que ela acessa ou executa.

Uma skill fica de fora se pede acesso amplo sem necessidade aparente, se a origem não é clara, ou se você não conseguiu confirmar o comando de instalação.

No máximo cinco. Se só duas passarem nos critérios, o documento tem duas.

## Segurança: o que dizer ao usuário

Uma skill de terceiro é instrução e, às vezes, código que roda com as permissões do agente. Uma skill pode conceder a si mesma acesso a ferramentas, então vale ler o arquivo `SKILL.md` e os scripts antes de instalar — principalmente os que executam comandos. Escreva isso no documento em uma frase, sem alarmismo, e nunca apresente uma skill de terceiro como auditada por você: você leu a descrição, não fez auditoria.

## Conflito com o contrato do projeto

Algumas skills trazem método próprio de trabalho — como planejar, como testar, quando fazer commit. Isso pode colidir com as rotinas do `CLAUDE.md` deste projeto (fim de tarefa, protocolo de bug, Definition of Done). Para cada skill desse tipo, diga onde há sobreposição e qual das duas o usuário deveria deixar mandar. Duas instruções conflitantes sobre o mesmo momento produzem um agente que segue ora uma, ora outra.

## Estrutura obrigatória

```markdown
# Skills recomendadas — [Nome do Projeto]

Verificado em [data]. Nenhuma destas é instalada automaticamente: instale só as que você aprovar. Skills de terceiros rodam com as permissões do agente — vale ler o SKILL.md e os scripts de cada uma antes.

## Recomendadas

### [Nome da skill]
- **O que faz:** [uma frase]
- **Por que ajuda neste projeto:** [a necessidade concreta — stack, onda do backlog, integração]
- **Origem:** [link do repositório ou do marketplace] · **Licença:** [qual]
- **O que acessa ou executa:** [ferramentas, comandos, rede — o que você verificou]
- **Sobreposição com o CLAUDE.md:** [nenhuma | onde, e qual deve mandar]
- **Instalação:** `[comando exato, como consta na origem]`

## Avaliadas e não recomendadas
[opcional: candidatas que pareciam servir e por que ficaram de fora — evita que sejam reavaliadas]

## Pedido de instalação

Depois de escolher, cole no Claude Code, mantendo só as que aprovou:

> Instale as skills abaixo, uma por vez. Antes de cada uma, mostre o que será instalado e de onde, e espere minha confirmação. Depois de instalar, confirme que foi carregada.
> - [nome] — `[comando]`
```

## Onde isto aparece nos outros documentos

- No `SETUP-RUNBOOK.md`, como passo **opcional** depois da instalação do ambiente, apontando para este arquivo.
- No `CLAUDE.md`, como uma linha da documentação de referência, com a instrução de instalar só o que o usuário aprovar. O `CLAUDE.md` nunca manda instalar.

## Regras específicas

- **Nunca instale nada ao gerar este documento.** Ele recomenda; quem decide é o usuário.
- **Copie o comando de instalação da origem, exatamente.** Não reconstrua de memória nem por analogia com outra skill.
- **Este documento não tem IDs do Blueprint a cobrir** e não entra na verificação de cobertura. Leva o frontmatter padrão, com a versão do Blueprint contra a qual a stack foi lida.
- **Envelhece rápido.** Se o projeto for retomado meses depois, reverifique antes de confiar — a data no topo existe para isso.
