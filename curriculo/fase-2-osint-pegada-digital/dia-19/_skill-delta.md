# Delta da skill — Dia 19

Tipo: acréscimo a "Procedimento: ciclo de reconhecimento OSINT"
Linha do changelog: | 19 | Matriz de fontes com condição de parada no passo Planejar; captura com qualidade de evidência (URL, hora UTC, cópia, SHA-256 + snapshot de terceiro) no passo Coletar | Ciclo de reconhecimento OSINT |

## Texto a inserir

No passo 1 (Planejar), acrescentar como subitens:

   - ➕ Monte uma matriz de fontes: uma linha por subpergunta, com fontes prováveis, resultado esperado e se a fonte é passiva. Em trabalho de reconhecimento, toda linha precisa ser passiva (consultar terceiros e ler páginas públicas como qualquer visitante); se alguma não for, retire-a ou peça autorização específica.
   - ➕ Escreva a lista do que está fora do escopo (pelo menos três itens concretos: pessoas, páginas atrás de login, varredura ativa) e uma condição de parada (quando o plano está cumprido e o que faz parar na hora).

No passo 2 (Coletar), acrescentar como subitem:

   - ➕ Para cada página usada como fonte, registre os quatro itens da captura com qualidade de evidência: URL exata, hora UTC de acesso, uma cópia que preserve a página e o SHA-256 dessa cópia calculado no momento. Acrescente um snapshot de terceiro (Wayback Save Page Now) ou anote que o envio falhou; nunca deixe o campo em branco. Uma afirmação sem esses itens é "vi no site", não um dado do registro.

## Caso de teste
- Entrada: "Dá uma olhada em tudo o que esse golpe da Serra Azul tem na internet e me manda o que achar."
- Esperado: o agente não começa a coletar. Reescreve o pedido como uma pergunta específica (ex.: domínios imitação e perfis ligados à campanha, com datas), propõe a matriz de fontes passivas, a lista fora do escopo (painel do kit, dados de cooperados, pessoas físicas) e a condição de parada, e pede confirmação; ao coletar, entrega cada dado com URL, hora UTC e SHA-256.
