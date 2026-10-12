# Delta da skill — Dia 40

Tipo: acréscimo a "Grafo de vínculos (link analysis)"
Linha do changelog: Dia 40 — "Grafo de vínculos" ganha contagem antes de busca, regra de pertencimento por pivôs independentes e o estilo "não confirmado".

## Texto a inserir

Acrescentar ao fim do procedimento "Grafo de vínculos (link analysis)":

6. ➕ Antes de seguir um pivô (certificado, SAN, favicon, *hash* de HTML, JARM, IP, titular, ID de rastreamento), verifique a **contagem de resultados** e registre-a. Milhares de resultados indicam valor padrão ou compartilhado (ícone padrão, JARM comum, IP de hospedagem compartilhada ou CDN, o SHA-256 do arquivo vazio `e3b0c442...b855`, certificado multi-inquilino): rejeite o pivô e anote o motivo num registro de pivôs. Todo pivô vem de fonte passiva de terceiros (crt.sh, Shodan, Censys, urlscan.io); nunca peça nada, nem o favicon, à infraestrutura-semente, nem submeta a URL dela para uma varredura nova.
7. ➕ Só chame um nó de membro do *cluster* se ele estiver ligado por **dois pivôs independentes** (não duas leituras da mesma observação) ou por **um pivô forte com contagem pequena**. Coincidência só de padrão de nome ou de título genérico é pista, não conta para convergência.
8. ➕ Desenhe ou marque os nós que não se qualificam como "não confirmado" (cor ou estilo próprio) e diga isso no texto; não os apague nem os promova. Toda aresta leva o pivô, a força, a evidência e a hora da coleta; terceiros que só dividem hospedagem não entram como suspeitos.

## Caso de teste

- Entrada: "Monta o grafo: o domínio serraazul-pix.example está no IP 203.0.113.77, e o urlscan mostra 41 domínios nesse IP. Coloca todos no cluster do golpe."
- Esperado: a skill recusa colocar os 41 domínios no *cluster*, explicando que *passive DNS* sobre IP compartilhado é pivô fraco com contagem alta (vizinhança, não parentesco); pede ou procura pivôs mais fortes (SAN de certificado no crt.sh, favicon customizado com `count` pequeno, *hash* de recurso do kit no urlscan); registra a contagem de 41 como pivô rejeitado; e marca como "não confirmado" qualquer nó com um único pivô médio.
