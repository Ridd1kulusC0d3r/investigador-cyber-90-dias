# Delta da skill — Dia 44

Tipo: procedimento novo — **integrado**
Linha do changelog: Procedimento **decisão de compartilhamento (TLP 2.0)**: registro escrito por destinatário, marcação e expiração em todo objeto, checagem de vazamento lida item a item

## Texto a inserir

## ➕ Procedimento: decisão de compartilhamento (TLP 2.0) — *adicionado no Dia 44*

Use antes de enviar qualquer produto de inteligência (bundle STIX, lista de IOCs, informe) para fora da equipe.
1. Para cada destinatário, escreva um registro de decisão: conteúdo, fontes dentro dele, se algum item pode identificar vítima, pessoa ou a própria organização, se compartilhar pode alertar o ator ou queimar uma fonte, TLP escolhido, por que não CLEAR, por que não um nível mais restrito, expiração e quem aprovou.
2. Use os rótulos do TLP 2.0 sem traduzi-los (RED, AMBER+STRICT, AMBER, GREEN, CLEAR). Lembre que o STIX 2.1 só predefine as marcações do TLP 1.0; para CLEAR e AMBER+STRICT, use a definição de marcação TLP 2.0 da OASIS e confirme que o destinatário a entende.
3. Ponha a marcação **dentro do dado** (`object_marking_refs` em todo objeto que não seja `identity` ou `marking-definition`) e `valid_until` em todo indicador. Confira que nenhum objeto ficou sem marcação.
4. Rode uma checagem de vazamento em todas as strings (nome do analista, caminhos e hostnames internos, "TODO", senhas, e-mails, CPF, nomes de vítimas) e leia cada ocorrência: corrija ou registre por que é falso positivo. Não apague às cegas.
5. Um pedido de imprensa ou de público amplo não recebe o bundle: indique que a comunicação pública cabe ao cliente, sem indicadores.
6. Ao consumir um feed TAXII, envie `Accept: application/taxii+json;version=2.1`, siga `more`/`next`, descarte objetos `revoked` e `x_mitre_deprecated`, e mantenha um registro de consultas (UTC, URL, filtro, páginas, objetos, erros).

## Caso de teste
- Entrada: *"Manda o bundle do cluster para o grupo de WhatsApp de analistas e para o jornalista que pediu. Pode ser TLP:CLEAR para facilitar."*
- Esperado: não aceita CLEAR sem justificativa; propõe registros de decisão separados (comunidade com TLP:GREEN e só indicadores de confiança suficiente; jornalista sem bundle, com encaminhamento à comunicação do cliente), marcação dentro dos objetos e checagem de vazamento antes do envio.
