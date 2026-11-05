# Security Specification — Especificação de Segurança

## Propósito
Consolidar as decisões de segurança relevantes ao projeto — autenticação, autorização, proteção de dado sensível — num documento que possa ser revisado isoladamente.

## Insumos necessários do Blueprint
Riscos e pontos de atenção (seção 14, especialmente qualquer nota sobre dado sensível), permissões (seção 12), atores.

## Estrutura obrigatória

```markdown
# Especificação de Segurança — [Nome do Projeto]

## Classificação de Dados
[quais entidades/campos envolvem dado sensível, pessoal ou financeiro, e por quê — deriva da seção 14 do Blueprint]

## Autenticação
[como usuários provam identidade]

## Autorização
[como a matriz de permissões da seção 12 do Blueprint é aplicada tecnicamente]

## Proteção de Dados
[criptografia em trânsito/repouso, mascaramento, retenção — no nível já decidido; o que não estiver decidido vira pendência]

## Superfícies de Risco Identificadas
[pontos do sistema onde um erro de segurança teria mais impacto, dado o que já se sabe do domínio]

## Conformidade
[qualquer requisito legal/regulatório já mencionado no Concept — ex.: tratamento de dado de saúde sob a LGPD. Não é uma opinião jurídica; é um registro do que já foi identificado como relevante e precisa de decisão]
```

## Regras específicas
- Este documento não substitui orientação jurídica — quando o domínio envolver dado sensível (saúde, financeiro, dado de menor de idade), registre isso como ponto de atenção que precisa de decisão informada, sem apresentar como certeza técnica algo que é, na verdade, uma decisão de compliance em aberto.
- Não gere este documento com uma lista genérica de boas práticas de segurança desconectada do projeto — cada item deve estar ancorado em algo específico do domínio ou do risco já identificado no Blueprint.
