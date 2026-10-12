# ➕ Procedimento: leitura de sistema de arquivos e linha do tempo MACB (Dia 51)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> Procedimento proposto no Dia 51; os itens marcados com ➕ e "(Dia 52)" foram acrescentados no Dia 52.

Use quando o usuário tiver uma imagem de disco ou pen drive (já adquirida e com hash conferido) e quiser saber o que havia nela e quando.
1. Trabalhe só na cópia verificada. Se houver tabela de partições (`mmls`), use o setor inicial (`-o`) em todas as ferramentas seguintes.
2. Registre os identificadores do volume (`fsstat`): tipo, rótulo, ID do volume, tamanho de setor e de *cluster*.
3. Liste nomes vivos e apagados (`fls -r -p`; só apagados com `-d`). Para cada apagado de interesse, leia os metadados (`istat`) antes do conteúdo (`icat -r`), e calcule o SHA-256 do recuperado, anotando-o ao lado do *inode*. Diga que a recuperação é confiável para arquivo pequeno e contíguo, e não para fragmentado no FAT; no ext4, sugira *carving*.
4. Compare assinatura (*magic bytes*) com extensão. Extensão trocada entra como observação, nunca como prova de intenção.
5. Antes de montar a linha do tempo, pergunte em que fuso o dispositivo gravou os horários. FAT grava hora local sem fuso; NTFS e ext4 gravam UTC. Confirme o fuso com uma fonte independente (configuração da estação, ou um evento com hora UTC conhecida em outro log) e escreva, ao lado de cada horário, de onde veio o fuso.
6. ➕ No Brasil, use `America/Sao_Paulo` (ou o fuso do estado) e lembre que não há horário de verão desde 2019; imagens anteriores podem ter UTC-2 no verão.
7. Na linha do tempo, separe o que o sistema de arquivos mostra ("arquivo gravado às X") do que ele não mostra (quem gravou, o que o arquivo faz).
8. ➕ No NTFS, leia os dois conjuntos de horários de cada arquivo de interesse: `$STANDARD_INFORMATION` (0x10, o que o Explorer mostra e que qualquer programa altera com `SetFileTime`) e `$FILE_NAME` (0x30, atualizado pelo driver ao criar, renomear ou mover). Nunca forme hipótese só com o `$SI`. (Dia 52)
9. ➕ Trate suspeita de *timestomping* (ATT&CK T1070.006) como soma de sinais, nunca um só: `$SI` Criado anterior ao `$FN` Criado, horário `$SI` de segundo inteiro (`uSecZeros`), arquivo mais velho que a pasta-mãe, `LastRecordChange` logo após a criação, nome ou local de disfarce, e fontes externas (`$UsnJrnl` com `BasicInfoChange`, Prefetch). Para cada anomalia, escreva primeiro a explicação inocente (instalador, extrator de ZIP, cópia entre volumes) e diga se a manteve ou descartou, e por quê. Dê a confiança na escala confirmado / altamente provável / provável / possível. (Dia 52)
10. ➕ Um registro com `InUse=False` mostra que um arquivo com aquele nome existiu em tal pasta e hora. Descreva relações de tempo como "precedeu"; não escreva "continha" ou "entregou" sem evidência do conteúdo. (Dia 52)
