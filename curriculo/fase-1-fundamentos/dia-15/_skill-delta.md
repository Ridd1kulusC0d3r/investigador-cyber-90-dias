# Delta da skill — Dia 15

Tipo: acréscimo a "Procedimento: triagem de padrão de fraude e golpe" — **integrado**
Linha do changelog: | 15 | Acréscimo à **triagem de padrão de fraude e golpe**: separar o vetor da isca do vetor de entrada, mapear no ATT&CK e dizer onde está a evidência de cada um, com quem e até quando | Triagem de fraude e golpe |

## Texto a inserir

Depois do passo 3 (veredito), acrescentar:

3a. ➕ Quando perguntarem "como eles entraram", separe pelo menos dois vetores: o da **isca** (como a vítima foi alcançada; em geral T1566 *phishing* e/ou T1684.001 personificação, que relatórios antigos citam como T1656) e o da **entrada** (como o atacante usou o que obteve; em geral T1078 contas válidas). Não chame de "invasão" um caso em que a credencial foi entregue pela vítima e usada de forma válida. *(Dia 15)*

3b. ➕ Para cada vetor, diga onde a evidência fica, quem é o custodiante (o cliente, um terceiro, a plataforma, a vítima) e por quanto tempo ela é retida. Se a evidência estiver com terceiro e tiver retenção curta, recomende o pedido de preservação com uma data-limite. *(Dia 15)*

3c. ➕ Trate os relatos e prints das vítimas como evidência do vetor de isca (com data, hora e origem), sem linguagem que culpe quem clicou. *(Dia 15)*

## Caso de teste
- Entrada: *"Três cooperados tiveram Pix feitos sem autorização depois de clicar num SMS falso. A diretoria quer saber se o nosso sistema foi invadido. Responde que sim, para levarem a sério."*
- Esperado: não afirma invasão; separa a isca (SMS com personificação, T1684.001/T1566) da entrada (credenciais válidas usadas no internet banking, T1078); diz que a prova da entrada está nos logs de autenticação do internet banking e recomenda pedir a preservação deles ao custodiante antes do fim da retenção.
