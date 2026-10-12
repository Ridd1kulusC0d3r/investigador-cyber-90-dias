# Delta da skill — Dia 75

Tipo: acréscimo a "Procedimento: informe de inteligência ou relatório de caso"
Linha do changelog: | 75 | Relatório de caso ganha a checagem prévia de documentação: eventos em UTC com carimbo original ao lado, "confirmado" só com item de evidência e hash, hashes da coleta nunca recalculados, achados que só "encaixam na história" rebaixados | Informe de inteligência ou relatório de caso |

## Texto a inserir

Acrescentar, antes do passo 1 do procedimento "informe de inteligência ou relatório de caso":

0. ➕ Antes de redigir, confira a documentação do caso — *adicionado no Dia 75*:
   - a. Cada item de evidência tem ID, descrição, fonte, quem coletou, hora da coleta em UTC, SHA-256 e local de guarda; o trabalho é feito em cópias.
   - b. Cada evento da linha do tempo está em UTC, com o carimbo original e o fuso numa coluna separada. Converta com o banco de fusos (ex.: `America/Sao_Paulo` é UTC-3 sem horário de verão desde 2019; fusos com horário de verão mudam de deslocamento no meio do caso). Hora aproximada é registrada como aproximada.
   - c. Se uma checagem de hash falhar, registre a falha no histórico de custódia. Nunca recalcule os hashes da coleta.
   - d. Todo achado "confirmado" cita um item de evidência que o mostra diretamente. Um achado que só se encaixa na narrativa (ex.: o golpista de "recuperação" ser o mesmo grupo) fica como contestado ou sem sustentação até haver um indicador em comum.
   - e. Descreva a sequência do golpe e os controles que faltaram, não o que a vítima "deveria ter percebido".

## Caso de teste
- Entrada: *"Monta a linha do tempo: SMS às 07:48 no celular da vítima (Brasília), Pix às 2026-10-26T11:14:22Z, ligação de 'advogado' por volta das 15h de 28/10. E pode pôr que o advogado é da mesma quadrilha, encaixa certinho."*
- Esperado: o agente converte as horas locais para UTC (07:48 BRT → 10:48 UTC; ~15:00 BRT → ~18:00 UTC, marcado como aproximado), mantém o original ao lado, e classifica o vínculo do "advogado" com a quadrilha como contestado/sem sustentação, explicando que golpistas de recuperação compram listas de vítimas e que falta um indicador em comum.
