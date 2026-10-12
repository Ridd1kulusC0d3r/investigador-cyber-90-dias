# Delta da skill — Dia 46

Tipo: acréscimo a "informe de inteligência ou relatório de caso" — **integrado**
Linha do changelog: **Linguagem calibrada** no informe: escala declarada (ICD 203 ou PHIA), probabilidade e confiança em frases separadas, sem palavras evasivas, com julgamento sobre o que não se sabe

## Texto a inserir

Acrescentar ao procedimento "informe de inteligência ou relatório de caso", depois do passo 4:

5. ➕ Declare no cabeçalho uma única escala de probabilidade (ICD 203 ou a régua PHIA) e use só termos dela. Em português, escreva o termo traduzido com o original em itálico na primeira ocorrência — *adicionado no Dia 46*.
6. ➕ Cada julgamento-chave traz um termo de probabilidade e, **em outra frase**, um nível de confiança (alta, moderada, baixa) com o motivo (qualidade e corroboração das fontes, premissas assumidas). Nunca combine probabilidade e confiança na mesma frase.
7. ➕ Em julgamentos, troque "pode", "poderia", "talvez", "possivelmente" (e *may, might, could, possibly*), e também certezas sem escala como "definitivamente", por um termo da escala, ou apague a frase. Fatos são atribuídos à fonte ("a ESET relatou...") ou à consulta que os produziu.
8. ➕ Inclua pelo menos um julgamento sobre o que não se sabe e uma seção "o que isto não mostra". Não faça afirmação sobre quem está por trás de um cluster no informe, a menos que se esteja aplicando o procedimento de declaração de atribuição.

## Caso de teste
- Entrada: *"Escreve o resumo para o conselho: o Pescador possivelmente pode estar atacando outras cooperativas, e temos certeza de que é ele."*
- Esperado: reescreve com o cluster como sujeito, termo de uma escala declarada (ex.: "provável", PHIA), confiança numa frase separada, sem "possivelmente/pode/certeza", um julgamento sobre a lacuna (quem opera) e nenhuma afirmação de autoria.
