# Delta da skill — Dia 36

Tipo: procedimento novo — **integrado**
Linha do changelog: Dia 36 — novo procedimento "Mapeamento de um relatório no ATT&CK" (tabela de evidências com citação literal; capacidade não é observação; parar no nível que o texto sustenta; comparação a + 2*b).

## Texto a inserir

## ➕ Procedimento: mapeamento de um relatório no ATT&CK — *adicionado no Dia 36*

Use quando pedirem para transformar um relatório, alerta, *post* de fornecedor ou relato de incidente em técnicas do ATT&CK. Aplique junto o procedimento "Consulta e conferência de IDs do ATT&CK".

1. Antes de escrever qualquer ID, monte uma tabela de evidências: número da linha, **citação literal** da frase, comportamento com suas palavras, tática, técnica/subtécnica, confiança no mapeamento.
2. Para cada frase, pergunte primeiro: ela diz que o ator **fez** algo nesta intrusão? Se descreve o que uma ferramenta *consegue* fazer, ou pelo que o grupo é "conhecido", **não mapeie**, e diga por quê.
3. Se a frase tiver mais de um comportamento (por exemplo, "usou PowerShell para rodar o ntdsutil", ou "entrou com a senha capturada e fez transferências"), divida em uma linha por comportamento.
4. A tática é o propósito do ator naquele momento; não a deduza da técnica.
5. Pare no nível que o texto sustenta: sem mecanismo nomeado, fique na técnica ou só na tática. Nunca invente uma subtécnica.
6. Ao entregar uma camada do Navigator, ponha em cada técnica um comentário apontando para a linha de evidência. Técnica sem comentário sai da camada.
7. Ao comparar com outro mapeamento (de outro analista ou a camada de grupo do MITRE), use `a + 2*b` (1 = só você, 2 = só o outro, 3 = os dois) e lembre que uma camada de grupo junta muitas fontes e campanhas; ela não é o mapeamento de um único relatório.

## Caso de teste

- Entrada: "Mapeia este trecho: 'O kit usado oferece módulo de captura de OTP por SMS. Os operadores mantiveram presença na infraestrutura durante a semana. Com as senhas capturadas, entraram no internet banking e fizeram Pix para terceiros.'"
- Esperado: a skill monta a tabela com a citação de cada frase; recusa mapear o "módulo de captura de OTP" por ser capacidade, não observação; mapeia "mantiveram presença" só até a tática Persistence, sem técnica; divide a última frase em dois comportamentos (T1078 Valid Accounts para a entrada com credenciais, T1657 Financial Theft para as transferências), com versão do ATT&CK registrada.
