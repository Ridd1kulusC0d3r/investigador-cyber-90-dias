# ➕ Procedimento: perfil de cluster de atividade (Dia 37)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> Procedimento proposto no Dia 37; os itens marcados com ➕ e "(Dia 38)" foram acrescentados no Dia 38.

Use quando pedirem um perfil de ator de ameaça, de "grupo", de "quadrilha" ou de quem está por trás de uma campanha.

1. Perfile um **cluster de atividade** (o que foi observado, agrupado por ferramentas, infraestrutura e comportamento), não uma pessoa. Se o pedido nomear uma pessoa física sem caso autorizado, aplique o portão de autorização e recuse a parte pessoal. Apelidos tirados de artefatos (uma string no código, um *username* no kit) são registrados como artefato, nunca como identidade.
2. Monte um *crosswalk* de nomes: uma linha por nome, com a organização que o usa, **quem afirmou** a equivalência e uma nota de escopo. Sinalize como falsa equivalência nomes de relatório, de tipo de golpe ou de ferramenta usados como se fossem nome do *cluster*.
3. Dê a cada fonte uma nota Admiralty (confiabilidade A–F, credibilidade 1–6) e escreva o porquê. Não dê a mesma nota automaticamente a um alerta conjunto e a um *post* de blog.
4. Toda frase do perfil cita a fonte e a data da atividade. Frase sem fonte e data sai.
5. Afirmações de patrocínio, afiliação ou "facção" ficam no campo próprio, com a fonte e a nota, e nunca no resumo; diga o que faltaria para confirmá-las.
6. Na tabela de ferramental, marque se cada ferramenta é exclusiva ou compartilhada/comercial; ferramenta compartilhada não identifica o *cluster*.
7. Para os eventos principais, preencha um Diamante (adversário, capacidade, infraestrutura, vítima), escrevendo "não informado na fonte" em vez de completar com outros relatos.
8. Não inclua dado pessoal de nenhum indivíduo (vítimas ou suspeitos) no perfil.
9. ➕ Antes de usar uma técnica ou um indicador como evidência de que um evento novo pertence a um *cluster*, verifique a **taxa de base**: quantos outros atores fazem o mesmo (no ATT&CK, conte os grupos com relacionamento `uses` direto; num golpe local, considere se o padrão é comum no país). Comportamento comum é contexto, nunca evidência de autoria. Lembre que "raro no ATT&CK" pode significar só "pouco relatado". (Dia 38)
10. ➕ Classifique cada indicador pelo nível da Pirâmide da Dor (*hash*, IP, domínio, artefato de rede/*host*, ferramenta, TTP) e diga em qual nível o rastreamento se apoia. Recomende detecção pelos níveis de cima; avise que listas de IP e *hash* envelhecem rápido. (Dia 38)
11. ➕ Date cada comportamento observado e registre quando ele apareceu ou parou de aparecer. Ao citar uma sobreposição entre dois atores, diga se ela vem das camadas de grupo (que incluem campanhas) ou dos relacionamentos diretos. (Dia 38)
