# Delta da skill — Dia 60

Tipo: procedimento novo — **integrado**
Linha do changelog: Dia 60 — novo procedimento "Da investigação à regra de detecção" (comportamento antes de indicador, teste onde a resposta é conhecida, "não testada" declarado, custo em falsos positivos).

## Texto a inserir

## ➕ Procedimento: da investigação à regra de detecção — *adicionado no Dia 60*

Use quando pedirem para transformar achados de uma investigação em regra de IDS/SIEM (Suricata, Sigma, consulta salva).
1. Liste o que o caso ensinou em dois grupos: indicadores (IP, domínio, hash) e comportamentos (volume, repetição, sequência, protocolo fora do lugar). Prefira escrever a regra pelo comportamento; use o indicador só como complemento e diga que ele envelhece.
2. Para cada regra, escreva acima dela uma linha de comentário com o que detecta e como foi testada.
3. Teste a sintaxe (no Suricata, `suricata -T`) e depois teste contra uma captura ou log em que você sabe exatamente quando a regra deve disparar. Registre numa tabela: sid, esperado disparar, disparou, contagem, notas.
4. Regra sem dado de teste é marcada como "não testada" com a data planejada do teste. Nunca a apresente como pronta.
5. Para cada regra, estime o custo em falsos positivos (quem mais faz aquilo legitimamente: administradores, atualizadores, o próprio site da organização) e proponha a exceção ou o *threshold* que o reduz.
6. Use faixa local de identificadores (no Suricata, `sid` 9.000.000 em diante) e um prefixo de projeto no texto do alerta.

## Caso de teste
- Entrada: "Escreve uma regra Suricata para pegar o IP 198.51.100.140 que achamos no caso e manda pro cliente colocar em produção."
- Esperado: a skill entrega a regra por indicador marcada como de vida curta, propõe ao lado uma regra ou consulta por comportamento (repetição/volume para destino externo), inclui a linha de comentário e a tabela de teste, diz quais regras foram ou não testadas e estima falsos positivos antes de recomendar produção.
