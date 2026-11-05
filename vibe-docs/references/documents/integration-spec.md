# Integration Specification — Especificação de Integrações

## Propósito
Detalhar cada integração com sistema externo (pagamento, autenticação de terceiros, e-mail, calendário, etc.) além do que a arquitetura já menciona em alto nível.

## Insumos necessários do Blueprint
Qualquer menção a integração externa nos requisitos técnicos (seção 13) ou nas funcionalidades — se nenhuma integração foi discutida no Concept, este documento não deve ser gerado ainda (não há o que detalhar sem inventar).

## Estrutura obrigatória (por integração)

```markdown
### Integração — [Nome do Serviço Externo]

**Finalidade:** [por que o sistema precisa dessa integração — remeta à FUN-xx ou UC-xx que a motiva]
**Direção:** [o sistema chama o serviço externo / o serviço externo chama o sistema / ambos]
**Autenticação com o serviço:** [tipo — API key, OAuth, etc., se já decidido; senão, pendência]
**Dados trocados:** [o que é enviado e o que é recebido]
**Tratamento de falha:** [o que o sistema faz se a integração estiver indisponível]
**Webhooks (se houver):** [eventos recebidos e como são processados]
```

## Regras específicas
- Se o serviço específico (ex.: qual gateway de pagamento) não foi decidido no Blueprint, descreva a integração pela finalidade funcional e registre o fornecedor como pendência — não escolha um fornecedor arbitrariamente.
- "Tratamento de falha" não é opcional mesmo que pareça um detalhe pequeno — é frequentemente a parte que falta quando alguém implementa a integração a partir deste documento.
