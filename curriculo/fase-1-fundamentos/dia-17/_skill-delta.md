# Delta da skill — Dia 17

Tipo: procedimento novo
Linha do changelog: | 17 | Procedimento **mapa de prontidão de evidência** (fonte e registro, retenção verificada, fora do host, custodiante; plano de até 5 ações, a primeira fecha o repúdio) | Prontidão de evidência |

## Texto a inserir

## ➕ Procedimento: mapa de prontidão de evidência — *adicionado no Dia 17*

Use depois de um modelo de ameaças, ou quando perguntarem "se X acontecer, a gente consegue provar?", ou no começo de um caso, para descobrir quais registros existem.
1. Para cada ameaça, responda quatro perguntas: (a) **fonte e registro**: qual sistema registraria e qual evento, campo ou padrão de linha mostraria a ameaça (nunca "os logs"); (b) **retenção**: por quanto tempo esse registro sobrevive; (c) **resistência a adulteração**: ele fica fora do host ou é só de acréscimo, ou o root do servidor pode apagá-lo; (d) **custodiante**: quem pode entregá-lo e em quanto tempo.
2. Só registre retenção a partir de algo verificado (arquivo de configuração lido, documentação com link). Caso contrário, escreva "não verificada" ou "desconhecida, perguntar a <custodiante>", e trate isso como achado.
3. Aponte os três padrões recorrentes: o servidor web registra a requisição mas não a identidade (falta auditoria na aplicação); os logs vivem na máquina que descrevem (falta envio para fora do host); terceiros guardam registros decisivos com retenção definida por contrato.
4. Quando a evidência de uma ameaça estiver fora do alcance do cliente (celular da vítima, operadora, provedor), diga isso e nomeie as fontes indiretas que o cliente controla.
5. Feche com um plano de no máximo cinco ações, ranqueadas pelo número de ameaças que cada uma torna investigáveis, cada uma com IDs de ameaça, registro criado, retenção com razão escrita (dentro dos limites de proteção de dados) e esforço em horas. A primeira ação fecha a lacuna de repúdio, se houver.

## Caso de teste
- Entrada: *"Nosso canal de denúncias vai ter nginx (14 dias) e mais nada. Se alguém exportar a planilha de denúncias e vazar, a gente descobre quem foi? Me dá um plano de logs completo, guarda tudo para sempre."*
- Esperado: responde que hoje não: o nginx mostra a requisição e o IP, não a conta; propõe log de auditoria da aplicação com campos (evento, protocolo, conta, IP, hora UTC), enviado para fora do servidor, como primeira ação; limita o plano a cinco ações; recusa "para sempre" e propõe uma retenção com razão escrita ligada à finalidade.
