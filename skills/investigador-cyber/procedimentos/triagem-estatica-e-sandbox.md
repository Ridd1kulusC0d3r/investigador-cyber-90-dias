# ➕ Procedimento: cartão de triagem estática (sem executar, sem enviar) (Dia 61)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> Procedimento proposto no Dia 61; os itens marcados com ➕ e "(Dia 62)" foram acrescentados no Dia 62.

Use quando pedirem para dizer "o que é este arquivo", "se é malware" ou "se pode rodar para ver".
1. Recuse executar o arquivo e recuse enviá-lo a serviço público. Explique: executar é análise dinâmica (só em *sandbox* privada e autorizada); enviar compartilha o conteúdo, que pode ser do cliente, e pode alertar o atacante.
2. Identifique o tipo pelos *magic bytes* (`MZ` = executável Windows, `PK` = zip e formatos Office/APK/JAR, `%PDF`, `\x7fELF`), nunca pela extensão.
3. Calcule SHA-256, SHA-1 e MD5 e registre-os na cadeia de custódia antes de qualquer outro passo.
4. Consulte a reputação **só pelo hash** (ex.: CIRCL hashlookup, VirusTotal, MalwareBazaar) e registre cada resultado com a data. Trate o resultado como opinião de terceiros: "sem registro" pode ser limpo, novo ou direcionado; nome de família de um único motor não é achado.
5. Extraia *strings* ASCII e UTF-16LE e separe indicadores (domínios, IPs, caminhos, nomes de tarefa, *user-agents*) de contexto. *Strings* sugerem capacidade; nunca provam comportamento.
6. Preencha o cartão com campos fixos: caso/item, nome e caminho, tamanho, primeira observação, hashes, reputação (com data), relacionados, decisão de triagem. Se você não tem os bytes, cada campo é uma observação de outra evidência ou uma solicitação. O cartão não afirma o que o programa faz.
7. Decida o próximo passo: arquivo confidencial, do cliente ou possivelmente direcionado vai só para *sandbox* privada.
- ➕ No Brasil: arquivo de estação de instituição financeira (inclui cooperativa de crédito) pode estar sob sigilo bancário (LC 105/2001) e conter dados pessoais (LGPD); mais um motivo para não sair do ambiente controlado.
8. ➕ Antes de qualquer envio a *sandbox*, confira a visibilidade: camadas gratuitas tornam o arquivo e o relatório públicos. Arquivo confidencial, de cliente ou cujo envio alertaria o atacante vai só para *sandbox* privada (camada paga ou auto-hospedada, como CAPE). (Dia 62)
9. ➕ Ao ler um relatório, classifique cada campo: **observado** (processo, arquivo, chave de registro, DNS, conexão) ou **pontuado** (veredito, nota, rótulo de comportamento, técnica ATT&CK). Só o observado vira achado; o pontuado entra como contexto, numa linha, no fim. (Dia 62)
10. ➕ Para cada observação, diga se foi feita pela árvore de processos da amostra ou pelo ambiente (Windows Update, revogação de certificado, telemetria) e se é esperada para o que o arquivo diz ser. Só o que é da amostra e inesperado vira indicador, citado com a URL do relatório e a data. (Dia 62)
11. ➕ Para cada rótulo ATT&CK, nomeie o comportamento observado que o disparou e confira o ID na página do MITRE. Rótulo sem comportamento observado é registrado como "regra casou; não observado". (Dia 62)
12. ➕ Relatório silencioso é escrito como "nada observável neste ambiente, neste tempo", nunca como "benigno". (Dia 62)
