# Delta da skill — Dia 08

Tipo: procedimento novo — "Ler um certificado e montar a linha do tempo de emissão" — **integrado**
Linha do changelog: Procedimento **certificado e Certificate Transparency**: SNI, SAN/emissor/validade/OID/serial/impressão digital, CT deduplicado por serial, DV de AC gratuita não prova malícia nem legitimidade

## Texto a inserir

## ➕ Procedimento: ler um certificado e montar a linha do tempo de emissão — *adicionado no Dia 08*

Use quando o caso envolver um site com HTTPS, quando perguntarem se "o cadeado" prova algo, ou quando for preciso datar ou relacionar domínios.
1. Obtenha o certificado conectando-se com o SNI correto (`openssl s_client -servername ...`). Salve o PEM, calcule o hash do arquivo e registre a impressão digital SHA-256 do certificado (bytes DER), que é o identificador a citar.
2. Leia: lista SAN (nomes cobertos; nomes inesperados ligam domínios), emissor, `notBefore`/`notAfter` em UTC (e ➕ BRT), número de série e OID de política (`2.23.140.1.2.1` DV, `2.23.140.1.2.2` OV, `2.23.140.1.1` EV).
3. Nunca trate DV de AC gratuita como evidência de malícia nem de legitimidade: ele prova só controle do domínio. O cadeado significa conexão cifrada, não identidade.
4. Consulte o Certificate Transparency (ex.: crt.sh) pelo domínio e por variações (`%marca%`). Remova duplicatas pelo número de série (pré-certificado e final) e ordene por `not_before`.
5. Monte a linha do tempo e marque: cadência de renovação, nome visto pela primeira vez, troca de AC. Relacione `notBefore` com os eventos do caso (ex.: horas antes do primeiro disparo).
6. Compare o emissor com o CAA do domínio e lembre que o CAA de um domínio não protege domínios imitação, que têm DNS próprio.
7. Lembre que, em TLS 1.3, um sensor passivo vê o SNI, mas não o certificado.

## Caso de teste
- Entrada: *"O site do golpe tem cadeado e certificado válido. Então pelo menos é um site 'verificado', né?"*
- Esperado: explica que o certificado (provavelmente DV de AC gratuita) só prova controle do domínio e cifra a conexão; não identifica o operador nem atesta legitimidade; sugere ler SAN, emissor e notBefore e consultar o CT para datar o site e achar domínios relacionados.
