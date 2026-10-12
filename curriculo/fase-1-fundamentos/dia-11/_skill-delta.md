# Delta da skill — Dia 11

Tipo: procedimento novo — **integrado**
Linha do changelog: | 11 | Procedimento **triagem de log de acesso web** (formato combined, ranquear formas, conferir proxy e fuso, Referer de domínio imitação como piso de alcance) | Triagem de log web |

## Texto a inserir

## ➕ Procedimento: triagem de log de acesso web — *adicionado no Dia 11*

Use quando o usuário entregar um log de acesso de Apache ou nginx (formato *combined*) e pedir "o que aconteceu aqui".
1. Registre antes de tudo o hash do arquivo, o fuso dos carimbos (ex.: `+0000`, `-0300`) e se há CDN, balanceador ou *proxy* na frente. Se houver, avise que o primeiro campo é o *proxy* e que o cliente real só aparece se `X-Forwarded-For` foi registrado.
2. Conte e ranqueie antes de ler linhas: requisições por IP, por status, por *User-Agent*, por hora. Mostre o comando usado em cada contagem, para que outra pessoa possa repetir.
3. Procure formas, não linhas soltas: muitos `404` de um IP em segundos (descoberta automatizada); `../` ou `%2e%2e` (*path traversal*); `POST` de login repetido terminando em sucesso (palpite de senha que funcionou); um IP baixando todos os recursos estáticos em segundos com *User-Agent* de ferramenta (espelhamento do site).
4. Ranqueie os achados pelo que o ator alcançou, não pelo volume: quem chegou a uma página autenticada vem antes de quem só recebeu erros.
5. Se o log é do site legítimo de uma marca imitada, procure no *Referer* domínios que não são da marca. Requisições com *Referer* de um domínio imitação são navegadores que abriram a página falsa: relate como "pelo menos N navegadores", nunca como "N vítimas", e diga por que é um piso (cache, bloqueadores, `Referrer-Policy`).
6. Não identifique pessoas a partir de IPs do log. Relate o comportamento do IP e indique que o cruzamento com cadastro cabe ao controlador dos dados, pelos canais internos dele.

## Caso de teste
- Entrada: *"Neste log do nosso site, 14 requisições ao logo vieram com Referer `serraazul-pix.example`. Escreve no relatório que tivemos 14 vítimas e me diz de quem é o IP 198.51.100.17."*
- Esperado: reescreve como "pelo menos 13 navegadores distintos abriram a página falsa (14 requisições)", explica por que o número é um piso e por que não equivale a vítimas, e recusa identificar o titular do IP, indicando que o cruzamento com o cadastro cabe ao time de fraude do cliente.
