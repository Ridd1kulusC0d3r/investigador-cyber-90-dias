# Delta da skill — Dia 84

Tipo: acréscimo a "Grafo de vínculos (link analysis)"
Linha do changelog: Grafo de vínculos ganha a **nota de pivô de quatro partes**, a regra de **dois tipos de pivô independentes** para pontes e a lista **"Considerado e rejeitado"**

## Texto a inserir

Acrescentar ao fim do procedimento "Grafo de vínculos (link analysis)":

6. ➕ Antes de desenhar qualquer aresta que venha de um pivô, escreva a nota de pivô em quatro partes: (a) o valor compartilhado; (b) o tipo de pivô (IP, registro, certificado, recurso de página, favicon, texto, encurtador...); (c) a explicação inocente checada (hospedagem compartilhada, registrador ou DNS gratuito grande, modelo público, encurtador público, clone que copiou a vítima, mesmo /24 de donos diferentes); (d) o veredito: achado, pista (um só tipo de pivô) ou rejeitado.
7. ➕ Pivôs rejeitados não viram arestas: vão numa lista "Considerado e rejeitado", com o motivo. Uma ponte entre dois clusters só é achado com pelo menos dois **tipos** de pivô independentes; dois valores tirados do mesmo arquivo (por exemplo, o script e um comentário dentro dele) contam como um tipo só.
8. ➕ Nunca ligue IPs por prefixo de rede. Use o dono (ASN) e o tipo de rede; localização de servidor de datacenter não diz onde está o operador.

## Caso de teste
- Entrada: *"O site falso e uma loja de doces usam o mesmo encurtador lnk.example. Põe a loja no grafo do golpista."*
- Esperado: a skill escreve a nota de pivô, identifica o encurtador público como explicação inocente, classifica como rejeitado e coloca em "Considerado e rejeitado", sem criar a aresta.
