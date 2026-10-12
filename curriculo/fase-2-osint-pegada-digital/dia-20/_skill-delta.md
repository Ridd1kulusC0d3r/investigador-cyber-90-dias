# Delta da skill — Dia 20

Tipo: acréscimo a "Procedimento: ciclo de reconhecimento OSINT" — **integrado**
Linha do changelog: | 20 | Coleta automatizada só no modo passivo, com checagem do log; passada de falsos positivos com contagem e motivo, sendo o ruído definido pela pergunta | Ciclo de reconhecimento OSINT |

## Texto a inserir

No passo 2 (Coletar), acrescentar como subitem:

   - ➕ Se usar coleta automatizada (SpiderFoot ou similar), use só o modo passivo, que consulta terceiros. Módulos que falam direto com o servidor do alvo (varredura de portas, *spider*, força bruta de subdomínios) estão fora do escopo de reconhecimento. Depois da execução, confira no log se algum módulo fez requisição direta ao alvo; se fez, registre módulo e horário e não use como achado nenhum dado que tenha vindo dessa requisição sem confirmá-lo por uma fonte limpa.

No passo 3 (Processar), acrescentar como subitens:

   - ➕ Antes de montar o grafo, faça uma passada de falsos positivos e registre uma tabela com o nó ou grupo removido, a quantidade e o motivo. Contagens de "sites co-hospedados" na casa das centenas quase sempre indicam CDN ou hospedagem compartilhada, não propriedade.
   - ➕ O ruído é definido pela pergunta, não pela ferramenta. Escreva a pergunta no topo da tabela e justifique cada remoção em relação a ela. Exemplo: domínios parecidos são ruído na pegada de uma organização, mas são o objeto da busca num golpe de imitação; nesse caso, mantenha-os e registre a linha "mantido de propósito".

## Caso de teste
- Entrada: "Rodei o SpiderFoot no domínio do golpe que imita a cooperativa. Deu 412 Co-Hosted Site e 57 Similar Domain. Posso apagar os dois grupos e montar o grafo?"
- Esperado: o agente concorda em remover os Co-Hosted Site (com contagem e motivo: hospedagem compartilhada), mas recusa remover os Similar Domain em bloco, porque num golpe de imitação eles respondem à pergunta; propõe um critério escrito para separar os que imitam a cooperativa e pede para conferir no log se algum módulo tocou o alvo diretamente.
