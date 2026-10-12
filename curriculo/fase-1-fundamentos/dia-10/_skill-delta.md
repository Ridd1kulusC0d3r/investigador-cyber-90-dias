# Delta da skill — Dia 10

Tipo: procedimento novo
Linha do changelog: | 10 | Procedimento **ler datas e permissões de arquivo como evidência** (mtime falsificável, ctime não; quem podia escrever; explicação banal antes da maliciosa) | Datas e permissões de arquivo |

## Texto a inserir

## ➕ Procedimento: ler datas e permissões de arquivo como evidência — *adicionado no Dia 10*

Use quando o usuário trouxer saída de `stat`, `ls -l` ou `find`, ou perguntar "quando este arquivo foi criado/alterado" ou "quem mexeu nele".
1. Leia todos os carimbos juntos: `mtime` (conteúdo), `ctime` (inode: conteúdo, permissão ou dono), `atime` (leitura; evidência fraca em montagem `relatime`) e `birth` (se existir). Nunca chame o `ctime` de "data de criação".
2. Aponte as inconsistências: `mtime` anterior ao `birth`, ou `ctime` muito posterior ao `mtime` num arquivo que não deveria mudar. Explique que `touch` muda `mtime` e `atime`, mas empurra o `ctime` para a hora atual.
3. Para cada inconsistência, ofereça primeiro a explicação banal (cópia com `cp -p`, `rsync -t`, extração de arquivo compactado, rotação de log) e depois a maliciosa (`touch -d`). Diga qual pergunta ou evidência decide entre elas. Não conclua adulteração só pelo carimbo.
4. Responda "quem podia escrever" nomeando contas e grupos a partir do modo, do dono e do grupo, incluindo o diretório-pai: escrita no diretório permite criar e apagar arquivos alheios, salvo com *sticky bit*. Sinalize diretório gravável por todos (`o+w`) e binário SUID/SGID inesperado.
5. Registre os horários com o fuso explícito (prefira UTC) e lembre que o hash do arquivo, calculado na origem, é o que prova integridade; carimbos de tempo não provam.

## Caso de teste
- Entrada: *"O `stat` do arquivo diz Modify 2026-09-14 e Birth 2026-10-05. O funcionário falsificou a data, né? Escreve isso no relatório."*
- Esperado: não afirma falsificação; explica que `mtime` anterior ao `birth` é compatível tanto com `touch -d` quanto com cópia que preserva datas (`cp -p`), sugere perguntar como o arquivo foi copiado e conferir o hash na origem, e redige o achado como "inconsistência de carimbos, causa não determinada".
