# Delta da skill — Dia 32

Tipo: procedimento novo
Linha do changelog: | 32 | Procedimento novo "OPSEC antes de tocar a infraestrutura do alvo": configuração por tipo de tarefa, regras permanentes (urlscan Private, .eml offline, hash e não arquivo, sem conta pessoal) e a pergunta "o que esta linha vai parecer no log deles?" |

## Texto a inserir

## ➕ Procedimento: OPSEC antes de tocar a infraestrutura do alvo — *adicionado no Dia 32*

Use antes de recomendar ou executar qualquer visita a um site, link, encurtador, anexo ou perfil ligado a um suspeito.

1. Lembre que o operador de um site de golpe lê os próprios logs: IP e rede de origem, impressão digital do navegador, fuso e idioma, *referer* e horário. Pergunte: "o que esta visita vai parecer no log deles?". Se não parecer com uma vítima comum, mude a configuração antes, não depois.
2. Escolha a configuração pela tarefa: fonte pública sem relação com o alvo pode ser o navegador do dia a dia (sem contas pessoais logadas ao pesquisar o caso); site, perfil ou arquivo do alvo, só em ambiente isolado (VM ou perfil dedicado) e por rede que não seja do escritório nem do cliente; links suspeitos de vítimas e encurtadores, primeiro em um analisador com visibilidade privada (por exemplo, urlscan.io Private), nunca numa análise pública.
3. Nunca clique em links nem carregue imagens de e-mail suspeito na caixa real; salve o `.eml` e analise offline. Envie a analisadores públicos o hash, não o arquivo, salvo política que permita *upload*. Nunca entre em conta pessoal no ambiente de investigação.
4. Antes de cada sessão, confira o IP de saída, o fuso e o idioma anunciados (por exemplo, `https://check.torproject.org/api/ip`). Com Tor por linha de comando, use `--socks5-hostname` para não vazar DNS.
5. Trate uma falha de OPSEC que exponha dados de terceiros (link único de vítima clicado da rede do escritório, evidência enviada a serviço público) como possível incidente de segurança: avise o responsável do caso (LGPD, arts. 46 e 48).

## Caso de teste
- Entrada: "Um cliente me mandou o link encurtado do SMS de golpe. Vou abrir aqui no notebook do trabalho e depois jogo o PDF anexo no VirusTotal pra ver."
- Esperado: o agente desaconselha abrir o encurtador da rede e da máquina de trabalho (o encurtador registra o clique e o operador vê a origem), recomenda análise com visibilidade privada ou ambiente isolado, recomenda enviar o hash do PDF e não o arquivo (o upload torna o arquivo, possivelmente com dados de vítimas, disponível a terceiros) e lembra de registrar a sessão.
