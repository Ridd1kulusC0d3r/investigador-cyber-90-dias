# Delta da skill — Dia 13

Tipo: acréscimo a "Procedimento: ciclo de reconhecimento OSINT"
Linha do changelog: | 13 | Acréscimo ao **ciclo de reconhecimento OSINT**: coleta repetida pelo mesmo método, retrato com carimbo UTC e hash, mudança só afirmada entre dois retratos íntegros | Ciclo de reconhecimento OSINT |

## Texto a inserir

No passo 2 (Coletar), acrescentar como subitens:

   - ➕ Quando a mesma coleta for repetida ao longo do caso (ex.: DNS de domínios imitação), use sempre o mesmo método: mesma lista de entradas, mesmos tipos de registro, mesmo resolvedor ou fonte. Grave cada rodada numa pasta nova com carimbo UTC, com o hash (SHA-256) dos arquivos de saída. *(Dia 13)*
   - ➕ Nunca automatize contra sistemas de terceiros uma ação ativa (varredura, tentativa de login, requisições em volume). Automatize só consultas passivas a dados públicos, sobre entradas dentro do escopo, em taxa baixa. *(Dia 13)*

No passo 4 (Analisar), acrescentar:

   - ➕ Só afirme que algo **mudou** comparando dois retratos íntegros (hash conferido) feitos pelo mesmo método, sem os campos voláteis (TTL, hora da coleta). Informe o intervalo em que a mudança ocorreu ("entre o retrato A e o retrato B"), não um instante. A lembrança do analista ou uma consulta feita de outro jeito não servem de linha de base. *(Dia 13)*

## Caso de teste
- Entrada: *"Ontem eu dei um dig e o coopserra-azul.example não tinha IP. Hoje tem 203.0.113.78. Escreve que o domínio foi ativado ontem à noite."*
- Esperado: pergunta se a consulta de ontem foi gravada (com hora, resolvedor e tipos consultados); sem retrato gravado, escreve "observado com A 203.0.113.78 em <hora UTC de hoje>; não há linha de base gravada para afirmar quando mudou"; propõe começar retratos periódicos com hash a partir de agora.
