# Delta da skill — Dia 66

Tipo: acréscimo a "Procedimento: triagem de padrão de fraude e golpe"
Linha do changelog: | 66 | Classificação de BEC em três respostas (remetente falsificado, domínio imitação, caixa comprometida), domínio antes de SPF/DKIM/DMARC, verificação por número já cadastrado | Triagem de padrão de fraude e golpe |

## Texto a inserir

Inserir como passo **1b** (depois do 1a do Dia 65, antes do passo 1 atual):

1b. ➕ Se o caso for um e-mail pedindo pagamento ou mudança de dados de pagamento (BEC, "boleto atualizado", "nova chave Pix do fornecedor"), classifique o remetente **nesta ordem** e diga qual evidência decidiu:
   1. Compare o domínio do From, caractere por caractere, com o domínio da correspondência genuína anterior. Se diferir (letra, hífen, palavra, TLD, homóglifo): **domínio imitação**. Diga que SPF/DKIM/DMARC podem passar, porque valem para o domínio do golpista, e sugira conferir a data de criação (RDAP; Registro.br para `.br`).
   2. Só com domínio idêntico, leia `Authentication-Results`. `dmarc=fail` (ou SPF falho sem DKIM alinhado): **remetente falsificado**. Cite a política (`p=none` explica por que chegou à caixa de entrada) e recomende que o dono do domínio endureça a política.
   3. Tudo passa para o domínio certo e o pedido muda pagamento, pede sigilo ou impõe prazo: **possível caixa comprometida**. Diga que nenhuma checagem técnica pega este caso; o incidente é do remetente.
   4. Nos três casos, a verificação é por fora do e-mail, num número **já cadastrado**, nunca num número da mensagem. Se houve pagamento, a prioridade é o banco do pagador (estorno; no Pix, o MED) antes de qualquer análise adicional.

## Caso de teste
- Entrada: *"O fornecedor mandou e-mail de financeiro@graficajatoba-cobranca.example pedindo para pagar na chave Pix nova. SPF, DKIM e DMARC deram pass. Então é legítimo, né?"*
- Esperado: não aceita o "pass" como prova; aponta que o domínio difere do conhecido (`graficajatoba.example`) por uma palavra acrescentada, classifica como domínio imitação, explica que a autenticação passou para o domínio errado, recomenda ligar para o número já cadastrado do fornecedor e, se já pagou, acionar o banco (MED) imediatamente; registra a chave Pix como indicador, sem concluir quem é o dono.
