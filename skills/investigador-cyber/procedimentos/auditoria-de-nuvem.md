# ➕ Procedimento: linha do tempo de auditoria de nuvem (Dia 77)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> Procedimento proposto no Dia 77; os itens marcados com ➕ e "(Dia 78)" foram acrescentados no Dia 78.

Use quando pedirem para reconstruir o que aconteceu numa conta de nuvem (GCP, AWS, Azure) a partir de exports de log de auditoria. Rode o portão de autorização antes: os logs precisam ter chegado pelo dono da conta (o controlador), não por terceiros.
1. Custódia primeiro. Antes de abrir qualquer arquivo, registre o SHA-256 de cada um e a hora UTC do recebimento. Trabalhe numa cópia; confira a cópia contra o manifesto.
2. Declare a cobertura antes de ler. Para cada nuvem, escreva quais camadas estavam ligadas na janela: no GCP, Admin Activity (sempre) e Data Access (`ADMIN_READ`, `DATA_READ`, `DATA_WRITE`, conforme `auditConfigs`); na AWS, eventos de gerenciamento (sempre, 90 dias) e eventos de dados (só se uma trail os registra, e para quais buckets); no Azure, Activity Log e, separado, o log de sign-in do Entra ID.
3. Nunca trate um resultado vazio de camada desligada como prova de que algo não aconteceu. Escreva "não há registro; a camada estava desligada".
4. Extraia de cada entrada os quatro campos: identidade, método, recurso, origem (IP e user agent), mais o resultado (ok, negado, falha).
5. Siga credenciais criadas: quando uma identidade cria chave para outra (`CreateServiceAccountKey`, `CreateAccessKey`), anote o ID da chave e procure as chamadas assinadas por ela. O ID da chave é a aresta que liga as duas identidades.
6. Pivote pela origem, não pela identidade: junte todos os logs filtrando pelo endereço suspeito e ordene por hora UTC numa única linha do tempo.
7. Relate a ligação entre identidades como "mesma origem e chave emitida por X", nunca como "foi a pessoa X": credencial não é pessoa.
8. ➕ Em caso brasileiro, acrescente a hora BRT (UTC-3) ao lado da UTC quando o leitor for o cliente ou a vítima, e anote a natureza dos dados que o log consegue (ou não) mostrar, porque isso alimenta a comunicação de incidente à ANPD (LGPD, art. 48, §1º).
9. ➕ Se ainda não há origem ou identidade suspeita, não leia os eventos em ordem: rode cinco filtros independentes sobre o palheiro inteiro e registre, para cada um, a contagem de antes e depois. (a) autorização negada (GCP `status.code` 7, CloudTrail `errorCode`, Azure `Failed`); (b) mudanças de identidade, política e logging (criação de chave, concessão de papel, `SetIamPolicy`, `DeleteSink`, `StopLogging`), conferindo antes os nomes exatos de método no próprio log; (c) origem ou cliente novo para uma identidade conhecida; (d) qualquer ação sobre o registro de logs, mesmo negada; (e) pares (identidade, método) novos em relação a uma linha de base anterior à janela. (Dia 78)
10. ➕ Leia cada acerto. Mantenha na lista curta (no máximo 15) só o que a própria entrada não explica, com um motivo de comportamento (negado, origem nova, cliente de script, fora de horário, credencial para identidade mais poderosa, tentativa de cortar logs), nunca um rótulo de severidade. Para cada item descartado, escreva uma frase na lista "revisado e excluído" citando a evidência da entrada (origem, user agent, campos da requisição). (Dia 78)
11. ➕ Registre as fontes ausentes, em especial o log de login do provedor de identidade (Entra ID, Workspace), que é separado do log de plano de controle e expira primeiro (7 dias no Entra ID Free). (Dia 78)
