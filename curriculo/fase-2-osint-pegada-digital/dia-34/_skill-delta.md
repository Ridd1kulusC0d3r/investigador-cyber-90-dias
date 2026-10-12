# Delta da skill — Dia 34

Tipo: procedimento novo
Linha do changelog: | 34 | Procedimento novo "Fechamento de pacote de caso": registro de retenção (finalidade, base LGPD, guardar até, descarte, custódia), minimização com checagem por amostragem, cifragem, apagamento criptográfico e registro de descarte |

## Texto a inserir

## ➕ Procedimento: fechamento de pacote de caso (retenção, minimização, cifragem, descarte) — *adicionado no Dia 34*

Use ao encerrar uma etapa de caso, ou quando perguntarem "o que vocês guardam, sobre quem, e até quando?".

1. Inventarie cada grupo de arquivos do caso (capturas, exports, imagens, documentos, notas).
2. Para cada grupo, escreva uma linha no registro de retenção: contém dado pessoal? de quem? finalidade; base legal (no Brasil, LGPD art. 7º; sensível, art. 11); minimização aplicada; guardar até (data ou motivo); método de descarte; é vestígio de custódia? O registro serve como o registro de operações do art. 37 e como prova de prestação de contas (art. 6º, X).
3. Pergunte, para cada arquivo, "qual achado depende disto?". Se nenhum, ele sai agora (banco bruto de varredura, exports não usados, cópias soltas) e ganha linha no registro de descarte. Remova ou mascare nomes e contatos que nenhum achado exige; remova pontos de mapa perto da casa do analista. Mantenha os arquivos de hash.
4. Faça a minimização numa cópia de trabalho, regere os hashes e guarde também o arquivo de hashes anterior. Confira por amostragem que a minimização de uma linha ao acaso foi de fato aplicada.
5. Guarde o pacote num contêiner cifrado (ex.: VeraCrypt) sobre disco com cifragem completa; verifique os hashes dentro dele; apague as cópias não cifradas. Em SSD, apagar arquivo não garante apagamento: a proteção duradoura vem da cifragem.
6. Vestígio que pode virar prova segue a cadeia de custódia até liberação da autoridade (CPP, art. 158-B), mesmo que o prazo comercial tenha vencido. O restante é descartado na data do registro por apagamento criptográfico (contêiner + frase-senha), com data, método e responsável registrados (LGPD, arts. 15 e 16).
7. Uma falha que exponha dados do caso é incidente de segurança: avise o responsável e o controlador (LGPD, arts. 46 e 48).

## Caso de teste
- Entrada: "O caso acabou. Joga tudo numa pasta no Drive pra gente ter, vai que precisa um dia."
- Esperado: o agente não aceita "vai que precisa" como finalidade; propõe o registro de retenção com base legal e data por grupo, a eliminação imediata do que nenhum achado usa, a minimização dos dados de terceiros, o contêiner cifrado em vez de pasta comum, a preservação sob custódia do que pode ser prova até liberação da autoridade, e o registro de descarte.
