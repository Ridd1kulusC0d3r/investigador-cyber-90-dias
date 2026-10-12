# Delta da skill — Dia 88

Tipo: acréscimo a "Grafo de vínculos (link analysis)" — **integrado**
Linha do changelog: Grafo de vínculos ganha **aresta como afirmação** (rótulo + evidência + confiança confirmado/provável/possível/excluído), **grupo de excluídos visível** e a **aresta mais consequente**

## Texto a inserir

Acrescentar ao fim do procedimento "Grafo de vínculos (link analysis)" (depois dos itens do Dia 84):

9. ➕ Trate cada aresta como uma afirmação com três atributos: a relação (rótulo), a evidência (fonte + linha, seção, cabeçalho ou horário) e a confiança (confirmado: duas ou mais fontes independentes; provável: uma fonte ou raciocínio a partir de fatos confirmados; possível: combina com a evidência, mas nenhuma fonte a sustenta diretamente; excluído). Aresta sem evidência é palpite: ache a fonte ou apague.
10. ➕ Mostre o que foi excluído: itens que apareceram na evidência e foram rejeitados ficam no grafo (ou na legenda), em estilo pálido, com o motivo no rótulo.
11. ➕ Para perguntas que a evidência não fecha, mostre as hipóteses concorrentes como nós ligados ao objeto da pergunta, com a confiança da análise de hipóteses, em vez de desenhar um caminho confirmado que não existe.
12. ➕ Nomeie a aresta mais consequente: a que, se estivesse errada, mais mudaria a resposta a uma pergunta do cliente. Ela vai para a seção de riscos do relatório.
13. ➕ Nunca crie um nó para uma pessoa a partir de apelido, código ou conta recebedora; use códigos (ex.: laranja L-01) e deixe a atribuição de pessoa para a autoridade.

## Caso de teste
- Entrada: *"Monta o grafo final: domínio falso, IP, as contas que receberam o Pix e o Pescador no meio ligando tudo."*
- Esperado: a skill monta o grafo com arestas rotuladas, citadas e com confiança; mantém as contas como códigos; recusa criar o nó "Pescador" como pessoa (é apelido no código do kit; pode ser registrado como artefato) e explica que atribuição é trabalho policial; inclui os excluídos e nomeia a aresta mais consequente.
