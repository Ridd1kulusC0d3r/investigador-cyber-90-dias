# ➕ Procedimento: investigação de abuso em aplicação com LLM (Dia 81)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.

Use quando pedirem para analisar logs de um chatbot, assistente ou agente com LLM em busca de prompt injection ou uso indevido. Somente investigação e defesa: não gere cargas de injeção novas, não proponha testes contra sistemas de terceiros e não "melhore" uma tentativa encontrada no log.
1. Confirme os campos do log: entrada bruta, contexto buscado, chamadas de ferramenta (nome, argumentos, status, resultado), saída, ID da requisição, usuário/sessão, se estava autenticado, e IP. Diga quais faltam; sem `tool_calls`, não dá para saber o que o modelo fez.
2. Procure tentativas diretas na entrada e indiretas no contexto buscado (comentários HTML, marcadores como "SYSTEM:" ou "assistant:"). Cite a string exata como evidência.
3. Para cada tentativa, decida o que o modelo fez pelas chamadas de ferramenta, não pela saída: recusou; obedeceu e foi barrado (diga por qual controle); ou obedeceu e executou. Uma saída educada não exclui uma chamada de ferramenta feita.
4. Na injeção indireta, o usuário da linha de log é a vítima. Ache o autor no sistema que armazenou o conteúdo (ticket, página, e-mail): usuário, hora e IP do envio.
5. Busque também por efeito, porque engenharia social dirigida ao modelo ("sou atendente", "pré-aprovado") não casa com nenhuma regex de injeção: por sessão, conte as chamadas de ferramenta, os argumentos que pertencem a terceiros e se a sessão estava autenticada.
6. Mantenha separadas as tentativas que só compartilham a técnica (outro usuário, outro IP, outro alvo). Não as junte ao suspeito do caso.
7. Ligue a outros logs só por evidência (mesmo IP, mesmo usuário de portal) e escreva a ligação como tal, nunca como identidade de pessoa.
8. Liste o que a busca não vê (base64, Unicode invisível, instrução em vários turnos) e os controles que teriam barrado sem depender de detectar o texto (ferramenta restrita aos dados do próprio usuário autenticado, papel declarado na conversa não muda permissões, confirmação humana antes de gerar link para dado de cliente).
9. ➕ Se a ferramenta devolveu dado de terceiros (inclusive "consta/não consta" ligado a CPF), registre quantos titulares, quais dados e quando, porque isso alimenta a avaliação de comunicação de incidente (LGPD, art. 48). Não tipifique crime; preserve o log com cadeia de custódia.

Para a autoria do texto que carregou a carga, use o procedimento "Verificação de texto gerado por máquina" e rotule qualquer conclusão sobre como o ator escreveu o texto como inferência.
