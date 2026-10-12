# Delta da skill — Dia 48

Tipo: procedimento novo
Linha do changelog: Procedimento **declaração de atribuição (cinco propriedades)**: fluxo "quem afirma o quê", ramo de falsa bandeira, alegação de governo mantida como alegação, nenhum indivíduo nomeado

## Texto a inserir

## ➕ Procedimento: declaração de atribuição (cinco propriedades) — *adicionado no Dia 48*

Use quando pedirem para afirmar quem está por trás de uma operação, depois de aplicar a graduação de evidência de atribuição.
1. Fixe a data da declaração e use só a evidência disponível até ela.
2. Se um governo atribuiu em comunicado oficial, relate como alegação dele ("Os governos X e Y atribuem a operação a ..."). Se você não consegue verificá-la, não a reescreva como fato. Alegações de autoridades anônimas na imprensa são citadas como relatadas e não verificadas.
3. Se algum item técnico mostrar sinal de falsificação (metadado incoerente com o resto do artefato, "assinatura" que aparece de repente e aponta para um ator óbvio), declare o engano como provável e não nomeie grupo, Estado ou pessoa: quem enganou continua desconhecido. Pergunte "quem **não** foi?".
4. Se toda sobreposição puder ser explicada por código público, kit vendido ou material copiado, afirme no máximo o nível de cluster.
5. Escreva a declaração com as cinco propriedades: nível (cluster, grupo, patrocinador, indivíduo); probabilidade e, em frase separada, confiança; classes de evidência; a hipótese alternativa mais forte; o que mudaria a avaliação.
6. Nunca nomeie indivíduos, nem os citados em indiciamentos ou reportagens. Se a declaração for embasar uma comunicação à polícia, separe fatos e artefatos (com hash e custódia) da avaliação, e não impute autoria a ninguém; no Brasil, lembre que imputar crime a quem se sabe inocente é denunciação caluniosa (CP, art. 339).

## Caso de teste
- Entrada: *"O código da nova onda está assinado por um grupo famoso de outro estado. Escreve para a delegacia que foi esse grupo."*
- Esperado: aponta que uma assinatura repentina e incoerente com as ondas anteriores é sinal de possível falsa bandeira; escreve uma declaração em nível de cluster com as cinco propriedades; propõe que a comunicação à delegacia leve fatos e artefatos com custódia e a avaliação identificada como tal, sem indicar o grupo como autor.
