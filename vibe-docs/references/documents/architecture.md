# Software Architecture / Technical Specification

## Propósito
Descrever como o sistema será construído a partir dos requisitos e do domínio já definidos — a primeira vez, no pipeline, que decisões de tecnologia entram em jogo.

## Insumos necessários do Blueprint
Funcionalidades, entidades, fluxos, requisitos técnicos iniciais já declarados (seção 13), riscos (seção 14, especialmente qualquer nota sobre dado sensível — isso normalmente vira requisito de arquitetura).

## Estrutura obrigatória

```markdown
# Arquitetura — [Nome do Projeto]

## Visão Arquitetural
[resumo de alto nível — estilo de arquitetura, principais componentes]

## Componentes e Responsabilidades
[cada componente/serviço e o que ele faz]

## Comunicação entre Componentes
[como os componentes conversam entre si]

## Fluxos de Dados
[como a informação se move pelo sistema nos fluxos principais — remeta aos fluxos do Blueprint]

## Persistência
[o que precisa ser armazenado e onde — nível conceitual; detalhe fica em `data-model.md`]

## Autenticação e Autorização
[como o sistema identifica quem é quem e aplica as permissões da seção 12 do Blueprint]

## Integrações Externas
[remeta a `integration-spec.md` se houver mais de uma integração relevante]

## Processamento Assíncrono / Eventos
[se aplicável — o que dispara o quê]

## Observabilidade
[o que precisa ser logado/monitorado, no nível que já for possível definir]

## Decisões Arquiteturais
[cada decisão relevante, com alternativas consideradas quando fizer sentido]

## Requisitos Não-Funcionais Relevantes
[remeta a `nfr.md` para o detalhamento completo]
```

## Regras específicas
- Não escolha tecnologia arbitrariamente. Quando uma tecnologia específica for necessária e o Blueprint não tiver essa decisão registrada, apresente 2-3 alternativas com trade-offs e marque como pendência de decisão — a menos que o Blueprint já tenha uma preferência declarada (seção 13), caso em que essa é a decisão a seguir.
- "Decisões Arquiteturais" deve registrar o porquê, não só o quê — isso é o que evita a mesma discussão se repetir quando o projeto crescer.
- Se o usuário pedir "especificação técnica" em vez de "arquitetura", use a mesma estrutura — são o mesmo documento neste processo, só com nomes diferentes pelo mesmo conteúdo.
