# ➕ Procedimento: logs de autenticação e linha do tempo de acesso (Dias 12 e 55)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> **Fusão:** o Dia 12 propôs "triagem de log de autenticação e linha do tempo" (Linux/SSH) e o Dia 55 propôs "leitura de logs de autenticação" (Windows, webmail, VPN, nuvem). São o mesmo trabalho e foram fundidos sem perder passos. Cada passo diz de que dia veio.

Use quando o usuário trouxer `auth.log`, `/var/log/secure`, saída de `journalctl`, `last` ou `lastb`, logs de entrada de um provedor de identidade, logs de *login* do Windows Security, webmail, VPN ou nuvem, e perguntar se houve invasão, ou quem entrou, de onde, como e quando. (Dias 12 e 55)

1. Estabeleça o relógio de cada fonte antes de ler: fuso, e ano quando o formato não traz (syslog clássico). (Dia 55) Estabeleça o formato do carimbo. Se for syslog clássico (sem ano e sem fuso), diga de onde vêm o ano e o fuso (datas do arquivo, rotação, `timedatectl`) antes de comparar com outra fonte. Converta tudo para UTC, mantendo o horário original ao lado. (Dia 12)
2. Conheça os eventos. No Windows, use os eventos 4624, 4625 (com `Status`/`SubStatus`), 4634/4647, 4648, 4672, 4688, 4720/4732, 7045 e 1102, e o `LogonType` (2 interativo, 3 rede, 4 *batch*, 5 serviço, 7 desbloqueio, 10 RDP, 11 cache). Ligue eventos de um mesmo *logon* pelo `LogonId`. No Linux, `Failed password` (com e sem `invalid user`), `Accepted password|publickey` e `session opened/closed`. (Dia 55)
3. Conte o ruído antes de ler: falhas por IP de origem e por *username*. Falhas sozinhas são ruído de fundo, salvo quando a origem ou o *username* se ligam ao caso (ex.: IP da infraestrutura investigada, nome da marca como *username*). (Dia 12)
4. Desenhe a linha de base antes da exceção: um mapa dia × hora por conta ou host. Descreva o normal (horário, tipo, origem) em uma ou duas frases. (Dia 55)
5. Para cada sucesso, compare origem, método (senha ou chave, e qual chave) e horário com a linha de base informada da conta. Peça a linha de base se ela não foi dada. (Dia 12)
6. Classifique as tentativas por origem: muitas contas com poucas tentativas = *password spray*; uma conta com muitas tentativas = força bruta; poucas tentativas numa conta, de origem nova, logo depois de um *phishing* = compatível com credencial capturada (ATT&CK T1078). Dê a classificação como hipótese, com o que cada alternativa preveria. (Dia 55)
7. Um sucesso mostra que a conta entrou daquela origem; não mostra como a senha foi conhecida. Diga isso explicitamente. (Dia 55)
8. Leia o que veio depois de cada sucesso fora da linha de base: comandos `sudo`, sessão aberta e fechada. Diga o que veio e o que não veio. (Dia 12)
9. Falhas que aparecem antes do evento principal ou de origem inesperada viram "questão em aberto", registradas com as linhas exatas e sem explicação inventada. (Dia 55)
10. Produza a linha do tempo em CSV (hora UTC, host, evento, usuário, IP de origem), uma linha por linha do log, rastreável. (Dia 12)
11. Escreva a avaliação com confiança calibrada, a hipótese concorrente e **o fato isolado que a derrubaria** (em geral, uma confirmação fora do log: a própria pessoa, um *ticket* de mudança, a escala de plantão). (Dia 12)
12. ➕ Ao falar da pessoa dona da conta, teste a versão dela contra o log antes de descartá-la, e não a trate como suspeita por ter caído num *phishing*. (Dia 55)
13. Não identifique o titular de um IP. Quem usava um IP numa data e hora é registro de conexão do provedor, que só sai por ordem judicial (no Brasil, Marco Civil, arts. 10, 13 e 22). (Dia 12)

Relacionado: [tempo e linha do tempo multifonte](tempo-e-linha-do-tempo-multifonte.md), para juntar estes logs a outras fontes.
