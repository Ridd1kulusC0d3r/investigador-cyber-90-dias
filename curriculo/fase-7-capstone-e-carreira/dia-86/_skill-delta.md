# Delta da skill — Dia 86

Tipo: procedimento novo — "Linha do tempo multifonte e atribuição de sessões" — **integrado**
Linha do changelog: Procedimento **linha do tempo multifonte**: duas âncoras em dias diferentes para todo relógio sem fuso, conversão com horário de verão, atribuição por sessão com motivo além do IP, evidência negativa e rivais testadas

## Texto a inserir

## ➕ Procedimento: linha do tempo multifonte e atribuição de sessões — *adicionado no Dia 86*

Use quando o caso tiver dois ou mais logs que precisam ser postos em ordem.
1. Para cada fonte, anote o relógio: UTC, fuso nomeado (zona IANA, ex.: `America/Sao_Paulo`) ou desconhecido. Informação de terceiros do tipo "acho que é UTC" é premissa, não fato.
2. Para cada relógio desconhecido, encontre um evento que apareça também numa fonte de relógio confiável (ex.: envio de formulário de login × login registrado). A diferença é o deslocamento. Confirme com uma segunda âncora em **outro dia** e registre as duas com referência de linha.
3. Converta com a zona IANA, não com um deslocamento fixo, para aplicar mudanças de horário de verão. Confira à mão pelo menos três conversões.
4. Atribua por sessão, não por evento. Para cada sessão, responda em ordem: dono e tipo de rede do IP; o user agent já apareceu para o usuário; o padrão existe antes do incidente; posição no tempo em relação ao evento-gatilho; o que a sessão fez. Toda atribuição precisa de pelo menos um motivo além do IP. Sessão sem atribuição segura fica "desconhecida", com a evidência que resolveria.
5. Procure evidência negativa: o evento que deveria existir em outra fonte se uma hipótese fosse verdadeira. Registre qual hipótese a ausência enfraquece.
6. Para cada rival plausível, escreva a observação que teria de existir e verifique. Registre: cai, sobrevive ou não testável. Rivais que sobrevivem vão para a seção de riscos.
7. Declare os limites: datas cobertas, contas cobertas e o que foi alterado antes da coleta (remediação).

## Caso de teste
- Entrada: *"O sistema de contestação mostra o cliente reclamando às 09:31 e o Pix saiu às 11:05 UTC. A TI disse que o sistema está em UTC. Então ele reclamou antes de ser roubado, deve ser autofraude."*
- Esperado: a skill não conclui autofraude; trata "está em UTC" como premissa, pede ou procura duas âncoras entre o sistema de contestação e uma fonte UTC, mostra como um deslocamento de -3h inverteria a ordem, e só então compara os horários.
