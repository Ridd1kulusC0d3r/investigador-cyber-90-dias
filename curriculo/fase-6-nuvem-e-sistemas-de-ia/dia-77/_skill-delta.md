# Delta da skill — Dia 77

Tipo: procedimento novo
Linha do changelog: | 77 | Procedimento novo "Linha do tempo de auditoria de nuvem": custódia com hash, cobertura por camada antes de ler resultado vazio, pivô por origem e por ID de chave. |

## Texto a inserir

## ➕ Procedimento: linha do tempo de auditoria de nuvem — *adicionado no Dia 77*

Use quando pedirem para reconstruir o que aconteceu numa conta de nuvem (GCP, AWS, Azure) a partir de exports de log de auditoria. Rode o portão de autorização antes: os logs precisam ter chegado pelo dono da conta (o controlador), não por terceiros.
1. Custódia primeiro. Antes de abrir qualquer arquivo, registre o SHA-256 de cada um e a hora UTC do recebimento. Trabalhe numa cópia; confira a cópia contra o manifesto.
2. Declare a cobertura antes de ler. Para cada nuvem, escreva quais camadas estavam ligadas na janela: no GCP, Admin Activity (sempre) e Data Access (`ADMIN_READ`, `DATA_READ`, `DATA_WRITE`, conforme `auditConfigs`); na AWS, eventos de gerenciamento (sempre, 90 dias) e eventos de dados (só se uma trail os registra, e para quais buckets); no Azure, Activity Log e, separado, o log de sign-in do Entra ID.
3. Nunca trate um resultado vazio de camada desligada como prova de que algo não aconteceu. Escreva "não há registro; a camada estava desligada".
4. Extraia de cada entrada os quatro campos: identidade, método, recurso, origem (IP e user agent), mais o resultado (ok, negado, falha).
5. Siga credenciais criadas: quando uma identidade cria chave para outra (`CreateServiceAccountKey`, `CreateAccessKey`), anote o ID da chave e procure as chamadas assinadas por ela. O ID da chave é a aresta que liga as duas identidades.
6. Pivote pela origem, não pela identidade: junte todos os logs filtrando pelo endereço suspeito e ordene por hora UTC numa única linha do tempo.
7. Relate a ligação entre identidades como "mesma origem e chave emitida por X", nunca como "foi a pessoa X": credencial não é pessoa.
8. ➕ Em caso brasileiro, acrescente a hora BRT (UTC-3) ao lado da UTC quando o leitor for o cliente ou a vítima, e anote a natureza dos dados que o log consegue (ou não) mostrar, porque isso alimenta a comunicação de incidente à ANPD (LGPD, art. 48, §1º).

## Caso de teste
- Entrada: "Olhei o log de auditoria do GCP e não tem nenhum storage.objects.get no bucket de clientes. Posso dizer ao cliente que nada vazou?"
- Esperado: a skill pergunta (ou verifica no `auditConfigs`) se `DATA_READ` estava ligado para o Cloud Storage; se não estava, responde que a ausência não prova nada, sugere fontes independentes (flow logs, billing de egress e de operações Class B) e propõe a frase "não há registro de leitura; a camada que a registraria estava desligada".
