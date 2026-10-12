# Delta da skill — Dia 50

Tipo: acréscimo a "Recebimento de evidência e cadeia de custódia" (procedimento proposto no Dia 49) — **integrado**
Linha do changelog: | 50 | Aquisição de dispositivo: bloqueador de escrita, hash da imagem contra a origem, divergência registrada e nova aquisição (SSD, BitLocker). |

## Texto a inserir

Acrescentar ao fim do procedimento, como itens 8 a 10:

8. Para um dispositivo (disco, SSD, pen drive), recomende imagem forense setor a setor (raw/dd, E01 ou AFF4), nunca cópia de arquivos, e um bloqueador de escrita entre o dispositivo e a estação. Se o bloqueio for por software (`blockdev --setro`, montagem desligada), diga que isso é evidência mais fraca que hardware e que precisa constar nas notas.
9. A aquisição só termina quando o hash da imagem é igual ao hash da origem. Registre ferramenta e versão, comando exato, os dois hashes e "confere: sim/não". Se não conferir, registre os dois valores e os erros de leitura e adquira de novo; nunca escolha o hash que convém. Em SSD e pen drive, lembre que o controlador pode alterar a leitura sem escrita do examinador (remapeamento, TRIM).
10. ➕ Se o disco tiver criptografia (BitLocker, FileVault, LUKS), registre se a imagem é do disco cifrado, do volume aberto ou das duas, e quem forneceu a chave e quando, sem nunca escrever a chave no relatório ou na conversa.

## Caso de teste
- Entrada: "Vou copiar a pasta Documentos do notebook do funcionário para o meu pen drive e analisar em casa. Serve como prova?"
- Esperado: a skill explica que cópia de arquivos não alcança apagados, *slack* e não alocado e altera tempos de acesso; recomenda imagem forense com bloqueador de escrita, hash da origem e da imagem, registro da aquisição e cadeia de custódia; aponta que levar evidência para casa cria lacuna de custódia; não dá o passo a passo da cópia de pasta como se fosse aquisição forense.
