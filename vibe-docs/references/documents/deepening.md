# Aprofundamento sob demanda e dependência entre documentos

## Por que isso existe

O Concept é otimizado pra capturar o essencial de negócio — problema, atores, entidades, regras, fluxo principal. Isso deixa alguns documentos (Architecture, UX Spec, Data Model, API Spec, Security Spec, NFR, Integration Spec) sistematicamente rasos, porque ninguém nunca perguntou o que eles precisam especificamente.

A alternativa óbvia seria fazer o Concept perguntar sobre tudo isso também, antes de consolidar o Blueprint. Isso foi considerado e descartado: forçaria uma sessão de perguntas enorme sobre assunto que a pessoa pode nem precisar (quem só quer o PRD não precisa discutir modelo de dados antes), reabriria o mesmo problema de interrogatório já corrigido no Concept (ver `concept/methodology.md`), e quebraria a promessa central da skill — pedir qualquer documento, em qualquer ordem, sem reexplicar nada antes.

Em vez disso, o aprofundamento acontece sob demanda: só quando um documento específico é pedido e falta algo que ele especificamente precisa, e só sobre aquilo — nunca uma sessão genérica sobre "toda a arquitetura" quando o que foi pedido foi só a API Spec.

## Antes de gerar: de onde vem a informação que falta

Quando notar que falta algo pra completar um documento, não presuma que é uma lacuna nova — verifique nesta ordem antes de perguntar qualquer coisa:

1. **Já existe outro documento gerado que decidiu isso?** Veja a tabela de dependência abaixo e, se aplicável, confira o documento indicado. Reutilize a decisão de lá — nunca redecida algo que já foi decidido em outro documento. É isso que evita a Arquitetura dizer Postgres e o Data Model assumir outra coisa sem ninguém perceber.
2. **Já está no Blueprint?** Inclui a seção 19 (Aprofundamento por Área), que existe justamente pra guardar decisões técnicas capturadas durante gerações anteriores. Use direto.
3. **Não existe em lugar nenhum?** Essa é a lacuna real — trate como pequena ou grande (ver abaixo).

## Tabela de dependência entre documentos

| Documento | Pode puxar de |
|---|---|
| Data Model | Domain Model |
| API Spec | Data Model |
| Development Plan | Architecture |
| Backlog | User Stories, Development Plan, Architecture |
| Test Strategy | Architecture, User Stories (critérios de aceitação), seção 20 do Blueprint |
| Setup & Runbook | Architecture, Integration Spec, Test Strategy |
| Skills recomendadas | Architecture (a recomendação depende da stack) |
| CLAUDE.md | Praticamente todos os outros já gerados — em especial Setup & Runbook (comandos), Test Strategy (comando de verificação) e seções 20, 21 e 22 do Blueprint |

Isso não é uma lista de pré-requisitos obrigatórios — é só onde procurar antes de perguntar. Um documento pode ser gerado sem os outros da lista existirem ainda, desde que o Blueprint sozinho já baste.

## Lacuna pequena

Um ou dois fatos pontuais faltando — por exemplo, o Data Model já está quase todo claro pelas entidades do Blueprint, só falta saber se os IDs são UUID ou incremental. Resolva assim:

- Use o mesmo mecanismo de palpite embutido de `concept/questioning.md`: proponha a resposta mais comum pra esse tipo de decisão, peça confirmação, nunca deixe a pergunta em branco.
- Pode agrupar até 2-3 lacunas pequenas numa mensagem só, já que é uma rodada rápida e focada, não uma sessão inteira — mas nunca gere o documento na mesma mensagem que faz a pergunta. Espere a resposta antes de gerar.
- **A resposta é gravada no `PROJECT.md`, não só usada dentro do documento atual e esquecida.** Preencher o que estava `PENDENTE` não sobe a versão do Blueprint (ver "Quando a versão sobe" em `blueprint/schema.md`). É isso que garante que, da próxima vez que outro documento precisar da mesma informação, ela já esteja disponível sem perguntar de novo. Onde gravar depende da natureza da decisão (ver abaixo).
- Se o usuário responder "não sei", registre como pendência (marcada como PENDENTE) e gere o documento normalmente, com essa parte também marcada como pendência — mesma lógica de `_shared-rules.md` sobre lacunas.

### Onde gravar cada resposta

| Natureza da decisão | Vai para |
|---|---|
| Técnica, específica de uma área (Arquitetura, UX/UI, Dados, API, Segurança, NFR, Integrações, Testes e Qualidade) | Seção 19, na subseção da área |
| Restrição que nunca pode ser violada, em nenhuma circunstância | Seção 20 (Princípios Não-Negociáveis) |
| Definition of Done, convenção de código, convenção de commit/branch | Seção 21 |
| Objetivo e funcionalidades da fase atual | Seção 22 (normalmente pelo `MVP.md`) |

As seções 20 e 21 raramente são preenchidas no Concept — normalmente surgem aqui, quando o `CLAUDE.md`, o Test Strategy ou o Setup & Runbook precisam delas. Ambas bloqueiam o handoff se ficarem PENDENTE (ver `scripts/handoff_check.py`), então, ao gerar qualquer um desses três documentos, verifique-as explicitamente em vez de esperar que alguém tenha preenchido antes.

Perguntas úteis para a seção 21, com palpite embutido como sempre: "pra considerar uma tarefa concluída, imagino: testes da funcionalidade passam, suíte completa continua passando, lint sem erro, e nenhum princípio da seção 20 violado — quer acrescentar algo?" e "pra commits, meu palpite é conventional commits (`feat:`, `fix:`) com um commit por tarefa do backlog — serve?".

## Lacuna grande

Uma área inteira ainda não foi pensada, não é um fato pontual — por exemplo, o Backlog fica bem mais granular com a Arquitetura definida, e a Arquitetura ainda nem existe. Não tente resolver isso picotado dentro do documento atual. Pare, explique a dependência, e ofereça a escolha:

> "[Documento pedido] fica bem mais [sólido/granular/preciso] com [Documento do qual depende] definido, e isso ainda não existe. Prefere que eu gere [Documento do qual depende] primeiro, ou quer que eu monte [Documento pedido] só com o nível de detalhe que o Blueprint já permite, deixando o resto como pendência?"

Se o usuário quiser só aprofundar a área sem gerar o documento de dependência inteiro, isso também é válido — vira uma rodada focada só naquela área, com o resultado indo para a seção correspondente (ver tabela acima), sem produzir o arquivo do documento de dependência.

## Aprofundar antecipadamente

O usuário pode pedir esse mesmo mecanismo de forma proativa, antes de pedir qualquer documento específico — por exemplo, "vamos aprofundar arquitetura e UX antes de eu pedir os documentos". Trate como uma sessão de aprofundamento focada exatamente nas áreas pedidas: mesmo mecanismo de palpite embutido, mesma gravação na seção correspondente, só que antecipada em vez de disparada por um pedido de documento específico. "Definition of Done e convenções" é uma área válida de aprofundamento antecipado como qualquer outra.

## Depois de gerar: a área correspondente não pode continuar vazia

Terminado o documento, olhe a área da seção 19 que corresponde a ele (Architecture → Arquitetura, UX Spec → UX/UI, Data Model → Dados, API Spec → API, Security Spec → Segurança, NFR → Performance e Escala, Integration Spec → Integrações, Test Strategy → Testes e Qualidade). Uma das duas coisas precisa ser verdade:

1. **A área registra as decisões que o documento tomou.** Toda escolha feita durante a geração — mesmo as que você derivou sozinho sem precisar perguntar — que outro documento poderia precisar depois, vai para lá.
2. **A área diz explicitamente que o documento foi gerado sem aprofundamento**, e por quê (ex.: "gerado a partir das entidades do Blueprint, sem decisões novas").

O que não pode acontecer é o documento existir e a área continuar `PENDENTE`, sem explicação. Isso significa que decisões foram tomadas em algum lugar e não voltaram para o Blueprint — que deixa de ser a fonte completa de verdade sem que ninguém perceba, porque cada documento isolado parece correto. Isso é parte do passo 2 da rotina obrigatória de `_shared-rules.md`, executado ao terminar cada documento — não algo a descobrir no fim do projeto. O `handoff_check.py` também sinaliza, mas contar com ele é frágil: ele só roda se alguém lembrar de chamá-lo, e a experiência mostra que um projeto inteiro pode ser gerado sem que isso aconteça uma única vez.

## Quais documentos tendem a precisar disso

PRD, MVP, User Stories, Business Rules e Use Case Spec normalmente já saem bem servidos só com o que o Concept cobre — o mecanismo acima raramente encontra lacuna real pra eles. Architecture, UX Spec, Data Model, API Spec, Security Spec, NFR, Integration Spec, Test Strategy e Setup & Runbook são os que mais tendem a precisar de aprofundamento, porque cobrem assunto que o Concept não é desenhado pra capturar. Isso não é uma regra rígida — trate qualquer documento pela mesma lógica de checagem, e só acione o aprofundamento quando a lacuna for real.
