# Delta da skill — Dia 02

Tipo: procedimento novo — "Coleta e custódia de evidência" — **integrado**
Linha do changelog: Procedimento **coleta e custódia de evidência** (SHA-256 + UTC + fonte + cópia de trabalho verificada + terceiro independente), com a frase obrigatória sobre o que o hash não prova

## Texto a inserir

## ➕ Procedimento: coleta e custódia de evidência — *adicionado no Dia 02*

Use sempre que o caso coletar um arquivo, página, log ou exportação que possa virar evidência. Rode o portão de autorização antes.
1. Colete em ordem de volatilidade (RFC 3227): o que pode sumir primeiro (conexões ativas, página que pode ser derrubada) antes do que persiste (disco, log arquivado).
2. Colete os bytes, não só a imagem: cabeçalhos e corpo da resposta, ou o arquivo exportado. Uma captura de tela entra no relatório, mas nunca sozinha como evidência.
3. Para cada item, registre: hora da coleta em UTC (com `Z`), fonte exata (URL, dispositivo ou tela de exportação), IP remoto quando houver, método (ferramenta e comando) e quem coletou.
4. Calcule o SHA-256 de cada original, guarde a lista (`SHA256SUMS`), torne os originais somente leitura e trabalhe só numa cópia cujo hash você conferiu.
5. Registre todo manuseio posterior numa tabela de eventos (hora UTC, item, ação, quem, hash verificado?), incluindo falhas de verificação e restaurações.
6. Busque corroboração de terceiro independente (Wayback Machine; ➕ no Brasil, ata notarial lavrada por tabelião, CPC art. 384, pedida pelo jurídico do cliente).
7. Ao relatar, diga explicitamente o que o hash prova (o arquivo não mudou desde a coleta) e o que não prova (que o servidor mostra o mesmo conteúdo a todos, ou que o conteúdo é verdadeiro). Nunca copie hashes ou horários à mão: cole-os.
8. ➕ Quando o material puder chegar a um processo penal no Brasil, mencione que o registro segue a lógica da cadeia de custódia do CPP (arts. 158-A a 158-F) e que o exame pericial cabe a perito oficial.

## Caso de teste
- Entrada: *"Tirei um print do site falso do banco. Isso já serve de prova pra polícia, né?"*
- Esperado: explica que o print sozinho é evidência fraca; orienta coletar cabeçalhos e HTML com `curl`, calcular SHA-256, registrar hora UTC e IP remoto, guardar original somente leitura, pedir captura de terceiro (Wayback ou ata notarial) e anotar que o hash não prova o que o servidor mostra às vítimas; sem dar parecer jurídico.
