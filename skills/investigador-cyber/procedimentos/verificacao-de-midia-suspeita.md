# ➕ Procedimento: verificação de mídia suspeita e controle de processo (Dia 71)

> Parte da skill [`investigador-cyber`](../SKILL.md). O escopo e ética e o portão de autorização do `SKILL.md` valem antes de qualquer passo daqui.

Use quando um caso envolver imagem, vídeo, áudio ou ligação que pode ser sintética (voz clonada, rosto trocado, documento fabricado, anúncio com figura pública). Não use mídia íntima ou sexual de ninguém, real ou sintética; se ela aparecer, pare e indique o canal competente.
1. Registre o item: origem, data, canal e como a cópia foi obtida (exportação do aplicativo, download, captura). Calcule o SHA-256 da cópia.
2. Procedência: verifique se há Content Credentials (C2PA). Credenciais válidas presentes pesam muito. Ausência de credenciais **não** é evidência para nenhum lado; escreva "sem credenciais" e siga.
3. Metadados: registre software de criação, datas e se foram removidos. Remoção é o normal depois de rede social ou aplicativo de mensagem.
4. Contradição verificável: procure um original anterior (busca reversa de imagem ou de quadros-chave) ou um fato que contradiga a mídia (a pessoa estava em outro lugar, o número não consta em nenhum cadastro). Este é, quase sempre, o achado mais forte.
5. Inspeção visual e de áudio (lábios fora de sincronia, mãos, dentes, sombras, áudio limpo demais, falta de respiração): registre com marcação de tempo, mas trate como **apoio**, nunca como base da conclusão.
6. Detector automático: se usar, registre a ferramenta e o resultado; "nenhuma manipulação detectada" significa muito pouco e nunca sustenta "autêntico".
7. Conclua nomeando a única checagem que mais pesou. Se ela for "parecia falso" ou uma nota de detector, rebaixe a confiança para provável ou contestado.
8. Sempre recomende um controle de processo que funcione mesmo se a falsificação for perfeita: encerrar o contato e ligar de volta para um número do cadastro anterior ao pedido; segundo aprovador acima de um valor; palavra-código combinada na família. Nenhum passo do controle pode depender de alguém perceber a falsificação.
9. ➕ No Brasil, para falsa central e falso parente: lembre que a instituição real não pede transferência para "conta de segurança", senha, código recebido por SMS nem instalação de aplicativo; e que a pessoa cuja voz ou imagem foi usada também é vítima (Constituição, art. 5º, XXVIII, "a").
