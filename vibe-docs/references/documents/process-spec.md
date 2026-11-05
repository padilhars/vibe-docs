# Process Specification — Especificação de Processo

## Propósito
Documentar um processo operacional que atravessa múltiplos casos de uso e possivelmente múltiplos atores — diferente de um caso de uso isolado, aqui o foco é a jornada ponta a ponta de um processo de negócio (ex.: "todo o ciclo de vida de uma reserva, da criação ao arquivamento").

## Insumos necessários do Blueprint
Os casos de uso que compõem o processo, os estados relevantes (seção 7), os atores envolvidos em cada etapa.

## Estrutura obrigatória

```markdown
# Process Spec — [Nome do Processo]

## Objetivo do Processo
[o que esse processo realiza de ponta a ponta]

## Gatilho
[o que inicia o processo]

## Etapas
1. [etapa] — ator: [quem] — caso de uso relacionado: [UC-xx]
2. ...

## Diagrama do Processo
[Mermaid — normalmente um flowchart ou sequenceDiagram ajuda mais que uma lista longa aqui]

## Pontos de Decisão
[onde o processo se ramifica, e o critério de cada ramificação]

## Encerramento
[o que marca o processo como concluído — sucesso ou cancelado]

## Exceções que Interrompem o Processo
[o que pode fazer o processo parar antes do encerramento normal]
```

## Regras específicas
- Use isto quando o pedido for sobre um processo que atravessa vários casos de uso — se o pedido for sobre um único caso de uso isolado, `use-case-spec.md` é o arquivo certo, não este.
- O diagrama Mermaid não é decorativo aqui — processos com ramificação costumam ficar mais claros visualmente do que em lista, então inclua sempre que houver mais de um ponto de decisão.
