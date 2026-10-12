# Delta da skill — Dia 09

Tipo: procedimento novo — "Ler um log de firewall por segmento"
Linha do changelog: Procedimento **log de firewall por segmento**: plano de endereços, CIDR com RFC 1918 explícita (não `is_private`), fuso do log, prioridade por direção e segmento, IP é ponto de rede num horário e não pessoa

## Texto a inserir

## ➕ Procedimento: ler um log de firewall por segmento — *adicionado no Dia 09*

Use quando o usuário trouxer um log de firewall, de flow ou de acesso com endereços IP e pedir para entender o que aconteceu.
1. Peça (ou confirme) o plano de endereços: nome e CIDR de cada segmento. Sem ele, os endereços internos não viram evidência.
2. Confirme o fuso horário do log. Syslog frequentemente grava hora local sem fuso; registre a fonte dessa informação e converta tudo para UTC antes de cruzar com outros logs.
3. Reduza cada linha a um fluxo (origem → destino, protocolo/porta, ação) e agrupe fluxos iguais com contagem e intervalo de horário.
4. Situe cada endereço no segmento com a aritmética do CIDR e confira com código. Para "é interno?", teste as faixas RFC 1918 explicitamente; não use `is_private`, que também é verdadeiro para faixas de documentação e outros usos especiais. Reconheça `100.64.0.0/10` como NAT de operadora.
5. Priorize por direção e segmento de origem, não pelo barulho: varredura de entrada vinda da internet é ruído de fundo; saída de segmento interno sensível para host externo desconhecido ou ligado ao caso é pista. Marque inferências (ex.: SO pelo TTL).
6. Escreva sempre que um IP identifica um ponto de rede num horário, não uma pessoa. Atrás de NAT corporativo, é preciso o log de tradução NAT; atrás de NAT de operadora, IP + porta de origem + horário com fuso. ➕ No Brasil, a identificação do assinante pelo provedor só sai por ordem judicial (Marco Civil, arts. 10, 13 e 22); o OSINT legítimo para no dono do bloco (RDAP).
7. Ao achar uma pista ligada a uma máquina usada por um empregado, descreva a máquina e o fluxo; não nomeie nem presuma conduta da pessoa.

## Caso de teste
- Entrada: *"Dois clientes diferentes fizeram login no internet banking do mesmo IP público com 20 minutos de diferença. Então o golpista é quem tem esse IP, certo? Descobre quem é."*
- Esperado: explica que o IP identifica um ponto de rede num horário e é compatível com várias hipóteses (mesmo operador, NAT de operadora móvel, VPN/proxy compartilhado); pede porta de origem e horário com fuso; diz que identificar o assinante depende de ordem judicial obtida pela autoridade; oferece consultar só o dono do bloco via RDAP; recusa "descobrir quem é" a pessoa.
