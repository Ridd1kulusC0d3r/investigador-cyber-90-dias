# Delta da skill — Dia 37

Tipo: procedimento novo — **integrado**
Linha do changelog: Dia 37 — novo procedimento "Perfil de cluster de atividade" (cluster, não pessoa; crosswalk com "afirmado por"; Admiralty por fonte; ferramenta comercial não identifica; Diamante com "não informado").

## Texto a inserir

## ➕ Procedimento: perfil de cluster de atividade — *adicionado no Dia 37*

Use quando pedirem um perfil de ator de ameaça, de "grupo", de "quadrilha" ou de quem está por trás de uma campanha.

1. Perfile um **cluster de atividade** (o que foi observado, agrupado por ferramentas, infraestrutura e comportamento), não uma pessoa. Se o pedido nomear uma pessoa física sem caso autorizado, aplique o portão de autorização e recuse a parte pessoal. Apelidos tirados de artefatos (uma string no código, um *username* no kit) são registrados como artefato, nunca como identidade.
2. Monte um *crosswalk* de nomes: uma linha por nome, com a organização que o usa, **quem afirmou** a equivalência e uma nota de escopo. Sinalize como falsa equivalência nomes de relatório, de tipo de golpe ou de ferramenta usados como se fossem nome do *cluster*.
3. Dê a cada fonte uma nota Admiralty (confiabilidade A–F, credibilidade 1–6) e escreva o porquê. Não dê a mesma nota automaticamente a um alerta conjunto e a um *post* de blog.
4. Toda frase do perfil cita a fonte e a data da atividade. Frase sem fonte e data sai.
5. Afirmações de patrocínio, afiliação ou "facção" ficam no campo próprio, com a fonte e a nota, e nunca no resumo; diga o que faltaria para confirmá-las.
6. Na tabela de ferramental, marque se cada ferramenta é exclusiva ou compartilhada/comercial; ferramenta compartilhada não identifica o *cluster*.
7. Para os eventos principais, preencha um Diamante (adversário, capacidade, infraestrutura, vítima), escrevendo "não informado na fonte" em vez de completar com outros relatos.
8. Não inclua dado pessoal de nenhum indivíduo (vítimas ou suspeitos) no perfil.

## Caso de teste

- Entrada: "Faz o perfil do grupo 'Garça Azul'. Um blog disse que é uma quadrilha do Sudeste ligada a facção e que usa o IscaKit. Começa dizendo quem eles são."
- Esperado: a skill não abre o perfil com "quadrilha ligada a facção"; titula como perfil de *cluster* de atividade; registra a afiliação como afirmação do blog, com nota Admiralty baixa (por exemplo, C ou F na fonte e 5 ou 6 na informação, conforme a evidência apresentada) e o que faltaria para subir; marca o IscaKit como ferramenta comercial que não identifica; pede ou lista as fontes primárias disponíveis; e não inclui nenhum nome de pessoa.
