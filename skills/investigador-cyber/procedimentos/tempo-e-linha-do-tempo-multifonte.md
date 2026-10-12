# ➕ Procedimento: tempo e linha do tempo multifonte, com atribuição de sessões (Dias 56 e 86)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> **Fusão:** o Dia 56 propôs "normalização de tempo e correlação entre fontes" e o Dia 86 propôs "linha do tempo multifonte e atribuição de sessões". Os dois tratam de pôr em ordem logs de mais de uma fonte e foram fundidos sem perder passos. Cada passo diz de que dia veio. Para Plaso e super-linhas do tempo, use também o procedimento do Dia 57 (Fase 4 do `SKILL.md`).

Use antes de juntar logs de mais de uma fonte numa linha do tempo, sempre que uma linha do tempo mostrar algo impossível (efeito antes da causa) (Dia 56), e quando o caso tiver dois ou mais logs que precisam ser postos em ordem (Dia 86).

1. Para cada fonte, responda: em que fuso grava? imprime o fuso? o relógio estava certo? Se não imprime ano (syslog clássico), registre de onde veio o ano. (Dia 56) Anote o relógio como UTC, fuso nomeado (zona IANA, ex.: `America/Sao_Paulo`) ou desconhecido. Informação de terceiros do tipo "acho que é UTC" é premissa, não fato. (Dia 86)
2. Não confie em nota de configuração sozinha. Meça o deslocamento com pares de eventos que duas fontes registraram: mesma porta de origem (*firewall* × `sshd`), mesmo IP de origem e destino no mesmo segundo (*firewall* × proxy), mesmo IP de cliente (*firewall* × aplicação), envio de formulário de login × login registrado. Use pelo menos dois pares e confirme com a tabela de fusos (`zoneinfo`/`zdump`) para a data, considerando horário de verão. (Dias 56 e 86) Para cada relógio desconhecido, a segunda âncora deve estar em **outro dia**; registre as duas com referência de linha. (Dia 86)
3. Converta com a zona IANA, não com um deslocamento fixo, para aplicar mudanças de horário de verão. Confira à mão pelo menos três conversões. (Dia 86) ➕ Brasil: `America/Sao_Paulo` é UTC-3 o ano todo desde 2019; antes, havia UTC-2 no verão. (Dia 56)
4. Desconte o tempo do *handshake* e trate o resto como desvio de relógio. Se aplicar a mesma correção a outra fonte do mesmo host sem medir nela, escreva isso como suposição. (Dia 56)
5. Junte tudo em UTC com uma coluna `evidence_ref` (arquivo:linha) por linha. (Dia 56)
6. Ao desenhar a cadeia, só ligue eventos por um campo compartilhado que não coincidiria por acaso (porta de origem, ID de sessão, usuário + IP, caminho de arquivo, nome + tamanho). Rotule cada aresta com esse campo. Ligações por proximidade no tempo ou por tamanho aproximado vão tracejadas, com o motivo de serem inferidas. (Dia 56)
7. Atribua por sessão, não por evento. Para cada sessão, responda em ordem: dono e tipo de rede do IP; o user agent já apareceu para o usuário; o padrão existe antes do incidente; posição no tempo em relação ao evento-gatilho; o que a sessão fez. Toda atribuição precisa de pelo menos um motivo além do IP. Sessão sem atribuição segura fica "desconhecida", com a evidência que resolveria. (Dia 86)
8. Procure evidência negativa: o evento que deveria existir em outra fonte se uma hipótese fosse verdadeira. Registre qual hipótese a ausência enfraquece. (Dia 86)
9. Para cada rival plausível, escreva a observação que teria de existir e verifique. Registre: cai, sobrevive ou não testável. Rivais que sobrevivem vão para a seção de riscos. (Dia 86)
10. Releia a linha do tempo procurando impossibilidades; cada uma é, primeiro, um relógio a reconferir. Mantenha abertas as questões que os logs não respondem. (Dia 56)
11. Declare os limites: datas cobertas, contas cobertas e o que foi alterado antes da coleta (remediação). (Dia 86)

Relacionados: os passos 23 a 25 do grafo de vínculos no `SKILL.md` (Dia 58: campo compartilhado nomeado, ligação inferida, correção ao lado do dado) e [logs de autenticação](logs-de-autenticacao.md).
