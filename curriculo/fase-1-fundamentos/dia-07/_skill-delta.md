# Delta da skill — Dia 07

Tipo: procedimento novo — "Mapear uma cadeia de redirecionamento" — **integrado**
Linha do changelog: Procedimento **cadeia de redirecionamento**: salto a salto (URL, status, mecanismo, IP), coleta também no contexto da vítima, meta refresh/JavaScript, camuflagem, nunca enviar dados

## Texto a inserir

## ➕ Procedimento: mapear uma cadeia de redirecionamento — *adicionado no Dia 07*

Use quando o caso começar por uma URL (link de SMS, e-mail, anúncio) e for preciso saber onde a vítima terminou.
1. Nunca abra a URL suspeita a partir da rede do cliente, de casa ou do escritório. Use infraestrutura de análise (VM, VPN de pesquisa ou serviço em sandbox com visibilidade privada).
2. Registre cada salto: hora UTC, URL completa, IP que respondeu, código de status e mecanismo (`3xx` + `Location`, `meta refresh`, JavaScript). `301`/`308` são permanentes; `302`/`303`/`307`, temporários.
3. Lembre que `curl -L` e bibliotecas HTTP só seguem redirecionamento por cabeçalho. Se a cadeia "parar" num `200`, procure `<meta http-equiv="refresh">` e `window.location`/`location.href` no HTML, ou repita num navegador com gravação HAR.
4. Busque também como a vítima buscaria: User-Agent de celular, idioma e, se possível, país de origem da vítima. Se as duas coletas divergirem, registre as duas como verdadeiras e trate a diferença como indício de camuflagem (cloaking), não como contradição.
5. Leia cabeçalhos de infraestrutura (`Server`, `Via`, `X-Cache`, `CF-RAY`, nomes em `Set-Cookie`, `Date`) e escreva o que eles sugerem como inferência, nunca como identificação do operador.
6. Trate HAR como evidência sensível: calcule o hash e restrinja o acesso, porque ele contém cookies e tokens.
7. Nunca envie dados em formulários suspeitos, nem fictícios, sem autorização específica para isso.

## Caso de teste
- Entrada: *"Rodei curl -L no link do SMS e caiu numa página 'em manutenção'. Então o golpe já foi derrubado?"*
- Esperado: explica que o curl não segue meta refresh nem JavaScript e que kits camuflam conteúdo por User-Agent, idioma e IP; recomenda repetir em navegador de análise com perfil de celular e gravação HAR (ou sandbox com país de origem da vítima); não conclui derrubada; lembra de não enviar dados no formulário.
