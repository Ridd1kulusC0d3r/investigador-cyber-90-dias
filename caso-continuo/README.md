# 🎬 Operação Isca — o caso que atravessa os 90 dias

> ➕ Camada nova deste repo. O original trabalha com exercícios e casos por fase (cooperativa de crédito no Dia 1, *case-lab* na Fase 4, *Blue Harbor* na Fase 6, *case packet* no capstone). **Todos eles continuam aqui, intactos.** A Operação Isca soma uma linha narrativa brasileira por cima, para que cada dia seja um capítulo e não um exercício solto.

Tudo é fictício. Domínios usam `.example` (reservado pela RFC 2606) e IPs usam as faixas de documentação `192.0.2.0/24`, `198.51.100.0/24` e `203.0.113.0/24` (RFC 5737). Nenhum nome real, nenhuma pessoa real.

## O cenário

Você acabou de entrar no time de investigação da **Vigia**, um MSSP fictício de Belo Horizonte. O primeiro cliente que cai na sua mesa é a **Cooperativa Serra Azul**, uma cooperativa de crédito do interior de Minas com 40 mil cooperados.

Na segunda-feira de manhã, a ouvidoria da cooperativa recebe 37 reclamações em duas horas. Todas iguais: um SMS dizendo *"Serra Azul: sua chave Pix foi bloqueada por segurança. Regularize em serraazul-pix.example"*. Quem clicou, digitou a senha. Três cooperados já tiveram transferências que não fizeram.

O gerente de risco liga para a Vigia. O contrato é assinado às 11h. Às 11h05, o caso é seu.

## O elenco (fictício)

| Personagem | Papel |
|---|---|
| **Você** | Analista de investigação júnior da Vigia |
| **Marta Quintão** | Gerente de risco da Serra Azul; quem assina a autorização |
| **Dr. Hélio Brandão** | Jurídico da cooperativa; aparece sempre que algo encosta na LGPD |
| **Rafa** | Analista sênior da Vigia, seu mentor; faz as perguntas incômodas |
| **"Pescador"** | Apelido interno do operador desconhecido por trás do kit de phishing |

## Os arcos (um por fase)

| Fase | Dias | O que acontece na Operação Isca |
|---|---|---|
| 1. Fundamentos | 1–18 | Você recebe o caso, escreve a autorização, aprende a ler o SMS, o domínio, o DNS e o certificado do site falso. Monta seu laboratório. |
| 2. OSINT e pegada digital | 19–34 | O ciclo OSINT completo sobre a infraestrutura do golpe. Aparecem perfis falsos da cooperativa no Instagram e no WhatsApp. |
| 3. Inteligência de ameaças | 35–48 | O kit não é novo: ele reaparece em outros 4 domínios de outras cooperativas. Você mapeia o "Pescador" no ATT&CK e escreve o primeiro informe. |
| 4. Forense e resposta | 49–64 | Um funcionário da cooperativa clicou no link pelo notebook corporativo. Agora tem disco, memória e logs para examinar. |
| 5. Fraude e engenharia social | 65–76 | As contas que receberam o Pix revelam uma rede de "laranjas". Você monta o grafo da quadrilha e entrevista um cooperado vítima sem revitimizá-lo. |
| 6. Nuvem e IA | 77–82 | O chatbot de atendimento da cooperativa foi usado para validar CPFs. Logs de nuvem e prompt injection. |
| 7. Capstone | 83–90 | O caso fecha: grafo final, linha do tempo, relatório com confiança calibrada e o pacote para a autoridade. |

## Regra da narrativa

Cada dia abre com uma cena curta (seção **🎬 Abertura do caso**) e termina quando o artefato do dia foi produzido. O original continua sendo a régua técnica; a Operação Isca é o motivo para fazer a prática.

## Capítulos publicados

### Fase 1. Fundamentos

- [Dia 01 — A ligação das 11h05](../curriculo/fase-1-fundamentos/dia-01/)
- [Dia 02 — O hash antes do café](../curriculo/fase-1-fundamentos/dia-02/)
- [Dia 03 — Doze pacotes e um silêncio](../curriculo/fase-1-fundamentos/dia-03/)
- [Dia 04 — Nove linhas da sede](../curriculo/fase-1-fundamentos/dia-04/)
- [Dia 05 — Quem perguntou primeiro](../curriculo/fase-1-fundamentos/dia-05/)
- [Dia 06 — O token esquecido](../curriculo/fase-1-fundamentos/dia-06/)
- [Dia 07 — O celular viu outra coisa](../curriculo/fase-1-fundamentos/dia-07/)
- [Dia 08 — O cadeado da véspera](../curriculo/fase-1-fundamentos/dia-08/)
- [Dia 09 — O endereço que não é da sede](../curriculo/fase-1-fundamentos/dia-09/)
- [Dia 10 — A pasta que todo mundo podia escrever](../curriculo/fase-1-fundamentos/dia-10/)
- [Dia 11 — O logo que entregou a cópia](../curriculo/fase-1-fundamentos/dia-11/)
- [Dia 12 — Domingo, 22h47](../curriculo/fase-1-fundamentos/dia-12/)
- [Dia 13 — O que mudou durante a noite](../curriculo/fase-1-fundamentos/dia-13/)
- [Dia 14 — Quatro arquivos que não batem](../curriculo/fase-1-fundamentos/dia-14/)
- [Dia 15 — Como eles entraram, se ninguém invadiu nada?](../curriculo/fase-1-fundamentos/dia-15/)
- [Dia 16 — O canal que o golpista também vai querer](../curriculo/fase-1-fundamentos/dia-16/)
- [Dia 17 — "Se acontecer, a gente consegue provar?"](../curriculo/fase-1-fundamentos/dia-17/)
- [Dia 18 — Um lugar seguro para abrir o IscaKit](../curriculo/fase-1-fundamentos/dia-18/)

### Fase 2. OSINT e pegada digital

- [Dia 19 — Quarenta abas e nenhuma prova](../curriculo/fase-2-osint-pegada-digital/dia-19/)
- [Dia 20 — Quatrocentos e doze vizinhos](../curriculo/fase-2-osint-pegada-digital/dia-20/)
- [Dia 21 — Um salto de cada vez](../curriculo/fase-2-osint-pegada-digital/dia-21/)
- [Dia 22 — O nó que não parecia nada](../curriculo/fase-2-osint-pegada-digital/dia-22/)
- [Dia 23 — O que o buscador lembra](../curriculo/fase-2-osint-pegada-digital/dia-23/)
- [Dia 24 — O espelho](../curriculo/fase-2-osint-pegada-digital/dia-24/)
- [Dia 25 — Três nomes, um perfil](../curriculo/fase-2-osint-pegada-digital/dia-25/)
- [Dia 26 — Entre duas capturas](../curriculo/fase-2-osint-pegada-digital/dia-26/)
- [Dia 27 — A foto que veio como documento](../curriculo/fase-2-osint-pegada-digital/dia-27/)
- [Dia 28 — Três vezes `%%EOF`](../curriculo/fase-2-osint-pegada-digital/dia-28/)
- [Dia 29 — Três minutos de diferença](../curriculo/fase-2-osint-pegada-digital/dia-29/)
- [Dia 30 — Um certificado, quatro nomes](../curriculo/fase-2-osint-pegada-digital/dia-30/)
- [Dia 31 — A pergunta que vem por escrito](../curriculo/fase-2-osint-pegada-digital/dia-31/)
- [Dia 32 — A página em branco](../curriculo/fase-2-osint-pegada-digital/dia-32/)
- [Dia 33 — Três perguntas sobre o mesmo ato](../curriculo/fase-2-osint-pegada-digital/dia-33/)
- [Dia 34 — O que fica, e até quando](../curriculo/fase-2-osint-pegada-digital/dia-34/)

### Fase 3. Inteligência de ameaças cibernéticas

- [Dia 35 — Quatro cooperativas, um kit](../curriculo/fase-3-inteligencia-de-ameacas/dia-35/)
- [Dia 36 — O alerta que tinha mais do que aconteceu](../curriculo/fase-3-inteligencia-de-ameacas/dia-36/)
- [Dia 37 — Três nomes para a mesma coisa (ou não)](../curriculo/fase-3-inteligencia-de-ameacas/dia-37/)
- [Dia 38 — O IP que todo mundo queria bloquear](../curriculo/fase-3-inteligencia-de-ameacas/dia-38/)
- [Dia 39 — O histórico do terminal](../curriculo/fase-3-inteligencia-de-ameacas/dia-39/)
- [Dia 40 — Quarenta e um vizinhos](../curriculo/fase-3-inteligencia-de-ameacas/dia-40/)
- [Dia 41 — O convite do grupo](../curriculo/fase-3-inteligencia-de-ameacas/dia-41/)
- [Dia 42 — "Somos os próximos?"](../curriculo/fase-3-inteligencia-de-ameacas/dia-42/)
- [Dia 43 — O grafo que só você entende](../curriculo/fase-3-inteligencia-de-ameacas/dia-43/)
- [Dia 44 — Quem pode ver isto?](../curriculo/fase-3-inteligencia-de-ameacas/dia-44/)
- [Dia 45 — Um Pescador ou um cardume?](../curriculo/fase-3-inteligencia-de-ameacas/dia-45/)
- [Dia 46 — Uma página para a Marta](../curriculo/fase-3-inteligencia-de-ameacas/dia-46/)
- [Dia 47 — "Mas quem é o Pescador?"](../curriculo/fase-3-inteligencia-de-ameacas/dia-47/)
- [Dia 48 — A assinatura bonita demais](../curriculo/fase-3-inteligencia-de-ameacas/dia-48/)

### Fase 4. Forense digital e investigação de incidentes

- [Dia 49 — O pen drive lacrado](../curriculo/fase-4-forense-e-resposta/dia-49/)
- [Dia 50 — Dois dispositivos na sacola](../curriculo/fase-4-forense-e-resposta/dia-50/)
- [Dia 51 — O ZIP que sumiu do pen drive](../curriculo/fase-4-forense-e-resposta/dia-51/)
- [Dia 52 — Um arquivo de 2021 numa pasta de ontem](../curriculo/fase-4-forense-e-resposta/dia-52/)
- [Dia 53 — Os 15 minutos que o Rafa comprou](../curriculo/fase-4-forense-e-resposta/dia-53/)
- [Dia 54 — Cinco minutos, de novo](../curriculo/fase-4-forense-e-resposta/dia-54/)
- [Dia 55 — O login que a caixa não fez](../curriculo/fase-4-forense-e-resposta/dia-55/)
- [Dia 56 — O ataque que começou antes do clique](../curriculo/fase-4-forense-e-resposta/dia-56/)
- [Dia 57 — O proxy que não sabia o ano](../curriculo/fase-4-forense-e-resposta/dia-57/)
- [Dia 58 — A história que a Marta vai ler](../curriculo/fase-4-forense-e-resposta/dia-58/)
- [Dia 59 — Cinco minutos, mais ou menos](../curriculo/fase-4-forense-e-resposta/dia-59/)
- [Dia 60 — A regra que morre na quinta-feira](../curriculo/fase-4-forense-e-resposta/dia-60/)
- [Dia 61 — O executável que ninguém vai abrir](../curriculo/fase-4-forense-e-resposta/dia-61/)
- [Dia 62 — Score 10/10](../curriculo/fase-4-forense-e-resposta/dia-62/)
- [Dia 63 — Uma consulta, uma conta, três sistemas](../curriculo/fase-4-forense-e-resposta/dia-63/)
- [Dia 64 — A frase que o Dr. Hélio riscou](../curriculo/fase-4-forense-e-resposta/dia-64/)

### Fase 5. Fraude, golpes e engenharia social

- [Dia 65 — A segunda onda](../curriculo/fase-5-fraude-e-engenharia-social/dia-65/)
- [Dia 66 — O boleto da Gráfica Jatobá](../curriculo/fase-5-fraude-e-engenharia-social/dia-66/)
- [Dia 67 — A conta L-03](../curriculo/fase-5-fraude-e-engenharia-social/dia-67/)
- [Dia 68 — O quadro na parede](../curriculo/fase-5-fraude-e-engenharia-social/dia-68/)
- [Dia 69 — L-04 em outro lugar](../curriculo/fase-5-fraude-e-engenharia-social/dia-69/)
- [Dia 70 — A parada obrigatória](../curriculo/fase-5-fraude-e-engenharia-social/dia-70/)
- [Dia 71 — A voz do gerente Cláudio](../curriculo/fase-5-fraude-e-engenharia-social/dia-71/)
- [Dia 72 — "Claro! Aqui está uma versão mais formal"](../curriculo/fase-5-fraude-e-engenharia-social/dia-72/)
- [Dia 73 — A mensagem que queria mandar no modelo](../curriculo/fase-5-fraude-e-engenharia-social/dia-73/)
- [Dia 74 — "Minha filha nem sabe ainda"](../curriculo/fase-5-fraude-e-engenharia-social/dia-74/)
- [Dia 75 — Sete arquivos e um papel dobrado](../curriculo/fase-5-fraude-e-engenharia-social/dia-75/)
- [Dia 76 — O cartão V4](../curriculo/fase-5-fraude-e-engenharia-social/dia-76/)

### Fase 6. Investigação em nuvem e sistemas de IA

- [Dia 77 — A Lia sabia demais](../curriculo/fase-6-nuvem-e-sistemas-de-ia/dia-77/)
- [Dia 78 — Cinco minutos da Marta](../curriculo/fase-6-nuvem-e-sistemas-de-ia/dia-78/)
- [Dia 79 — O organograma mente](../curriculo/fase-6-nuvem-e-sistemas-de-ia/dia-79/)
- [Dia 80 — Uma aresta só](../curriculo/fase-6-nuvem-e-sistemas-de-ia/dia-80/)
- [Dia 81 — A Lia não mente, mas também não desconfia](../curriculo/fase-6-nuvem-e-sistemas-de-ia/dia-81/)
- [Dia 82 — A conta não mente](../curriculo/fase-6-nuvem-e-sistemas-de-ia/dia-82/)

### Fase 7. Capstone e carreira

- [Dia 83 — O cofre de evidências](../curriculo/fase-7-capstone-e-carreira/dia-83/)
- [Dia 84 — Nove pivôs, três verdadeiros](../curriculo/fase-7-capstone-e-carreira/dia-84/)
- [Dia 85 — As cinco perguntas da Marta](../curriculo/fase-7-capstone-e-carreira/dia-85/)
- [Dia 86 — O relógio que ninguém acertou](../curriculo/fase-7-capstone-e-carreira/dia-86/)
- [Dia 87 — "Não ligue para a agência"](../curriculo/fase-7-capstone-e-carreira/dia-87/)
- [Dia 88 — A parede vira um arquivo](../curriculo/fase-7-capstone-e-carreira/dia-88/)
- [Dia 89 — O rascunho que o Dr. Hélio devolveu](../curriculo/fase-7-capstone-e-carreira/dia-89/)
- [Dia 90 — O que fica do caso](../curriculo/fase-7-capstone-e-carreira/dia-90/)

## Notas de continuidade

O caso foi escrito em blocos paralelos. Os fatos fixos e a linha do tempo de DNS estão na seção 7 do [guia de produção](../curriculo/_GUIA-DE-PRODUCAO.md). Pontas que o leitor atento vai notar, e que fazem parte do caso:

- **`serraazul-seguranca.example` muda de IP.** Até 9/out resolve para `203.0.113.78` (vizinho do site falso no mesmo AS, sem resposta); depois, para `203.0.113.77`. DNS é foto com data: sempre registre quando consultou.
- **`203.0.113.150` aparece três vezes.** No Dia 09, como origem de uma sessão de cooperado no internet banking; no Dia 81, numa sessão do chatbot que a análise trata como alvo separado; no Dia 86, como o "dispositivo novo" que entra nas contas das vítimas. Só no capstone as três aparições se ligam, e a pergunta "eu deveria ter ligado isso antes?" é parte do exercício.
