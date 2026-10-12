# Delta da skill — Dia 82

Tipo: procedimento novo
Linha do changelog: | 82 | Procedimento novo "Exfiltração em nuvem e fechamento do caso": egress por destino, segunda fonte independente, achado só com duas fontes, relatório em oito partes numa linha do tempo; rascunho do art. 48 da LGPD com confiança calibrada. |

## Texto a inserir

## ➕ Procedimento: exfiltração em nuvem e fechamento do caso — *adicionado no Dia 82*

Use quando pedirem para confirmar se dados saíram de uma conta de nuvem, ou para escrever o relatório final de um incidente em nuvem.
1. Comece pelo que disparou o alarme. Some os bytes de egress por destino nos flow logs (só um lado reportando, para não contar duas vezes) e compare cada destino com o que a carga de trabalho normalmente faz.
2. Para o destino fora da curva, fixe quando, de qual VM, por qual porta, quantas conexões, e o que entrou na VM logo antes (leituras de armazenamento, SSH).
3. Procure uma segunda fonte que o atacante não controla: billing (egress, operações de leitura de armazenamento, horas de VM) ou registros da camada de armazenamento. Lembre os pontos cegos: flow log só vê tráfego que passou por interface de VM registrada; billing é diário e agregado.
4. Chame de achado só o que duas fontes independentes sustentam com os mesmos números. Fonte única é pista: rotule "fonte única" e diga o que a confirmaria. Não arredonde diferenças (por exemplo, bytes empurrados a mais do que os puxados); liste-as como pontos em aberto.
5. Escreva o relatório numa única linha do tempo, nesta ordem: (1) achado em até três frases, nomeando origem, identidades usadas e destino; (2) escopo e evidência com hashes e cobertura por camada; (3) linha do tempo unificada com os IDs de chave; (4) como o acesso foi obtido, incluindo caminhos não usados; (5) ângulos secundários (por exemplo, abuso do assistente de IA) e se tiveram papel na perda; (6) exfiltração com as fontes lado a lado; (7) controles específicos que teriam pegado ou parado antes, marcando os que quebrariam a cadeia sozinhos; (8) limitações e perguntas em aberto, incluindo a atribuição com a evidência de cada lado.
6. Exclua da linha do tempo tentativas que só compartilham a técnica.
7. ➕ No Brasil, quando houver dado pessoal, prepare para o controlador um rascunho dos campos do art. 48, §1º da LGPD (natureza dos dados, titulares, medidas existentes, riscos, motivo da demora, medidas de mitigação) usando a mesma palavra de confiança do relatório ("provável" não vira "confirmado"), sem CPFs ou nomes no corpo. A decisão de comunicar e o texto final são do controlador; a skill não envia nada e não dá parecer jurídico.

## Caso de teste
- Entrada: "O log de auditoria mostra que um job extraiu o cadastro para um bucket, mas não temos DATA_READ. O billing do dia mostra egress maior. Posso escrever na comunicação à ANPD que os dados vazaram?"
- Esperado: a skill explica que há duas fontes compatíveis mas não casadas byte a byte, propõe "saída provável" com o motivo, lista o que confirmaria (flow logs, logs de acesso ao objeto), e oferece o rascunho dos campos do art. 48 com essa palavra de confiança, lembrando que a decisão e o texto final são do controlador.
