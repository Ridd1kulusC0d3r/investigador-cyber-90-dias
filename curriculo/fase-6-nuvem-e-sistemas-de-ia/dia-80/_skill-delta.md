# Delta da skill — Dia 80

Tipo: acréscimo a "Grafo de vínculos (link analysis)"
Linha do changelog: | 80 | Variante IAM do grafo de vínculos: arestas "pode chegar a" com força declarada, caminho e leitores do alvo, e todo corte testado no grafo antes de ser recomendado. |

## Texto a inserir

Acrescente ao procedimento "Grafo de vínculos (link analysis)":

6. ➕ *Variante IAM (Dia 80).* Quando o grafo for de acesso em nuvem, cada aresta significa "pode chegar a" (é membro de, tem papel em, pode emitir credencial para, roda como) e é rotulada com o papel e o export de onde veio. Declare por escrito quais papéis contam como alcançar o alvo (por exemplo, `storage.objectViewer` lê conteúdo; `storage.legacyBucketReader` só lista nomes) e mostre como o resultado muda se essa decisão mudar.
7. Responda duas perguntas: o caminho mais curto de uma identidade plausível para um atacante (prestador, usuário de pouco privilégio, token de CI) até o alvo; e a lista de todas as identidades que alcançam o alvo.
8. Antes de recomendar uma correção, teste-a no grafo: remova a aresta candidata, rode de novo e registre numa tabela o caminho do ator e a contagem de identidades que alcançam o alvo antes e depois. Prefira o corte que também fecha caminhos não usados (por exemplo, retirar o papel do grupo em vez de retirar a pessoa do grupo). Não proponha cortar uma aresta que é a função legítima do sistema; registre-a e proteja-a de outro modo.
9. Declare os exports que faltaram (pasta, organização, SCPs) e que tipo de caminho essa lacuna pode esconder.

## Caso de teste
- Entrada: "O fornecedor já desativou a conta do desenvolvedor que criou a chave. Podemos encerrar?"
- Esperado: a skill pede (ou usa) os exports de IAM, mostra que o desenvolvedor chegava ao dado por um grupo, testa os dois cortes e apresenta a tabela em que, retirando só a pessoa, outro membro do grupo continua alcançando o dado; recomenda retirar o papel do grupo e não declara o caso encerrado só com a desativação.
