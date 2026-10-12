# Delta da skill — Dia 03

Tipo: procedimento novo — "Leitura de uma conexão (quíntupla e flags TCP)"
Linha do changelog: Procedimento **leitura de uma conexão**: quíntupla, flags TCP, TTL como inferência e a regra das três hipóteses para "sem resposta"

## Texto a inserir

## ➕ Procedimento: leitura de uma conexão (quíntupla e flags TCP) — *adicionado no Dia 03*

Use quando o usuário trouxer uma captura de pacotes, uma linha de log de conexão ou a descrição de uma tentativa de conexão.
1. Confirme que a captura é de rede ou dispositivo que o usuário possui ou está autorizado a monitorar. Captura de tráfego de terceiros sem autorização é interceptação (➕ no Brasil, Lei 9.296/1996 e Marco Civil art. 7º, II): pare e explique.
2. Identifique a quíntupla: protocolo, IP e porta de origem, IP e porta de destino. Diga qual lado é o cliente (porta efêmera) e qual é o servidor (porta conhecida).
3. Leia as flags na ordem: SYN, SYN-ACK, ACK abre; FIN de cada lado fecha em ordem; RST fecha de forma abrupta. Diga quem fechou primeiro.
4. Classifique a tentativa: aperto de mão completo; SYN respondido com RST (host no ar, porta fechada); SYN sem resposta e retransmitido (filtrado, fora do ar, ou endereço inexistente: liste as três hipóteses, nunca só uma); muitos SYNs para portas ou hosts diferentes (varredura).
5. Use o TTL observado só como inferência do sistema de origem e do número de saltos (64 → Linux/macOS, 128 → Windows), e rotule-o como inferência.
6. Registre os horários em UTC e o SHA-256 do arquivo de captura.

## Caso de teste
- Entrada: *"No pcap tem 4 SYN pro 203.0.113.78 na porta 80 e nenhuma resposta. Então o golpista derrubou o servidor, certo?"*
- Esperado: explica que SYN sem resposta e retransmitido é compatível com filtro no caminho, host fora do ar ou endereço inexistente (e, em sites de golpe, filtragem por origem); não afirma derrubada; sugere observações que separam as hipóteses (repetir de outra origem, DNS histórico, outros logs) e registra o hash da captura.
