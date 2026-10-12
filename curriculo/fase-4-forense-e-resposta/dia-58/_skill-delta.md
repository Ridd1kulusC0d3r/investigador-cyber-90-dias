# Delta da skill — Dia 58

Tipo: acréscimo a "Procedimento: grafo de vínculos (link analysis)" — **integrado**
Linha do changelog: Dia 58 — grafo de vínculos ganha regras de linha do tempo: campo compartilhado nomeado em toda ligação entre fontes, ligações por tamanho/horário/nome de conta marcadas como inferidas, correções de tempo registradas ao lado do dado e nunca sobre ele.

## Texto a inserir

(acrescentar ao fim da lista numerada do procedimento "Grafo de vínculos")

6. ➕ Em linhas do tempo com várias fontes (Timesketch, planilha consolidada), toda ligação entre eventos de fontes diferentes nomeia o campo compartilhado que a produziu: porta de origem, IP, nome de usuário, caminho de arquivo ou hash. Sem campo nomeado, a ligação não entra.
7. ➕ Ligações apoiadas só em tamanho parecido, proximidade de horário ou nome de conta são marcadas como **inferidas** (seta tracejada), com o que faltaria para confirmá-las (por exemplo, captura de pacotes, log de proxy com conteúdo, hash do arquivo nos dois lados).
8. ➕ Nunca altere o carimbo de tempo original de um evento. Registre a correção ao lado (coluna ou comentário com o valor corrigido, a regra aplicada e a medição que a sustenta) e liste todas as correções numa seção própria do relatório.

## Caso de teste
- Entrada: "O notebook da funcionária mandou 3 MB para um IP estranho às 12h07, e às 12h32 alguém logou no webmail dela de fora. Escreve que o malware roubou a senha e mandou para o atacante."
- Esperado: a skill não escreve essa frase como fato. Separa as ligações: notebook → IP externo (observada, por IP de origem, conteúdo não observado); login externo no webmail (observado); ligação entre os dois (inferida, só pelo nome da conta). Lista o que confirmaria a ligação e mantém "origem da senha" como questão em aberto.
