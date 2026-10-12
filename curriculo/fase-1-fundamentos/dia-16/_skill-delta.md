# Delta da skill — Dia 16

Tipo: procedimento novo
Linha do changelog: | 16 | Procedimento **modelagem de ameaças com STRIDE** (DFD com fronteiras, STRIDE por elemento, ameaça específica com mitigação, repúdio que aponta o log que falta, minimização antes de proteger) | Modelagem de ameaças |

## Texto a inserir

## ➕ Procedimento: modelagem de ameaças com STRIDE — *adicionado no Dia 16*

Use quando pedirem para avaliar "o que pode dar errado" num sistema, canal ou fluxo, antes de lançá-lo ou depois de um incidente (para listar quais caminhos estavam abertos).
1. Descreva o sistema como diagrama de fluxo de dados: entidades externas, processos, armazenamentos, fluxos rotulados com o que carregam e fronteiras de confiança. Se faltar informação para desenhar, pergunte. Mantenha o modelo pequeno (até uns dez elementos).
2. Passe cada elemento pela regra STRIDE por elemento: entidades externas (S, R); processos (S, T, R, I, D, E); armazenamentos (T, I, D, e R se for log); fluxos (T, I, D). Priorize fluxos que cruzam fronteira.
3. Para cada ameaça, escreva título, descrição que nomeia campos, páginas ou componentes **deste** sistema, severidade e mitigação. Ameaça genérica ("pode haver ataque") não conta.
4. Inclua pelo menos uma ameaça de repúdio que diga qual log de auditoria falta e quais campos ele precisa ter (conta, hora UTC, IP de origem, objeto afetado).
5. Para cada dado pessoal no sistema, pergunte primeiro se ele é necessário para a finalidade (no Brasil, LGPD art. 6º, III); só depois proponha como protegê-lo.
6. Considere o ator adversário concreto do caso, se houver: inclua a ameaça de ele imitar o próprio canal ou controle que está sendo criado.
7. Feche nomeando o fluxo de maior risco e a fronteira que ele cruza, em uma frase.

## Caso de teste
- Entrada: *"Vamos lançar um formulário 'Denuncie um golpe' que pede telefone, link, print e CPF, e a ouvidoria exporta uma planilha semanal por e-mail. Faz o modelo de ameaças rápido, só a parte técnica."*
- Esperado: monta o DFD com fronteiras; lista ameaças nas seis letras, específicas do sistema; inclui a falsificação do próprio canal por SMS (S), o upload de arquivo malicioso aberto por atendente (T), a falta de log de auditoria de exportação (R, com campos) e a planilha por e-mail com CPF (I), propondo antes de tudo não coletar o CPF; fecha com o fluxo de maior risco.
