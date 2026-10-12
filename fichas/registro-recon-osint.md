# Registro de reconhecimento OSINT

> Tradução de [`worksheets/osint-recon-log.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/worksheets/osint-recon-log.md), © ThiefDroppers (MIT), com campos brasileiros somados (➕).

Use uma cópia por ciclo de reconhecimento (planejar, coletar, processar, analisar, relatar). O [Dia 22](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/curriculum/phase-2-osint-digital-footprint/day-22.md) é o primeiro laboratório que a usa.

## Planejamento
- Pergunta (uma frase específica):
- Autorização ou contexto do caso:
- ➕ Registro de autorização (caminho + SHA-256), do Dia 01:
- ➕ Base legal LGPD do tratamento (art. 7º, inciso):
- Fora do escopo (nomeie as pessoas, contas e sistemas sobre os quais você não vai coletar):

## Registro de coleta
Registre cada dado no momento da coleta, não depois.

| # | Dado | Fonte (URL, ferramenta ou registro) | Data e hora de acesso (com fuso) | ➕ SHA-256 da captura | Observações |
|---|---|---|---|---|---|
| 1 | | | | | |

> ➕ Dica: `python scripts/registrar_evidencia.py captura.png "descrição"` gera a hora UTC e o hash.

## Resumo processado
[Agrupe por entidade ou por pergunta, não por fonte.]

## Análise
Confirmado significa que pelo menos 2 fontes independentes concordam. Provável significa 1 fonte apenas. Contestado significa que as fontes divergem.

| Achado | Confiança (confirmado, provável ou contestado) | Números das fontes no registro de coleta |
|---|---|---|
| | | |

## Relatório
[Escreva os achados com a mesma palavra de confiança que a tabela de análise dá a cada um. Um achado provável continua provável no relatório.]
