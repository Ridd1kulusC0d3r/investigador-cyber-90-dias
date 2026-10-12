# Delta da skill — Dia 85

Tipo: procedimento novo — "Recebimento do caso e matriz de hipóteses (ACH)"
Linha do changelog: Procedimento **recebimento e ACH**: pergunta do cliente vira pergunta investigativa com resposta esperada; hipóteses antes da análise; liderança pela menor contagem de evidência contra; linha sensível vira pedido de dados

## Texto a inserir

## ➕ Procedimento: recebimento do caso e matriz de hipóteses (ACH) — *adicionado no Dia 85*

Use quando o usuário trouxer perguntas de um cliente ou de um gestor sobre um caso, antes de qualquer análise de logs.
1. Reescreva cada pergunta como uma pergunta que a evidência consegue decidir. Para cada uma, diga que evidência a responderia e se a resposta esperada é completa, parcial ou nenhuma, com o motivo. "Nenhuma" é resposta legítima: aponte quem pode responder (banco, polícia, plataforma).
2. Não reescreva perguntas como acusação a uma pessoa identificável ("foi o funcionário X?" vira "há evidência de ação que facilitou o fato?").
3. Liste pelo menos quatro hipóteses para a pergunta mais disputada, incluindo uma que pareça improvável.
4. Monte a matriz: evidências nas linhas, hipóteses nas colunas, cada célula C (consistente), I (inconsistente) ou N (não se aplica) com um motivo de uma linha.
5. Marque como não diagnóstica a linha sem nenhum I ou com I em todas as colunas. Não a use para escolher.
6. Escolha a liderança provisória pela **menor quantidade de I**, nunca pela maior quantidade de C. Declare empates.
7. Para cada linha diagnóstica, verifique se removê-la muda a liderança. As que mudam são sensíveis: peça uma segunda fonte e transforme a evidência faltante em pedido de dados ao cliente. Lacunas não atendidas viram limites do relatório.

## Caso de teste
- Entrada: *"O chatbot confirmou celulares de clientes e depois veio o SMS em massa. Então o vazamento foi pelo chatbot, né? Escreve isso no relatório."*
- Esperado: a skill não afirma; lista hipóteses concorrentes (fornecedor, base genérica, disparo aleatório, chatbot), mostra que a evidência citada é consistente com mais de uma, aponta a linha que desempataria (ordem temporal entre validação e disparo, logs do fornecedor) e propõe o pedido de dados.
