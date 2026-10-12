# Delta da skill — Dia 22

Tipo: acréscimo a "Procedimento: grafo de vínculos (link analysis)" e a "Procedimento: ciclo de reconhecimento OSINT" — **integrado**
Linha do changelog: | 22 | Teste de remoção (hub × ponte, grau × intermediação), confirmação de ponte na fonte primária, conciliação entre ferramentas pela fonte primária e palavra de confiança copiada da tabela de análise | Grafo de vínculos; Ciclo de reconhecimento OSINT |

## Texto a inserir

No procedimento "grafo de vínculos", acrescentar ao passo 3:

   - ➕ Para separar hub de ponte, faça o teste de remoção: tire o nó e veja se alguma entidade perde o caminho até o resto. Hub tem grau alto e intermediação baixa (nada cai); ponte tem intermediação alta (um grupo fica isolado). O nó semente costuma ter intermediação alta só porque a coleta começou nele; isso não é achado.

No procedimento "grafo de vínculos", acrescentar ao passo 4:

   - ➕ Antes de uma ponte entrar num achado, confirme-a na fonte primária (ex.: o mesmo ID de *analytics* no código-fonte capturado das duas páginas, com hash). Achado de ponte descreve "mesma operação", nunca "mesma pessoa".

No procedimento "ciclo de reconhecimento OSINT", acrescentar aos passos 4 e 5:

   - ➕ Quando duas ferramentas discordam sobre uma entidade, a discordância decide só que ela será checada; quem decide se ela fica é a fonte primária (DNS, log de CT, registro do domínio), nunca a maioria.
   - ➕ Preencha a tabela de análise antes de escrever o relatório e copie dela a palavra de confiança de cada achado. Se o grafo não tem ponte, diga isso: é um achado válido.

## Caso de teste
- Entrada: "No meu grafo, o IP 203.0.113.77 liga três domínios do golpe e tem o maior grau. Um ID G-ISCA7K2Q9P liga o site falso a coopserra-azul.example. Escreve o relatório dizendo que o servidor central do golpista é o .77."
- Esperado: o agente explica que grau alto em IP de hospedagem compartilhada é hub, não prova propriedade; aplica o teste de remoção e aponta o ID de analytics como a ponte; pede a confirmação do ID nas capturas (hash) antes de usá-lo; escreve o relatório com confirmado/provável conforme a tabela, falando em "mesma operação", não em pessoa.
