# Scripts

Seis verificadores em `vibe-docs/scripts/`. Python 3.8+, só biblioteca padrão. A skill os roda sozinha nos momentos certos; você também pode rodá-los à mão.

Todos recebem a pasta do projeto (onde estão o `PROJECT.md` e os documentos derivados):

```bash
python3 vibe-docs/scripts/<script>.py <pasta-do-projeto> [argumentos]
```

Os verificadores saem com **0** quando está tudo certo e **1** quando encontram problema — dá para usá-los num CI do seu repositório de documentação.

| Script | Pergunta que responde | Quando a skill roda |
|---|---|---|
| `find_references.py` | Onde este ID é citado? | Antes de qualquer alteração de decisão |
| `check_traceability.py` | Algum documento cita ID que não existe no Blueprint? | Depois de gerar ou editar um documento |
| `check_staleness.py` | Quais documentos saíram de uma versão antiga do Blueprint? | Depois de alterar uma decisão |
| `check_coverage.py` | Alguma decisão nunca chegou aos documentos onde é obrigatória? | Ao terminar um documento agregador |
| `project_status.py` | Como está o projeto? | Pedidos de status |
| `handoff_check.py` | Dá para entregar ao Claude Code? | Antes da implementação |

## `find_references.py <pasta> <ID>`

Lista arquivo e linha de cada ocorrência do ID. É a base da análise de impacto: a skill monta o plano de propagação a partir daqui, não da memória da conversa.

```bash
python3 vibe-docs/scripts/find_references.py projects/clinica BR-04
```

## `check_traceability.py <pasta>`

Monta o registro de IDs válidos a partir do `PROJECT.md` (`BR-`, `UC-`, `ENT-`, `FUN-`, `OBJ-`, `REQ-`, `API-`…) e aponta, com arquivo e linha, qualquer ID citado nos outros documentos que não esteja lá — sinal de invenção ou de drift.

## `check_staleness.py <pasta>`

Compara o `version` do Blueprint com o `version` declarado no frontmatter de cada derivado. Só funciona se a versão do Blueprint for incrementada a cada alteração — a skill faz isso; se você editar à mão, faça também.

## `check_coverage.py <pasta>`

Verifica conteúdo, não versão: toda `BR-xx` e `PRINC-xx` aparece onde é obrigatória, e toda funcionalidade do recorte do MVP consta no `MVP.md`. Pega o documento gerado antes de uma regra existir — que o `check_staleness` não vê, porque a versão dele foi sincronizada depois.

## `project_status.py <pasta>`

Mostra quais dos 21 tipos já existem e extrai do Blueprint as seções de estado, pendências, sugestões futuras, aprofundamento por área, princípios e Definition of Done. Não é um verificador: não falha.

## `handoff_check.py <pasta>`

Verificação pré-entrega: documentos essenciais presentes, nenhuma pendência crítica, seções 20 e 21 preenchidas e todos os `@imports` do `CLAUDE.md` apontando para arquivos que existem.

## "Revise tudo"

Quando você pede uma revisão completa, a skill roda `check_coverage`, `check_traceability`, `check_staleness` e `handoff_check`, e depois revisa à mão o que nenhum script alcança: seções 15 e 19 ainda marcando como pendente algo já resolvido, pendência resolvida cujo texto antigo ficou, e afirmação escrita como fato sem decisão por trás.
