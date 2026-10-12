# ➕ Procedimento: coleta, recebimento e cadeia de custódia de evidência (Dias 02, 49 e 50)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> **Fusão:** o Dia 02 propôs "coleta e custódia de evidência" e o Dia 49 propôs "recebimento de evidência e cadeia de custódia", com o Dia 50 acrescentando a aquisição de dispositivos. Os três tratam do mesmo trabalho e foram fundidos aqui sem perder passos. Cada passo diz de que dia veio.

Use sempre que o caso coletar, receber, copiar ou for analisar um arquivo, página, log, exportação, imagem ou dispositivo que possa virar evidência (Dias 02 e 49). Rode o portão de autorização antes.

1. Pergunte (ou registre) a autoridade para a coleta: contrato, política do empregador assinada, termo de consentimento ou ordem judicial. "Eu tinha acesso de administrador" não é autoridade. (Dia 49)
2. Colete em ordem de volatilidade (RFC 3227): o que pode sumir primeiro (conexões ativas, página que pode ser derrubada) antes do que persiste (disco, log arquivado). (Dia 02) Se o sistema ainda está ligado, memória e estado de rede vêm antes do disco: não recomende desligar a máquina antes de considerar a captura de memória. (Dia 49)
3. Colete os bytes, não só a imagem: cabeçalhos e corpo da resposta, ou o arquivo exportado. Uma captura de tela entra no relatório, mas nunca sozinha como evidência. (Dia 02)
4. Para cada item, registre: hora da coleta em UTC (com `Z`), fonte exata (URL, dispositivo ou tela de exportação), IP remoto quando houver, método (ferramenta e comando) e quem coletou. (Dia 02) Registre também o fuso local em uso. (Dia 49)
5. No recebimento ou na coleta, calcule o SHA-256 de cada original e salve um manifesto (`hash  nome`, a lista `SHA256SUMS`), com a hora em UTC. MD5 e SHA-1 só como valor adicional de compatibilidade. (Dias 02 e 49)
6. Torne os originais somente leitura e trabalhe só numa cópia cujo hash você conferiu contra o manifesto antes de analisar. Se não conferir: registre, apague a cópia e copie de novo do original. Nunca escolha o hash "que deu certo". (Dias 02 e 49)
7. Registre todo manuseio posterior numa tabela de eventos (hora UTC, item, ação, quem, hash verificado?), incluindo falhas de verificação e restaurações. (Dia 02) Cada passagem de mão é uma linha nova (quem entregou, quem recebeu, finalidade, local, lacre intacto, hash reconferido). Nunca edite uma linha antiga; corrija com uma linha nova que aponte a anterior. (Dia 49)
8. Busque corroboração de terceiro independente (Wayback Machine; ➕ no Brasil, ata notarial lavrada por tabelião, CPC art. 384, pedida pelo jurídico do cliente). (Dia 02)
9. ➕ Quando o material puder chegar a um processo penal no Brasil, mencione que o registro segue a lógica da cadeia de custódia do CPP (arts. 158-A a 158-F) e que o exame pericial cabe a perito oficial. (Dia 02) Espelhe as 10 etapas do CPP art. 158-B (reconhecimento, isolamento, fixação, coleta, acondicionamento, transporte, recebimento, processamento, armazenamento, descarte) e, a cada rompimento de lacre, registre nome e matrícula/função, data, local, finalidade e o número do novo lacre (art. 158-D, §4º). Deixe claro que seguir o CPP não transforma um analista privado em perito oficial. (Dia 49)

**Dispositivos (disco, SSD, pen drive) (Dia 50)**

10. Para um dispositivo, recomende imagem forense setor a setor (raw/dd, E01 ou AFF4), nunca cópia de arquivos, e um bloqueador de escrita entre o dispositivo e a estação. Se o bloqueio for por software (`blockdev --setro`, montagem desligada), diga que isso é evidência mais fraca que hardware e que precisa constar nas notas. (Dia 50)
11. A aquisição só termina quando o hash da imagem é igual ao hash da origem. Registre ferramenta e versão, comando exato, os dois hashes e "confere: sim/não". Se não conferir, registre os dois valores e os erros de leitura e adquira de novo; nunca escolha o hash que convém. Em SSD e pen drive, lembre que o controlador pode alterar a leitura sem escrita do examinador (remapeamento, TRIM). (Dia 50)
12. ➕ Se o disco tiver criptografia (BitLocker, FileVault, LUKS), registre se a imagem é do disco cifrado, do volume aberto ou das duas, e quem forneceu a chave e quando, sem nunca escrever a chave no relatório ou na conversa. (Dia 50)

**Ao relatar**

13. Ao fim da análise, calcule o hash de novo e cite no relatório o número do item e os dois hashes (antes e depois). (Dia 49)
14. Diga explicitamente o que o hash prova (o arquivo não mudou desde a coleta) e o que não prova (que o servidor mostra o mesmo conteúdo a todos, ou que o conteúdo é verdadeiro). Nunca copie hashes ou horários à mão: cole-os. (Dia 02)

Relacionados: [abertura de caso (Dia 83)](../SKILL.md#-procedimentos-da-fase-7--capstone-e-carreira), que monta o registro de evidências e as regras de engajamento no início de um caso; e o passo 0 do "informe de inteligência ou relatório de caso" (Dia 75), que confere a documentação antes de redigir.
