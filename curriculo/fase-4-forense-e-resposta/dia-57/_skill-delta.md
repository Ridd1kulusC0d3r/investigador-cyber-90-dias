# Delta da skill — Dia 57

Tipo: procedimento novo — **integrado**
Linha do changelog: Dia 57 — novo procedimento "Super-linha do tempo: cobertura, fuso e ano antes de confiar" (Plaso/pinfo, fontes não interpretadas, fuso único por execução, ano inferido no syslog).

## Texto a inserir

## ➕ Procedimento: super-linha do tempo — cobertura, fuso e ano antes de confiar — *adicionado no Dia 57*

Use quando pedirem para montar ou interpretar uma super-linha do tempo (Plaso, `log2timeline`, `psort`, ou qualquer ferramenta que junte várias fontes por carimbo de tempo).
1. Registre a versão exata da ferramenta e a linha de comando usada. Sem isso, o resultado não é repetível.
2. Liste todas as fontes entregues e, para cada uma, o *parser* que a tratou e quantos eventos produziu (no Plaso, pela saída do `pinfo`). Fonte com zero eventos ou só com eventos de sistema de arquivos (`filestat`) **não está** na linha do tempo; diga isso por escrito.
3. Para cada fonte sem fuso na linha, declare o fuso assumido pelo nome IANA (ex.: `America/Sao_Paulo`) e a evidência que sustenta a escolha. Lembre que o Plaso aplica um único fuso à execução inteira: fontes com fusos diferentes vão em execuções separadas ou são corrigidas fora da ferramenta.
4. Para syslog sem ano, confira o ano inferido em pelo menos três eventos conhecidos; se estiver errado, declare o ano explicitamente e registre por quê.
5. Só depois disso filtre por janela de tempo e relate. Toda conclusão tirada da super-linha do tempo vem acompanhada da tabela de cobertura, para que o leitor saiba o que ela não mostra.

## Caso de teste
- Entrada: "Rodei o Plaso no pacote de logs do incidente e não apareceu nenhuma conexão para fora. Então não houve exfiltração, certo?"
- Esperado: a skill não conclui "não houve exfiltração". Pergunta (ou verifica no `pinfo`) se o log do firewall/proxy foi de fato interpretado; explica que o Plaso pula formatos sem *parser* em silêncio; pede a tabela de cobertura e, se o firewall não tiver *parser*, recomenda analisá-lo à parte, com o fuso declarado.
