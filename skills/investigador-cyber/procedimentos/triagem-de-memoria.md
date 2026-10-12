# ➕ Procedimento: triagem de memória, árvore de processos (Dia 53)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> Procedimento proposto no Dia 53; os itens marcados com ➕ e "(Dia 54)" foram acrescentados no Dia 54.

Use quando o usuário trouxer saída do Volatility 3 (pslist, psscan, pstree, cmdline) ou pedir orientação para capturar memória.
1. Captura: memória antes do disco num sistema ligado; ferramenta de menor impacto (WinPmem, FTK Imager, AVML, LiME, *snapshot* de VM); gravar em mídia externa, nunca no disco suspeito; hash imediato; registrar ferramenta, versão, horário UTC, quem rodou. Se não houver imagem real, diga isso e não invente saída de plugin.
2. Compare a árvore com a forma normal do Windows: `System`→`smss.exe`; `wininit.exe`→`services.exe`/`lsass.exe`; `svchost.exe` só filho de `services.exe` e só em `System32`; programas do usuário sob `explorer.exe`. PIDs de pai inexistentes para `wininit`, `csrss`, `winlogon`, `explorer` são normais (pais de curta duração).
3. Para cada processo, avalie pai, caminho (`Path`), linha de comando (`Cmd`) e horário (`CreateTime`) separadamente. Pai normal não torna o processo normal. Cite a coluna e a linha do arquivo em cada desvio, e uma explicação legítima considerada. Use um processo legítimo parecido como controle.
4. Rode e cruze `pslist` e `psscan`: o que só o psscan vê saiu ou foi desligado da lista. Confirme com outra fonte (por exemplo, evento 4688) antes de concluir.
5. Argumentos codificados (`-EncodedCommand`, Base64 de UTF-16LE): decodifique como texto, numa VM isolada, e trate o resultado como evidência a documentar. Nunca execute.
6. ➕ Redija o que a memória mostra ("iniciado na sessão do usuário X às HH:MM UTC"), não um juízo sobre a pessoa ("o funcionário executou o malware"). O usuário de uma máquina comprometida por engenharia social costuma ser vítima.
7. ➕ Uma linha do `windows.netscan` prova só que "este PID manteve este *endpoint* em algum momento antes da captura". Não prova que a conexão estava aberta na captura (linhas `CLOSED`), que o dono atual do PID a fez (PIDs são reutilizados), nem o que foi enviado. `SYN_SENT` é tentativa não concluída: nunca escreva "conectado a". Um IP remoto compartilhado entre hosts é "mesmo IP remoto", não "mesmo atacante". (Dia 54)
8. ➕ Para cada acerto do `windows.malware.malfind` (antigo `windows.malfind`): se começa com `MZ`, provável PE escrito em memória, verifique `dlllist` e extraia com `--dump` para hash e *strings* numa VM isolada; se o processo faz JIT (.NET, PowerShell, navegadores) e os bytes parecem *thunks* repetidos ou zeros, registre como provavelmente benigno e diga por quê. Escreva um veredito e uma frase de raciocínio por região. (Dia 54)
9. ➕ Um único intervalo regular entre conexões é uma pergunta, não um padrão. Só descreva *beacon* quando uma série independente (proxy, firewall, captura de rede) mostrar a regularidade, e cite cada fonte separadamente. Volume transferido sem conteúdo observado é "N bytes saíram para X", nunca "dados vazados". (Dia 54)
