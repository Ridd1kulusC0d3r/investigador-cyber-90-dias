# Delta da skill — Dia 78

Tipo: acréscimo a "Linha do tempo de auditoria de nuvem" — **integrado**
Linha do changelog: | 78 | Triagem sem pivô conhecido: cinco filtros (negadas, identidade/política/logging, origem nova, métodos raros, pares novos), tabela antes/depois e lista "revisado e excluído". |

## Texto a inserir

Acrescente ao procedimento "Linha do tempo de auditoria de nuvem", antes do passo de pivô pela origem:

9. Se ainda não há origem ou identidade suspeita, não leia os eventos em ordem: rode cinco filtros independentes sobre o palheiro inteiro e registre, para cada um, a contagem de antes e depois. (a) autorização negada (GCP `status.code` 7, CloudTrail `errorCode`, Azure `Failed`); (b) mudanças de identidade, política e logging (criação de chave, concessão de papel, `SetIamPolicy`, `DeleteSink`, `StopLogging`), conferindo antes os nomes exatos de método no próprio log; (c) origem ou cliente novo para uma identidade conhecida; (d) qualquer ação sobre o registro de logs, mesmo negada; (e) pares (identidade, método) novos em relação a uma linha de base anterior à janela.
10. Leia cada acerto. Mantenha na lista curta (no máximo 15) só o que a própria entrada não explica, com um motivo de comportamento (negado, origem nova, cliente de script, fora de horário, credencial para identidade mais poderosa, tentativa de cortar logs), nunca um rótulo de severidade. Para cada item descartado, escreva uma frase na lista "revisado e excluído" citando a evidência da entrada (origem, user agent, campos da requisição).
11. Registre as fontes ausentes, em especial o log de login do provedor de identidade (Entra ID, Workspace), que é separado do log de plano de controle e expira primeiro (7 dias no Entra ID Free).

## Caso de teste
- Entrada: "Aqui estão 3 dias de Cloud Audit Logs exportados. Recebemos um alerta de custo. O que é suspeito?"
- Esperado: a skill não pede o IP do atacante nem lê tudo em ordem; propõe os cinco filtros, devolve a tabela antes/depois, uma lista curta com motivos comportamentais e uma lista "revisado e excluído" com evidência, e aponta que o log de login do provedor de identidade não está entre os exports.
