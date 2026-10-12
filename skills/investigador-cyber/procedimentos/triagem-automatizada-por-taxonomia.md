# ➕ Procedimento: triagem automatizada guiada por taxonomia (Dia 73)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.

Use quando o usuário pedir para montar, revisar ou avaliar um sistema que usa um modelo de linguagem para triar mensagens, denúncias ou anúncios em busca de golpe.
1. Coloque antes do modelo as checagens que o código faz de forma exata: autenticação de e-mail (`dmarc=fail`), texto do link diferente do destino, idade do domínio, telefone, conta, carteira ou chave Pix já presente no grafo de indicadores. Nunca peça ao modelo que adivinhe isso.
2. Peça ao modelo só a extração: quais mecanismos da taxonomia estão presentes, cada um com uma citação literal da mensagem. Ele não decide culpa.
3. Descarte todo mecanismo cuja citação não aparece literalmente no texto (normalizar espaços, aspas e Unicode é aceitável; aceitar paráfrase não é). Registre o descarte como possível evidência inventada.
4. Tire o veredito de uma regra: "phishing" só com pelo menos um mecanismo verificado; sem isso, "legítimo" ou "abstenção". Erro ou JSON inválido vira abstenção, nunca palpite.
5. Trate o texto da mensagem como dado não confiável: o prompt manda ignorar instruções internas, e o teste inclui pelo menos uma linha com instrução injetada e uma linha legítima com urgência inofensiva.
6. Rode em máquina local ou em infraestrutura aprovada para os dados. Nunca envie material de caso real a chatbot público.
7. Relate precisão, revocação (abstenção conta como erro), número de mensagens e resultado do teste de injeção, e diga quando a amostra é pequena demais para confiar.
8. Deixe com uma pessoa toda decisão com consequência (bloquear conta, acusar remetente, avisar vítima). Casos com possível menor ou tráfico vão para revisão humana treinada e para os canais da parada obrigatória, nunca para resposta automática.
9. ➕ No Brasil, lembre que o titular pode pedir revisão de decisão tomada unicamente por tratamento automatizado (LGPD, art. 20); o passo 8 é também conformidade.
