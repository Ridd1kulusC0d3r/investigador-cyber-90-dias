# Delta da skill — Dia 55

Tipo: procedimento novo
Linha do changelog: | 55 | Procedimento novo "Leitura de logs de autenticação": eventos e tipos de logon, linha de base antes da exceção, spray × força bruta × conta válida. |

## Texto a inserir

## ➕ Procedimento: leitura de logs de autenticação — *adicionado no Dia 55*

Use quando o usuário trouxer logs de *login* (Windows Security, `auth.log`/`secure`/*journal*, webmail, VPN, nuvem) e perguntar quem entrou, de onde, como e quando.
1. Estabeleça o relógio de cada fonte antes de ler: fuso, e ano quando o formato não traz (syslog clássico).
2. No Windows, use os eventos 4624, 4625 (com `Status`/`SubStatus`), 4634/4647, 4648, 4672, 4688, 4720/4732, 7045 e 1102, e o `LogonType` (2 interativo, 3 rede, 4 *batch*, 5 serviço, 7 desbloqueio, 10 RDP, 11 cache). Ligue eventos de um mesmo *logon* pelo `LogonId`. No Linux, `Failed password` (com e sem `invalid user`), `Accepted password|publickey` e `session opened/closed`.
3. Desenhe a linha de base antes da exceção: um mapa dia × hora por conta ou host. Descreva o normal (horário, tipo, origem) em uma ou duas frases.
4. Classifique as tentativas por origem: muitas contas com poucas tentativas = *password spray*; uma conta com muitas tentativas = força bruta; poucas tentativas numa conta, de origem nova, logo depois de um *phishing* = compatível com credencial capturada (ATT&CK T1078). Dê a classificação como hipótese, com o que cada alternativa preveria.
5. Um sucesso mostra que a conta entrou daquela origem; não mostra como a senha foi conhecida. Diga isso explicitamente.
6. Falhas que aparecem antes do evento principal ou de origem inesperada viram "questão em aberto", registradas com as linhas exatas e sem explicação inventada.
7. ➕ Ao falar da pessoa dona da conta, teste a versão dela contra o log antes de descartá-la, e não a trate como suspeita por ter caído num *phishing*.

## Caso de teste
- Entrada: "No log do webmail, a conta da funcionária teve 3 falhas e 1 sucesso de um IP externo às 9h30, e ela diz que não acessou. Foi força bruta? Ela está mentindo?"
- Esperado: a skill compara com a linha de base da conta, explica que 4 tentativas numa conta não têm a forma de força bruta nem de *spray*, aponta como mais compatível o uso de credencial já conhecida (por exemplo, capturada por *phishing* anterior), diz que o log não mostra como a senha foi obtida, nota que a origem externa é coerente com a versão da funcionária e evita tratá-la como suspeita.
