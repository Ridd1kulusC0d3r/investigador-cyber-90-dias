# Dados do Dia 26 (fictícios)

- `cdx-serraazul-seguranca.json` e `cdx-serraazul-pix.json`: respostas sintéticas no formato `output=json` da API CDX da Wayback (a primeira linha é o cabeçalho). O `digest` é SHA-1 em base32 do conteúdo, como na Wayback.
- `copias-id_/`: as cópias "limpas" de cada versão (o que `.../web/<timestamp>id_/<url>` devolveria).
- `cdx-densidade-serraazul.txt`: carimbos de todas as capturas sob `serraazul.example/*`, para o Passo 3:

```bash
cut -c1-6 cdx-densidade-serraazul.txt | sort | uniq -c
```

Tudo fictício. Os domínios `.example` não existem na Wayback real.
