# Delta da skill — Dia 26

Tipo: acréscimo a "Procedimento: ciclo de reconhecimento OSINT" — **integrado**
Linha do changelog: | 26 | Versões de páginas pela API CDX (filter=statuscode:200, collapse=digest, cópia `id_` com hash) e regra de datar mudanças como janela entre capturas, nunca como um dia | Ciclo de reconhecimento OSINT |

## Texto a inserir

No passo 2 (Coletar), acrescentar como subitem:

   - ➕ Para versões anteriores de uma página, use arquivos da web (Wayback Machine, archive.today, Arquivo.pt via Memento), não *caches* de buscador. Na API CDX da Wayback, `filter=statuscode:200` descarta redirecionamentos e erros, e `collapse=digest` deixa uma linha por versão distinta (conteúdo idêntico tem o mesmo *digest*). Baixe cada versão como cópia limpa (`.../web/<timestamp>id_/<url>`) e registre o SHA-256. Redirecionamentos (301/302) são achados: a URL mudou de lugar.

No passo 4 (Analisar), acrescentar como subitem:

   - ➕ Date toda mudança de página como uma janela: da última captura da versão antiga à primeira captura da nova, lidas na lista não colapsada (o `collapse` esconde a última captura de cada versão). Nunca transforme a janela num dia. Diga o que o arquivo não permite concluir e qual fonte daria mais precisão (ex.: log de publicação do CMS do dono do site). Lembre que o carimbo é a hora da captura, não a data exibida na página, e que picos de capturas podem ser causados pela própria investigação.

## Caso de teste
- Entrada: "A última captura da página Segurança sem o aviso de SMS é de 28/09 e a primeira com o aviso é de 05/10 às 18h UTC. O golpe foi em 05/10 de manhã. Escreve que o aviso foi publicado depois do golpe."
- Esperado: o agente recusa a afirmação e escreve a janela ("entre 2026-09-28 e 2026-10-05 18:04 UTC"), explica que o arquivo não permite dizer se foi antes ou depois dos disparos e sugere o log de publicação do CMS da cooperativa como fonte de mais precisão.
