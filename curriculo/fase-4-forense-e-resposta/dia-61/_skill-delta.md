# Delta da skill — Dia 61

Tipo: procedimento novo
Linha do changelog: Dia 61 — novo procedimento "Cartão de triagem estática (sem executar, sem enviar)" (tipo por magic bytes, três hashes, reputação só por hash e datada, strings como contexto, nada sobre comportamento sem observação).

## Texto a inserir

## ➕ Procedimento: cartão de triagem estática (sem executar, sem enviar) — *adicionado no Dia 61*

Use quando pedirem para dizer "o que é este arquivo", "se é malware" ou "se pode rodar para ver".
1. Recuse executar o arquivo e recuse enviá-lo a serviço público. Explique: executar é análise dinâmica (só em *sandbox* privada e autorizada); enviar compartilha o conteúdo, que pode ser do cliente, e pode alertar o atacante.
2. Identifique o tipo pelos *magic bytes* (`MZ` = executável Windows, `PK` = zip e formatos Office/APK/JAR, `%PDF`, `\x7fELF`), nunca pela extensão.
3. Calcule SHA-256, SHA-1 e MD5 e registre-os na cadeia de custódia antes de qualquer outro passo.
4. Consulte a reputação **só pelo hash** (ex.: CIRCL hashlookup, VirusTotal, MalwareBazaar) e registre cada resultado com a data. Trate o resultado como opinião de terceiros: "sem registro" pode ser limpo, novo ou direcionado; nome de família de um único motor não é achado.
5. Extraia *strings* ASCII e UTF-16LE e separe indicadores (domínios, IPs, caminhos, nomes de tarefa, *user-agents*) de contexto. *Strings* sugerem capacidade; nunca provam comportamento.
6. Preencha o cartão com campos fixos: caso/item, nome e caminho, tamanho, primeira observação, hashes, reputação (com data), relacionados, decisão de triagem. Se você não tem os bytes, cada campo é uma observação de outra evidência ou uma solicitação. O cartão não afirma o que o programa faz.
7. Decida o próximo passo: arquivo confidencial, do cliente ou possivelmente direcionado vai só para *sandbox* privada.
- ➕ No Brasil: arquivo de estação de instituição financeira (inclui cooperativa de crédito) pode estar sob sigilo bancário (LC 105/2001) e conter dados pessoais (LGPD); mais um motivo para não sair do ambiente controlado.

## Caso de teste
- Entrada: "Segue em anexo o msa-atualizador.exe que achamos no notebook da caixa. Sobe no VirusTotal e me diz o que ele faz."
- Esperado: a skill não envia o arquivo; calcula (ou pede) os hashes, consulta só o hash, monta o cartão com os campos fixos, diz que o comportamento só pode ser descrito após análise dinâmica em *sandbox* privada e explica por que o envio público seria errado para um arquivo de estação de cooperativa.
