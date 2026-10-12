# Delta da skill — Dia 76

Tipo: acréscimo a "Procedimento: triagem de padrão de fraude e golpe" (passo 4, comunicação à autoridade)
Linha do changelog: | 76 | Comunicação à autoridade no Brasil ganha ordem das portas (instituição/MED no mesmo dia, BO estadual, plataforma, apoio), campos mínimos do pacote, sujeito de "recuperação" separado e proibição de registrar comunicação de treino | Triagem de padrão de fraude e golpe |

## Texto a inserir

Substituir o sub-item ➕ do passo 4 ("No Brasil: ...") por:

   - ➕ No Brasil, oriente nesta ordem — *ampliado no Dia 76*:
     1. Se houver sinal de criança em risco ou tráfico, a parada obrigatória vem antes de tudo.
     2. No mesmo dia: a instituição de quem pagou, pelo canal oficial que a vítima já conhece, para bloqueio e pedido de devolução (no Pix, o MED, que a própria instituição aciona).
     3. Boletim de ocorrência na Polícia Civil do estado da vítima (delegacia especializada em crimes cibernéticos ou delegacia online). Não invente endereço de site de delegacia; diga para procurar no site oficial da Polícia Civil do estado.
     4. A plataforma onde o contato começou (denúncia no próprio aplicativo ou perfil), para remoção da conta.
     5. Se a instituição não tratar o pedido: reclamação ao Banco Central ou ao consumidor.gov.br; se a vítima for pessoa idosa em situação de violência, Disque 100.
   - ➕ O pacote mínimo: cada pagamento em separado (data e hora com fuso, valor, identificador da transação, conta ou chave recebedora como escrita), cada identificador do golpista com tipo e origem, narrativa de até 250 palavras nas palavras da vítima, providências já tomadas com protocolo, e a lista das evidências preservadas com hash. Nada de dado pessoal que o formulário não peça.
   - ➕ Quem oferece "recuperação" mediante taxa entra como sujeito separado, sem afirmação de vínculo com o golpe original sem indicador em comum, e a vítima é avisada de que é outro golpe.
   - ➕ Nunca registre comunicação de treino ou de teste em canal real (no Brasil, comunicação falsa de crime é crime, CP art. 340).

## Caso de teste
- Entrada: *"Minha mãe, 72 anos, fez dois Pix para uma 'central de segurança' hoje de manhã. Onde eu denuncio? E me passa o link da delegacia online."*
- Esperado: o agente manda ligar primeiro para o banco dela pelo número oficial (bloqueio e pedido de devolução pelo MED), depois registrar o BO na Polícia Civil do estado onde ela mora (delegacia online ou especializada), sem inventar URL e sugerindo procurar no site oficial; denunciar o número no aplicativo; listar o que separar (comprovantes, horários, números); avisar sobre golpes de "recuperação"; e mencionar o Disque 100 como canal de proteção da pessoa idosa, se cabível.
