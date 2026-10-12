# Delta da skill — Dia 54

Tipo: acréscimo a "Triagem de memória: árvore de processos" (procedimento proposto no Dia 53) — **integrado**
Linha do changelog: | 54 | Memória e rede: o que uma linha do netscan prova, veredito do malfind com JIT como explicação inocente, intervalo × padrão. |

## Texto a inserir

Acrescentar ao fim do procedimento, como itens 7 a 9:

7. Uma linha do `windows.netscan` prova só que "este PID manteve este *endpoint* em algum momento antes da captura". Não prova que a conexão estava aberta na captura (linhas `CLOSED`), que o dono atual do PID a fez (PIDs são reutilizados), nem o que foi enviado. `SYN_SENT` é tentativa não concluída: nunca escreva "conectado a". Um IP remoto compartilhado entre hosts é "mesmo IP remoto", não "mesmo atacante".
8. Para cada acerto do `windows.malware.malfind` (antigo `windows.malfind`): se começa com `MZ`, provável PE escrito em memória, verifique `dlllist` e extraia com `--dump` para hash e *strings* numa VM isolada; se o processo faz JIT (.NET, PowerShell, navegadores) e os bytes parecem *thunks* repetidos ou zeros, registre como provavelmente benigno e diga por quê. Escreva um veredito e uma frase de raciocínio por região.
9. Um único intervalo regular entre conexões é uma pergunta, não um padrão. Só descreva *beacon* quando uma série independente (proxy, firewall, captura de rede) mostrar a regularidade, e cite cada fonte separadamente. Volume transferido sem conteúdo observado é "N bytes saíram para X", nunca "dados vazados".

## Caso de teste
- Entrada: "O netscan mostra o processo suspeito com uma conexão CLOSED e outra ESTABLISHED para o mesmo IP, 5 minutos de diferença, e o proxy mostra 3 MB enviados para ele. Posso escrever 'beacon confirmado e exfiltração de dados de clientes'?"
- Esperado: a skill separa as afirmações: o netscan mostra que o PID manteve os dois *endpoints*; dois pontos não fazem padrão, mas a série do proxy, se longa e regular, sustenta "conexões a intervalos de ~300 s"; os 3 MB são volume com conteúdo não observado; propõe redação sem "confirmado" e sem "dados de clientes", e lembra que a decisão de comunicar incidente (LGPD art. 48) é do controlador.
