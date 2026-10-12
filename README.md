# 🕵️ Investigador Cyber 90 Dias

### *Caso Aberto* — 90 dias de investigação cibernética: OSINT, inteligência de ameaças, forense digital e fraude, em português e com o Brasil dentro.

[![Licença: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-0d4da5)](LICENSE)
[![Baseado em](https://img.shields.io/badge/baseado%20em-ThiefDroppers-0d4da5)](https://github.com/thiefdroppers/cyber-investigator-skills)
[![Currículo](https://img.shields.io/badge/curr%C3%ADculo-90%20dias-0d4da5)](curriculo/)
[![Python](https://img.shields.io/badge/python-s%C3%B3%20stdlib-3776ab)](scripts/)
[![Conteúdo](https://img.shields.io/badge/conte%C3%BAdo-90%2F90%20dias-2ea44f)](curriculo/)
[![Estudado](https://img.shields.io/badge/estudado-0%2F90-orange)](curriculo/)

---

## De onde vem

Este repositório é o meu diário de estudo do **[Cyber Investigator Skills](https://github.com/thiefdroppers/cyber-investigator-skills)**, criado e mantido pela **[ThiefDroppers](https://thiefdroppers.com)** sob licença MIT. Todo o crédito do currículo, da metodologia e da skill original é deles.

O que eu faço aqui é **somar, nunca substituir**:

- a estrutura do original fica intacta: as mesmas 7 fases, os mesmos 90 dias, as mesmas práticas, os mesmos checkpoints;
- tudo é traduzido para o português com rigor técnico;
- em cima disso entra uma camada nova, sempre marcada com ➕.

O original está incluído como submódulo em [`upstream/`](upstream/), apontando direto para o repositório da ThiefDroppers.

## O que este repositório soma ao original

| ➕ Camada | O que é |
|---|---|
| 🎬 **Operação Isca** | Um caso fictício brasileiro que atravessa os 90 dias: um golpe do "Pix bloqueado" contra uma cooperativa mineira. Cada dia é um capítulo. [Ver o caso](caso-continuo/). |
| 🇧🇷 **Prática BR** | Um exercício extra por dia no contexto brasileiro. Se o dia fica com dois exercícios, ótimo. |
| ⚖️ **Camada jurídica BR** | Código Penal (arts. 154-A e 147-A), LGPD, Marco Civil, cadeia de custódia do CPP, ligados ao tema de cada dia. |
| 🧠 **Camada 8** | O fator humano do tema: o viés do investigador, a psicologia da vítima, a engenharia social do golpista. |
| 🤖 **Skill que cresce** | A skill de agente do original, traduzida, e acrescida de um procedimento a cada dia estudado. [Ver a skill](skills/investigador-cyber/SKILL.md) · [histórico](skills/investigador-cyber/CHANGELOG-DA-SKILL.md). |
| 📓 **Notebook Colab por dia** | Código comentado linha a linha, quiz interativo e geração dos artefatos do dia. Só Python padrão. |
| 💡 **Inovação OSINT do dia** | Uma técnica, fonte ou biblioteca Python simples ligada ao tema. |
| 🥷 **Ranks Jutsu** | As fases viram ranks: D (fase 1) → C → B → A → **S** (capstone). |

## O roteiro

| Fase | Dias | Rank | Temas centrais | Artefato prático (do original) |
|---|---|---|---|---|
| [1. Fundamentos](curriculo/#fase-1-fundamentos-dias-1-a-18) | 1–18 | D | Redes, Linux, fundamentos de segurança, ética do investigador | Mapa de topologia da rede de casa ou do lab; primeiro pcap capturado e lido no Wireshark |
| [2. OSINT e pegada digital](curriculo/#fase-2-osint-e-pegada-digital-dias-19-a-34) | 19–34 | C | Ciclo OSINT, metadados, reconhecimento em redes sociais, direito e OSINT | Grafo de vínculos no Maltego CE de uma entidade pública; 5 imagens geolocalizadas no mapa |
| [3. Inteligência de ameaças](curriculo/#fase-3-intelig%C3%AAncia-de-amea%C3%A7as-cibern%C3%A9ticas-dias-35-a-48) | 35–48 | B | MITRE ATT&CK, TTPs de atores, enriquecimento de IOCs | Grafo de pivô de infraestrutura (domínio → IP → certificado → domínios relacionados); heatmap no ATT&CK Navigator |
| [4. Forense e resposta](curriculo/#fase-4-forense-digital-e-investiga%C3%A7%C3%A3o-de-incidentes-dias-49-a-64) | 49–64 | B | Forense de disco e memória, análise de logs, forense de rede | Linha do tempo no Timesketch a partir de logs cruzados; gráficos de conversação no Wireshark |
| [5. Fraude e engenharia social](curriculo/#fase-5-fraude-golpes-e-engenharia-social-dias-65-a-76) | 65–76 | A | Taxonomia de golpes, indicadores de aliciamento e tráfico, fraude com IA | Grafo de quadrilha ligando indicadores compartilhados (telefones, chaves de pagamento, domínios) |
| [6. Nuvem e sistemas de IA](curriculo/#fase-6-investiga%C3%A7%C3%A3o-em-nuvem-e-sistemas-de-ia-dias-77-a-82) | 77–82 | A | Logs de auditoria de nuvem, abuso de IAM, abuso de IA e LLM | Grafo de acesso IAM; grafo de caminho de ataque entre recursos mal configurados |
| [7. Capstone e carreira](curriculo/#fase-7-capstone-e-carreira-dias-83-a-90) | 83–90 | **S** | Uma investigação simulada completa, do recebimento ao relatório | Grafo do caso ligando todas as entidades e evidências, mais o relatório escrito |

Status dia a dia: [`curriculo/README.md`](curriculo/). Os 90 dias já estão escritos (📝); cada um vira ✅ quando você faz a prática e o artefato existe.

Pontos jurídicos que os autores preferiram não afirmar sem conferir na fonte estão listados em [PENDENCIAS.md](PENDENCIAS.md).

## Ética e regras do jogo

Leia antes de começar. Tudo aqui é para uso **autorizado, defensivo e lícito**: proteger sistemas, investigar incidentes que você foi autorizado a investigar, pesquisar ameaças e padrões de golpe, e proteger pessoas. Não cobre perseguição, assédio, exposição de dados pessoais (*doxxing*) nem a mira em um indivíduo privado fora de um trabalho legítimo e autorizado.

A regra que atravessa todas as fases é **cace padrões, não pessoas**. Se estiver em dúvida se algo que você quer praticar é autorizado, trate como não autorizado e use um laboratório, um CTF ou as suas próprias contas. O [Dia 01](curriculo/fase-1-fundamentos/dia-01/) trata disso a fundo, já com a lei brasileira.

## Como estudar

1. Leia o [COMECE-AQUI.md](COMECE-AQUI.md).
2. Faça o [Dia 01](curriculo/fase-1-fundamentos/dia-01/) e o [notebook dele no Colab](https://colab.research.google.com/github/Ridd1kulusC0d3r/investigador-cyber-90-dias/blob/main/curriculo/fase-1-fundamentos/dia-01/dia-01.ipynb).
3. Um dia só conta como feito quando o **artefato** existe. Ler a página não conclui o dia.
4. Todas as ferramentas do roteiro são gratuitas ou têm plano gratuito que cobre os laboratórios.

## Estrutura

```
investigador-cyber-90-dias/
├── curriculo/                 os 90 dias (pt-BR) + mapa-dos-dias.csv + modelo do dia
│   └── fase-N-.../dia-NN/     README.md (o dia) + dia-NN.ipynb (Colab) + _skill-delta.md
├── caso-continuo/             🎬 Operação Isca, o caso que atravessa os 90 dias
├── skills/
│   ├── investigador-cyber/    🤖 a skill pt-BR que cresce a cada dia + changelog
│   └── setores-br/            skills de setor brasileiras (nascem ao longo do roteiro)
├── fichas/                    fichas de trabalho traduzidas + campos BR
├── caso-continuo/dados/       dados sintéticos do caso brasileiro, por dia
├── scripts/                   ferramentas stdlib: novo_dia, gerar_indice, registrar_evidencia,
│                              testar_notebook, verificar_repo, listar_pendencias
└── upstream/                  o repositório original da ThiefDroppers (submódulo)
```

## Repositórios irmãos

Mesma filosofia (estudo aberto, crédito ao autor original, camada BR, Colab):

- [python-para-osint-21-dias](https://github.com/Ridd1kulusC0d3r/python-para-osint-21-dias), a partir do curso de cipher387
- [linux-para-osint-21-dias](https://github.com/Ridd1kulusC0d3r/linux-para-osint-21-dias), a partir do curso de cipher387

## Contribuindo

Correções de tradução, novas práticas BR e casos de teste para a skill são bem-vindos por *issue* ou *pull request*. Correções que valem para o conteúdo original devem ir também para o [repositório da ThiefDroppers](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/CONTRIBUTING.md).

## Licença

[MIT](LICENSE). O conteúdo original é © 2026 ThiefDroppers; as camadas somadas são © 2026 Deivison Lourenço. Detalhes em [CREDITOS.md](CREDITOS.md).

---

<sub>Mantido por **Deivison Lourenço** ([@Ridd1kulusC0d3r](https://github.com/Ridd1kulusC0d3r)) · [LinkedIn](https://www.linkedin.com/in/deivisonlourencos) · Material de estudo; não constitui orientação jurídica.</sub>
