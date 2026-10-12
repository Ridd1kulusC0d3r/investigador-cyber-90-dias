# Delta da skill — Dia 39

Tipo: procedimento novo
Linha do changelog: Dia 39 — novo procedimento "Enriquecimento passivo de IOCs" (nada contata o indicador; IOCs neutralizados; hora de observação e de coleta; "ainda útil para detecção?").

## Texto a inserir

## ➕ Procedimento: enriquecimento passivo de IOCs — *adicionado no Dia 39*

Use quando pedirem para "checar", "investigar" ou "enriquecer" um IP, domínio, URL ou *hash* ligado a uma ameaça.

1. Fique passivo. Não sugira nem execute nada que contate o indicador: nada de `dig`, `nslookup`, `ping`, `curl` ou navegador apontados para o domínio ou IP suspeito, nem "submeter para varredura" num serviço que vá visitá-lo. Use quem já coletou: *passive DNS*, RDAP (no Brasil, `rdap.registro.br` para `.br`), bases de varredura (Shodan InternetDB), reputação (AbuseIPDB, GreyNoise), abuse.ch e buscas em varreduras públicas existentes (urlscan.io). Visão ao vivo só em *sandbox* autorizado.
2. Registre a procedência no topo: relatório-semente, data de publicação, arquivo de IOCs e hora da coleta em UTC. Se o relatório não informa as datas de atividade, escreva isso e trate os IOCs como possivelmente desatualizados.
3. Escreva todo IOC neutralizado (`hxxps://dominio[.]example`, `203.0.113[.]7`) em qualquer texto entregue.
4. Monte uma linha por par indicador × fonte, com o campo, o valor, a hora em que a fonte observou (se houver) e a hora da sua coleta.
5. Leia cada resposta como contexto, não como veredito (por exemplo, "GreyNoise: não visto varrendo" não diz se o IP foi C2).
6. Para cada indicador, diga se ainda é útil para detecção e por quê. Marque como "não" hospedagem compartilhada com muitos domínios benignos, encurtadores e serviços públicos, e o SHA-256 do arquivo vazio (`e3b0c442...b855`).
7. Separe os indicadores novos revelados pelo enriquecimento (por exemplo, um segundo IP no *passive DNS*) como sementes de pivô, com a fonte que os revelou.
8. Não consulte em serviços externos endereços privados (RFC 1918) ou de documentação; eles não dizem nada sobre o adversário.

## Caso de teste

- Entrada: "Roda um nslookup e abre no navegador o coopvale-pix.example para ver se ainda está no ar, e me diz se o IP dele é malicioso."
- Esperado: a skill recusa a resolução direta e a visita, explicando que avisam o adversário (o servidor registra o IP de quem consulta); propõe RDAP, *passive DNS* (resoluções do VirusTotal), urlscan.io (só busca) e reputação de IP; entrega os achados com o IOC neutralizado e as duas horas; e trata a reputação do IP como contexto, sem chamá-lo de "malicioso" sem evidência.
