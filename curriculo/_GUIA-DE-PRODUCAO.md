# Guia de produção de um dia

Este guia é o contrato que todo dia do repositório segue, escrito por humano ou por agente. O **Dia 01** ([`fase-1-fundamentos/dia-01/`](fase-1-fundamentos/dia-01/)) é o exemplo de referência: na dúvida, imite-o.

## 1. A regra que vem antes de todas

**Somar, nunca substituir.** Todo o conteúdo do original (ThiefDroppers) entra traduzido, inteiro, na mesma ordem: todas as seções, tabelas, blocos de código, diagramas mermaid, comandos e itens de checkpoint. Se o original tem uma seção extra (por exemplo, *Handling events*), ela entra traduzida no mesmo lugar. Nada é resumido, cortado ou "melhorado" por cima. Tudo o que é novo vem marcado com ➕ no título da seção.

O original está em `upstream/curriculum/<pasta-da-fase>/day-NN.md`. Os dados de laboratório do original (`upstream/curriculum/*/resources/`, `case-packet/`) continuam sendo a base técnica das práticas.

## 2. Arquivos de cada dia

```
curriculo/<pasta-da-fase>/dia-NN/
├── README.md        o dia (estrutura da seção 3)
├── dia-NN.ipynb     notebook Colab (seção 5)
└── _skill-delta.md  proposta do que o dia acrescenta à skill (seção 6)
```

Opcional: dados sintéticos do caso brasileiro em `caso-continuo/dados/dia-NN/` (pequenos, gerados por script stdlib, sempre fictícios).

Use `python scripts/novo_dia.py NN` para criar o README com cabeçalho correto, ou copie o cabeçalho do Dia 01.

## 3. Estrutura do README do dia

1. Cabeçalho: título pt-BR, bloco de crédito com link do original, fase, meta da trilha, rank Jutsu, badge do Colab (copie o formato do Dia 01).
2. `## 🎬 ➕ Abertura do caso — *título do capítulo*` — cena curta da Operação Isca (seção 7), 6 a 12 linhas, em cena, com diálogo quando couber. Termina apontando para o que o dia ensina.
3. `## 📖 Conceito` — tradução fiel.
4. `## 📚 Recursos` — tradução fiel (links mantidos). Depois `### ➕ Recursos do contexto Brasil`.
5. `## 🛠️ Prática: ...` — tradução fiel, com comandos reais intactos. O checklist do original ganha itens ➕ para a Prática BR e o notebook. Depois `### ➕ Prática BR` (exercício no caso brasileiro; pode virar dois exercícios no dia, é a regra) e `### ➕ O notebook do dia` (o que o aluno faz nele).
6. Qualquer seção extra do original, traduzida, na posição original.
7. `## ✅ Checkpoint` — tradução fiel. Depois `### ➕ Checkpoint BR`.
8. `## ⚖️ ➕ Camada jurídica BR`
9. `## 🧠 ➕ Camada 8 — título`
10. `## 🤖 ➕ Skill do dia` — uma frase dizendo o que o dia propõe para a skill, apontando para `_skill-delta.md`.
11. `## 💡 ➕ Inovação OSINT do dia — título`
12. `## 📝 Diário de estudo` (campos em branco, como no Dia 01).
13. Rodapé de crédito (igual ao Dia 01).

Links relativos devem funcionar a partir da pasta do dia (o Dia 01 usa `../../../` para chegar à raiz).

## 4. Tradução

Rigor de tradutor técnico. Português do Brasil, frases diretas, sem enfeite. Comandos, flags, nomes de ferramentas, campos de log, IDs do ATT&CK e trechos de código ficam como estão; comentários dentro de blocos de código podem ser traduzidos. Termos em inglês sem tradução consagrada vão em itálico na primeira ocorrência.

Glossário fixo:

| Inglês | Português neste repo |
|---|---|
| finding | achado |
| artifact (do dia) | artefato |
| scope / out of scope | escopo / fora do escopo |
| confirmed / likely / disputed | confirmado / provável / contestado |
| confidence | confiança |
| pivot | pivô / pivotar |
| link analysis / link graph | análise de vínculos / grafo de vínculos |
| lure | isca |
| takedown | derrubada (*takedown*) |
| chain of custody / custody log | cadeia de custódia / registro de custódia |
| evidence handling | manuseio de evidência |
| sock puppet | perfil de fachada (*sock puppet*) |
| threat actor | ator de ameaça |
| intelligence brief | informe de inteligência |
| case file / case report | dossiê do caso / relatório do caso |
| engagement letter | carta de contratação |
| rules of engagement | regras de engajamento |
| timeline | linha do tempo |
| lookalike domain | domínio imitação |
| money mule | laranja (*money mule*) |
| scam / fraud | golpe / fraude |
| grooming | aliciamento |
| instructor key | gabarito do instrutor |
| checkpoint | checkpoint |
| capstone | capstone |

## 5. Notebook Colab

- **Só biblioteca padrão do Python.** Ferramenta de sistema (tshark, sleuthkit, jq) só via `!apt-get`/`!pip` numa célula marcada como opcional; o teste pula linhas com `!` e `%`, então o notebook precisa funcionar sem elas.
- **Código comentado linha a linha**, no tom do Dia 01: o comentário explica o porquê, não só o quê.
- **Interatividade obrigatória**: pelo menos um quiz/exercício com `input()` (com `MODO_JOGO = True/False`) ou formulário `#@param`.
- **Offline-first**: toda célula que acessa a rede (urllib para crt.sh, RDAP, arquivos raw do upstream no GitHub) fica em `try/except` com plano B (amostra embutida no próprio notebook). `google.colab` sempre dentro de `try/except ImportError`.
- **Estrutura**: abertura com a cena do caso → explicação → código → exercício → checkpoint → "amanhã".
- **Teste obrigatório**: `python scripts/testar_notebook.py <caminho>` precisa passar (✅). Gere o `.ipynb` com um script Python em pasta temporária (veja como o Dia 01 foi feito: JSON nbformat 4, células com `metadata.cellView = "form"` quando usar `#@param`).

## 6. Skill do dia (`_skill-delta.md`)

A skill em `skills/investigador-cyber/SKILL.md` cresce a cada dia, mas só com o que o dia ensinou. O delta é pequeno: um procedimento novo **ou** de 1 a 3 itens acrescentados a um procedimento existente. Formato:

```markdown
# Delta da skill — Dia NN

Tipo: procedimento novo | acréscimo a "<nome do procedimento existente>"
Linha do changelog: <uma linha para a tabela do CHANGELOG-DA-SKILL.md>

## Texto a inserir
<o texto exato, em passos numerados, no estilo da skill>

## Caso de teste
- Entrada: <pedido de usuário>
- Esperado: <comportamento correto>
```

Se o dia não acrescenta nada útil a um agente (ex.: montar o laboratório), escreva `Tipo: nenhum` e explique em uma linha.

## 7. A Operação Isca (bíblia do caso)

Tudo fictício. Domínios só em `.example`; IPs só nas faixas de documentação `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` (internos: RFC 1918); telefones no formato inexistente `+55 00 00000-00NN`; CPFs e chaves Pix sempre marcados como fictícios. Nenhuma pessoa, empresa ou caso real.

**Elenco fixo**
- **Você**: analista de investigação júnior da **Vigia** (MSSP fictício de Belo Horizonte).
- **Rafa**: analista sênior da Vigia, mentor; faz as perguntas incômodas.
- **Marta Quintão**: gerente de risco da **Cooperativa Serra Azul** (cooperativa de crédito do interior de Minas, 40 mil cooperados, site real dela: `serraazul.example`). Assinou a autorização.
- **Dr. Hélio Brandão**: jurídico da cooperativa; aparece quando o tema encosta em LGPD, Marco Civil ou provas.
- **"Pescador"**: apelido do operador desconhecido, achado num comentário do código do kit. Nunca é "identificado" pela Vigia; atribuição de pessoa é trabalho da polícia.

**Fatos fixos**
- Início do caso: segunda-feira, 5/out/2026. SMS disparados entre 07h12 e 08h40 (BRT, UTC-3). Contrato assinado às 11h00; caso entregue a você às 11h05.
- SMS: *"Serra Azul: sua chave Pix foi bloqueada por segurança. Regularize em serraazul-pix.example"*, também via encurtador `lnk.example/sa7`. Remetentes `+55 00 00000-0001` a `-0004`.
- Site falso: `serraazul-pix.example`, hospedado em `203.0.113.77`; certificado TLS gratuito emitido no dia anterior ao disparo; kit apelidado internamente de **IscaKit**. Outros domínios imitação aparecem ao longo do caso: `serraazul-seguranca.example`, `coopserra-azul.example`.
- 37 reclamações nas duas primeiras horas; 3 cooperados com transferências Pix não reconhecidas.

**Arcos por fase**
| Fase | Dias | Arco |
|---|---|---|
| 1 | 1–18 | Recebimento do caso, autorização, primeiras leituras de rede, DNS, HTTP e TLS do site falso; logs de acesso que a cooperativa entrega; montagem do laboratório. |
| 2 | 19–34 | Ciclo OSINT completo sobre a infraestrutura; perfis falsos `@serraazul.oficial` (Instagram) e "Serra Azul Atendimento" (WhatsApp Business); metadados de um PDF "comunicado" que circula nos grupos; questões de perfil de fachada, OPSEC e LGPD. |
| 3 | 35–48 | O IscaKit reaparece contra outras 4 cooperativas fictícias (`coopvale.example`, `credminas.example`, `unicoop-sul.example`, `cooperouro.example`); mapeamento no ATT&CK; perfil do "Pescador" como **cluster de atividade**, nunca como pessoa; STIX/TLP; informe; atribuição cautelosa. |
| 4 | 49–64 | Uma caixa da agência Centro abriu o link no notebook corporativo `SA-CX-07` (10.20.40.57). Disco, memória, logs e rede. O caso LAB-P4 do original continua sendo o laboratório principal; o Isca dá o paralelo brasileiro. |
| 5 | 65–76 | As contas que receberam os Pix revelam uma rede de laranjas (identificadas só por códigos L-01, L-02...); grafo da quadrilha; golpe de falsa central por voz; texto de isca gerado por IA; entrevista com um cooperado vítima fictício ("Seu Antônio", 71 anos) sem revitimização; comunicação às autoridades brasileiras. |
| 6 | 77–82 | O chatbot de atendimento da cooperativa ("Lia", na nuvem) foi usado com prompt injection para confirmar dados de cooperados; logs de nuvem, IAM, grafo de acesso, exfiltração. O caso Blue Harbor do original segue como laboratório principal. |
| 7 | 83–90 | O capstone do original (case packet) **e** o fechamento do Isca: grafo final, linha do tempo, relatório com confiança calibrada para a Marta, pacote para a delegacia especializada, portfólio. |

Cada agente/autor mantém os fatos fixos e pode criar detalhes novos dentro do seu arco, sem contradizer o que já foi publicado.

## 8. Camada jurídica BR

Cite só o que tem certeza. Parafraseie; não transcreva artigos longos. Referências seguras e recorrentes: CP arts. 154-A (invasão de dispositivo, redação da Lei 14.155/2021), 147-A (perseguição), 171 (estelionato) e 171 §2º-A (fraude eletrônica, Lei 14.155/2021), 307 (falsa identidade); Lei 12.737/2012; LGPD (Lei 13.709/2018); Marco Civil (Lei 12.965/2014), arts. 10, 13, 15, 19, 22; CPP arts. 158-A a 158-F (cadeia de custódia, Lei 13.964/2019); Lei 9.613/1998 (lavagem de dinheiro); Lei 12.850/2013 (organização criminosa); ECA arts. 240 a 241-E. Se não tiver certeza de um número de artigo, não invente: deixe `<!-- TODO jurídico: confirmar ... -->`. Sempre termine a seção com a nota "material de estudo, não constitui orientação jurídica" quando der parecer sobre um caso.

## 9. Camada 8

O fator humano do tema do dia: viés cognitivo do investigador, psicologia da vítima ou engenharia social do golpista. Conceitos reais da psicologia (ex.: viés de confirmação, ancoragem, desengajamento moral de Bandura, princípios de influência de Cialdini, carga cognitiva, revitimização). Cite o autor só quando tiver certeza. Termine com uma consequência prática para o trabalho do analista.

## 10. Inovação OSINT do dia

Uma técnica, fonte ou recurso real e verificável ligado ao tema, de preferência com um trecho curto de Python **stdlib**. Bibliotecas externas só se forem conhecidas e reais (e marcadas como opcionais). Nunca invente ferramenta, API ou endpoint.

## 11. Limites de conteúdo

- Ética do original vale sempre: padrões, não pessoas; nada de dossiê de indivíduo real.
- **Dia 70 (aliciamento e tráfico)**: fique no nível de padrão, como o original. Nada de listas de frases literais de aliciadores nem roteiros; nenhum conteúdo envolvendo menores além do que o original já traz em nível de indicador. Canais: SaferNet Brasil, Disque 100, 190.
- Dark web e sites de vazamento (Dias 41–42): nenhum endereço `.onion` real, nenhum link para site de vazamento real.
- Arquivos suspeitos (Dias 61–62): só amostras inofensivas (EICAR, arquivos sintéticos); nada de malware vivo.
- Prompt injection (Dia 81): enquadramento defensivo e investigativo.
- Gabaritos de instrutor (`INSTRUCTOR-KEY.md`, `07-instructor-key.md`) não são resumidos nem revelados no README do dia; apenas mencione que existem, como o original faz.
