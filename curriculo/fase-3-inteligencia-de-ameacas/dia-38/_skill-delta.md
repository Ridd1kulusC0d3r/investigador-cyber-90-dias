# Delta da skill — Dia 38

Tipo: acréscimo a "Perfil de cluster de atividade" (procedimento proposto no Dia 37) — **integrado**
Linha do changelog: Dia 38 — "Perfil de cluster de atividade" ganha taxa de base, nível da Pirâmide da Dor e datas de comportamento.

## Texto a inserir

Acrescentar ao fim do procedimento "Perfil de cluster de atividade":

9. Antes de usar uma técnica ou um indicador como evidência de que um evento novo pertence a um *cluster*, verifique a **taxa de base**: quantos outros atores fazem o mesmo (no ATT&CK, conte os grupos com relacionamento `uses` direto; num golpe local, considere se o padrão é comum no país). Comportamento comum é contexto, nunca evidência de autoria. Lembre que "raro no ATT&CK" pode significar só "pouco relatado".
10. Classifique cada indicador pelo nível da Pirâmide da Dor (*hash*, IP, domínio, artefato de rede/*host*, ferramenta, TTP) e diga em qual nível o rastreamento se apoia. Recomende detecção pelos níveis de cima; avise que listas de IP e *hash* envelhecem rápido.
11. Date cada comportamento observado e registre quando ele apareceu ou parou de aparecer. Ao citar uma sobreposição entre dois atores, diga se ela vem das camadas de grupo (que incluem campanhas) ou dos relacionamentos diretos.

## Caso de teste

- Entrada: "Chegou um SMS novo: 'Sua chave Pix foi bloqueada, regularize em coopnova-pix.example'. É o mesmo grupo do IscaKit? Usa o T1566.002 que bate."
- Esperado: a skill responde que o texto do SMS e a técnica T1566.002 são comuns (46 grupos no ATT&CK v19.2, e o golpe do "Pix bloqueado" é usado por muitos operadores no Brasil), portanto não ligam o SMS ao *cluster*; indica os sinais mais distintivos a procurar (favicon customizado, a *string* no JavaScript, padrão de registro e de certificado), por fontes passivas; e devolve a ligação como "não determinada" até que esses sinais apareçam.
