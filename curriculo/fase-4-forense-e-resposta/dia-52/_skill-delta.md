# Delta da skill — Dia 52

Tipo: acréscimo a "Leitura de sistema de arquivos e linha do tempo MACB" (procedimento proposto no Dia 51)
Linha do changelog: | 52 | NTFS: comparar $SI e $FN, pesar sinais de timestomp com explicações inocentes, "precedeu" em vez de "continha". |

## Texto a inserir

Acrescentar ao fim do procedimento, como itens 8 a 10:

8. No NTFS, leia os dois conjuntos de horários de cada arquivo de interesse: `$STANDARD_INFORMATION` (0x10, o que o Explorer mostra e que qualquer programa altera com `SetFileTime`) e `$FILE_NAME` (0x30, atualizado pelo driver ao criar, renomear ou mover). Nunca forme hipótese só com o `$SI`.
9. Trate suspeita de *timestomping* (ATT&CK T1070.006) como soma de sinais, nunca um só: `$SI` Criado anterior ao `$FN` Criado, horário `$SI` de segundo inteiro (`uSecZeros`), arquivo mais velho que a pasta-mãe, `LastRecordChange` logo após a criação, nome ou local de disfarce, e fontes externas (`$UsnJrnl` com `BasicInfoChange`, Prefetch). Para cada anomalia, escreva primeiro a explicação inocente (instalador, extrator de ZIP, cópia entre volumes) e diga se a manteve ou descartou, e por quê. Dê a confiança na escala confirmado / altamente provável / provável / possível.
10. Um registro com `InUse=False` mostra que um arquivo com aquele nome existiu em tal pasta e hora. Descreva relações de tempo como "precedeu"; não escreva "continha" ou "entregou" sem evidência do conteúdo.

## Caso de teste
- Entrada: "A MFT mostra que o arquivo atualizador.exe tem SI<FN True. Posso escrever que houve timestomping e que o ZIP baixado antes entregou o executável?"
- Esperado: a skill pede os outros sinais (uSecZeros, pasta-mãe, LastRecordChange, fontes fora da MFT), lembra que extratores de ZIP produzem o mesmo padrão, propõe uma confiança calibrada (não "confirmado" só com a MFT) e reescreve a relação com o ZIP como "o ZIP existiu X segundos antes; o registro não mostra que ele continha o executável".
