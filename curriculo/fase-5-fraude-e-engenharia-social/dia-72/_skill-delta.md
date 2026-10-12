# Delta da skill — Dia 72

Tipo: acréscimo a "Procedimento: verificação de texto gerado por máquina"
Linha do changelog: | 72 | Verificação de texto gerado por máquina ganha marcadores de resíduo em pt-BR, a regra da persona incompatível/mudança de voz como observação, e o peso médio da aresta de redação idêntica | Verificação de texto gerado por máquina |

## Texto a inserir

Acrescentar ao fim do passo 1 (resíduo de chatbot):

   - ➕ Em português, o resíduo aparece também como "Claro! Aqui está uma versão...", "Segue uma sugestão de mensagem:", flexões de gênero padronizadas ("Prezado(a)", "cooperado(a)") e marcadores não preenchidos entre colchetes ("[Nome do Cooperado]", "[link]", "[Agência]"). Flexão entre parênteses sozinha é fraca: modelos de comunicado humano também a usam.

Acrescentar como novo passo, depois do passo 5:

   5a. ➕ Registre como observação (não como sinal de máquina nem como mecanismo) a **persona incompatível**, quando quem diz ser uma pessoa comum escreve como departamento de marketing, e a **mudança repentina de voz** no meio de uma conversa, que pode indicar troca de operador ou passagem para um modelo.

Acrescentar ao fim do passo 8:

   - ➕ Peso da aresta: redação incomum idêntica (ou resíduo idêntico) entre denúncias é vínculo **médio** no grafo, porque roteiros e kits são vendidos e copiados. Nunca sustenta sozinha que dois casos são o mesmo operador; para isso é preciso um indicador forte (mesma chave Pix, conta, telefone ou domínio registrado).

## Caso de teste
- Entrada: *"Duas mensagens, uma contra a Serra Azul e outra contra a Coopvale, começam com 'Claro! Aqui está uma versão mais formal da mensagem'. Então é o mesmo golpista, certo? E isso prova que é golpe?"*
- Esperado: o agente responde que o resíduo idêntico indica uso de modelo e sustenta um vínculo médio de "mesmo modelo de texto" entre os casos, mas não prova o mesmo operador nem decide o veredito de golpe; o veredito depende dos mecanismos (pedido de ação por link, regularização de chave Pix etc.), que ele lista com citação.
