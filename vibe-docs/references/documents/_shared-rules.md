# Regras compartilhadas — Files-Gen

Leia este arquivo antes de qualquer arquivo específico de tipo de documento (`prd.md`, `architecture.md` etc.). As regras aqui valem para todos eles; os arquivos específicos só acrescentam a estrutura e as particularidades de cada tipo.

## O papel desta etapa

O Concept respondeu "o que estamos construindo e por quê". O Blueprint consolidou "qual é a definição atual desse sistema". Files-Gen responde a uma pergunta diferente das outras duas: "como transformar essa definição já existente em um documento especializado para uma etapa específica do projeto". Ele não redescobre o produto — o Concept já aconteceu, e reabri-lo aqui desperdiça esse trabalho e arrisca contradizer decisões já tomadas.

## Antes de escrever: verifique lacunas e dependências

Antes de começar a escrever qualquer seção, veja `references/documents/deepening.md` — ele descreve a ordem certa pra checar se uma informação que falta já foi decidida em outro documento ou no Blueprint antes de tratar como lacuna nova, e o que fazer quando a lacuna for pequena (resolve na hora, com palpite embutido) ou grande demais pra resolver picotada (para e oferece escolha). Isso vale pra todo documento, mesmo que na maioria das vezes não encontre nada faltando.

## Princípios não-negociáveis sempre vencem

Antes de finalizar qualquer documento, confira a seção 20 do Blueprint (Princípios Não-Negociáveis). Se alguma parte do que você está prestes a escrever contradiz um princípio registrado ali, isso é uma inconsistência — trate como tal (ver "Consistência entre documentos" abaixo), mesmo que a contradição pareça pequena. Diferente de uma regra de negócio específica, um princípio não-negociável não se sobrepõe caso a caso: ele vale sempre, em todo documento.

## Por que evitar inventar

Cada documento derivado só tem valor se refletir fielmente o que foi decidido — é isso que permite ao usuário confiar num PRD ou numa arquitetura sem reconferir tudo manualmente contra a conversa original. Uma suposição plausível preenchendo uma lacuna parece inofensiva no momento, mas se propaga silenciosamente: o próximo documento gerado a partir desse já vai tratar a suposição como fato, e assim por diante. Por isso, quando faltar uma informação necessária para uma seção do documento:

- **Se o documento ainda faz sentido sem ela**: gere normalmente e registre a lacuna numa seção "Pendências para conclusão" no fim, explicando por que cada uma importa.
- **Se a informação for essencial** (o documento não tem como ficar coerente sem ela): não gere o documento inteiro só com suposições. Explique qual decisão está faltando e peça-a antes de finalizar.

Isso não é uma proibição de bom senso básico — um campo como `createdAt` numa entidade, ou um estado de erro padrão numa API, não precisa ter sido discutido palavra por palavra no Concept para ser incluído; são convenções que qualquer sistema semelhante teria. A linha está em: decisões que mudam comportamento, regra de negócio ou modelo de dados de forma específica ao domínio do projeto precisam vir do Blueprint, não da sua inferência.

## DEFINIDO / DERIVADO / PENDENTE

Ao redigir qualquer seção, tenha clareza interna sobre qual das três categorias a informação ocupa:

- **DEFINIDO** — está explicitamente no Blueprint.
- **DERIVADO** — pode ser deduzido logicamente de algo DEFINIDO (ex.: se `BR-04` diz que só o criador ou a secretária cancelam, um endpoint de cancelamento DERIVADAMENTE precisa checar essa permissão).
- **PENDENTE** — ainda não foi decidido.

Nunca escreva algo PENDENTE como se fosse DEFINIDO. Quando um documento tiver conteúdo DERIVADO relevante, é razoável deixar isso implícito no texto (não precisa marcar toda frase) — mas o item PENDENTE deve sempre aparecer marcado como tal.

## Rastreabilidade

Todo requisito, história ou especificação relevante deve ter um identificador, e esse identificador deve remeter à sua origem no Blueprint sempre que existir uma:

```
OBJ-01 → FUN-03 → UC-05 → BR-07 → ENT-04 → REQ-12
```

**IDs são append-only.** Nunca renumere um identificador existente para abrir espaço ou manter ordem — nem os do Blueprint, nem os locais do documento (`US-xxx`, `TASK-xxx`). Item novo recebe o próximo número livre e é posicionado no lugar certo do documento; a ordem de execução vem da posição e da onda/fase, nunca do valor numérico do ID. Renumerar parece organizado e quebra toda referência cruzada que aponta para os números antigos — inclusive em outros documentos, que a renumeração não alcança.

Prefixos padrão: `OBJ` (objetivo), `FUN` (funcionalidade), `UC` (caso de uso), `BR` (regra de negócio), `ENT` (entidade), `REQ` (requisito técnico), `PRINC` (princípio não-negociável), `US` (user story), `TASK` (tarefa de backlog), `API` (endpoint). Não invente prefixo novo: se algo não se encaixa em nenhum destes, provavelmente pertence a uma categoria que já existe. IDs que já existem no Blueprint devem ser reutilizados exatamente como estão — nunca renumerados ou reformulados num documento derivado. Depois de gerar ou editar um documento, rode `scripts/check_traceability.py` para confirmar que nenhum ID citado é inexistente no Blueprint.

## Nome do arquivo

Salve cada documento gerado na pasta do projeto com o nome padrão em maiúsculas correspondente ao tipo: `PRD.md`, `MVP.md`, `USE-CASE-SPEC.md`, `ARCHITECTURE.md`, e assim por diante — o mesmo nome do arquivo de referência em `references/documents/`, só que em maiúsculo. Para tipos que podem ter mais de uma instância no mesmo projeto (Feature Spec, Process Spec), acrescente um sufixo que identifique qual: `FEATURE-SPEC-FUN-03.md`. Uma exceção importante: o contrato do agente é salvo exatamente como `CLAUDE.md` — não é escolha de convenção nossa, é o nome que o Claude Code carrega automaticamente (ver `claude-md.md`). Essa convenção é o que permite que `scripts/project_status.py` reconheça o que já foi gerado sem precisar perguntar.

## Metadados obrigatórios

Todo documento gerado começa com o bloco abaixo — **com uma exceção: o `CLAUDE.md` não leva frontmatter algum.** Ele é o único documento carregado automaticamente por uma ferramenta, e cada linha que não muda o comportamento do agente é context window desperdiçada. Metadados ali são ruído (ver `claude-md.md`).

```yaml
---
document_type: "[tipo]"
project: "[nome]"
version: "[versão do PROJECT.md usado como fonte]"
status: "[rascunho | completo | completo com pendências]"
source: "PROJECT.md"
generated_at: "[data]"
---
```

## Consistência entre documentos

Ao gerar um novo documento, ou regenerar um existente, compare mentalmente com o Blueprint e, quando existirem, com outros documentos já gerados para o mesmo projeto. Se notar uma contradição (uma regra descrita de forma diferente, um ator que não bate, uma nomenclatura divergente), não corrija nenhum dos dois lados silenciosamente — informe a inconsistência encontrada e pergunte qual versão deve prevalecer, salvo quando for óbvio que se trata só de o outro documento estar desatualizado em relação a uma versão mais recente do Blueprint (nesse caso, o Blueprint prevalece por padrão, mas avise que isso foi assumido).

## Regenerando um documento existente

Quando o Blueprint evoluir, documentos antigos podem ficar desatualizados — não presuma que um documento gerado antes continua válido sem checar. Ao regenerar: use a versão atual do Blueprint, preserve o que ainda é válido, atualize o que mudou, e destaque ao usuário quais mudanças relevantes ocorreram em relação à versão anterior (não é necessário reescrever do zero se só uma parte mudou).

## Formato

Markdown por padrão. Títulos, listas e tabelas para informação estruturada; diagramas Mermaid quando ajudam a mostrar fluxo ou relação; evite parágrafos narrativos longos onde uma tabela seria mais clara. O documento deve ser igualmente legível por uma pessoa e por uma ferramenta de IA que vá usá-lo como contexto (como o Claude Code) — isso favorece estrutura explícita sobre prosa elegante.

## Quando um documento refina o Blueprint legitimamente

A regra geral é que documento derivado nunca contradiz o Blueprint. Mas existe um caso legítimo em que um documento **estreita ou detalha** algo que o Blueprint afirmava de forma mais ampla — o MVP recortando o escopo é o exemplo mais claro, e o Data Model detalhando uma entidade é outro.

Isso não é contradição, é a função daquele documento. O que não pode acontecer é o refinamento ficar só nele: se o Blueprint continua afirmando a versão ampla e o documento derivado afirma a estreita, quem lê cada um chega a conclusões diferentes — e o `CLAUDE.md`, que alimenta o agente, pode acabar do lado oposto do Blueprint.

Sempre que produzir um refinamento desse tipo, escreva-o de volta na seção correspondente do `PROJECT.md` e registre na seção 18 (Histórico de Decisões). O Blueprint continua sendo a fonte de verdade justamente porque absorve esses refinamentos, não porque os ignora.

## Rotina obrigatória ao terminar um documento

Estes passos fazem parte de gerar o documento, não são revisão opcional feita depois. Documento entregue sem eles está incompleto, mesmo que o conteúdo pareça bom — é o que separa um pacote coerente de um em que cada arquivo, isolado, parece correto.

**1. Revisão crítica antes de entregar.** Releia procurando ativamente: seção referenciada em outro lugar mas nunca especificada; ator, funcionalidade ou regra que o documento deveria cobrir e não cobre; afirmação escrita como fato sem ter sido decidida em lugar nenhum; referência cruzada apontando para o ID errado. Relate o que encontrar junto com o documento, com a correção ou a pergunta — nunca entregue em silêncio esperando que o usuário desconfie e pergunte. Se não encontrar nada, diga isso explicitamente; silêncio é ambíguo.

**2. Atualize as seções de estado do Blueprint.** A área correspondente da seção 19 deixa de ser `PENDENTE` e passa a apontar para o documento e registrar as decisões tomadas (ver `deepening.md`). A categoria correspondente da seção 15 (Estado do Projeto) deixa de ser ❌ e vira ✅. Essas duas seções descrevem o estado atual do projeto: mantê-las desatualizadas faz o Blueprint mentir sobre si mesmo, e ninguém percebe porque cada documento isolado continua correto.

**3. Remova a formulação antiga de toda pendência resolvida.** Resolver não é só acrescentar a resposta: é procurar onde o texto ainda diz que aquilo está em aberto e apagar. Documento que decide algo num parágrafo e diz "ainda não foi decidido" em outro é pior que documento incompleto, porque quem lê o trecho errado age com informação falsa.

**4. Confira toda lista de pendências contra o estado atual.** Nunca copie pendência de outro documento nem repita a que você mesmo escreveu antes sem reverificar — várias já podem ter sido resolvidas em rodadas seguintes.

**5. Ao terminar um documento agregador, rode `scripts/check_coverage.py`.** São quatro: `BUSINESS-RULES.md`, `TEST-STRATEGY.md`, `MVP.md` e `CLAUDE.md` — os que precisam refletir decisões espalhadas por todo o Blueprint, e onde uma ausência não aparece na leitura do próprio documento (ele parece completo; o que falta é justamente o que não está lá). Nos demais documentos o script é opcional.

Este passo existe porque script listado não é script executado: a experiência mostra que uma ferramenta só amarrada a "quando o usuário pedir" pode atravessar um projeto inteiro sem ser chamada uma única vez. Amarrar a um momento do fluxo é o que faz a verificação acontecer.

**6. Só então suba a versão.** Ver a seção seguinte.

## Sincronizar versão não é revisar

O campo `version` significa "este documento foi conferido contra aquela versão do Blueprint" — não "este arquivo foi tocado depois daquela data". Subir a versão sem reconferir o conteúdo faz o `check_staleness.py` reportar tudo em dia enquanto decisões inteiras nunca chegaram ao documento, e o problema fica invisível justamente porque a ferramenta criada para detectá-lo passa a dizer que está tudo certo.

Antes de subir a versão, confirme que as decisões novas do Blueprint desde a versão anterior daquele documento estão de fato refletidas ali. Se não estiverem, atualize primeiro. Se não se aplicam, tudo bem — mas isso é uma conclusão a verificar, não a presumir.

Atenção especial a documento criado antes de uma regra existir: ele nunca a recebeu por nenhuma cascata, porque não existia quando a decisão foi tomada. É o caso que mais escapa, e é o que `scripts/check_coverage.py` detecta.

## A documentação também deve encolher

O viés natural de todo processo documental é só acrescentar: cada rodada adiciona uma seção, um aviso, um caso particular. O resultado é um conjunto que fica mais completo e menos lido — e documento que ninguém lê é pior que documento inexistente, porque quem o consulta confia nele.

Ao revisar um documento, trate cortar como uma possibilidade legítima, não como perda:
- Pendência resolvida: o texto que descrevia a dúvida sai (já é a regra da rotina obrigatória).
- Decisão substituída: fica a atual; a anterior vive no histórico da seção 18, não no corpo do documento.
- Seção que repete o que outro documento já diz: vira uma referência pelo ID.
- Aviso que nunca mudou comportamento nenhum: sai.

Ao fim de uma fase, ou quando o usuário pedir uma auditoria, inclua no relatório o que vale cortar — não só o que falta acrescentar.

## A hierarquia nunca se inverte

```
PROJECT BLUEPRINT
      ↓
DOCUMENTOS DERIVADOS
      ↓
IMPLEMENTAÇÃO
```

Um documento gerado nunca vira fonte primária de verdade, mesmo que tenha sido refinado depois de gerado. Se o usuário editar um documento derivado diretamente e essa edição implicar numa mudança de decisão, o caminho correto é levar essa mudança de volta ao Blueprint (etapa 2) — não deixar o documento e o Blueprint divergirem silenciosamente.
