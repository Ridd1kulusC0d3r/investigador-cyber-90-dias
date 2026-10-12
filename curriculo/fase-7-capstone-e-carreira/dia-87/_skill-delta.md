# Delta da skill — Dia 87

Tipo: acréscimo a "Triagem de padrão de fraude e golpe"
Linha do changelog: Triagem de fraude ganha o **mapa frase → controle contornado**, os **pontos de quebra** e a regra de **escrever controles, não culpas**

## Texto a inserir

Acrescentar ao fim do procedimento "Triagem de padrão de fraude e golpe":

5. ➕ Para cada mensagem ou ação do golpista, identifique o controle (técnico ou de processo) que ela foi feita para contornar, com a frase citada como evidência. Exemplo: "não ligue para a agência" contorna o controle "ligar para o número oficial". Uma frase que desencoraja uma verificação é, em si, um indicador forte.
6. ➕ Liste os pontos de quebra: os momentos em que um controle, se existisse e fosse usado, teria parado o golpe. Para cada um, nomeie o controle e cite a evidência de que estava ausente ou foi contornado. Inclua pelo menos um controle de processo.
7. ➕ Nunca descreva a vítima ou um funcionário como descuidado, ingênuo ou culpado. Onde uma pessoa agiu, nomeie o controle que deveria ter dado suporte a ela.
8. ➕ Ao generalizar o caso num padrão reutilizável, retire todo nome, domínio, IP, número, valor e data. Se uma linha só faz sentido com o caso aberto, reescreva.

## Caso de teste
- Entrada: *"Analisa esse WhatsApp: 'Aqui é da Central de Segurança. Regularize sua chave Pix em 30 minutos. Não ligue para a agência, as linhas estão congestionadas.' O cliente caiu porque é desatento, né?"*
- Esperado: a skill pontua os mecanismos com citações (urgência, falsa central, contorno de processo), mapeia "não ligue para a agência" ao controle de ligar para o número oficial, recusa a caracterização "desatento" e reescreve como controle ausente, e lembra os canais (instituição da vítima/MED, delegacia, denúncia na plataforma).
