# Delta da skill — Dia 56

Tipo: procedimento novo
Linha do changelog: | 56 | Procedimento novo "Normalização de tempo e correlação entre fontes": três perguntas por fonte, correção medida por pares, evidence_ref, arestas rotuladas e inferidas. |

## Texto a inserir

## ➕ Procedimento: normalização de tempo e correlação entre fontes — *adicionado no Dia 56*

Use antes de juntar logs de mais de uma fonte numa linha do tempo, e sempre que uma linha do tempo mostrar algo impossível (efeito antes da causa).
1. Para cada fonte, responda: em que fuso grava? imprime o fuso? o relógio estava certo? Se não imprime ano (syslog clássico), registre de onde veio o ano.
2. Não confie em nota de configuração sozinha. Meça o deslocamento com pares de eventos que duas fontes registraram: mesma porta de origem (*firewall* × `sshd`), mesmo IP de origem e destino no mesmo segundo (*firewall* × proxy), mesmo IP de cliente (*firewall* × aplicação). Use pelo menos dois pares e confirme com a tabela de fusos (`zoneinfo`/`zdump`) para a data, considerando horário de verão. ➕ Brasil: `America/Sao_Paulo` é UTC-3 o ano todo desde 2019; antes, havia UTC-2 no verão.
3. Desconte o tempo do *handshake* e trate o resto como desvio de relógio. Se aplicar a mesma correção a outra fonte do mesmo host sem medir nela, escreva isso como suposição.
4. Junte tudo em UTC com uma coluna `evidence_ref` (arquivo:linha) por linha.
5. Ao desenhar a cadeia, só ligue eventos por um campo compartilhado que não coincidiria por acaso (porta de origem, ID de sessão, usuário + IP, caminho de arquivo, nome + tamanho). Rotule cada aresta com esse campo. Ligações por proximidade no tempo ou por tamanho aproximado vão tracejadas, com o motivo de serem inferidas.
6. Releia a linha do tempo procurando impossibilidades; cada uma é, primeiro, um relógio a reconferir. Mantenha abertas as questões que os logs não respondem.

## Caso de teste
- Entrada: "Juntei o firewall, o proxy e o webmail e ordenei. O login do atacante no webmail aparece às 09:32, antes do clique no link às 11:19. Então a senha não veio do phishing?"
- Esperado: a skill pergunta o fuso de cada fonte, sugere medir o deslocamento por pares de eventos (por exemplo, o mesmo IP de cliente no firewall e no webmail), mostra que uma diferença de exatamente 3 h indica firewall em horário de Brasília sem fuso, refaz a ordem em UTC e só então avalia a relação com o *phishing*, rotulando essa ligação como inferida se nenhum campo a sustentar.
