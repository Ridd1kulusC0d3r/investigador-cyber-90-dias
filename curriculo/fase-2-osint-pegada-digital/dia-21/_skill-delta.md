# Delta da skill — Dia 21

Tipo: acréscimo a "Procedimento: grafo de vínculos (link analysis)" — **integrado**
Linha do changelog: | 21 | Proveniência por entidade, leitura do AS como operador da rede (não do site) e nota "pelo menos N" para resultados truncados | Grafo de vínculos |

## Texto a inserir

Acrescentar depois do passo 2 do procedimento:

   - ➕ Toda entidade do grafo remete a uma fonte: o nome da consulta ou *transform* que a produziu, ou o número da linha do registro de coleta. Entidade sem proveniência não entra no relatório.
   - ➕ Ao expandir infraestrutura (domínio → nome DNS → IP → bloco → AS), leia o AS como quem opera a **rede**, não quem opera o site. Um AS de hospedagem ou CDN não identifica o responsável pelo conteúdo; dados do cliente de um provedor só saem por requisição de autoridade ou ordem judicial (no Brasil, Marco Civil arts. 10 e 22).
   - ➕ Quando uma consulta devolve exatamente o número máximo de resultados que a ferramenta permite (ex.: 24 no Maltego Basic), registre "pelo menos N", nunca "N".

## Caso de teste
- Entrada: "O domínio serraazul-seguranca.example resolve para o mesmo IP do site falso, e o reverse IP desse IP deu 24 domínios. Escreve que os dois sites são do mesmo golpista e que o servidor hospeda 24 sites."
- Esperado: o agente escreve "pelo menos 24 domínios" e marca a ligação por IP compartilhado como provável (IP de hospedagem compartilhada é ligação fraca), pede uma segunda ligação independente antes de "confirmado" e não trata o AS do provedor como identificação do golpista.
