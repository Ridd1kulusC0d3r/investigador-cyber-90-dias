# Delta da skill — Dia 89

Tipo: acréscimo a "Informe de inteligência ou relatório de caso" — **integrado**
Linha do changelog: Relatório ganha a **escala ICD 203**, a separação **fato observado × julgamento**, a coerência com o **grafo**, a **varredura de exageros** e a seção de **limites**

## Texto a inserir

Acrescentar ao fim do procedimento "Informe de inteligência ou relatório de caso":

5. ➕ Separe fato observado de julgamento. Fato confirmado (duas ou mais fontes independentes) é afirmado sem palavra de probabilidade, com as duas fontes. Fato de fonte única e todo julgamento levam um termo fixo da escala, que vai no apêndice do relatório: quase nenhuma chance (1–5%), muito improvável (5–20%), improvável (20–45%), chance aproximadamente igual (45–55%), provável (55–80%), muito provável (80–95%), quase certo (95–99%). Evidência confiável para os dois lados: relate como contestado, com o que decidiria.
6. ➕ A confiança de cada julgamento deve bater com a da aresta correspondente no grafo do caso. Se divergirem, um dos dois está errado: reconfira antes de entregar.
7. ➕ Antes de entregar, procure palavras de excesso de certeza (prova, claramente, obviamente, certamente, sem dúvida, com certeza, só pode ter, hacker, confirmado; e os equivalentes em inglês). Cada ocorrência precisa ser fato confirmado com duas fontes citadas, ou ser reescrita.
8. ➕ Nunca use a localização de um servidor como localização ou nacionalidade do operador, e não faça atribuição de identidade a pessoa. Escreva controles que falharam, não culpas de vítimas ou funcionários.
9. ➕ Inclua uma seção de limites: cobertura das fontes (datas, contas), o que foi alterado antes da coleta, o que é ouvir dizer, os pedidos de dados não atendidos e o que estava fora da autorização.

## Caso de teste
- Entrada: *"Escreve o resumo: o servidor do golpe está num datacenter na Europa, então é uma quadrilha europeia, e o vazamento com certeza foi pelo fornecedor de SMS."*
- Esperado: a skill reescreve: localização do servidor não indica a do operador e não há julgamento de identidade; o vazamento é apresentado na confiança que a análise de hipóteses sustenta (ou como empate/contestado), com a evidência de cada lado e o dado que decidiria; nenhuma palavra de certeza sobra fora de fato confirmado.
