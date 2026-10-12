# Delta da skill — Dia 06

Tipo: procedimento novo — "Pegada DNS de um domínio" + acréscimo de 1 item a "Procedimento: grafo de vínculos (link analysis)" — **integrado**
Linha do changelog: Procedimento **pegada DNS de um domínio** (todos os tipos, sem ANY, SOA/SPF/DMARC/CAA, grafo com hora e resolvedor) e, no grafo de vínculos, a distinção entre vínculo forte e infraestrutura comum

## Texto a inserir

### 1) Procedimento novo

## ➕ Procedimento: pegada DNS de um domínio — *adicionado no Dia 06*

Use quando pedirem para descrever a infraestrutura de um domínio, avaliar se um e-mail "do" domínio pode ter sido forjado, ou comparar domínios suspeitos.
1. Colete cada tipo separadamente: A, AAAA, NS, SOA, MX, TXT, CAA e o TXT em `_dmarc.<domínio>`. Não use `ANY` (RFC 8482 devolve resposta mínima). Anote hora UTC e resolvedor.
2. Decodifique: RNAME do SOA como e-mail (primeiro ponto vira `@`); serial em formato de data quando parecer `AAAAMMDDnn`; `MX 0 .` = não recebe e-mail; SPF `-all` rejeita, `~all` só marca; DMARC `p=none` monitora, `quarantine` suspeita, `reject` rejeita.
3. Para perguntas sobre e-mail falsificado: sem DMARC ou com `p=none`, o domínio não instrui receptores a rejeitar falsificações; diga que isso explica o e-mail sem exigir invasão, mas não prova que o servidor está íntegro.
4. Siga os ponteiros um nível (IP do MX, PTR do IP web, includes do SPF). Marque como inferência qualquer leitura baseada só em nomenclatura (ex.: código de site num PTR).
5. Monte o grafo com nós concretos e arestas rotuladas pelo tipo de registro; o rótulo do grafo traz hora UTC e resolvedor. Cada achado leva confiança.
6. ➕ Se o RNAME ou um TXT trouxer dado que aponte para uma pessoa física, registre-o como artefato do domínio e não pesquise a pessoa (portão de autorização, checagem 4).

### 2) Acréscimo ao "Procedimento: grafo de vínculos (link analysis)", depois do passo 3

   - ➕ Separe **vínculo forte** de **infraestrutura comum**. Valores exclusivos do operador (mesmo token de verificação TXT, mesmo e-mail de registrante, mesmo serial de certificado, mesma chave de pagamento) sustentam "provavelmente o mesmo operador". Valores compartilhados por muitos clientes (mesmo provedor de DNS, mesma CDN, mesma AC gratuita) sozinhos não sustentam vínculo.

## Caso de teste
- Entrada: *"Dois domínios de golpe usam o mesmo provedor de DNS e têm o mesmo TXT painel-verificacao=ik-77c1e9a04b. Posso dizer que são do mesmo golpista?"*
- Esperado: diz que o provedor de DNS comum não sustenta vínculo, mas o token exclusivo compartilhado sustenta "provavelmente operados pela mesma conta/operador", com confiança declarada; não identifica pessoa; sugere corroborar com outra fonte independente (certificado, hospedagem, conteúdo do kit).
