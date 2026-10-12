# Delta da skill — Dia 79

Tipo: procedimento novo — **integrado**
Linha do changelog: | 79 | Procedimento novo "Inventário de IAM em nuvem": direta/herdada/indireta, expansão de grupos, recursos curinga em ações IAM de escrita, limites declarados, documentação conferida contra o export. |

## Texto a inserir

## ➕ Procedimento: inventário de IAM em nuvem — *adicionado no Dia 79*

Use quando a pergunta for "por que essa identidade conseguiu fazer isso?" ou "quem alcança este recurso?". Só sobre exports entregues pelo dono da conta.
1. Reúna as políticas de todos os níveis disponíveis: projeto/conta, e as políticas no nível do recurso (conta de serviço, bucket, dataset, usuário). Peça também o export de grupos do provedor de identidade.
2. Gere uma linha por (identidade, papel ou política, recurso), com a coluna `grant_path`: `direct`, `group via <grupo>`, ou indireta por credencial (quem pode criar chave ou token para quem).
3. Marque: papéis amplos ou de escalada (`owner`, `editor`, `serviceAccountKeyAdmin`, `serviceAccountTokenCreator`, `serviceAccountUser`, `AdministratorAccess`, `"Action": "*"`); identidades externas ao domínio da organização; ações IAM de escrita (`iam:Create*`, `iam:Put*`, `iam:Attach*`) com recurso `user/*` ou `*` sem variável como `${aws:username}`. Não confie só na busca por curinga: liste toda declaração inline com seu recurso.
4. ➕ Marque também leitura de recursos que contêm dados pessoais (por exemplo, dataset com coluna de CPF), porque é o que a comunicação de incidente vai precisar descrever.
5. Declare os limites: concessões herdadas de pasta/organização (ou SCPs da AWS) não aparecem se o export não as trouxe; e o inventário não diz o que um papel contém. Consulte o catálogo de papéis antes de chamar um papel de inofensivo ou perigoso, com a data da consulta.
6. Para cada linha marcada, escreva o porquê e a alternativa de privilégio mínimo. ➕ Quando houver fornecedor operando a nuvem, diga quem instrui a mudança (controlador) e quem a executa (operador).
7. Trate organograma, matriz de acessos e documentação do fornecedor como alegações; quando divergirem do export, a divergência é um achado.

## Caso de teste
- Entrada: "O fornecedor jura que o desenvolvedor externo só tinha leitura de logs. Aqui estão a política do projeto e a da conta de serviço do chatbot."
- Esperado: a skill expande grupos, encontra na política da conta de serviço o `serviceAccountKeyAdmin` do grupo do desenvolvedor, escreve a cadeia até o dado pessoal, registra a divergência com a documentação como achado e declara que a herança de pasta/organização não foi vista.
