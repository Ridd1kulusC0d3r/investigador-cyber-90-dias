# Delta da skill — Dia 14

Tipo: procedimento novo — **integrado**
Linha do changelog: | 14 | Procedimento **classificar o incidente pela tríade CID** (uma propriedade por etapa, registro que prova, log que precisava existir, o que não prova; integridade por conteúdo, não por nome) | Tríade CID |

## Texto a inserir

## ➕ Procedimento: classificar o incidente pela tríade CID — *adicionado no Dia 14*

Use quando pedirem para dizer "o que foi afetado" num incidente, ou quando uma comparação de hashes, um log ou um relato sugerir que dados foram vistos, alterados ou ficaram indisponíveis.
1. Quebre o incidente em etapas (ex.: ler a caixa postal, depois alterar a fatura). Classifique cada etapa separadamente: C (o dado chegou a quem não devia), I (mudança não autorizada), D (não pôde ser usado quando preciso). Acrescente autenticidade quando o ator não era quem parecia, e não repúdio quando a pergunta é ligar a ação ao autor.
2. Para cada etapa, nomeie o registro ou campo específico que provaria a violação (ex.: evento de criação da regra de encaminhamento com IP e parâmetros; Windows 4663, 4720, 4738, 1102, 7034). Nunca responda "os logs".
3. Diga qual registro precisava já estar ligado e retido antes do incidente. Se a leitura nunca foi auditada, diga que a violação de confidencialidade não pode ser demonstrada, em vez de supô-la ou descartá-la.
4. Diga o que a evidência não prova (quais mensagens foram lidas, quem estava ao teclado).
5. Integridade se afirma por conteúdo, não por nome: antes de dizer "arquivo alterado" a partir de hashes que não batem, verifique renomeação (mesmo hash com outro nome), crescimento de log *append-only* (a versão antiga é prefixo exato da nova) e compactação. Lembre que `sha256sum -c` só confere arquivos já listados: arquivos novos e removidos exigem comparar as listas.
6. Se a evidência da etapa está com terceiros (ex.: o servidor do golpista guarda o que as vítimas digitaram), diga isso e indique que o caminho é a autoridade, não o acesso.

## Caso de teste
- Entrada: *"Rodei sha256sum -c com o manifesto de ontem nos logs que o TI mandou hoje e deu FAILED em quatro arquivos. Escreve para o cliente que os logs foram adulterados."*
- Esperado: não afirma adulteração; pergunta se houve rotação de logs entre as entregas; propõe comparar os manifestos por conteúdo (mesmo hash com outro nome), testar se as versões antigas são prefixo exato das novas e descompactar arquivos `.gz` antes de comparar; redige "nenhuma violação de integridade demonstrada até agora" enquanto as checagens não forem feitas.
