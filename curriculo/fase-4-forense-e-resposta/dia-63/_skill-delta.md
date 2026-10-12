# Delta da skill — Dia 63

Tipo: procedimento novo
Linha do changelog: Dia 63 — novo procedimento "Correlação no SIEM: ingestão primeiro, entidade antes da hipótese" (conferência de ingestão, consulta por entidade, sequência com aperto contra falsos positivos, mapeamento de tipos).

## Texto a inserir

## ➕ Procedimento: correlação no SIEM — ingestão primeiro, entidade antes da hipótese — *adicionado no Dia 63*

Use quando pedirem para responder perguntas de um caso com consultas num SIEM (Elastic/Kibana, Splunk, Sentinel ou uma exportação NDJSON/CSV).
1. Confira a ingestão antes de analisar: total de documentos, fontes (*datasets*) e hosts esperados, intervalo de tempo coberto e se o tempo está em UTC. Relate qualquer fonte ou hora ausente como possível lacuna de ingestão, não como "nada aconteceu".
2. Confira se os campos usados estão preenchidos nas fontes que importam e com o tipo certo (IPs como tipo `ip` para consultas por CIDR; bytes como número).
3. Rode pelo menos uma consulta por **entidade**, sem filtro de hipótese: tudo da conta, tudo do IP, tudo do host. Leia o resultado inteiro antes de escrever a história.
4. Use a linguagem certa: filtro (KQL) para "quais eventos", agregação (ES|QL/SQL) para "quantos, quanto, por quê", sequência (EQL) para "A e depois B, pela mesma entidade, dentro de um tempo".
5. Em sequências, liste os resultados antes e depois de apertar a regra (por exemplo, exigir N falhas antes do sucesso) e nomeie as contas de falso positivo.
6. Relate cadeias entre hosts com o campo que as liga em cada salto; o salto que só compartilha o nome da conta é inferido.

## Caso de teste
- Entrada: "Rodei no SIEM 'falha seguida de sucesso em 30 minutos' e deu 3 contas. Então as três foram comprometidas?"
- Esperado: a skill não conclui comprometimento. Pede (ou faz) o detalhamento de cada sequência: número de falhas, origem (interna/externa), horário; aponta que um erro de digitação seguido de login normal casa com a regra ingênua; propõe apertar (ex.: 3+ falhas, origem externa) e mostra o resultado antes/depois.
