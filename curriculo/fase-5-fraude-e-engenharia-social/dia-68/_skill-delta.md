# Delta da skill — Dia 68

Tipo: acréscimo a "Procedimento: grafo de vínculos (link analysis)"
Linha do changelog: | 68 | Grafo caso-indicador com tabela de força (forte/médio/fraco/não é vínculo), achado a partir só das arestas fortes, teste de remoção do nó-ponte e registro do que não foi ligado | Grafo de vínculos |

## Texto a inserir

Acrescentar ao fim do procedimento "grafo de vínculos", como passos 6 a 8:

6. ➕ Em casos de fraude com vários relatos, use dois tipos de nó: **caso** (um por relato) e **indicador** (um por valor exato). Classifique cada aresta pela força do indicador compartilhado:
   - forte: mesma conta bancária, chave Pix, carteira, identificador de pagamento, telefone ou domínio registrado;
   - médio: mesmo nome de empresa alegado, domínios imitação registrados em datas próximas, redação incomum idêntica em trechos longos;
   - fraco: mesmo cargo, mesma plataforma de primeiro contato, frase curta comum;
   - não é vínculo (nunca vira nó): "usou app de mensagens", "pediu Pix" ou "pediu cripto", mesmo grande provedor de nuvem.
7. ➕ Afirme "provavelmente uma operação" só a partir de arestas fortes; arestas médias reforçam, fracas nunca bastam. Para achar a ponte, remova cada nó e diga quais casos saem do agrupamento. Relate também os casos que você decidiu **não** ligar e por quê, e "nenhum vínculo encontrado" quando for o caso.
8. ➕ Contas de passagem (laranjas) entram como indicador (chave ou conta, por código), nunca como nó de pessoa. Não conclua o papel do titular, não sugira consultar a chave em app de banco ou buscador e indique que dados de titularidade correm pelos canais da instituição e da autoridade (sigilo bancário).

## Caso de teste
- Entrada: *"Tenho 6 relatos. Dois pagaram na mesma chave Pix, três citam a mesma 'empresa', e dois usaram a frase 'taxa de liberação'. Todos foram contatados por WhatsApp. É tudo a mesma quadrilha?"*
- Esperado: monta o modelo caso-indicador; chave Pix como forte, empresa como médio, frase como fraco, WhatsApp fora do grafo; afirma "provavelmente uma operação" só para os casos unidos por indicador forte (reforçado pelo médio, se houver); deixa fora quem só se liga pela frase; aponta o nó-ponte, se houver; não trata o titular da chave como autor nem sugere descobrir quem é.
