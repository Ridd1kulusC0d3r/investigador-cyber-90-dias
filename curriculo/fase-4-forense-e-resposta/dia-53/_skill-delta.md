# Delta da skill — Dia 53

Tipo: procedimento novo
Linha do changelog: | 53 | Procedimento novo "Triagem de memória: árvore de processos": árvore normal do Windows, pslist × psscan, decodificar sem executar, redação sem culpar o usuário. |

## Texto a inserir

## ➕ Procedimento: triagem de memória, árvore de processos — *adicionado no Dia 53*

Use quando o usuário trouxer saída do Volatility 3 (pslist, psscan, pstree, cmdline) ou pedir orientação para capturar memória.
1. Captura: memória antes do disco num sistema ligado; ferramenta de menor impacto (WinPmem, FTK Imager, AVML, LiME, *snapshot* de VM); gravar em mídia externa, nunca no disco suspeito; hash imediato; registrar ferramenta, versão, horário UTC, quem rodou. Se não houver imagem real, diga isso e não invente saída de plugin.
2. Compare a árvore com a forma normal do Windows: `System`→`smss.exe`; `wininit.exe`→`services.exe`/`lsass.exe`; `svchost.exe` só filho de `services.exe` e só em `System32`; programas do usuário sob `explorer.exe`. PIDs de pai inexistentes para `wininit`, `csrss`, `winlogon`, `explorer` são normais (pais de curta duração).
3. Para cada processo, avalie pai, caminho (`Path`), linha de comando (`Cmd`) e horário (`CreateTime`) separadamente. Pai normal não torna o processo normal. Cite a coluna e a linha do arquivo em cada desvio, e uma explicação legítima considerada. Use um processo legítimo parecido como controle.
4. Rode e cruze `pslist` e `psscan`: o que só o psscan vê saiu ou foi desligado da lista. Confirme com outra fonte (por exemplo, evento 4688) antes de concluir.
5. Argumentos codificados (`-EncodedCommand`, Base64 de UTF-16LE): decodifique como texto, numa VM isolada, e trate o resultado como evidência a documentar. Nunca execute.
6. ➕ Redija o que a memória mostra ("iniciado na sessão do usuário X às HH:MM UTC"), não um juízo sobre a pessoa ("o funcionário executou o malware"). O usuário de uma máquina comprometida por engenharia social costuma ser vítima.

## Caso de teste
- Entrada: "O pstree mostra que o atualizador.exe é filho do explorer.exe. Então é normal, certo? E posso dizer no relatório que a funcionária executou o vírus?"
- Esperado: a skill explica que pai `explorer.exe` é normal para programas do usuário, mas pede caminho, linha de comando, horário e um controle legítimo; sugere cruzar com psscan e com outras fontes; e reescreve a frase do relatório como "o processo foi iniciado na sessão do usuário X às HH:MM UTC", sem atribuir culpa.
