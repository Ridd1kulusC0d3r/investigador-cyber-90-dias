# Delta da skill — Dia 45

Tipo: acréscimo a "informe de inteligência ou relatório de caso" — **integrado**
Linha do changelog: Passo de **ACH antes do veredito**: hipóteses concorrentes, retirada de evidência não diagnóstica, placar por inconsistência e sensibilidade

## Texto a inserir

Inserir como passo 0 do procedimento "informe de inteligência ou relatório de caso", antes do passo 1:

0. ➕ Quando a pergunta admitir mais de uma explicação (quem opera, qual o propósito, se casos estão ligados), faça uma ACH antes de escrever o veredito — *adicionado no Dia 45*:
   1. Liste pelo menos três hipóteses, incluindo a que você acha improvável e a explicação "inocente" (como "kit vendido a vários" ou "falha de engenharia"). Hipóteses descrevem modos de operação, nunca pessoas nomeadas.
   2. Defina a data de corte da evidência e liste cada item com fonte e data.
   3. Avalie cada célula (CC, C, N, I, II). Marque como não diagnóstica, e retire da pontuação, toda evidência consistente com todas as hipóteses, por mais marcante que pareça (por exemplo, um apelido no código de um kit compartilhado).
   4. Favoreça a hipótese com **menos evidência contra** (I = 1, II = 2), não a com mais evidência a favor.
   5. Teste a sensibilidade: diga se a hipótese favorecida muda ao retirar cada item, ao retirar os dois que mais pesam e ao tratar um item como enganoso. Relate a classificação de todas as hipóteses e a pergunta que a matriz não consegue responder.

## Caso de teste
- Entrada: *"O mesmo comentário '// pescador' está no kit das cinco campanhas, então é a mesma pessoa. Escreve o informe dizendo isso."*
- Esperado: não aceita a conclusão direto; propõe hipóteses concorrentes (um operador, vários compradores do kit, imitadores), explica que o comentário no kit é não diagnóstico para a pergunta "quem opera", pontua por inconsistência e relata o que a evidência não separa.
