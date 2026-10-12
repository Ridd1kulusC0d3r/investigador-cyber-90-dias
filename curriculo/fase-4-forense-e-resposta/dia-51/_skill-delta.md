# Delta da skill — Dia 51

Tipo: procedimento novo — **integrado**
Linha do changelog: | 51 | Procedimento novo "Leitura de sistema de arquivos e linha do tempo MACB": camadas do TSK, apagado com ressalva, assinatura × extensão, fuso declarado por horário. |

## Texto a inserir

## ➕ Procedimento: leitura de sistema de arquivos e linha do tempo MACB — *adicionado no Dia 51*

Use quando o usuário tiver uma imagem de disco ou pen drive (já adquirida e com hash conferido) e quiser saber o que havia nela e quando.
1. Trabalhe só na cópia verificada. Se houver tabela de partições (`mmls`), use o setor inicial (`-o`) em todas as ferramentas seguintes.
2. Registre os identificadores do volume (`fsstat`): tipo, rótulo, ID do volume, tamanho de setor e de *cluster*.
3. Liste nomes vivos e apagados (`fls -r -p`; só apagados com `-d`). Para cada apagado de interesse, leia os metadados (`istat`) antes do conteúdo (`icat -r`), e calcule o SHA-256 do recuperado, anotando-o ao lado do *inode*. Diga que a recuperação é confiável para arquivo pequeno e contíguo, e não para fragmentado no FAT; no ext4, sugira *carving*.
4. Compare assinatura (*magic bytes*) com extensão. Extensão trocada entra como observação, nunca como prova de intenção.
5. Antes de montar a linha do tempo, pergunte em que fuso o dispositivo gravou os horários. FAT grava hora local sem fuso; NTFS e ext4 gravam UTC. Confirme o fuso com uma fonte independente (configuração da estação, ou um evento com hora UTC conhecida em outro log) e escreva, ao lado de cada horário, de onde veio o fuso.
6. ➕ No Brasil, use `America/Sao_Paulo` (ou o fuso do estado) e lembre que não há horário de verão desde 2019; imagens anteriores podem ter UTC-2 no verão.
7. Na linha do tempo, separe o que o sistema de arquivos mostra ("arquivo gravado às X") do que ele não mostra (quem gravou, o que o arquivo faz).

## Caso de teste
- Entrada: "O fls mostra que o arquivo malware.zip foi criado no pen drive às 08:35. Posso escrever no relatório que o funcionário copiou o malware às 08:35?"
- Esperado: a skill pergunta o sistema de arquivos e o fuso; se for FAT, avisa que 08:35 é hora local sem fuso e pede confirmação por fonte independente; reescreve o achado como "um arquivo chamado malware.zip foi gravado no pen drive às 08:35 (hora local, fuso X confirmado por Y)" e explica que o FAT não mostra quem copiou nem o conteúdo do arquivo.
