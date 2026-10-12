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

- [Dia 01 — A ligação das 11h05](../curriculo/fase-1-fundamentos/dia-01/)
