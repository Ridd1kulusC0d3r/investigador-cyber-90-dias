# ➕ Procedimento: metadados de arquivo (Dia 27)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.
>
> Procedimento proposto no Dia 27; os itens marcados com ➕ e "(Dia 28)" foram acrescentados no Dia 28.

Use quando receber uma imagem (ou, a partir do Dia 28, um documento) e precisar dizer onde, quando e como ela foi produzida. Passe antes pelo portão de autorização.

1. Antes de ler qualquer campo, guarde o original como somente leitura, calcule o SHA-256 e trabalhe numa cópia. Nunca edite a evidência, nem para "corrigir" um campo.
2. Pergunte como o arquivo chegou. Imagem baixada de rede social costuma vir sem EXIF (removido no upload); ausência de metadado não é, sozinha, sinal de má-fé. Peça o arquivo original ("enviado como documento", anexo de e-mail), não um print.
3. Leia `Software` e `ModifyDate`. Se nomearem um editor, o arquivo não é o original da câmera: extraia a `ThumbnailImage` e compare o enquadramento. Diferença de enquadramento é achado sobre a edição.
4. Converta a hora local (`DateTimeOriginal` + `OffsetTimeOriginal`) para UTC e compare com `GPSDateStamp`/`GPSTimeStamp`. Registre "bate" ou "não bate"; se não bater, baixe a confiança e diga por quê.
5. Converta as coordenadas para decimal com sinal (S e W negativos). Confira se o sinal bate com as tags `Ref` e com a cena visual. Se não bater, marque a coordenada como contestada; não escolha um lado sem evidência visual.
6. Cada ponto que você relatar leva método (EXIF ou visual), confiança e fonte. Ponto visual exige pelo menos três pistas independentes e checagem de sombra (SunCalc ou cálculo equivalente).
7. Trate `SerialNumber`, `Make` e `Model` como artefatos para agrupar arquivos de uma mesma campanha. Não os use para identificar o dono do aparelho; isso é atribuição de pessoa, trabalho da autoridade com ordem judicial.
8. Não geolocalize residências de pessoas privadas nem pessoas como tema da imagem. Se a coordenada apontar para uma casa, registre só que o campo existe e pare.
9. ➕ **Documentos PDF.** Conte os marcadores `%%EOF` e verifique se o arquivo é linearizado. Trate 2 como normal num PDF linearizado e 3 ou mais (ou 2 sem linearização) como sinal de atualizações incrementais. Nesse caso, leia o dicionário Info de **cada** revisão, não só o último que o exiftool mostra, e, se possível, recorte o arquivo no primeiro `%%EOF` para ler a versão original. Registre o hash do recorte como vestígio derivado. (Dia 28)
10. ➕ **Documentos Office.** Leia `docProps/core.xml` e `docProps/app.xml`. Retire `dc:creator`, `cp:lastModifiedBy` e qualquer outro campo com nome de pessoa antes de agregar ou relatar; o padrão não precisa deles. Uma data de criação muito anterior à data do documento é linhagem de modelo: registre, mas não trate como achado sozinha. (Dia 28)
11. ➕ **Compare com a linha de base.** Antes de chamar um `Producer` de suspeito, monte (ou peça) a tabela software × ano dos documentos legítimos da organização. Anomalia é o que foge dessa linha de base, por exemplo um serviço de PDF online num comunicado institucional. Lembre que `Author`, `Title` e `CreationDate` podem ter sido herdados do documento legítimo reaproveitado e não provam autoria. (Dia 28)
