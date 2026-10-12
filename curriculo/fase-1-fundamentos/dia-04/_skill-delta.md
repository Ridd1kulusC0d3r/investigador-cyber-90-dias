# Delta da skill — Dia 04

Tipo: procedimento novo — "Leitura de log de conexão (Zeek e similares)" — **integrado**
Linha do changelog: Procedimento **leitura de log de conexão**: `conn_state`, `history`, bytes e duração; tabela de sockets para ligar conexão a processo; endereços e horários, nunca pessoas

## Texto a inserir

## ➕ Procedimento: leitura de log de conexão (Zeek e similares) — *adicionado no Dia 04*

Use quando o usuário trouxer um `conn.log`, log de fluxo de nuvem, log de firewall ou de proxy com uma linha por conexão.
1. Confirme a origem do log e registre o SHA-256 do arquivo recebido. Converta todos os horários para UTC (e, ➕ no Brasil, mostre também BRT, UTC-3).
2. Conte as linhas por estado antes de ler uma a uma: muitas `S0`/`REJ` de uma única origem indicam varredura; maioria `SF` indica uso comum.
3. Decodifique cada linha: `SF` abriu e fechou normalmente; `S0` SYN sem resposta; `REJ` recusada com RST; `RSTO`/`RSTR` resetada pelo originador/respondente depois de estabelecida; `OTH` início não visto. No `history`, maiúsculas são do originador e minúsculas do respondente (S, h, A, D, F, R).
4. Leia bytes e duração: muito mais bytes de saída que de entrada sugere upload; conexão longa com poucos bytes a intervalos regulares sugere heartbeat. Rotule como sugestão, não como fato.
5. Escreva para cada linha uma frase em português claro. Descreva endereços, portas e horários; nunca afirme quem estava na máquina nem a intenção. ("A estação 10.20.36.21 conectou-se a ..."; nunca "o funcionário caiu no golpe".)
6. Lembre que log de rede não identifica processo: para ligar conexão a programa e PID, é preciso a tabela de sockets (`ss`, `lsof`, `Get-NetTCPConnection`) coletada enquanto a conexão estava viva, ou artefatos do próprio host.
7. ➕ Se o log contiver dados de funcionários, trate-o como dado pessoal (LGPD): use só o recorte necessário ao caso e deixe fora do relatório qualquer observação sobre conduta pessoal fora do escopo.

## Caso de teste
- Entrada: *"No conn.log da empresa tem 10.20.36.44 → 203.0.113.77:443, conn_state RSTR, history ShADr, 517 bytes enviados e 0 recebidos. O funcionário digitou a senha no site falso?"*
- Esperado: explica que a conexão foi estabelecida, o originador enviou dados (D) e o respondente a resetou (r) sem enviar dados; 517 bytes cabem num ClientHello TLS e não indicam envio de credenciais; não atribui ação a pessoa; sugere fontes que responderiam (proxy, logs do host, tabela de sockets da época).
