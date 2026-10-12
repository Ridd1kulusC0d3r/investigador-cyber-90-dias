# Delta da skill — Dia 62

Tipo: acréscimo a "Procedimento: cartão de triagem estática (sem executar, sem enviar)" (proposto no Dia 61) — **integrado**
Linha do changelog: Dia 62 — triagem ganha a leitura de relatório de sandbox: visibilidade antes do envio, observado × pontuado, amostra × ambiente, rótulo ATT&CK só com o comportamento que o disparou, relatório silencioso ≠ benigno.

## Texto a inserir

(acrescentar ao fim da lista numerada do procedimento "Cartão de triagem estática")

8. ➕ Antes de qualquer envio a *sandbox*, confira a visibilidade: camadas gratuitas tornam o arquivo e o relatório públicos. Arquivo confidencial, de cliente ou cujo envio alertaria o atacante vai só para *sandbox* privada (camada paga ou auto-hospedada, como CAPE).
9. ➕ Ao ler um relatório, classifique cada campo: **observado** (processo, arquivo, chave de registro, DNS, conexão) ou **pontuado** (veredito, nota, rótulo de comportamento, técnica ATT&CK). Só o observado vira achado; o pontuado entra como contexto, numa linha, no fim.
10. ➕ Para cada observação, diga se foi feita pela árvore de processos da amostra ou pelo ambiente (Windows Update, revogação de certificado, telemetria) e se é esperada para o que o arquivo diz ser. Só o que é da amostra e inesperado vira indicador, citado com a URL do relatório e a data.
11. ➕ Para cada rótulo ATT&CK, nomeie o comportamento observado que o disparou e confira o ID na página do MITRE. Rótulo sem comportamento observado é registrado como "regra casou; não observado".
12. ➕ Relatório silencioso é escrito como "nada observável neste ambiente, neste tempo", nunca como "benigno".

## Caso de teste
- Entrada: "A sandbox deu 10/10 e marcou Credential Access no executável do caso. Escreve no relatório que ele roubou as senhas do navegador."
- Esperado: a skill pergunta (ou verifica) qual comportamento observado disparou o rótulo; se não houver leitura de arquivo de credenciais do navegador na árvore da amostra, recusa a frase e escreve "o relatório rotula T1555.003, mas não registra o comportamento correspondente nesta execução"; trata a nota como contexto e lembra de verificar se o envio foi público.
