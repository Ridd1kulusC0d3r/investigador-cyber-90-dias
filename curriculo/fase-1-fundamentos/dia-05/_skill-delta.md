# Delta da skill — Dia 05

Tipo: procedimento novo — "Seguir uma cadeia de resolução DNS"
Linha do changelog: Procedimento **cadeia de resolução DNS**: proveniência (resolvedor + hora), CNAME até o A, TTL e respostas divergentes, onde ficam os logs, arquivo hosts

## Texto a inserir

## ➕ Procedimento: seguir uma cadeia de resolução DNS — *adicionado no Dia 05*

Use quando um caso começar por um nome (link de golpe, domínio em log, host em configuração de malware) ou quando duas fontes derem IPs diferentes para o mesmo nome.
1. Para cada consulta, registre a proveniência: resolvedor usado (`SERVER`) e hora em UTC (`WHEN`). Sem isso, a resposta não é evidência.
2. Leia `status` (NOERROR existe; NXDOMAIN não existe *para esse resolvedor*; SERVFAIL o resolvedor não obteve resposta) e as flags (`aa` = autoritativa; sem `aa` = cache ou recursivo).
3. Siga cada CNAME até o registro A ou AAAA final, anotando o TTL de cada salto. Se o fim for CDN ou nuvem compartilhada, diga que o IP sozinho não identifica o operador.
4. Trate respostas diferentes como hipóteses legítimas antes de chamá-las de erro: cache com TTL diferente, resolvedor com política de bloqueio (➕ RPZ em redes corporativas), resposta geográfica, ou mudança de registro.
5. Aponte onde existem logs: o resolvedor recursivo registra qual cliente perguntou e quando, mesmo que a conexão tenha sido bloqueada. ➕ No Brasil, logs do resolvedor do cliente são dele e saem por contrato; dados de navegação guardados por provedor de terceiros só por ordem judicial (Marco Civil).
6. Se a vítima relatar que digitou o endereço correto e caiu no site falso, considere arquivo hosts adulterado ou DNS do roteador alterado (pharming): nenhum log de rede mostraria isso. Registre o relato como dado, sem desacreditar a vítima.

## Caso de teste
- Entrada: *"De dentro da empresa o domínio do golpe dá NXDOMAIN, mas de casa resolve para 203.0.113.77. Qual dos dois está mentindo?"*
- Esperado: explica que os dois podem estar corretos (bloqueio por política no resolvedor interno, como RPZ, versus resolução pública); pede SERVER e WHEN das duas consultas; sugere conferir a zona na seção AUTHORITY e o log do resolvedor interno; não conclui que o domínio saiu do ar.
