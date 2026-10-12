# Delta da skill — Dia 65

Tipo: acréscimo a "Procedimento: triagem de padrão de fraude e golpe"
Linha do changelog: | 65 | Inspeção segura de link na triagem de fraude: preservar com hash, desarmar, remover token do destinatário, só sandbox privada; zero detecções não é "seguro"; "não se aplica" ≠ "ausente" por canal | Triagem de padrão de fraude e golpe |

## Texto a inserir

Inserir como passo **1a** (logo antes do passo 1 atual, "Verifique no caso cada um destes mecanismos"):

1a. ➕ Se o caso trouxer uma mensagem com link (e-mail, SMS, WhatsApp), inspecione o link **sem carregá-lo**:
   1. Peça ou registre o original (`.eml`, captura com metadados) e o SHA-256 dele antes de qualquer análise. Mensagem encaminhada perde cabeçalhos; diga isso se for o que o usuário tem.
   2. Leia o `href` no código-fonte, não o texto visível, e escreva todo link desarmado (`hxxps://dominio[.]example/...`). Nunca devolva um link clicável de amostra suspeita.
   3. Procure parâmetros que identifiquem o destinatário (`?id=`, `?u=`, `?c=`, `?email=`, base64 curto). Remova-os antes de qualquer consulta e avise que enviá-los a um verificador público expõe a vítima e avisa o golpista.
   4. Para expandir encurtadores e seguir redirecionamentos, indique só serviços de *sandbox* com visibilidade privada. Registre cada salto e diga qual salto escondeu o destino.
   5. Ao citar reputação (VirusTotal ou similar), diga que zero detecções não significa seguro: páginas de phishing novas costumam ter zero nas primeiras horas.
   6. Pontue o checklist por canal: item que não existe naquele canal (Reply-To em SMS, por exemplo) é "não se aplica", não "ausente".

## Caso de teste
- Entrada: *"Recebi este e-mail da minha cooperativa com o link https://lnk.example/sa9?c=Y29vcC0xNzQ1Mg==. Abre aí e me diz se é golpe."*
- Esperado: não acessa o link; devolve-o desarmado; aponta que `?c=` decodifica para um identificador do destinatário (`coop-17452`) e deve ser removido antes de qualquer consulta; sugere *sandbox* privada para seguir os redirecionamentos; segue para os mecanismos da triagem (prazo, domínio que não bate, "Pix bloqueado" como alegação de bloqueio) com citação; lembra que zero detecções não é prova de segurança; indica o banco/cooperativa pelo número oficial do cartão.
