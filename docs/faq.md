# FAQ

### A skill não disparou

Ela dispara pela intenção, não por comando. Apresente um problema e uma ideia de sistema, ou peça explicitamente: *"use a vibe-docs para iniciar um projeto"*. Confira em **Customize → Skills** se ela está ativada.

### Pedi um PRD e ela pediu o `PROJECT.md`

Comportamento esperado: documentos saem do Blueprint. Envie o arquivo ou, se quiser mesmo pular a descoberta, diga isso — ela faz um Concept expresso e avisa que várias seções sairão como PENDENTE.

### Por que tantas perguntas?

O Concept existe para encontrar as decisões que ninguém tomou. Para acelerar, reaja aos palpites em bloco ("tudo certo, exceto o 3") ou diga que o projeto é pequeno — a profundidade é proporcional.

### Ela sugeriu algo e eu não respondi. Virou requisito?

Não. Proposta não respondida vai para 🔵 Sugestões futuras no checkpoint. Só entra em 🟢 o que você afirmou ou aceitou.

### Funciona sem execução de código?

No Claude.ai, não: skills exigem a execução de código e criação de arquivos ligada. Se ela estiver desligada pela organização, fale com o administrador ([Guia do administrador](guia-do-admin.md)). No Claude Code ela sempre está disponível.

### Posso editar o `PROJECT.md` à mão?

Pode. Incremente o campo `version` ao fazer isso, para que o `check_staleness.py` saiba o que ficou para trás, e registre a decisão na seção 18.

### Os documentos saem em inglês

O idioma vem do campo `idioma_documentacao` do Blueprint. Se estiver vazio, a skill deveria perguntar antes da primeira geração; defina-o e peça para regenerar.

### Um script acusou ID inexistente

Ou o documento inventou um ID (corrija o documento), ou falta uma decisão no Blueprint (adicione-a lá e depois cite). Nunca crie o ID só no documento derivado.

### A skill avalia se vale a pena construir o sistema?

Não, por design. A decisão de construir é anterior à conversa. Restrições técnicas sérias encontradas na pesquisa viram risco na seção 14, não objeção ao projeto.
