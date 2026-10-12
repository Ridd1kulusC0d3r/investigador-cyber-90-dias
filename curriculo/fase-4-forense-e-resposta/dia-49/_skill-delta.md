# Delta da skill — Dia 49

Tipo: procedimento novo — **integrado**
Linha do changelog: | 49 | Procedimento novo "Recebimento de evidência e cadeia de custódia": hash no recebimento, cópia conferida, erro documentado, campos dos arts. 158-B e 158-D do CPP. |

## Texto a inserir

## ➕ Procedimento: recebimento de evidência e cadeia de custódia — *adicionado no Dia 49*

Use quando o usuário receber, copiar ou for analisar um arquivo, imagem ou dispositivo que pode virar prova. Rode o portão de autorização antes.
1. Pergunte (ou registre) a autoridade para a coleta: contrato, política do empregador assinada, termo de consentimento ou ordem judicial. "Eu tinha acesso de administrador" não é autoridade.
2. Se o sistema ainda está ligado, lembre a ordem de volatilidade da RFC 3227: memória e estado de rede antes do disco. Não recomende desligar a máquina antes de considerar a captura de memória.
3. No recebimento, calcule o SHA-256 de cada arquivo e salve um manifesto (`hash  nome`), com a hora em UTC e o fuso local em uso. MD5 e SHA-1 só como valor adicional de compatibilidade.
4. Separe original (somente leitura) e cópia de trabalho. Confira a cópia contra o manifesto antes de analisar. Se não conferir: registre, apague a cópia e copie de novo do original. Nunca escolha o hash "que deu certo".
5. Registre cada passagem de mão numa linha nova (quem entregou, quem recebeu, finalidade, local, lacre intacto, hash reconferido). Nunca edite uma linha antiga; corrija com uma linha nova que aponte a anterior.
6. ➕ No Brasil, espelhe as 10 etapas do CPP art. 158-B (reconhecimento, isolamento, fixação, coleta, acondicionamento, transporte, recebimento, processamento, armazenamento, descarte) e, a cada rompimento de lacre, registre nome e matrícula/função, data, local, finalidade e o número do novo lacre (art. 158-D, §4º). Deixe claro que seguir o CPP não transforma um analista privado em perito oficial.
7. Ao fim da análise, calcule o hash de novo e cite no relatório o número do item e os dois hashes (antes e depois).

## Caso de teste
- Entrada: "Recebi um pen drive com os logs do firewall do cliente. Já abri no Excel e corrigi umas linhas quebradas. Como faço o hash para o relatório?"
- Esperado: a skill explica que o arquivo editado não é mais o original; pede o original (ou uma nova cópia do cliente), orienta hash SHA-256 no recebimento, cópia de trabalho conferida, registro do erro no log de ações e linha nova no formulário de custódia; menciona os campos do art. 158-B/158-D se o contexto for brasileiro; não "calcula o hash" do arquivo editado como se fosse o original.
