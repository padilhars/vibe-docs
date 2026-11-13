# Scripts

Seis verificadores em `vibe-docs/scripts/`, mais `_common.py`, o módulo que eles compartilham (não é um comando). Python 3.8+, só biblioteca padrão. A skill os roda sozinha nos momentos certos; você também pode rodá-los à mão.

Todos recebem a pasta que contém o `PROJECT.md`. Funcionam nos dois layouts: tudo numa pasta só, durante a documentação, ou `CLAUDE.md` na raiz do repositório com o restante em `docs/`, depois do handoff (nesse caso, passe `docs/`; o `CLAUDE.md` é encontrado na pasta acima).

```bash
python3 vibe-docs/scripts/<script>.py <pasta-do-projeto> [argumentos]
```

Os verificadores saem com **0** quando está tudo certo e **1** quando encontram problema — dá para usá-los num CI do seu repositório de documentação.

| Script | Pergunta que responde | Quando a skill roda |
|---|---|---|
| `find_references.py` | Onde este ID é citado? | Antes de qualquer alteração de decisão |
| `check_traceability.py` | Algum documento cita ID que não existe no Blueprint? | Depois de gerar ou editar um documento |
| `check_staleness.py` | Quais documentos saíram de uma versão antiga do Blueprint? | Ao fim de toda alteração de decisão e ao retomar um projeto |
| `check_coverage.py` | Alguma decisão nunca chegou aos documentos onde é obrigatória? | Ao terminar um documento agregador e ao fim de toda alteração de decisão |
| `project_status.py` | Como está o projeto? | Ao retomar um projeto e em pedidos de status |
| `handoff_check.py` | Dá para entregar ao Claude Code? | Ao terminar o `CLAUDE.md` e antes da implementação |

## `find_references.py <pasta> <ID>`

Lista arquivo e linha de cada ocorrência do ID. A busca é pelo ID inteiro: `TASK-01` não devolve `TASK-010`. É a base da análise de impacto: a skill monta o plano de propagação a partir daqui, não da memória da conversa.

```bash
python3 vibe-docs/scripts/find_references.py projects/clinica BR-04
```

## `check_traceability.py <pasta>`

Monta o registro de IDs válidos a partir do `PROJECT.md` (`OBJ-`, `FUN-`, `UC-`, `BR-`, `ENT-`, `REQ-`, `PRINC-`) e aponta, com arquivo e linha, qualquer ID citado nos outros documentos que não esteja lá — sinal de invenção ou de drift. Identificadores próprios de documento (`US-`, `TASK-`, `API-`) não são cobrados do Blueprint, e marcadores do template (`- BR-01: PENDENTE`) não contam como ID definido.

## `check_staleness.py <pasta>`

Compara o `version` do Blueprint com o `version` declarado no frontmatter de cada derivado. Só funciona se a versão do Blueprint subir quando uma decisão muda ou entra — a skill faz isso; se você editar à mão, faça também (a regra está em [Conceitos](conceitos.md#versionamento-e-documentos-desatualizados)). `STATE.md` e `LEARNINGS.md` ficam fora da comparação.

## `check_coverage.py <pasta>`

Verifica conteúdo, não versão: toda `BR-xx` e `PRINC-xx` aparece onde é obrigatória, e toda funcionalidade do recorte do MVP consta no `MVP.md`. A comparação é pelo ID inteiro: citar `BR-100` não cobre a `BR-10`. Pega o documento gerado antes de uma regra existir — que o `check_staleness` não vê, porque a versão dele foi sincronizada depois.

## `project_status.py <pasta>`

Mostra quais dos 23 tipos já existem e extrai do Blueprint as seções de estado, pendências, sugestões futuras, aprofundamento por área, princípios, Definition of Done e fase atual. Não é um verificador: não falha.

## `handoff_check.py <pasta>`

Verificação pré-entrega. **Bloqueia** quando:

- falta um documento essencial: `CLAUDE.md`, `ARCHITECTURE.md`, `BACKLOG.md`, `TEST-STRATEGY.md`, `SETUP-RUNBOOK.md`, `STATE.md` ou `LEARNINGS.md`;
- há pendência crítica aberta na seção 16;
- o `MVP.md` existe, mas o recorte não voltou para a seção 4;
- a seção 22 não diz quais funcionalidades a fase inclui;
- as seções 20 ou 21 têm item PENDENTE;
- o `CLAUDE.md` não traz a rotina de fim de tarefa ou o protocolo de bug;
- o `CLAUDE.md` aponta para um arquivo que não existe.

**Avisa**, sem bloquear, quando falta um documento recomendado (Data Model, Business Rules, API Spec, Development Plan), quando o `CLAUDE.md` passa de 200 linhas ou começa com frontmatter, quando ele importa com `@` algo além de `STATE.md` e `LEARNINGS.md`, e quando um documento técnico existe mas sua área na seção 19 segue PENDENTE.

## `_common.py`

Não é executado diretamente. Concentra o que os seis scripts precisam fazer do mesmo jeito: o padrão de ID, a lista de tokens técnicos que parecem ID e não são (`SHA-256`, `UTF-8`…), a leitura de uma seção do Blueprint, a leitura das pendências críticas em qualquer formato de lista e a localização do `CLAUDE.md` nos dois layouts. Antes cada script tinha a sua cópia, e as cópias divergiam.

## "Revise tudo"

Quando você pede uma revisão completa, a skill roda `check_coverage`, `check_traceability`, `check_staleness` e `handoff_check`, e depois revisa à mão o que nenhum script alcança: seções 15 e 19 ainda marcando como pendente algo já resolvido, pendência resolvida cujo texto antigo ficou, e afirmação escrita como fato sem decisão por trás.
