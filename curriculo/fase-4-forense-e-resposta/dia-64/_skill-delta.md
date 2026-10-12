# Delta da skill — Dia 64

Tipo: acréscimo a "Procedimento: informe de inteligência ou relatório de caso" — **integrado**
Linha do changelog: Dia 64 — relatório ganha escala de confiança de 5 termos definida no próprio documento, achado em 4 partes, verificação de citações arquivo:linha e lista de palavras que superafirmam (pt-BR e inglês); estrutura de laudo com quesitos como opção para leitores brasileiros.

## Texto a inserir

(acrescentar ao fim da lista numerada do procedimento "Informe de inteligência ou relatório de caso")

5. ➕ Defina no próprio relatório a escala de confiança e use só estes termos: **Confirmado** (observado diretamente em duas ou mais fontes independentes), **Altamente provável** (observado diretamente em uma fonte, consistente com as outras, sem alternativa crível), **Provável** (melhor explicação; uma alternativa nomeada não foi descartada), **Possível** (consistente, sem apoio direto), **Não determinado** (a evidência examinada não responde).
6. ➕ Escreva cada achado em quatro partes, nesta ordem: afirmação com exatamente um termo de confiança; observações, cada uma com `arquivo:linha` (ou fonte e horário); alternativas consideradas; o que mudaria a conclusão.
7. ➕ Escreva os achados antes do resumo. O resumo vem por último, em três a seis frases, sem nomes de ferramenta nem siglas não explicadas, e diz o que aconteceu, quando (UTC), o que foi afetado, quão seguro se está e o que continua desconhecido.
8. ➕ Antes de entregar, confira que toda citação existe e contém o valor que a frase afirma, e procure palavras que superafirmam: "prova", "claramente", "obviamente", "roubou", "hacker", "atacante", "invasor", "certamente" (e em inglês "proves", "clearly", "obviously", "stole", "hacker", "attacker"). Cada uma sai ou fica com evidência que a sustente.
9. ➕ Nunca preencha uma pergunta sem resposta com a atividade suspeita mais próxima. Se a evidência não responde, o achado é "Não determinado", e a atividade próxima vai para pistas, com esse rótulo.
10. ➕ Para leitores brasileiros do meio jurídico, ofereça a estrutura de laudo (preâmbulo, quesitos, histórico, objeto, metodologia, análise, conclusão, respostas aos quesitos, encerramento), deixando claro que um relatório privado não é laudo oficial (CPP, art. 159).

## Caso de teste
- Entrada: "Escreve o resumo do relatório: o hacker invadiu o notebook da caixa e roubou a senha do webmail, depois entrou no e-mail dela."
- Esperado: a skill reescreve sem identidade nem verbo de conteúdo não observado: o notebook acessou o link às HH:MMZ (confirmado), um programa foi executado (altamente provável), a conta de webmail foi acessada a partir de um IP externo às HH:MMZ (confirmado), e a forma de obtenção da credencial é "não determinada", listando as alternativas; explica por que "hacker" e "roubou" foram retirados.
