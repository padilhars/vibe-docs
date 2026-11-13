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

Pode. Se você alterou ou acrescentou uma decisão, incremente o campo `version`, para que o `check_staleness.py` saiba o que ficou para trás, e registre a decisão na seção 18. Preencher algo que estava PENDENTE não sobe a versão.

### Os documentos saem em inglês

O idioma vem do campo `idioma_documentacao` do Blueprint. Se estiver vazio, a skill deveria perguntar antes da primeira geração; defina-o e peça para regenerar.

### Um script acusou ID inexistente

Ou o documento inventou um ID (corrija o documento), ou falta uma decisão no Blueprint (adicione-a lá e depois cite). Nunca crie o ID só no documento derivado.

### O que é a simulação que aparece antes do Blueprint?

Uma verificação que narra o sistema em uso nos primeiros dias, procurando onde ele quebra. Ela acontece depois do checkpoint e antes de o `PROJECT.md` ser gravado, porque é o momento em que corrigir é mais barato. Você também pode pedi-la depois: *"que problemas podem aparecer no uso diário?"*.

### Gerei um documento e os outros apareceram como desatualizados

Não deveria acontecer só por gerar. A versão do Blueprint sobe quando uma decisão muda ou entra, não quando algo pendente é preenchido. Se subiu, houve decisão nova: peça *"que documentos estão desatualizados?"* e atualize os listados.

### Meu `CLAUDE.md` foi gerado numa versão anterior da skill

Peça para regenerá-lo. O formato anterior à v3.2 importava vários documentos com `@`, o que no Claude Code carrega todos eles inteiros em toda sessão, e não trazia a rotina de fim de tarefa, o protocolo de bug nem o `LEARNINGS.md`.

### A skill instala outras skills no meu projeto?

Não. Ela pesquisa e recomenda, num documento com origem, licença e o que cada uma acessa. Instalar é decisão sua.

### O Claude Code já tem memória. Para que o `LEARNINGS.md`?

A memória automática fica na máquina de quem rodou a sessão. O `LEARNINGS.md` fica no repositório: é versionado, pode ser revisado e vale para qualquer pessoa ou máquina que continue o projeto.

### A skill avalia se vale a pena construir o sistema?

Não, por design. A decisão de construir é anterior à conversa. Restrições técnicas sérias encontradas na pesquisa viram risco na seção 14, não objeção ao projeto.
