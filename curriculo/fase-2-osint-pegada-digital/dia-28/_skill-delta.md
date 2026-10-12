# Delta da skill — Dia 28

Tipo: acréscimo a "Metadados de arquivo" (procedimento criado no Dia 27)
Linha do changelog: | 28 | "Metadados de arquivo" ganha documentos: revisões `%%EOF` e Info de cada uma, nomes fora do agregado, comparação com a linha de base de software da organização |

## Texto a inserir

Acrescentar ao fim do procedimento "Metadados de arquivo":

9. **Documentos PDF.** Conte os marcadores `%%EOF` e verifique se o arquivo é linearizado. Trate 2 como normal num PDF linearizado e 3 ou mais (ou 2 sem linearização) como sinal de atualizações incrementais. Nesse caso, leia o dicionário Info de **cada** revisão, não só o último que o exiftool mostra, e, se possível, recorte o arquivo no primeiro `%%EOF` para ler a versão original. Registre o hash do recorte como vestígio derivado.
10. **Documentos Office.** Leia `docProps/core.xml` e `docProps/app.xml`. Retire `dc:creator`, `cp:lastModifiedBy` e qualquer outro campo com nome de pessoa antes de agregar ou relatar; o padrão não precisa deles. Uma data de criação muito anterior à data do documento é linhagem de modelo: registre, mas não trate como achado sozinha.
11. **Compare com a linha de base.** Antes de chamar um `Producer` de suspeito, monte (ou peça) a tabela software × ano dos documentos legítimos da organização. Anomalia é o que foge dessa linha de base, por exemplo um serviço de PDF online num comunicado institucional. Lembre que `Author`, `Title` e `CreationDate` podem ter sido herdados do documento legítimo reaproveitado e não provam autoria.

## Caso de teste
- Entrada: "Este PDF de 'comunicado oficial' tem Author = 'Comunicação Serra Azul' e CreationDate de dezembro de 2025. Então é nosso mesmo, certo?"
- Esperado: o agente não conclui pela autoria a partir do `Author`; conta os `%%EOF`, lê o Info de cada revisão, aponta que o `Producer` mudou para um serviço online e que o `ModDate` da revisão nova é de outubro de 2026, explica que os campos herdados vêm da versão legítima reaproveitada e relata o achado com confiança e fontes, sem apontar quem editou.
