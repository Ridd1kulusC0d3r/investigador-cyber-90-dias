# Delta da skill — Dia 59

Tipo: procedimento novo
Linha do changelog: Dia 59 — novo procedimento "Análise de fluxo e beacon sem pacotes" (grau da evidência de rede, intervalos com dispersão, outliers, limite do que fluxo prova).

## Texto a inserir

## ➕ Procedimento: análise de fluxo e *beacon* sem pacotes — *adicionado no Dia 59*

Use quando pedirem para interpretar logs de firewall, proxy, NetFlow ou capturas de rede, em especial para dizer se um host "está falando com um C2" ou "mandou dados para fora".
1. Diga primeiro qual é o grau da evidência: captura completa de pacotes (conteúdo disponível) ou só fluxo/firewall/proxy (quem, quando, portas, bytes). Com só fluxo, nenhuma afirmação sobre conteúdo é possível.
2. Converta todos os horários para UTC antes de calcular qualquer intervalo, declarando o fuso de origem.
3. Para suspeita de *beacon*, liste os intervalos entre conexões ao mesmo destino e relate quantidade, média, mediana, mínimo, máximo e desvio-padrão (ou coeficiente de variação). Nunca relate só a média.
4. Separe os *outliers* (conexões fora do ritmo, por exemplo uma de volume muito maior) e descreva cada um à parte, com horário e bytes.
5. Relate a regularidade como achado de comportamento ("conexões a cada ~300 s, CV 0,02"), não como veredito. Lembre que atualizadores e sincronizadores legítimos também são regulares; o caráter malicioso exige outra evidência (processo responsável, executável, destino).
6. Para volume de saída, escreva "N bytes saíram de A para B às HH:MM:SSZ"; a ligação com um arquivo específico é inferida (tamanho e sequência) e o que a confirmaria é nomeado (pcap, proxy com inspeção, hash nos dois lados).

## Caso de teste
- Entrada: "Tenho o log do firewall: o notebook conectou em 198.51.100.140 umas 30 vezes de manhã e uma vez mandou 3 MB. Me confirma que é malware exfiltrando a planilha de cooperados."
- Esperado: a skill calcula (ou pede para calcular) os intervalos com dispersão, separa a conexão de 3 MB como *outlier*, descreve a regularidade como comportamento, diz que o firewall não mostra conteúdo e que a ligação com "a planilha de cooperados" não pode ser afirmada; lista o que confirmaria (processo dono da conexão, captura, artefato no disco).
