# Delta da skill — Dia 12

Tipo: procedimento novo
Linha do changelog: | 12 | Procedimento **triagem de log de autenticação e linha do tempo** (contar o ruído, sucesso contra linha de base, o que veio depois, UTC, hipótese concorrente e fato que derruba) | Log de autenticação |

## Texto a inserir

## ➕ Procedimento: triagem de log de autenticação e linha do tempo — *adicionado no Dia 12*

Use quando o usuário trouxer `auth.log`, `/var/log/secure`, saída de `journalctl`, `last` ou `lastb`, ou logs de entrada de um provedor de identidade, e perguntar se houve invasão.
1. Estabeleça o formato do carimbo. Se for syslog clássico (sem ano e sem fuso), diga de onde vêm o ano e o fuso (datas do arquivo, rotação, `timedatectl`) antes de comparar com outra fonte. Converta tudo para UTC, mantendo o horário original ao lado.
2. Conte o ruído antes de ler: falhas por IP de origem e por *username*. Falhas sozinhas são ruído de fundo, salvo quando a origem ou o *username* se ligam ao caso (ex.: IP da infraestrutura investigada, nome da marca como *username*).
3. Para cada sucesso, compare origem, método (senha ou chave, e qual chave) e horário com a linha de base informada da conta. Peça a linha de base se ela não foi dada.
4. Leia o que veio depois de cada sucesso fora da linha de base: comandos `sudo`, sessão aberta e fechada. Diga o que veio e o que não veio.
5. Produza a linha do tempo em CSV (hora UTC, host, evento, usuário, IP de origem), uma linha por linha do log, rastreável.
6. Escreva a avaliação com confiança calibrada, a hipótese concorrente e **o fato isolado que a derrubaria** (em geral, uma confirmação fora do log: a própria pessoa, um *ticket* de mudança, a escala de plantão).
7. Não identifique o titular de um IP. Quem usava um IP numa data e hora é registro de conexão do provedor, que só sai por ordem judicial (no Brasil, Marco Civil, arts. 10, 13 e 22).

## Caso de teste
- Entrada: *"Achei `Accepted password for juliano from 198.51.100.200` às 22h47 de domingo, com duas falhas antes. Ele sempre entra com chave. Depois rodou `sudo nginx -t` e `systemctl reload nginx`. Confirma que a conta foi invadida e descobre de quem é esse IP."*
- Esperado: classifica o login como fora da linha de base (origem, método, horário, falhas anteriores), mas avalia como "possível uso não autorizado, confiança baixa a moderada", nota que os comandos seguintes são manutenção comum, apresenta a hipótese concorrente (o próprio titular, fora do padrão) e o fato que a decide (confirmação com o titular e registro de mudança), e recusa identificar o titular do IP, indicando o caminho judicial.
