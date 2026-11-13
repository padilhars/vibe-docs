# Estado do Projeto (Maturidade)

## Por que não usar percentual

Um número como "78% completo" soa preciso, mas essa precisão não existe de verdade — não há uma unidade objetiva de "quanto falta" num projeto de software. O efeito prático de um percentual é passar confiança que a informação não sustenta, e não diz nada sobre **onde** focar a atenção. Um checklist qualitativo por categoria faz as duas coisas que importam: mostra o que já está sólido e aponta exatamente onde ainda falta trabalho.

## Formato

Para cada categoria abaixo, use um dos três status:

- ✅ **definido** — coberto o suficiente para gerar documentos derivados com confiança
- ⚠️ **parcial** — algo foi discutido, mas ainda tem lacuna relevante (diga qual)
- ❌ **não discutido** — a categoria nem entrou na conversa ainda

```
Atores                        ✅ definidos
Entidades principais          ✅ definidas
Fluxo principal               ✅ definido
Casos de borda                ⚠️ parcial (recorrência ok, cancelamento por terceiros pendente)
Permissões                    ✅ definidas
Regras de negócio             ✅ definidas
Integrações externas          ❌ não discutido
Requisitos não-funcionais     ❌ não discutido
Riscos / dados sensíveis      ⚠️ parcial (identificado, sem detalhamento)
Testes e qualidade            ❌ não discutido
```

Em projetos pequenos, é esperado que algumas categorias fiquem ❌ e isso não seja problema — ver a nota de proporcionalidade em `schema.md`. O checklist serve para mostrar onde falta atenção, não para exigir que tudo esteja ✅ antes de consolidar.

## Categorias padrão a checar

Atores, Entidades principais, Fluxo principal, Casos de borda, Permissões, Regras de negócio, Integrações externas, Requisitos não-funcionais, Riscos / dados sensíveis, Testes e qualidade. Adicione categorias específicas do domínio quando fizer sentido (ex.: "Regras de recorrência" num sistema de agendamento).

## Quando usar isso

- No checkpoint de revisão, antes de consolidar (`review-checklist.md`).
- Sempre que o usuário pedir explicitamente o estado do projeto ("como está o projeto até agora?", "o que falta?").
- Como parte do critério para você mesmo sugerir consolidação (ver `references/concept/methodology.md`): se a maioria das categorias-chave está ✅, é um bom sinal para propor fechar o Concept.
