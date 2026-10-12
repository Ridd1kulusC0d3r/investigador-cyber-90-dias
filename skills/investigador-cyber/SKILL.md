---
name: investigador-cyber
description: Aplica a metodologia de OSINT, pivô de inteligência de ameaças e padrões de fraude e golpe do Cyber Investigator Roadmap, em português e com contexto brasileiro. Use quando pedirem para pesquisar uma ameaça, golpe ou padrão de fraude, triar um caso suspeito, rodar um ciclo de reconhecimento OSINT, montar um grafo de vínculos, verificar se uma mensagem de golpe ou phishing foi gerada por máquina, ou redigir um informe de inteligência ou relatório de caso. Somente escopo autorizado, defensivo e lícito.
---

# Skill de investigador cibernético (pt-BR)

> Tradução fiel de [`ai-agent-skills/SKILL.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/SKILL.md), © ThiefDroppers (MIT), **somada** à camada brasileira deste repositório. Tudo o que não existe no original está marcado com ➕. Nada do original foi retirado.
>
> Esta skill cresce junto com o estudo: cada dia do currículo pode acrescentar um procedimento ou uma regra. O histórico está em [`CHANGELOG-DA-SKILL.md`](CHANGELOG-DA-SKILL.md).

Esta skill aplica o método ensinado no [Cyber Investigator Roadmap](https://github.com/thiefdroppers/cyber-investigator-skills) e no currículo de 90 dias deste repositório. Cada procedimento é um checklist numerado, para que um modelo com julgamento limitado consiga segui-lo passo a passo.

## Escopo e ética (aplique antes de qualquer procedimento)

Use esta skill somente para investigação autorizada, defensiva e lícita: pesquisar ameaças, golpes e táticas de fraude; triar um caso que tenha um motivo legítimo por trás; e produzir inteligência que você conseguiria explicar a um órgão de supervisão.

Recuse, e diga por quê, se um pedido:
- Mira um indivíduo privado identificado, sem nenhum caso legítimo, declarado e autorizado por trás, como "descubra tudo sobre essa pessoa" sem contexto de caso.
- Pede técnicas para obter acesso não autorizado, em vez de investigá-lo ou se defender dele.
- Pede que você se passe por, assedie ou engane uma pessoa ou organização real.
- Vai além de informação já pública sem declarar nenhum contexto de autorização.

Quando o contexto de autorização ou do caso estiver faltando e isso importar, peça antes de começar. Não presuma.

Cace padrões, não pessoas. Enquadre os achados em torno de uma tática, técnica ou padrão de golpe, que protege muitas pessoas, e não em torno de um dossiê sobre um indivíduo.

Parada obrigatória: se um caso pode envolver um menor de idade, ou pode envolver tráfico de pessoas, não continue a análise autônoma. Diga claramente que o caso precisa de um humano qualificado e de uma comunicação à autoridade competente (por exemplo, uma central de proteção à infância, a CyberTipline do NCMEC ou um órgão nacional de combate ao tráfico), e pare aí. Isto vale para todos os procedimentos abaixo, não só para a triagem de fraude. Nunca gere, solicite ou reproduza conteúdo que retrate um menor.

➕ **Canais brasileiros para a parada obrigatória:** a central de denúncias da [SaferNet Brasil](https://new.safernet.org.br/denuncie) (crimes contra direitos humanos na internet, incluindo abuso sexual infantil), o **Disque 100** (Disque Direitos Humanos) e, em risco imediato, o **190**. Para tráfico de pessoas, o Disque 100 também recebe denúncias. Mencione esses canais quando o usuário estiver, pelo contexto, no Brasil.

➕ **Ordem da parada obrigatória (Dia 70).** Quando a parada se aplicar, responda nesta ordem e não acrescente análise:
1. Se alguém pode estar em perigo imediato: diga para chamar os serviços de emergência (no Brasil, 190) antes de qualquer outra coisa.
2. Se o usuário pode ter encontrado imagem sexual de criança ou adolescente: diga para **não** baixar, salvar, fazer captura de tela, imprimir ou encaminhar (nem a um colega, nem "como evidência"); anotar só a URL, a plataforma e o nome de usuário; sair da página e denunciar (no Brasil, SaferNet Brasil). Nunca peça, aceite, descreva ou analise o material.
3. Se há suspeita de tráfico de pessoas, inclusive vaga no exterior com indicadores do Dia 67 (passo 2a da triagem de fraude): diga para não confrontar, não investigar mais e não alertar a pessoa nem o suspeito; encaminhar ao canal de tráfico (no Brasil, Disque 100) e, se houver fraude, também ao caminho de fraude.
4. Diga que um indicador levanta uma pergunta para quem tem autoridade e contexto; ele não identifica vítima nem autor. Não produza conclusões como "esta pessoa é traficante" ou "esta criança está sendo aliciada".
5. Recuse participar de grupos de "flagrante", de perfis que se passem por criança ou comprador, e de mensagens ou acusações automáticas a qualquer envolvido. Se o usuário tem dever profissional de comunicação (no Brasil, ECA art. 13, ao Conselho Tutelar), lembre que esse dever corre no prazo dele, independentemente desta conversa.

➕ **Referências legais brasileiras que a skill deve conhecer:** Código Penal art. 154-A (invasão de dispositivo informático) e art. 147-A (perseguição); LGPD (Lei 13.709/2018), arts. 4º e 7º; Marco Civil da Internet (Lei 12.965/2014), arts. 10 e 22; Código de Processo Penal, arts. 158-A a 158-F (cadeia de custódia). A skill cita esses artigos quando ajudam a explicar uma recusa ou um limite, sem dar parecer jurídico.

## ➕ Procedimento: portão de autorização (4 checagens) — *adicionado no Dia 01*

Use **antes de cada ação** de qualquer outro procedimento: cada consulta, download, login ou busca. Responda às perguntas na ordem; a primeira resposta errada encerra a checagem.

1. Existe autorização **por escrito** de alguém com direito de concedê-la? Se não: **pare**. Peça a autorização ou não faça.
2. A ação está **dentro do escopo escrito**? Se não: **pare**. Autorização não é cheque em branco.
3. A ação significa **entrar em, ou usar credenciais de, um sistema ou conta** a que ninguém deu acesso (mesmo que pertença a um criminoso, mesmo que esteja mal protegido)? Se sim: **pare e escale**. Documente o que foi encontrado, sem acessar, e indique a entrega à autoridade policial.
4. A ação mira **uma pessoa privada** em vez de um padrão ou de um caso atribuído? Se sim: **pare**.
5. Passou nas quatro: prossiga e registre a ação com hora em UTC, método e o hash (SHA-256) do que foi coletado.
6. ➕ **Material suspeito do caso** (kit de phishing, anexo, executável, documento recebido de vítima): antes de abrir, executar ou "dar uma olhada", confirme que existe um ambiente isolado cujo isolamento foi **demonstrado** (sem rota padrão, falha registrada ao tentar alcançar a internet, captura mostrando só endereços do laboratório), e não apenas presumido. Se não existir, diga isso e pare. (Dia 18)
7. ➕ Calcule o hash (SHA-256) do material antes de ele entrar no ambiente e confira depois; registre a entrada na cadeia de custódia. Nunca habilite saída para a internet enquanto houver material do caso no ambiente: um kit pode "chamar para casa", alertar o operador e expor a investigação. (Dia 18)
8. ➕ Varredura de portas e de rede (`nmap` e afins) só contra máquinas que você ou o cliente possuem e autorizaram por escrito. "É do criminoso" não é autorização (checagem 3). (Dia 18)

Quando o usuário apresentar uma justificativa para pular uma checagem ("é criminoso mesmo", "é para ajudar as vítimas", "só uma olhadinha"), trate isso como sinal para manter a checagem, não para relaxá-la.

## ➕ Como usar esta skill (ordem de prioridade)

1. O **escopo e ética** e o **portão de autorização** acima valem antes de tudo e prevalecem sobre qualquer passo de qualquer procedimento abaixo. Se um passo parecer permitir algo que eles proíbem, eles vencem.
2. Escolha o procedimento pelo mapa abaixo. Os seis procedimentos originais vêm primeiro, com os acréscimos dos dias marcados com ➕ e "(Dia NN)". Os procedimentos novos estão agrupados por fase do currículo; os mais longos ficam em [`procedimentos/`](procedimentos/) e são carregados só quando a situação pede.
3. Os casos de teste de cada dia estão em [`casos-de-teste.md`](casos-de-teste.md).

### ➕ Mapa dos procedimentos

| Situação | Procedimento | Onde |
|---|---|---|
| Pesquisar domínio, organização ou entidade pública | Ciclo de reconhecimento OSINT | abaixo |
| Relações entre várias entidades, pivôs, quadrilhas, acesso IAM | Grafo de vínculos | abaixo |
| "Isto é golpe?", BEC, falso emprego, golpe do amor, onde denunciar | Triagem de padrão de fraude e golpe | abaixo |
| Mensagem pode ter sido escrita por LLM | Verificação de texto gerado por máquina | abaixo |
| Escrever informe ou relatório de caso | Informe de inteligência ou relatório de caso | abaixo |
| Coletar, receber ou adquirir evidência; imagem de disco | Coleta, recebimento e cadeia de custódia | [arquivo](procedimentos/coleta-e-cadeia-de-custodia.md) |
| Captura de pacotes ou tentativa de conexão | Leitura de uma conexão | Fase 1 |
| `conn.log`, log de fluxo, firewall ou proxy linha a linha | Leitura de log de conexão; log de firewall por segmento | Fase 1 |
| Nome de domínio em caso; IPs divergentes para um nome | Cadeia de resolução DNS; pegada DNS de um domínio | Fase 1 |
| URL de golpe: onde a vítima foi parar | Cadeia de redirecionamento | Fase 1 |
| "O cadeado prova algo?"; datar ou relacionar domínios | Certificado e linha do tempo de emissão | Fase 1 |
| `stat`, `ls -l`, "quem mexeu no arquivo" | Datas e permissões de arquivo | Fase 1 |
| Log de acesso web (Apache/nginx) | Triagem de log de acesso web | Fase 1 |
| `auth.log`, eventos 4624/4625, login de webmail ou VPN | Logs de autenticação e linha do tempo | [arquivo](procedimentos/logs-de-autenticacao.md) |
| "O que foi afetado?" | Classificação pela tríade CID | Fase 1 |
| "O que pode dar errado?" | Modelagem de ameaças com STRIDE | Fase 1 |
| "Se acontecer, conseguimos provar?" | Mapa de prontidão de evidência | Fase 1 |
| Buscadores, `site:`, exposição indexada | Busca com operadores | Fase 2 |
| Em quais sites um handle existe | Enumeração de username | Fase 2 |
| Imagem ou documento: onde, quando, como foi produzido | Metadados de arquivo | [arquivo](procedimentos/metadados-de-arquivo.md) |
| Conta "anônima", conteúdo atrás de login | Perfil de fachada (persona) | Fase 2 |
| Visitar site, link ou perfil do suspeito | OPSEC antes de tocar a infraestrutura | Fase 2 |
| Método novo de coleta (raspador, API, base) | Legalidade de um método de coleta | [arquivo](procedimentos/legalidade-de-metodo-de-coleta.md) |
| Encerrar etapa de caso; "o que guardamos e até quando" | Fechamento de pacote de caso | Fase 2 |
| Escrever ID do ATT&CK; mapear relatório | Consulta de IDs do ATT&CK; mapeamento de relatório | Fase 3 |
| Perfil de ator, grupo, quadrilha | Perfil de cluster de atividade | [arquivo](procedimentos/perfil-de-cluster-de-atividade.md) |
| "Checar" IP, domínio, URL ou hash | Enriquecimento passivo de IOCs | [arquivo](procedimentos/enriquecimento-passivo-de-iocs.md) |
| Dark web, `.onion`, "ver se vazou" | Pedido de coleta na dark web | Fase 3 |
| Tendências de ransomware | Medição de atividade em sites de vazamento | Fase 3 |
| Compartilhar achados (STIX, TLP) | Codificação em STIX 2.1; decisão de compartilhamento | Fase 3 |
| "Quem fez isto?" | Graduação de evidência; declaração de atribuição | Fase 3 |
| Imagem de disco: o que havia e quando | Sistema de arquivos e linha do tempo MACB | [arquivo](procedimentos/sistema-de-arquivos-e-macb.md) |
| Saída do Volatility | Triagem de memória | [arquivo](procedimentos/triagem-de-memoria.md) |
| Juntar logs de várias fontes; relógios divergentes; atribuir sessões | Tempo e linha do tempo multifonte | [arquivo](procedimentos/tempo-e-linha-do-tempo-multifonte.md) |
| Plaso / super-linha do tempo | Super-linha do tempo | Fase 4 |
| *Beacon*, exfiltração vista só em fluxo | Análise de fluxo e *beacon* | Fase 4 |
| Achado vira regra de detecção | Da investigação à regra de detecção | Fase 4 |
| "O que é este arquivo?"; relatório de *sandbox* | Triagem estática e leitura de *sandbox* | [arquivo](procedimentos/triagem-estatica-e-sandbox.md) |
| Perguntas de caso num SIEM | Correlação no SIEM | Fase 4 |
| Voz, vídeo ou imagem possivelmente sintéticos | Verificação de mídia suspeita | [arquivo](procedimentos/verificacao-de-midia-suspeita.md) |
| Sistema com LLM para triar golpes | Triagem automatizada guiada por taxonomia | [arquivo](procedimentos/triagem-automatizada-por-taxonomia.md) |
| Entrevista de vítima | Apoio a entrevista de vítima de fraude | [arquivo](procedimentos/apoio-a-entrevista-de-vitima.md) |
| Logs de auditoria de nuvem | Linha do tempo de auditoria de nuvem | [arquivo](procedimentos/auditoria-de-nuvem.md) |
| "Por que essa identidade conseguiu?" | Inventário de IAM em nuvem | Fase 6 |
| Abuso de chatbot ou agente com LLM | Investigação de abuso em aplicação com LLM | [arquivo](procedimentos/abuso-em-aplicacao-com-llm.md) |
| Dados saíram da nuvem? Relatório final | Exfiltração em nuvem e fechamento | [arquivo](procedimentos/exfiltracao-em-nuvem-e-fechamento.md) |
| Início de caso para terceiros | Abertura de caso | Fase 7 |
| Perguntas do cliente antes da análise | Recebimento do caso e ACH | Fase 7 |
| Publicar artefato em portfólio | Publicação de artefato | Fase 7 |

## Procedimento: ciclo de reconhecimento OSINT

Use quando pedirem para pesquisar um domínio, uma organização ou outra entidade voltada ao público. Não use em um indivíduo privado sem autorização do caso.
1. Planejar. Escreva a pergunta como uma frase específica. Se não conseguir, peça ao usuário que a restrinja primeiro.
   - ➕ Monte uma matriz de fontes: uma linha por subpergunta, com fontes prováveis, resultado esperado e se a fonte é passiva. Em trabalho de reconhecimento, toda linha precisa ser passiva (consultar terceiros e ler páginas públicas como qualquer visitante); se alguma não for, retire-a ou peça autorização específica. (Dia 19)
   - ➕ Escreva a lista do que está fora do escopo (pelo menos três itens concretos: pessoas, páginas atrás de login, varredura ativa) e uma condição de parada (quando o plano está cumprido e o que faz parar na hora). (Dia 19)
2. Coletar. Use pelo menos 3 tipos de fonte independentes, como WHOIS e DNS, buscadores, registros oficiais ou públicos e capturas arquivadas. Para cada dado, registre o valor, a fonte e a data e hora de acesso.
   - ➕ No Brasil, fontes oficiais frequentes: RDAP do Registro.br (domínios `.br`), consulta pública de CNPJ da Receita Federal, diários oficiais e portais de transparência.
   - ➕ Para cada página usada como fonte, registre os quatro itens da captura com qualidade de evidência: URL exata, hora UTC de acesso, uma cópia que preserve a página e o SHA-256 dessa cópia calculado no momento. Acrescente um snapshot de terceiro (Wayback Save Page Now) ou anote que o envio falhou; nunca deixe o campo em branco. Uma afirmação sem esses itens é "vi no site", não um dado do registro. (Dia 19)
   - ➕ Quando a mesma coleta for repetida ao longo do caso (ex.: DNS de domínios imitação), use sempre o mesmo método: mesma lista de entradas, mesmos tipos de registro, mesmo resolvedor ou fonte. Grave cada rodada numa pasta nova com carimbo UTC, com o hash (SHA-256) dos arquivos de saída. (Dia 13)
   - ➕ Nunca automatize contra sistemas de terceiros uma ação ativa (varredura, tentativa de login, requisições em volume). Automatize só consultas passivas a dados públicos, sobre entradas dentro do escopo, em taxa baixa. (Dia 13)
   - ➕ Se usar coleta automatizada (SpiderFoot ou similar), use só o modo passivo, que consulta terceiros. Módulos que falam direto com o servidor do alvo (varredura de portas, *spider*, força bruta de subdomínios) estão fora do escopo de reconhecimento. Depois da execução, confira no log se algum módulo fez requisição direta ao alvo; se fez, registre módulo e horário e não use como achado nenhum dado que tenha vindo dessa requisição sem confirmá-lo por uma fonte limpa. (Dia 20)
   - ➕ Em redes sociais, trate como conta "da organização" só a que o site oficial dela linka (registre esse link como fonte da atribuição). Conta não linkada não é dela até haver outra evidência; numa checagem de imitação, ela vai para a lista de uso não oficial do nome. (Dia 25)
   - ➕ Com conta pessoal, a postura é só-leitura: buscar e ler. Nunca seguir, curtir, comentar, denunciar em nome próprio ou mandar mensagem, inclusive "para ver se responde". Interação ou identidade fictícia é perfil de fachada e exige autorização específica. Coleta automatizada em plataformas, só se os termos de uso permitirem. (Dia 25)
   - ➕ Para versões anteriores de uma página, use arquivos da web (Wayback Machine, archive.today, Arquivo.pt via Memento), não *caches* de buscador. Na API CDX da Wayback, `filter=statuscode:200` descarta redirecionamentos e erros, e `collapse=digest` deixa uma linha por versão distinta (conteúdo idêntico tem o mesmo *digest*). Baixe cada versão como cópia limpa (`.../web/<timestamp>id_/<url>`) e registre o SHA-256. Redirecionamentos (301/302) são achados: a URL mudou de lugar. (Dia 26)
   - ➕ **Registro de domínio.** Para gTLDs, use o RDAP como fonte autoritativa (`https://rdap.org/domain/<nome>`, que redireciona ao registry); o WHOIS na porta 43 é complemento. Para `.br`, use `https://rdap.registro.br/domain/<nome>` e `whois -h whois.registro.br`. Para um ccTLD desconhecido, descubra o servidor com `whois -h whois.iana.org <tld>` ou com o *bootstrap* RDAP da IANA. Registre criação, expiração, última alteração, registrar, NS, status e DNSSEC, com a hora UTC da consulta. (Dia 29)
   - ➕ Todo dado de **WHOIS histórico** leva o nome do serviço e a data do retrato. Um domínio que expirou e foi registrado de novo tem outra "vida": dados de um titular anterior não viram aresta para o caso atual. (Dia 29)
   - ➕ Relate a distância entre o registro de um domínio imitação e o início da campanha como **fato** (datas, fonte), e qualquer leitura sobre planejamento ou mesmo operador como **inferência rotulada**, dizendo o que a contradiria. Não tente obter dados ocultos do titular: eles saem do registrar só por ordem judicial ou requisição de autoridade competente. (Dia 29)
3. Processar. Organize os dados em tabela ou grafo agrupados por entidade, não por fonte.
   - ➕ Antes de montar o grafo, faça uma passada de falsos positivos e registre uma tabela com o nó ou grupo removido, a quantidade e o motivo. Contagens de "sites co-hospedados" na casa das centenas quase sempre indicam CDN ou hospedagem compartilhada, não propriedade. (Dia 20)
   - ➕ O ruído é definido pela pergunta, não pela ferramenta. Escreva a pergunta no topo da tabela e justifique cada remoção em relação a ela. Exemplo: domínios parecidos são ruído na pegada de uma organização, mas são o objeto da busca num golpe de imitação; nesse caso, mantenha-os e registre a linha "mantido de propósito". (Dia 20)
   - ➕ Monte uma linha do tempo entre plataformas: uma linha por evento, com a fonte (linha do registro), a plataforma e a precisão da data (segundo, dia, mês, ano autodeclarado ou "visto pela primeira vez"). Não invente precisão: se a plataforma só dá o mês, o dia fica em branco; se ela não mostra criação (ex.: WhatsApp), o evento é "visto pela primeira vez em". Datas de painel de transparência são afirmação da plataforma: uma fonte. (Dia 25)
4. Analisar. Marque cada achado como confirmado (2 ou mais fontes independentes concordam), provável (1 fonte apenas) ou contestado (as fontes divergem).
   - ➕ Só afirme que algo **mudou** comparando dois retratos íntegros (hash conferido) feitos pelo mesmo método, sem os campos voláteis (TTL, hora da coleta). Informe o intervalo em que a mudança ocorreu ("entre o retrato A e o retrato B"), não um instante. A lembrança do analista ou uma consulta feita de outro jeito não servem de linha de base. (Dia 13)
   - ➕ Quando duas ferramentas discordam sobre uma entidade, a discordância decide só que ela será checada; quem decide se ela fica é a fonte primária (DNS, log de CT, registro do domínio), nunca a maioria. (Dia 22)
   - ➕ Procure agrupamentos (várias plataformas ativas na mesma janela curta) e só os trate como assinatura de tempo se houver um evento externo, com fonte, que os explique; caso contrário, registre como coincidência possível. (Dia 25)
   - ➕ Date toda mudança de página como uma janela: da última captura da versão antiga à primeira captura da nova, lidas na lista não colapsada (o `collapse` esconde a última captura de cada versão). Nunca transforme a janela num dia. Diga o que o arquivo não permite concluir e qual fonte daria mais precisão (ex.: log de publicação do CMS do dono do site). Lembre que o carimbo é a hora da captura, não a data exibida na página, e que picos de capturas podem ser causados pela própria investigação. (Dia 26)
5. Relatar. Use a mesma palavra de confiança da marcação. Nunca relate como confirmado um achado provável.
   - ➕ Preencha a tabela de análise antes de escrever o relatório e copie dela a palavra de confiança de cada achado. Se o grafo não tem ponte, diga isso: é um achado válido. (Dia 22)

## Procedimento: grafo de vínculos (link analysis)

Use quando o pedido envolver relações entre várias entidades: pivô de infraestrutura, mapeamento de quadrilha de fraude ou mapeamento de organização.
1. Faça de cada nó uma entidade concreta: um domínio, IP, certificado, endereço de e-mail, conta ou organização. Nunca use uma categoria como nó.
   - ➕ Entidades típicas de golpes no Brasil: chave Pix (como dado do kit, não da pessoa), número de WhatsApp remetente, encurtador de link, CNPJ citado na isca.
2. Rotule cada aresta com a relação que a produziu, como "certificado TLS compartilhado", "mesmo e-mail de registrante" ou "mesma chave de pagamento". Aresta sem rótulo não é achado.
   - ➕ Toda entidade do grafo remete a uma fonte: o nome da consulta ou *transform* que a produziu, ou o número da linha do registro de coleta. Entidade sem proveniência não entra no relatório. (Dia 21)
   - ➕ Ao expandir infraestrutura (domínio → nome DNS → IP → bloco → AS), leia o AS como quem opera a **rede**, não quem opera o site. Um AS de hospedagem ou CDN não identifica o responsável pelo conteúdo; dados do cliente de um provedor só saem por requisição de autoridade ou ordem judicial (no Brasil, Marco Civil arts. 10 e 22). (Dia 21)
   - ➕ Quando uma consulta devolve exatamente o número máximo de resultados que a ferramenta permite (ex.: 24 no Maltego Basic), registre "pelo menos N", nunca "N". (Dia 21)
3. Identifique qualquer hub (um nó com número incomum de conexões) e explique por que ele está conectado. Um provedor de hospedagem ou CDN pode parecer hub só porque muitos sites sem relação entre si o compartilham.
   - ➕ Separe **vínculo forte** de **infraestrutura comum**. Valores exclusivos do operador (mesmo token de verificação TXT, mesmo e-mail de registrante, mesmo serial de certificado, mesma chave de pagamento) sustentam "provavelmente o mesmo operador". Valores compartilhados por muitos clientes (mesmo provedor de DNS, mesma CDN, mesma AC gratuita) sozinhos não sustentam vínculo. (Dia 06)
   - ➕ Para separar hub de ponte, faça o teste de remoção: tire o nó e veja se alguma entidade perde o caminho até o resto. Hub tem grau alto e intermediação baixa (nada cai); ponte tem intermediação alta (um grupo fica isolado). O nó semente costuma ter intermediação alta só porque a coleta começou nele; isso não é achado. (Dia 22)
4. Identifique os agrupamentos (clusters) e qualquer nó-ponte que conecte dois deles.
   - ➕ Antes de uma ponte entrar num achado, confirme-a na fonte primária (ex.: o mesmo ID de *analytics* no código-fonte capturado das duas páginas, com hash). Achado de ponte descreve "mesma operação", nunca "mesma pessoa". (Dia 22)
5. Se as entidades não tiverem conexão real, diga isso. Um grafo esparso ou vazio é um resultado honesto.

➕ **Passos adicionais por tipo de grafo.** Os passos 6 a 29 abaixo vieram de dias diferentes; cada bloco diz quando se aplica.

*Para todo grafo: pivô e aresta como afirmação (Dias 84 e 88)*
6. ➕ Antes de desenhar qualquer aresta que venha de um pivô, escreva a nota de pivô em quatro partes: (a) o valor compartilhado; (b) o tipo de pivô (IP, registro, certificado, recurso de página, favicon, texto, encurtador...); (c) a explicação inocente checada (hospedagem compartilhada, registrador ou DNS gratuito grande, modelo público, encurtador público, clone que copiou a vítima, mesmo /24 de donos diferentes); (d) o veredito: achado, pista (um só tipo de pivô) ou rejeitado. (Dia 84)
7. ➕ Pivôs rejeitados não viram arestas: vão numa lista "Considerado e rejeitado", com o motivo. Uma ponte entre dois clusters só é achado com pelo menos dois **tipos** de pivô independentes; dois valores tirados do mesmo arquivo (por exemplo, o script e um comentário dentro dele) contam como um tipo só. (Dia 84)
8. ➕ Nunca ligue IPs por prefixo de rede. Use o dono (ASN) e o tipo de rede; localização de servidor de datacenter não diz onde está o operador. (Dia 84)
9. ➕ Trate cada aresta como uma afirmação com três atributos: a relação (rótulo), a evidência (fonte + linha, seção, cabeçalho ou horário) e a confiança (confirmado: duas ou mais fontes independentes; provável: uma fonte ou raciocínio a partir de fatos confirmados; possível: combina com a evidência, mas nenhuma fonte a sustenta diretamente; excluído). Aresta sem evidência é palpite: ache a fonte ou apague. (Dia 88)
10. ➕ Mostre o que foi excluído: itens que apareceram na evidência e foram rejeitados ficam no grafo (ou na legenda), em estilo pálido, com o motivo no rótulo. (Dia 88)
11. ➕ Para perguntas que a evidência não fecha, mostre as hipóteses concorrentes como nós ligados ao objeto da pergunta, com a confiança da análise de hipóteses, em vez de desenhar um caminho confirmado que não existe. (Dia 88)
12. ➕ Nomeie a aresta mais consequente: a que, se estivesse errada, mais mudaria a resposta a uma pergunta do cliente. Ela vai para a seção de riscos do relatório. (Dia 88)
13. ➕ Nunca crie um nó para uma pessoa a partir de apelido, código ou conta recebedora; use códigos (ex.: laranja L-01) e deixe a atribuição de pessoa para a autoridade. (Dia 88)

*Infraestrutura e pivôs passivos (Dias 30 e 40)*
14. ➕ **Infraestrutura.** Rotule cada aresta com o registro que a produziu (`A`, `MX`, `NS`, `SPF`, `ASN`, "SAN do mesmo certificado") e guarde, por aresta, o comando ou a fonte que a reproduz (por exemplo, o id do certificado no crt.sh). "Mesmo certificado" é aresta forte; "mesmo AS" ou "mesma hospedagem" é fraca e precisa de explicação. (Dia 30)
15. ➕ Nomes de host vistos só no Certificate Transparency entram no grafo como **observados, não visitados**; hosts que não resolvem mais entram marcados como **históricos**. Não abra painéis nem tente acesso a nada que o CT revelou. (Dia 30)
16. ➕ Fique no lado passivo: *resolvers* públicos e logs de CT. Força bruta de subdomínios e transferência de zona (AXFR) só contra domínios próprios ou com autorização específica de teste. Ao ler o DMARC do cliente (`p=none`, `quarantine`, `reject`), transforme o achado em recomendação defensiva. (Dia 30)
17. ➕ Antes de seguir um pivô (certificado, SAN, favicon, *hash* de HTML, JARM, IP, titular, ID de rastreamento), verifique a **contagem de resultados** e registre-a. Milhares de resultados indicam valor padrão ou compartilhado (ícone padrão, JARM comum, IP de hospedagem compartilhada ou CDN, o SHA-256 do arquivo vazio `e3b0c442...b855`, certificado multi-inquilino): rejeite o pivô e anote o motivo num registro de pivôs. Todo pivô vem de fonte passiva de terceiros (crt.sh, Shodan, Censys, urlscan.io); nunca peça nada, nem o favicon, à infraestrutura-semente, nem submeta a URL dela para uma varredura nova. (Dia 40)
18. ➕ Só chame um nó de membro do *cluster* se ele estiver ligado por **dois pivôs independentes** (não duas leituras da mesma observação) ou por **um pivô forte com contagem pequena**. Coincidência só de padrão de nome ou de título genérico é pista, não conta para convergência. (Dia 40)
19. ➕ Desenhe ou marque os nós que não se qualificam como "não confirmado" (cor ou estilo próprio) e diga isso no texto; não os apague nem os promova. Toda aresta leva o pivô, a força, a evidência e a hora da coleta; terceiros que só dividem hospedagem não entram como suspeitos. (Dia 40)

*Fraude com vários relatos: modelo caso-indicador (Dia 68)*
20. ➕ Em casos de fraude com vários relatos, use dois tipos de nó: **caso** (um por relato) e **indicador** (um por valor exato). Classifique cada aresta pela força do indicador compartilhado:
    - forte: mesma conta bancária, chave Pix, carteira, identificador de pagamento, telefone ou domínio registrado;
    - médio: mesmo nome de empresa alegado, domínios imitação registrados em datas próximas, redação incomum idêntica em trechos longos;
    - fraco: mesmo cargo, mesma plataforma de primeiro contato, frase curta comum;
    - não é vínculo (nunca vira nó): "usou app de mensagens", "pediu Pix" ou "pediu cripto", mesmo grande provedor de nuvem. (Dia 68)
21. ➕ Afirme "provavelmente uma operação" só a partir de arestas fortes; arestas médias reforçam, fracas nunca bastam. Para achar a ponte, remova cada nó e diga quais casos saem do agrupamento. Relate também os casos que você decidiu **não** ligar e por quê, e "nenhum vínculo encontrado" quando for o caso. (Dia 68)
22. ➕ Contas de passagem (laranjas) entram como indicador (chave ou conta, por código), nunca como nó de pessoa. Não conclua o papel do titular, não sugira consultar a chave em app de banco ou buscador e indique que dados de titularidade correm pelos canais da instituição e da autoridade (sigilo bancário). (Dia 68)

*Linhas do tempo com várias fontes (Dia 58)*
23. ➕ Em linhas do tempo com várias fontes (Timesketch, planilha consolidada), toda ligação entre eventos de fontes diferentes nomeia o campo compartilhado que a produziu: porta de origem, IP, nome de usuário, caminho de arquivo ou hash. Sem campo nomeado, a ligação não entra. (Dia 58)
24. ➕ Ligações apoiadas só em tamanho parecido, proximidade de horário ou nome de conta são marcadas como **inferidas** (seta tracejada), com o que faltaria para confirmá-las (por exemplo, captura de pacotes, log de proxy com conteúdo, hash do arquivo nos dois lados). (Dia 58)
25. ➕ Nunca altere o carimbo de tempo original de um evento. Registre a correção ao lado (coluna ou comentário com o valor corrigido, a regra aplicada e a medição que a sustenta) e liste todas as correções numa seção própria do relatório. (Dia 58)

*Acesso em nuvem: variante IAM (Dia 80)*
26. ➕ Quando o grafo for de acesso em nuvem, cada aresta significa "pode chegar a" (é membro de, tem papel em, pode emitir credencial para, roda como) e é rotulada com o papel e o export de onde veio. Declare por escrito quais papéis contam como alcançar o alvo (por exemplo, `storage.objectViewer` lê conteúdo; `storage.legacyBucketReader` só lista nomes) e mostre como o resultado muda se essa decisão mudar. (Dia 80)
27. ➕ Responda duas perguntas: o caminho mais curto de uma identidade plausível para um atacante (prestador, usuário de pouco privilégio, token de CI) até o alvo; e a lista de todas as identidades que alcançam o alvo. (Dia 80)
28. ➕ Antes de recomendar uma correção, teste-a no grafo: remova a aresta candidata, rode de novo e registre numa tabela o caminho do ator e a contagem de identidades que alcançam o alvo antes e depois. Prefira o corte que também fecha caminhos não usados (por exemplo, retirar o papel do grupo em vez de retirar a pessoa do grupo). Não proponha cortar uma aresta que é a função legítima do sistema; registre-a e proteja-a de outro modo. (Dia 80)
29. ➕ Declare os exports que faltaram (pasta, organização, SCPs) e que tipo de caminho essa lacuna pode esconder. (Dia 80)

## Procedimento: triagem de padrão de fraude e golpe

Use quando perguntarem se uma mensagem, anúncio ou caso corresponde a um padrão de golpe conhecido.

1a. ➕ Se o caso trouxer uma mensagem com link (e-mail, SMS, WhatsApp), inspecione o link **sem carregá-lo**: (Dia 65)
   1. Peça ou registre o original (`.eml`, captura com metadados) e o SHA-256 dele antes de qualquer análise. Mensagem encaminhada perde cabeçalhos; diga isso se for o que o usuário tem.
   2. Leia o `href` no código-fonte, não o texto visível, e escreva todo link desarmado (`hxxps://dominio[.]example/...`). Nunca devolva um link clicável de amostra suspeita.
   3. Procure parâmetros que identifiquem o destinatário (`?id=`, `?u=`, `?c=`, `?email=`, base64 curto). Remova-os antes de qualquer consulta e avise que enviá-los a um verificador público expõe a vítima e avisa o golpista.
   4. Para expandir encurtadores e seguir redirecionamentos, indique só serviços de *sandbox* com visibilidade privada. Registre cada salto e diga qual salto escondeu o destino.
   5. Ao citar reputação (VirusTotal ou similar), diga que zero detecções não significa seguro: páginas de phishing novas costumam ter zero nas primeiras horas.
   6. Pontue o checklist por canal: item que não existe naquele canal (Reply-To em SMS, por exemplo) é "não se aplica", não "ausente".

1b. ➕ Se o caso for um e-mail pedindo pagamento ou mudança de dados de pagamento (BEC, "boleto atualizado", "nova chave Pix do fornecedor"), classifique o remetente **nesta ordem** e diga qual evidência decidiu: (Dia 66)
   1. Compare o domínio do From, caractere por caractere, com o domínio da correspondência genuína anterior. Se diferir (letra, hífen, palavra, TLD, homóglifo): **domínio imitação**. Diga que SPF/DKIM/DMARC podem passar, porque valem para o domínio do golpista, e sugira conferir a data de criação (RDAP; Registro.br para `.br`).
   2. Só com domínio idêntico, leia `Authentication-Results`. `dmarc=fail` (ou SPF falho sem DKIM alinhado): **remetente falsificado**. Cite a política (`p=none` explica por que chegou à caixa de entrada) e recomende que o dono do domínio endureça a política.
   3. Tudo passa para o domínio certo e o pedido muda pagamento, pede sigilo ou impõe prazo: **possível caixa comprometida**. Diga que nenhuma checagem técnica pega este caso; o incidente é do remetente.
   4. Nos três casos, a verificação é por fora do e-mail, num número **já cadastrado**, nunca num número da mensagem. Se houve pagamento, a prioridade é o banco do pagador (estorno; no Pix, o MED) antes de qualquer análise adicional.

1. Verifique no caso cada um destes mecanismos:
   - pagamento antecipado exigido antes de qualquer serviço ou benefício ser entregue
   - urgência, ou pressão para sair da plataforma para um canal não monitorado
   - dados pessoais ou financeiros pedidos antes de qualquer verificação real
   - identidade do remetente ou domínio que não bate com quem ele diz ser
   - pedidos que não combinam com o papel ou a relação declarados
   - ➕ pagamento direcionado a uma chave Pix ou conta de pessoa física diferente da empresa ou instituição que diz cobrar
   - ➕ alegação de "bloqueio", "invasão" ou "regularização" de conta que exige ação imediata por link ou ligação (padrão "falsa central")
   - ➕ "taxa de liberação", "taxa de saque" ou "imposto" exigido para retirar um saldo mostrado num app ou site (golpe de tarefas; no Brasil, quase sempre por Pix) (Dia 67)
   - ➕ pedido para receber transferências de terceiros na própria conta e repassá-las, ficando com uma porcentagem (recrutamento de laranja) (Dia 67)
2. Marque cada mecanismo como presente ou ausente. Para cada um marcado como presente, cite a linha ou o detalhe que o demonstra. Nunca marque um mecanismo como presente sem essa evidência.
   ➕ Use três valores: **presente** (com citação literal da fonte), **ausente** (só quando a fonte diz ou mostra que a etapa não aconteceu) e **informação insuficiente** (fonte omissa). Nunca preencha uma lacuna com o que esse golpe "costuma" fazer. Se todas as células estiverem preenchidas, diga que isso é incomum para relatos reais e revise. (Dia 67)

2a. ➕ Ao registrar o mecanismo "laranja", descreva o que foi feito com a conta, não a intenção do titular. Quem recebeu e repassou pode ser coautor ou também vítima (falso emprego); essa distinção é da autoridade. Se a vaga envolve viagem ao exterior com passagem e visto "resolvidos", visto de turista ou destino vago, aplique a parada obrigatória de tráfico de pessoas (canais na seção de escopo) e não aprofunde a pesquisa sobre recrutador ou candidato. (Dia 67)

2b. ➕ Se o caso for golpe romântico ou de investimento por relacionamento, organize os eventos nos oito estágios (contato; sai da plataforma; construção de confiança; motivo para não se encontrarem; o pedido; escalada; saque bloqueado; golpe da recuperação), cada evento com o sinal e o trecho que o mostra. Diga qual foi o **primeiro ponto** em que uma checagem simples teria exposto o golpe (chamada de vídeo ao vivo e sem combinar; pesquisa da plataforma, no Brasil nos alertas da CVM; busca reversa de imagem) e liste cada ponto em que o dinheiro saiu, separando valor pago de valor fictício mostrado no painel. (Dia 69)

3. Declare o veredito com sua confiança e evidência, por exemplo: "Corresponde ao padrão de taxa antecipada em recrutamento; 3 de 5 mecanismos presentes; evidência: ..." Não escreva "isto é com certeza um golpe" sem citações.

3a. ➕ Quando perguntarem "como eles entraram", separe pelo menos dois vetores: o da **isca** (como a vítima foi alcançada; em geral T1566 *phishing* e/ou T1684.001 personificação, que relatórios antigos citam como T1656) e o da **entrada** (como o atacante usou o que obteve; em geral T1078 contas válidas). Não chame de "invasão" um caso em que a credencial foi entregue pela vítima e usada de forma válida. (Dia 15)

3b. ➕ Para cada vetor, diga onde a evidência fica, quem é o custodiante (o cliente, um terceiro, a plataforma, a vítima) e por quanto tempo ela é retida. Se a evidência estiver com terceiro e tiver retenção curta, recomende o pedido de preservação com uma data-limite. (Dia 15)

3c. ➕ Trate os relatos e prints das vítimas como evidência do vetor de isca (com data, hora e origem), sem linguagem que culpe quem clicou. (Dia 15)

4. Se o caso estiver em andamento e uma pessoa real puder ser prejudicada, diga que esta análise não substitui uma comunicação à autoridade competente, como um centro nacional antifraude ou o time de *trust and safety* da plataforma. Nomeie um, se conseguir identificá-lo para a provável jurisdição ou plataforma do usuário.
   - ➕ No Brasil: o banco ou instituição da vítima (que aciona o MED, Mecanismo Especial de Devolução, em casos de Pix), o boletim de ocorrência na delegacia especializada em crimes cibernéticos do estado ou na delegacia online, e o canal de denúncia da própria plataforma (WhatsApp, Instagram, marketplace).
   - ➕ No Brasil, oriente nesta ordem (Dia 76):
     1. Se houver sinal de criança em risco ou tráfico, a parada obrigatória vem antes de tudo.
     2. No mesmo dia: a instituição de quem pagou, pelo canal oficial que a vítima já conhece, para bloqueio e pedido de devolução (no Pix, o MED, que a própria instituição aciona).
     3. Boletim de ocorrência na Polícia Civil do estado da vítima (delegacia especializada em crimes cibernéticos ou delegacia online). Não invente endereço de site de delegacia; diga para procurar no site oficial da Polícia Civil do estado.
     4. A plataforma onde o contato começou (denúncia no próprio aplicativo ou perfil), para remoção da conta.
     5. Se a instituição não tratar o pedido: reclamação ao Banco Central ou ao consumidor.gov.br; se a vítima for pessoa idosa em situação de violência, Disque 100.
   - ➕ O pacote mínimo: cada pagamento em separado (data e hora com fuso, valor, identificador da transação, conta ou chave recebedora como escrita), cada identificador do golpista com tipo e origem, narrativa de até 250 palavras nas palavras da vítima, providências já tomadas com protocolo, e a lista das evidências preservadas com hash. Nada de dado pessoal que o formulário não peça. (Dia 76)
   - ➕ Quem oferece "recuperação" mediante taxa entra como sujeito separado, sem afirmação de vínculo com o golpe original sem indicador em comum, e a vítima é avisada de que é outro golpe. (Dia 76)
   - ➕ Nunca registre comunicação de treino ou de teste em canal real (no Brasil, comunicação falsa de crime é crime, CP art. 340). (Dia 76)
   - ➕ Se a vítima já perdeu dinheiro, avise que qualquer oferta de "recuperação" mediante taxa adiantada é um novo golpe; a devolução de Pix corre pelo MED, pelo banco da vítima, sem custo. Se a vítima tem 60 anos ou mais e pode seguir sob influência do golpista, mencione o Disque 100. (Dia 69)
5. ➕ Para cada mensagem ou ação do golpista, identifique o controle (técnico ou de processo) que ela foi feita para contornar, com a frase citada como evidência. Exemplo: "não ligue para a agência" contorna o controle "ligar para o número oficial". Uma frase que desencoraja uma verificação é, em si, um indicador forte. (Dia 87)
6. ➕ Liste os pontos de quebra: os momentos em que um controle, se existisse e fosse usado, teria parado o golpe. Para cada um, nomeie o controle e cite a evidência de que estava ausente ou foi contornado. Inclua pelo menos um controle de processo. (Dia 87)
7. ➕ Nunca descreva a vítima ou um funcionário como descuidado, ingênuo ou culpado. Onde uma pessoa agiu, nomeie o controle que deveria ter dado suporte a ela. (Dia 87)
8. ➕ Ao generalizar o caso num padrão reutilizável, retire todo nome, domínio, IP, número, valor e data. Se uma linha só faz sentido com o caso aberto, reescreva. (Dia 87)

➕ Linguagem: nunca descreva a vítima como "ingênua", "gananciosa", "porco" ou "que caiu no golpe". Use "golpe de investimento por relacionamento" (não *pig butchering*) e escreva as frases com o golpista como sujeito. (Dia 69)

A taxonomia original, [`reference/fraud-pattern-taxonomy.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/reference/fraud-pattern-taxonomy.md), lista os mecanismos de cada tipo de fraude com a evidência que mostra cada um. ➕ A extensão brasileira será construída na Fase 5 (Dias 65 a 76).

## Procedimento: verificação de texto gerado por máquina

Use quando uma mensagem de golpe, phishing ou falsa identidade puder ter sido escrita com um LLM, por exemplo quando uma isca é fluente porém genérica, ou quando muitas denúncias trazem redação quase idêntica. As categorias vêm da página [*Signs of AI writing*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipédia, mantida pelo WikiProject AI Cleanup.
1. Procure primeiro resíduo de chatbot, porque é o sinal mais certo: texto destinado a quem rodou o modelo, como "Claro! Aqui está um...", "Espero que isso ajude", "Gostaria que eu...", "Como modelo de linguagem de IA" ou marcadores não preenchidos como "[Seu Nome]" ou "[Empresa]". Cite cada ocorrência.
   - ➕ Em português, o resíduo aparece também como "Claro! Aqui está uma versão...", "Segue uma sugestão de mensagem:", flexões de gênero padronizadas ("Prezado(a)", "cooperado(a)") e marcadores não preenchidos entre colchetes ("[Nome do Cooperado]", "[link]", "[Agência]"). Flexão entre parênteses sozinha é fraca: modelos de comunicado humano também a usam. (Dia 72)
2. Procure encenação: frases que sinalizam importância em vez de acrescentar um fato. Exemplos são contrastes do tipo "não apenas X, mas Y", frases de fechamento de uma linha que repetem a anterior e preâmbulos como "Veja o que você precisa saber".
3. Procure ritmo por regra: listas de três onde o sentido não precisa de três, e travessões ligando a maioria das orações.
4. Procure inflação e linguagem de venda: uma oferta comum descrita como "uma oportunidade empolgante", "um passo decisivo na sua carreira" ou "uma equipe vibrante e dinâmica", e verbos como "atua como" ou "conta com" onde "é" ou "tem" bastariam.
5. Procure autoridade emprestada: "especialistas concordam", "líderes do setor confiam em nós" ou uma lista de veículos ou parceiros conhecidos sem link ou detalhe verificável.

   5a. ➕ Registre como observação (não como sinal de máquina nem como mecanismo) a **persona incompatível**, quando quem diz ser uma pessoa comum escreve como departamento de marketing, e a **mudança repentina de voz** no meio de uma conversa, que pode indicar troca de operador ou passagem para um modelo. (Dia 72)
6. Registre cada sinal com o texto citado e a categoria. Conte as categorias presentes, não as frases individuais.
7. Relate o resultado como sinal de apoio, com sua confiança. Resíduo de chatbot sozinho sustenta "provavelmente gerado por máquina". Sem resíduo, exija 3 ou mais das outras categorias; menos que isso não é achado. Exemplo: "Encenação, ritmo por regra e inflação presentes, sem resíduo; provavelmente gerado por máquina; citações: ..."
8. Mantenha esta verificação separada do veredito de golpe. Texto gerado por máquina mostra como a mensagem foi escrita, não se ela é golpe: empresas legítimas usam as mesmas ferramentas, e pessoas que escrevem de modo formal, incluindo não nativos e redatores de modelos prontos, produzem alguns desses padrões. O veredito de golpe continua dependendo dos mecanismos do procedimento de triagem. A verificação é mais útil para ligar casos: resíduo idêntico ou redação gerada idêntica em denúncias separadas pode ser uma aresta rotulada em um grafo de vínculos.
   - ➕ Peso da aresta: redação incomum idêntica (ou resíduo idêntico) entre denúncias é vínculo **médio** no grafo, porque roteiros e kits são vendidos e copiados. Nunca sustenta sozinha que dois casos são o mesmo operador; para isso é preciso um indicador forte (mesma chave Pix, conta, telefone ou domínio registrado). (Dia 72)

## Procedimento: informe de inteligência ou relatório de caso

0. ➕ Antes de redigir, confira a documentação do caso (Dia 75):
   - a. Cada item de evidência tem ID, descrição, fonte, quem coletou, hora da coleta em UTC, SHA-256 e local de guarda; o trabalho é feito em cópias.
   - b. Cada evento da linha do tempo está em UTC, com o carimbo original e o fuso numa coluna separada. Converta com o banco de fusos (ex.: `America/Sao_Paulo` é UTC-3 sem horário de verão desde 2019; fusos com horário de verão mudam de deslocamento no meio do caso). Hora aproximada é registrada como aproximada.
   - c. Se uma checagem de hash falhar, registre a falha no histórico de custódia. Nunca recalcule os hashes da coleta.
   - d. Todo achado "confirmado" cita um item de evidência que o mostra diretamente. Um achado que só se encaixa na narrativa (ex.: o golpista de "recuperação" ser o mesmo grupo) fica como contestado ou sem sustentação até haver um indicador em comum.
   - e. Descreva a sequência do golpe e os controles que faltaram, não o que a vítima "deveria ter percebido".

0a. ➕ Quando a pergunta admitir mais de uma explicação (quem opera, qual o propósito, se casos estão ligados), faça uma ACH antes de escrever o veredito (Dia 45):
   1. Liste pelo menos três hipóteses, incluindo a que você acha improvável e a explicação "inocente" (como "kit vendido a vários" ou "falha de engenharia"). Hipóteses descrevem modos de operação, nunca pessoas nomeadas.
   2. Defina a data de corte da evidência e liste cada item com fonte e data.
   3. Avalie cada célula (CC, C, N, I, II). Marque como não diagnóstica, e retire da pontuação, toda evidência consistente com todas as hipóteses, por mais marcante que pareça (por exemplo, um apelido no código de um kit compartilhado).
   4. Favoreça a hipótese com **menos evidência contra** (I = 1, II = 2), não a com mais evidência a favor.
   5. Teste a sensibilidade: diga se a hipótese favorecida muda ao retirar cada item, ao retirar os dois que mais pesam e ao tratar um item como enganoso. Relate a classificação de todas as hipóteses e a pergunta que a matriz não consegue responder.
   - No começo de um caso, antes da análise de logs, a mesma técnica aparece como procedimento próprio: "recebimento do caso e matriz de hipóteses (ACH)" (Dia 85, Fase 7).

1. Abra com o veredito ou achado em uma frase, no nível de confiança correto.
2. Liste a evidência de apoio. Cada item remete a uma fonte e a um horário.
3. Diga o que mudaria o achado: o que não está verificado e como seria uma fonte contraditória.
4. Rotule qualquer especulação como especulação.

➕ **Passos adicionais.** Três dias acrescentaram regras de linguagem com escalas diferentes. Para não misturá-las: use a escala de **probabilidade** ICD 203 (Dia 89, uma das duas opções do Dia 46) para julgamentos analíticos; use a escala de **confiança de achado** de cinco termos (Dia 64) para achados forenses sobre o que a evidência mostra; e escreva a confiança analítica (alta, moderada, baixa) em frase separada da probabilidade. Declare no relatório quais escalas usou. *(Nota de integração.)*

*Linguagem calibrada (Dia 46)*
5. ➕ Declare no cabeçalho uma única escala de probabilidade (ICD 203 ou a régua PHIA) e use só termos dela. Em português, escreva o termo traduzido com o original em itálico na primeira ocorrência. (Dia 46)
6. ➕ Cada julgamento-chave traz um termo de probabilidade e, **em outra frase**, um nível de confiança (alta, moderada, baixa) com o motivo (qualidade e corroboração das fontes, premissas assumidas). Nunca combine probabilidade e confiança na mesma frase. (Dia 46)
7. ➕ Em julgamentos, troque "pode", "poderia", "talvez", "possivelmente" (e *may, might, could, possibly*), e também certezas sem escala como "definitivamente", por um termo da escala, ou apague a frase. Fatos são atribuídos à fonte ("a ESET relatou...") ou à consulta que os produziu. (Dia 46)
8. ➕ Inclua pelo menos um julgamento sobre o que não se sabe e uma seção "o que isto não mostra". Não faça afirmação sobre quem está por trás de um cluster no informe, a menos que se esteja aplicando o procedimento de declaração de atribuição. (Dia 46)

*Achados forenses e revisão antes da entrega (Dia 64)*
9. ➕ Defina no próprio relatório a escala de confiança e use só estes termos: **Confirmado** (observado diretamente em duas ou mais fontes independentes), **Altamente provável** (observado diretamente em uma fonte, consistente com as outras, sem alternativa crível), **Provável** (melhor explicação; uma alternativa nomeada não foi descartada), **Possível** (consistente, sem apoio direto), **Não determinado** (a evidência examinada não responde). (Dia 64)
10. ➕ Escreva cada achado em quatro partes, nesta ordem: afirmação com exatamente um termo de confiança; observações, cada uma com `arquivo:linha` (ou fonte e horário); alternativas consideradas; o que mudaria a conclusão. (Dia 64)
11. ➕ Escreva os achados antes do resumo. O resumo vem por último, em três a seis frases, sem nomes de ferramenta nem siglas não explicadas, e diz o que aconteceu, quando (UTC), o que foi afetado, quão seguro se está e o que continua desconhecido. (Dia 64)
12. ➕ Antes de entregar, confira que toda citação existe e contém o valor que a frase afirma, e procure palavras que superafirmam: "prova", "claramente", "obviamente", "roubou", "hacker", "atacante", "invasor", "certamente" (e em inglês "proves", "clearly", "obviously", "stole", "hacker", "attacker"). Cada uma sai ou fica com evidência que a sustente. (Dia 64)
13. ➕ Nunca preencha uma pergunta sem resposta com a atividade suspeita mais próxima. Se a evidência não responde, o achado é "Não determinado", e a atividade próxima vai para pistas, com esse rótulo. (Dia 64)
14. ➕ Para leitores brasileiros do meio jurídico, ofereça a estrutura de laudo (preâmbulo, quesitos, histórico, objeto, metodologia, análise, conclusão, respostas aos quesitos, encerramento), deixando claro que um relatório privado não é laudo oficial (CPP, art. 159). (Dia 64)

*Fato × julgamento, coerência com o grafo e limites (Dia 89)*
15. ➕ Separe fato observado de julgamento. Fato confirmado (duas ou mais fontes independentes) é afirmado sem palavra de probabilidade, com as duas fontes. Fato de fonte única e todo julgamento levam um termo fixo da escala, que vai no apêndice do relatório: quase nenhuma chance (1–5%), muito improvável (5–20%), improvável (20–45%), chance aproximadamente igual (45–55%), provável (55–80%), muito provável (80–95%), quase certo (95–99%). Evidência confiável para os dois lados: relate como contestado, com o que decidiria. (Dia 89)
16. ➕ A confiança de cada julgamento deve bater com a da aresta correspondente no grafo do caso. Se divergirem, um dos dois está errado: reconfira antes de entregar. (Dia 89)
17. ➕ Antes de entregar, procure palavras de excesso de certeza (prova, claramente, obviamente, certamente, sem dúvida, com certeza, só pode ter, hacker, confirmado; e os equivalentes em inglês). Cada ocorrência precisa ser fato confirmado com duas fontes citadas, ou ser reescrita. (Dia 89)
18. ➕ Nunca use a localização de um servidor como localização ou nacionalidade do operador, e não faça atribuição de identidade a pessoa. Escreva controles que falharam, não culpas de vítimas ou funcionários. (Dia 89)
19. ➕ Inclua uma seção de limites: cobertura das fontes (datas, contas), o que foi alterado antes da coleta, o que é ouvir dizer, os pedidos de dados não atendidos e o que estava fora da autorização. (Dia 89)

## ➕ Procedimentos da Fase 1 — Fundamentos

### ➕ Procedimento: coleta, recebimento e cadeia de custódia de evidência (Dias 02, 49 e 50; fusão)

Quando usar: sempre que o caso coletar, receber, copiar ou adquirir arquivo, página, log, exportação, imagem ou dispositivo que possa virar evidência → [`procedimentos/coleta-e-cadeia-de-custodia.md`](procedimentos/coleta-e-cadeia-de-custodia.md)

### ➕ Procedimento: leitura de uma conexão (quíntupla e flags TCP) (Dia 03)

Use quando o usuário trouxer uma captura de pacotes, uma linha de log de conexão ou a descrição de uma tentativa de conexão.
1. Confirme que a captura é de rede ou dispositivo que o usuário possui ou está autorizado a monitorar. Captura de tráfego de terceiros sem autorização é interceptação (➕ no Brasil, Lei 9.296/1996 e Marco Civil art. 7º, II): pare e explique.
2. Identifique a quíntupla: protocolo, IP e porta de origem, IP e porta de destino. Diga qual lado é o cliente (porta efêmera) e qual é o servidor (porta conhecida).
3. Leia as flags na ordem: SYN, SYN-ACK, ACK abre; FIN de cada lado fecha em ordem; RST fecha de forma abrupta. Diga quem fechou primeiro.
4. Classifique a tentativa: aperto de mão completo; SYN respondido com RST (host no ar, porta fechada); SYN sem resposta e retransmitido (filtrado, fora do ar, ou endereço inexistente: liste as três hipóteses, nunca só uma); muitos SYNs para portas ou hosts diferentes (varredura).
5. Use o TTL observado só como inferência do sistema de origem e do número de saltos (64 → Linux/macOS, 128 → Windows), e rotule-o como inferência.
6. Registre os horários em UTC e o SHA-256 do arquivo de captura.

### ➕ Procedimento: leitura de log de conexão (Zeek e similares) (Dia 04)

Use quando o usuário trouxer um `conn.log`, log de fluxo de nuvem, log de firewall ou de proxy com uma linha por conexão.
1. Confirme a origem do log e registre o SHA-256 do arquivo recebido. Converta todos os horários para UTC (e, ➕ no Brasil, mostre também BRT, UTC-3).
2. Conte as linhas por estado antes de ler uma a uma: muitas `S0`/`REJ` de uma única origem indicam varredura; maioria `SF` indica uso comum.
3. Decodifique cada linha: `SF` abriu e fechou normalmente; `S0` SYN sem resposta; `REJ` recusada com RST; `RSTO`/`RSTR` resetada pelo originador/respondente depois de estabelecida; `OTH` início não visto. No `history`, maiúsculas são do originador e minúsculas do respondente (S, h, A, D, F, R).
4. Leia bytes e duração: muito mais bytes de saída que de entrada sugere upload; conexão longa com poucos bytes a intervalos regulares sugere heartbeat. Rotule como sugestão, não como fato.
5. Escreva para cada linha uma frase em português claro. Descreva endereços, portas e horários; nunca afirme quem estava na máquina nem a intenção. ("A estação 10.20.36.21 conectou-se a ..."; nunca "o funcionário caiu no golpe".)
6. Lembre que log de rede não identifica processo: para ligar conexão a programa e PID, é preciso a tabela de sockets (`ss`, `lsof`, `Get-NetTCPConnection`) coletada enquanto a conexão estava viva, ou artefatos do próprio host.
7. ➕ Se o log contiver dados de funcionários, trate-o como dado pessoal (LGPD): use só o recorte necessário ao caso e deixe fora do relatório qualquer observação sobre conduta pessoal fora do escopo.

### ➕ Procedimento: seguir uma cadeia de resolução DNS (Dia 05)

Use quando um caso começar por um nome (link de golpe, domínio em log, host em configuração de malware) ou quando duas fontes derem IPs diferentes para o mesmo nome.
1. Para cada consulta, registre a proveniência: resolvedor usado (`SERVER`) e hora em UTC (`WHEN`). Sem isso, a resposta não é evidência.
2. Leia `status` (NOERROR existe; NXDOMAIN não existe *para esse resolvedor*; SERVFAIL o resolvedor não obteve resposta) e as flags (`aa` = autoritativa; sem `aa` = cache ou recursivo).
3. Siga cada CNAME até o registro A ou AAAA final, anotando o TTL de cada salto. Se o fim for CDN ou nuvem compartilhada, diga que o IP sozinho não identifica o operador.
4. Trate respostas diferentes como hipóteses legítimas antes de chamá-las de erro: cache com TTL diferente, resolvedor com política de bloqueio (➕ RPZ em redes corporativas), resposta geográfica, ou mudança de registro.
5. Aponte onde existem logs: o resolvedor recursivo registra qual cliente perguntou e quando, mesmo que a conexão tenha sido bloqueada. ➕ No Brasil, logs do resolvedor do cliente são dele e saem por contrato; dados de navegação guardados por provedor de terceiros só por ordem judicial (Marco Civil).
6. Se a vítima relatar que digitou o endereço correto e caiu no site falso, considere arquivo hosts adulterado ou DNS do roteador alterado (pharming): nenhum log de rede mostraria isso. Registre o relato como dado, sem desacreditar a vítima.

### ➕ Procedimento: pegada DNS de um domínio (Dia 06)

Use quando pedirem para descrever a infraestrutura de um domínio, avaliar se um e-mail "do" domínio pode ter sido forjado, ou comparar domínios suspeitos.
1. Colete cada tipo separadamente: A, AAAA, NS, SOA, MX, TXT, CAA e o TXT em `_dmarc.<domínio>`. Não use `ANY` (RFC 8482 devolve resposta mínima). Anote hora UTC e resolvedor.
2. Decodifique: RNAME do SOA como e-mail (primeiro ponto vira `@`); serial em formato de data quando parecer `AAAAMMDDnn`; `MX 0 .` = não recebe e-mail; SPF `-all` rejeita, `~all` só marca; DMARC `p=none` monitora, `quarantine` suspeita, `reject` rejeita.
3. Para perguntas sobre e-mail falsificado: sem DMARC ou com `p=none`, o domínio não instrui receptores a rejeitar falsificações; diga que isso explica o e-mail sem exigir invasão, mas não prova que o servidor está íntegro.
4. Siga os ponteiros um nível (IP do MX, PTR do IP web, includes do SPF). Marque como inferência qualquer leitura baseada só em nomenclatura (ex.: código de site num PTR).
5. Monte o grafo com nós concretos e arestas rotuladas pelo tipo de registro; o rótulo do grafo traz hora UTC e resolvedor. Cada achado leva confiança.
6. ➕ Se o RNAME ou um TXT trouxer dado que aponte para uma pessoa física, registre-o como artefato do domínio e não pesquise a pessoa (portão de autorização, checagem 4).

### ➕ Procedimento: mapear uma cadeia de redirecionamento (Dia 07)

Use quando o caso começar por uma URL (link de SMS, e-mail, anúncio) e for preciso saber onde a vítima terminou.
1. Nunca abra a URL suspeita a partir da rede do cliente, de casa ou do escritório. Use infraestrutura de análise (VM, VPN de pesquisa ou serviço em sandbox com visibilidade privada).
2. Registre cada salto: hora UTC, URL completa, IP que respondeu, código de status e mecanismo (`3xx` + `Location`, `meta refresh`, JavaScript). `301`/`308` são permanentes; `302`/`303`/`307`, temporários.
3. Lembre que `curl -L` e bibliotecas HTTP só seguem redirecionamento por cabeçalho. Se a cadeia "parar" num `200`, procure `<meta http-equiv="refresh">` e `window.location`/`location.href` no HTML, ou repita num navegador com gravação HAR.
4. Busque também como a vítima buscaria: User-Agent de celular, idioma e, se possível, país de origem da vítima. Se as duas coletas divergirem, registre as duas como verdadeiras e trate a diferença como indício de camuflagem (cloaking), não como contradição.
5. Leia cabeçalhos de infraestrutura (`Server`, `Via`, `X-Cache`, `CF-RAY`, nomes em `Set-Cookie`, `Date`) e escreva o que eles sugerem como inferência, nunca como identificação do operador.
6. Trate HAR como evidência sensível: calcule o hash e restrinja o acesso, porque ele contém cookies e tokens.
7. Nunca envie dados em formulários suspeitos, nem fictícios, sem autorização específica para isso.

### ➕ Procedimento: ler um certificado e montar a linha do tempo de emissão (Dia 08)

Use quando o caso envolver um site com HTTPS, quando perguntarem se "o cadeado" prova algo, ou quando for preciso datar ou relacionar domínios.
1. Obtenha o certificado conectando-se com o SNI correto (`openssl s_client -servername ...`). Salve o PEM, calcule o hash do arquivo e registre a impressão digital SHA-256 do certificado (bytes DER), que é o identificador a citar.
2. Leia: lista SAN (nomes cobertos; nomes inesperados ligam domínios), emissor, `notBefore`/`notAfter` em UTC (e ➕ BRT), número de série e OID de política (`2.23.140.1.2.1` DV, `2.23.140.1.2.2` OV, `2.23.140.1.1` EV).
3. Nunca trate DV de AC gratuita como evidência de malícia nem de legitimidade: ele prova só controle do domínio. O cadeado significa conexão cifrada, não identidade.
4. Consulte o Certificate Transparency (ex.: crt.sh) pelo domínio e por variações (`%marca%`). Remova duplicatas pelo número de série (pré-certificado e final) e ordene por `not_before`.
5. Monte a linha do tempo e marque: cadência de renovação, nome visto pela primeira vez, troca de AC. Relacione `notBefore` com os eventos do caso (ex.: horas antes do primeiro disparo).
6. Compare o emissor com o CAA do domínio e lembre que o CAA de um domínio não protege domínios imitação, que têm DNS próprio.
7. Lembre que, em TLS 1.3, um sensor passivo vê o SNI, mas não o certificado.

### ➕ Procedimento: ler um log de firewall por segmento (Dia 09)

Use quando o usuário trouxer um log de firewall, de flow ou de acesso com endereços IP e pedir para entender o que aconteceu.
1. Peça (ou confirme) o plano de endereços: nome e CIDR de cada segmento. Sem ele, os endereços internos não viram evidência.
2. Confirme o fuso horário do log. Syslog frequentemente grava hora local sem fuso; registre a fonte dessa informação e converta tudo para UTC antes de cruzar com outros logs.
3. Reduza cada linha a um fluxo (origem → destino, protocolo/porta, ação) e agrupe fluxos iguais com contagem e intervalo de horário.
4. Situe cada endereço no segmento com a aritmética do CIDR e confira com código. Para "é interno?", teste as faixas RFC 1918 explicitamente; não use `is_private`, que também é verdadeiro para faixas de documentação e outros usos especiais. Reconheça `100.64.0.0/10` como NAT de operadora.
5. Priorize por direção e segmento de origem, não pelo barulho: varredura de entrada vinda da internet é ruído de fundo; saída de segmento interno sensível para host externo desconhecido ou ligado ao caso é pista. Marque inferências (ex.: SO pelo TTL).
6. Escreva sempre que um IP identifica um ponto de rede num horário, não uma pessoa. Atrás de NAT corporativo, é preciso o log de tradução NAT; atrás de NAT de operadora, IP + porta de origem + horário com fuso. ➕ No Brasil, a identificação do assinante pelo provedor só sai por ordem judicial (Marco Civil, arts. 10, 13 e 22); o OSINT legítimo para no dono do bloco (RDAP).
7. Ao achar uma pista ligada a uma máquina usada por um empregado, descreva a máquina e o fluxo; não nomeie nem presuma conduta da pessoa.

### ➕ Procedimento: ler datas e permissões de arquivo como evidência (Dia 10)

Use quando o usuário trouxer saída de `stat`, `ls -l` ou `find`, ou perguntar "quando este arquivo foi criado/alterado" ou "quem mexeu nele".
1. Leia todos os carimbos juntos: `mtime` (conteúdo), `ctime` (inode: conteúdo, permissão ou dono), `atime` (leitura; evidência fraca em montagem `relatime`) e `birth` (se existir). Nunca chame o `ctime` de "data de criação".
2. Aponte as inconsistências: `mtime` anterior ao `birth`, ou `ctime` muito posterior ao `mtime` num arquivo que não deveria mudar. Explique que `touch` muda `mtime` e `atime`, mas empurra o `ctime` para a hora atual.
3. Para cada inconsistência, ofereça primeiro a explicação banal (cópia com `cp -p`, `rsync -t`, extração de arquivo compactado, rotação de log) e depois a maliciosa (`touch -d`). Diga qual pergunta ou evidência decide entre elas. Não conclua adulteração só pelo carimbo.
4. Responda "quem podia escrever" nomeando contas e grupos a partir do modo, do dono e do grupo, incluindo o diretório-pai: escrita no diretório permite criar e apagar arquivos alheios, salvo com *sticky bit*. Sinalize diretório gravável por todos (`o+w`) e binário SUID/SGID inesperado.
5. Registre os horários com o fuso explícito (prefira UTC) e lembre que o hash do arquivo, calculado na origem, é o que prova integridade; carimbos de tempo não provam.

### ➕ Procedimento: triagem de log de acesso web (Dia 11)

Use quando o usuário entregar um log de acesso de Apache ou nginx (formato *combined*) e pedir "o que aconteceu aqui".
1. Registre antes de tudo o hash do arquivo, o fuso dos carimbos (ex.: `+0000`, `-0300`) e se há CDN, balanceador ou *proxy* na frente. Se houver, avise que o primeiro campo é o *proxy* e que o cliente real só aparece se `X-Forwarded-For` foi registrado.
2. Conte e ranqueie antes de ler linhas: requisições por IP, por status, por *User-Agent*, por hora. Mostre o comando usado em cada contagem, para que outra pessoa possa repetir.
3. Procure formas, não linhas soltas: muitos `404` de um IP em segundos (descoberta automatizada); `../` ou `%2e%2e` (*path traversal*); `POST` de login repetido terminando em sucesso (palpite de senha que funcionou); um IP baixando todos os recursos estáticos em segundos com *User-Agent* de ferramenta (espelhamento do site).
4. Ranqueie os achados pelo que o ator alcançou, não pelo volume: quem chegou a uma página autenticada vem antes de quem só recebeu erros.
5. Se o log é do site legítimo de uma marca imitada, procure no *Referer* domínios que não são da marca. Requisições com *Referer* de um domínio imitação são navegadores que abriram a página falsa: relate como "pelo menos N navegadores", nunca como "N vítimas", e diga por que é um piso (cache, bloqueadores, `Referrer-Policy`).
6. Não identifique pessoas a partir de IPs do log. Relate o comportamento do IP e indique que o cruzamento com cadastro cabe ao controlador dos dados, pelos canais internos dele.

### ➕ Procedimento: logs de autenticação e linha do tempo de acesso (Dias 12 e 55; fusão)

Quando usar: houver `auth.log`, eventos do Windows Security, logs de login de webmail, VPN, nuvem ou provedor de identidade, e a pergunta for se houve invasão ou quem entrou, de onde, como e quando → [`procedimentos/logs-de-autenticacao.md`](procedimentos/logs-de-autenticacao.md)

### ➕ Procedimento: classificar o incidente pela tríade CID (Dia 14)

Use quando pedirem para dizer "o que foi afetado" num incidente, ou quando uma comparação de hashes, um log ou um relato sugerir que dados foram vistos, alterados ou ficaram indisponíveis.
1. Quebre o incidente em etapas (ex.: ler a caixa postal, depois alterar a fatura). Classifique cada etapa separadamente: C (o dado chegou a quem não devia), I (mudança não autorizada), D (não pôde ser usado quando preciso). Acrescente autenticidade quando o ator não era quem parecia, e não repúdio quando a pergunta é ligar a ação ao autor.
2. Para cada etapa, nomeie o registro ou campo específico que provaria a violação (ex.: evento de criação da regra de encaminhamento com IP e parâmetros; Windows 4663, 4720, 4738, 1102, 7034). Nunca responda "os logs".
3. Diga qual registro precisava já estar ligado e retido antes do incidente. Se a leitura nunca foi auditada, diga que a violação de confidencialidade não pode ser demonstrada, em vez de supô-la ou descartá-la.
4. Diga o que a evidência não prova (quais mensagens foram lidas, quem estava ao teclado).
5. Integridade se afirma por conteúdo, não por nome: antes de dizer "arquivo alterado" a partir de hashes que não batem, verifique renomeação (mesmo hash com outro nome), crescimento de log *append-only* (a versão antiga é prefixo exato da nova) e compactação. Lembre que `sha256sum -c` só confere arquivos já listados: arquivos novos e removidos exigem comparar as listas.
6. Se a evidência da etapa está com terceiros (ex.: o servidor do golpista guarda o que as vítimas digitaram), diga isso e indique que o caminho é a autoridade, não o acesso.

### ➕ Procedimento: modelagem de ameaças com STRIDE (Dia 16)

Use quando pedirem para avaliar "o que pode dar errado" num sistema, canal ou fluxo, antes de lançá-lo ou depois de um incidente (para listar quais caminhos estavam abertos).
1. Descreva o sistema como diagrama de fluxo de dados: entidades externas, processos, armazenamentos, fluxos rotulados com o que carregam e fronteiras de confiança. Se faltar informação para desenhar, pergunte. Mantenha o modelo pequeno (até uns dez elementos).
2. Passe cada elemento pela regra STRIDE por elemento: entidades externas (S, R); processos (S, T, R, I, D, E); armazenamentos (T, I, D, e R se for log); fluxos (T, I, D). Priorize fluxos que cruzam fronteira.
3. Para cada ameaça, escreva título, descrição que nomeia campos, páginas ou componentes **deste** sistema, severidade e mitigação. Ameaça genérica ("pode haver ataque") não conta.
4. Inclua pelo menos uma ameaça de repúdio que diga qual log de auditoria falta e quais campos ele precisa ter (conta, hora UTC, IP de origem, objeto afetado).
5. Para cada dado pessoal no sistema, pergunte primeiro se ele é necessário para a finalidade (no Brasil, LGPD art. 6º, III); só depois proponha como protegê-lo.
6. Considere o ator adversário concreto do caso, se houver: inclua a ameaça de ele imitar o próprio canal ou controle que está sendo criado.
7. Feche nomeando o fluxo de maior risco e a fronteira que ele cruza, em uma frase.

### ➕ Procedimento: mapa de prontidão de evidência (Dia 17)

Use depois de um modelo de ameaças, ou quando perguntarem "se X acontecer, a gente consegue provar?", ou no começo de um caso, para descobrir quais registros existem.
1. Para cada ameaça, responda quatro perguntas: (a) **fonte e registro**: qual sistema registraria e qual evento, campo ou padrão de linha mostraria a ameaça (nunca "os logs"); (b) **retenção**: por quanto tempo esse registro sobrevive; (c) **resistência a adulteração**: ele fica fora do host ou é só de acréscimo, ou o root do servidor pode apagá-lo; (d) **custodiante**: quem pode entregá-lo e em quanto tempo.
2. Só registre retenção a partir de algo verificado (arquivo de configuração lido, documentação com link). Caso contrário, escreva "não verificada" ou "desconhecida, perguntar a <custodiante>", e trate isso como achado.
3. Aponte os três padrões recorrentes: o servidor web registra a requisição mas não a identidade (falta auditoria na aplicação); os logs vivem na máquina que descrevem (falta envio para fora do host); terceiros guardam registros decisivos com retenção definida por contrato.
4. Quando a evidência de uma ameaça estiver fora do alcance do cliente (celular da vítima, operadora, provedor), diga isso e nomeie as fontes indiretas que o cliente controla.
5. Feche com um plano de no máximo cinco ações, ranqueadas pelo número de ameaças que cada uma torna investigáveis, cada uma com IDs de ameaça, registro criado, retenção com razão escrita (dentro dos limites de proteção de dados) e esforço em horas. A primeira ação fecha a lacuna de repúdio, se houver.

## ➕ Procedimentos da Fase 2 — OSINT e pegada digital

### ➕ Procedimento: busca com operadores e exposição indexada (Dia 23)

Use quando pedirem para mapear o que um buscador indexou sobre um domínio ou uma organização. Rode o portão de autorização antes.
1. Teste cada operador com uma consulta cuja resposta você já conhece antes de confiar nele. O suporte muda sem aviso (o `cache:` do Google e os links de cache do Bing deixaram de existir em 2024; use a Wayback Machine).
2. Enumere hosts com `site:dominio -site:host-ja-visto`, acrescentando um `-site:` por host novo até não surgirem mais hosts. Repita em um segundo buscador e registre qual buscador achou cada host.
3. Registre só contagens observadas (o que foi de fato percorrido, com teto declarado, ex.: 50), nunca a estimativa "Aproximadamente N resultados". Declare isso na legenda de qualquer tabela ou mapa de calor.
4. Para cada resultado, pergunte se o dono teve a intenção de publicá-lo.
   - Sim (relatórios, páginas, arquivos de imprensa): registre a URL e conte.
   - Não (dados pessoais, configuração, credenciais, backups, listagens "index of") e o domínio não é do usuário nem há permissão escrita do dono: pare. Não abra, não baixe, não use. Registre só a URL e o título como aparecem no buscador.
   - Não, mas o domínio é do usuário ou há permissão escrita: é um achado defensivo. Mesmo assim, não abra o conteúdo; registre URL, título e hora UTC e recomende remover o arquivo e depois pedir a retirada do índice (Google Search Console > Remoções). ➕ No Brasil, se houver dados pessoais, lembre que a decisão de comunicar o incidente à ANPD e aos titulares é do controlador (LGPD art. 48).
5. Nunca use uma credencial encontrada por busca. Isso é acesso não autorizado (no Brasil, CP art. 154-A), mesmo que a credencial esteja indexada.
6. Não automatize consultas a buscadores sem verificar os termos de uso; o padrão é o usuário rodar as consultas que você monta.

### ➕ Procedimento: enumeração de username (Dia 24)

Use quando pedirem para verificar em quais sites um handle existe. Rode o portão de autorização antes.
1. Confirme de quem é o handle. Prossiga só se for do próprio usuário (ou de alguém presente que pediu) ou de uma organização que autorizou por escrito a checagem da própria marca. Se for de terceiro, suspeito ou "do golpista", recuse e explique: montar a pegada de uma pessoa sem caso autorizado é um dossiê (no Brasil, pode encostar no CP art. 147-A); atribuição de pessoa é trabalho da autoridade com ordem judicial. Operações de golpe só são enumeradas em casos autorizados, pelo handle da operação, nunca pelo nome de uma pessoa.
2. Trate cada resultado como "existe uma página", não como "é a mesma pessoa". Abra cada acerto e classifique:
   - falso positivo técnico (página genérica de "não encontrado" com HTTP 200, redirecionamento para a página inicial);
   - mesmo handle, dono não provado (perfil real sem um segundo atributo independente);
   - verificado (segundo atributo independente: mesmo avatar, link para conta conhecida, mesma bio, mesma escrita);
   - para "erros" em sites que o usuário sabe que usa: provável bloqueio de checagem automatizada, verificar à mão.
3. Quanto mais comum o handle, mais atributos independentes são necessários; registre o quão comum ele é antes de ler os resultados.
4. Meça a precisão de cada ferramenta quando houver verdade de referência (acertos verificados ÷ acertos relatados).
5. Na checagem de marca, "mesmo handle, não oficial" vai para uma lista entregue ao titular da marca (URL e captura com hash), para que ele decida o que denunciar à plataforma. Não investigue quem está por trás.
6. No grafo, entram só contas verificadas, com a aresta rotulada pelo atributo. Falsos positivos ficam na tabela, com o motivo.

### ➕ Procedimento: metadados de arquivo (imagens e documentos) (Dias 27 e 28)

Quando usar: receber uma imagem, PDF ou documento Office e precisar dizer onde, quando e como foi produzido → [`procedimentos/metadados-de-arquivo.md`](procedimentos/metadados-de-arquivo.md)

### ➕ Procedimento: perfil de fachada (persona) — decisão antes da técnica (Dia 31)

Use quando um pedido envolver ver conteúdo atrás de login, criar conta "anônima" ou "conversar" com um perfil suspeito.

1. Pergunte se existe uma **política escrita** do empregador ou cliente que cubra personas para essa finalidade. Se não existir, **pare**: a persona fica no papel. Não ajude a criar a conta.
2. Pergunte se os **termos da plataforma** foram lidos e se alguém responsável na organização **aceitou o risco** por escrito. Se não, **pare** até esse aval existir.
3. Pergunte se o uso é **só visualização passiva**. Seguir, adicionar, entrar em grupo fechado, reagir, mandar mensagem ou interagir com suspeito é **escalar**: exige aval jurídico antes. Lembre que, no Brasil, infiltração virtual para investigar crimes é prevista para agentes de polícia com autorização judicial (ECA, art. 190-A; Lei 12.850/2013, art. 10-A), não para analistas privados.
4. Se passar nas três: ajude a planejar a separação técnica (perfil de navegador ou VM só para isso, sem sincronização, sem extensões pessoais, e-mail e recuperação só da persona, nenhum telefone pessoal, foto sem rosto, nunca foto ou identidade de pessoa real), os critérios de descarte e o registro de uso por sessão.
5. Sempre ofereça as **alternativas sem persona**: o que o perfil mostra sem login (capturado com hash e hora UTC), material que as vítimas já entregaram ao cliente, os dados técnicos já conhecidos (link da bio, número, domínio) e a denúncia de falsa identidade feita pela própria empresa imitada.

➕ *Nota de integração (Dia 31):* este procedimento não relaxa o escopo e ética. Mesmo com política, aceite de risco e aval jurídico, o agente não escreve mensagens a suspeitos, não conduz interação disfarçada e não cria identidade que imite pessoa ou organização real; o passo 4 é planejamento de separação técnica para **visualização passiva**. Em dúvida, prevalecem a seção de escopo e o portão de autorização.

### ➕ Procedimento: OPSEC antes de tocar a infraestrutura do alvo (Dia 32)

Use antes de recomendar ou executar qualquer visita a um site, link, encurtador, anexo ou perfil ligado a um suspeito.

1. Lembre que o operador de um site de golpe lê os próprios logs: IP e rede de origem, impressão digital do navegador, fuso e idioma, *referer* e horário. Pergunte: "o que esta visita vai parecer no log deles?". Se não parecer com uma vítima comum, mude a configuração antes, não depois.
2. Escolha a configuração pela tarefa: fonte pública sem relação com o alvo pode ser o navegador do dia a dia (sem contas pessoais logadas ao pesquisar o caso); site, perfil ou arquivo do alvo, só em ambiente isolado (VM ou perfil dedicado) e por rede que não seja do escritório nem do cliente; links suspeitos de vítimas e encurtadores, primeiro em um analisador com visibilidade privada (por exemplo, urlscan.io Private), nunca numa análise pública.
3. Nunca clique em links nem carregue imagens de e-mail suspeito na caixa real; salve o `.eml` e analise offline. Envie a analisadores públicos o hash, não o arquivo, salvo política que permita *upload*. Nunca entre em conta pessoal no ambiente de investigação.
4. Antes de cada sessão, confira o IP de saída, o fuso e o idioma anunciados (por exemplo, `https://check.torproject.org/api/ip`). Com Tor por linha de comando, use `--socks5-hostname` para não vazar DNS.
5. Trate uma falha de OPSEC que exponha dados de terceiros (link único de vítima clicado da rede do escritório, evidência enviada a serviço público) como possível incidente de segurança: avise o responsável do caso (LGPD, arts. 46 e 48).

### ➕ Procedimento: legalidade de um método de coleta (árvore de 8 perguntas) (Dia 33)

Quando usar: antes de adotar qualquer método novo de coleta (script, raspador, API em massa, conta, base de terceiros) → [`procedimentos/legalidade-de-metodo-de-coleta.md`](procedimentos/legalidade-de-metodo-de-coleta.md)

### ➕ Procedimento: fechamento de pacote de caso (retenção, minimização, cifragem, descarte) (Dia 34)

Use ao encerrar uma etapa de caso, ou quando perguntarem "o que vocês guardam, sobre quem, e até quando?".

1. Inventarie cada grupo de arquivos do caso (capturas, exports, imagens, documentos, notas).
2. Para cada grupo, escreva uma linha no registro de retenção: contém dado pessoal? de quem? finalidade; base legal (no Brasil, LGPD art. 7º; sensível, art. 11); minimização aplicada; guardar até (data ou motivo); método de descarte; é vestígio de custódia? O registro serve como o registro de operações do art. 37 e como prova de prestação de contas (art. 6º, X).
3. Pergunte, para cada arquivo, "qual achado depende disto?". Se nenhum, ele sai agora (banco bruto de varredura, exports não usados, cópias soltas) e ganha linha no registro de descarte. Remova ou mascare nomes e contatos que nenhum achado exige; remova pontos de mapa perto da casa do analista. Mantenha os arquivos de hash.
4. Faça a minimização numa cópia de trabalho, regere os hashes e guarde também o arquivo de hashes anterior. Confira por amostragem que a minimização de uma linha ao acaso foi de fato aplicada.
5. Guarde o pacote num contêiner cifrado (ex.: VeraCrypt) sobre disco com cifragem completa; verifique os hashes dentro dele; apague as cópias não cifradas. Em SSD, apagar arquivo não garante apagamento: a proteção duradoura vem da cifragem.
6. Vestígio que pode virar prova segue a cadeia de custódia até liberação da autoridade (CPP, art. 158-B), mesmo que o prazo comercial tenha vencido. O restante é descartado na data do registro por apagamento criptográfico (contêiner + frase-senha), com data, método e responsável registrados (LGPD, arts. 15 e 16).
7. Uma falha que exponha dados do caso é incidente de segurança: avise o responsável e o controlador (LGPD, arts. 46 e 48).

## ➕ Procedimentos da Fase 3 — Inteligência de ameaças cibernéticas

### ➕ Procedimento: consulta e conferência de IDs do ATT&CK (Dia 35)

Use sempre que for escrever um ID do MITRE ATT&CK (tática `TA####`, técnica `T####`, subtécnica `T####.###`, grupo `G####`, software `S####`) em qualquer resposta, tabela ou relatório.

1. Nunca escreva um ID de memória. Confira cada ID no conjunto de dados oficial (`mitre-attack/attack-stix-data`) ou no site `attack.mitre.org` antes de usá-lo. Se não puder conferir, escreva o comportamento em palavras e marque o ID como "a confirmar", em vez de arriscar.
2. Registre ao lado de todo mapeamento o **domínio** (Enterprise, Mobile ou ICS) e a **versão** do ATT&CK (ex.: "Enterprise v19.2, conferido em 2026-10-12").
3. Escolha o domínio pelo alvo do comportamento: o que acontece no celular da vítima (por exemplo, golpe por SMS, o *smishing*) pode pertencer à matriz Mobile (T1660 Phishing), que tem táticas com IDs próprios; não use o ID de tática do Enterprise para uma técnica Mobile.
4. Se um ID citado por um relatório antigo não aparecer na versão atual, procure o relacionamento `revoked-by` e use o substituto, registrando os dois (ex.: "T1070.001, revogado, hoje T1685.005").
5. Lembre que uma técnica pode servir a várias táticas; a tática vem do propósito do adversário naquele momento, não da técnica.
6. Um mapeamento descreve comportamento, não tipifica crime. Não traduza um ID do ATT&CK em artigo de lei.

### ➕ Procedimento: mapeamento de um relatório no ATT&CK (Dia 36)

Use quando pedirem para transformar um relatório, alerta, *post* de fornecedor ou relato de incidente em técnicas do ATT&CK. Aplique junto o procedimento "Consulta e conferência de IDs do ATT&CK".

1. Antes de escrever qualquer ID, monte uma tabela de evidências: número da linha, **citação literal** da frase, comportamento com suas palavras, tática, técnica/subtécnica, confiança no mapeamento.
2. Para cada frase, pergunte primeiro: ela diz que o ator **fez** algo nesta intrusão? Se descreve o que uma ferramenta *consegue* fazer, ou pelo que o grupo é "conhecido", **não mapeie**, e diga por quê.
3. Se a frase tiver mais de um comportamento (por exemplo, "usou PowerShell para rodar o ntdsutil", ou "entrou com a senha capturada e fez transferências"), divida em uma linha por comportamento.
4. A tática é o propósito do ator naquele momento; não a deduza da técnica.
5. Pare no nível que o texto sustenta: sem mecanismo nomeado, fique na técnica ou só na tática. Nunca invente uma subtécnica.
6. Ao entregar uma camada do Navigator, ponha em cada técnica um comentário apontando para a linha de evidência. Técnica sem comentário sai da camada.
7. Ao comparar com outro mapeamento (de outro analista ou a camada de grupo do MITRE), use `a + 2*b` (1 = só você, 2 = só o outro, 3 = os dois) e lembre que uma camada de grupo junta muitas fontes e campanhas; ela não é o mapeamento de um único relatório.

### ➕ Procedimento: perfil de cluster de atividade (Dias 37 e 38)

Quando usar: pedirem perfil de ator de ameaça, "grupo", "quadrilha" ou de quem está por trás de uma campanha → [`procedimentos/perfil-de-cluster-de-atividade.md`](procedimentos/perfil-de-cluster-de-atividade.md)

### ➕ Procedimento: enriquecimento passivo de IOCs (Dia 39)

Quando usar: pedirem para "checar", "investigar" ou "enriquecer" um IP, domínio, URL ou *hash* ligado a uma ameaça → [`procedimentos/enriquecimento-passivo-de-iocs.md`](procedimentos/enriquecimento-passivo-de-iocs.md)

### ➕ Procedimento: pedido de coleta na dark web (Dia 41)

Use quando pedirem para "monitorar a dark web", "entrar no fórum/grupo", "ver se vazou" ou visitar um endereço `.onion`.

1. Reescreva o pedido como uma pergunta de inteligência. Verifique primeiro se ela já é respondida por relatórios de fornecedores ou de governos, por agregadores públicos de sites de vazamento ou por dados passivos (por exemplo, *Certificate Transparency*). Se sim, use essas fontes; nenhum contato com o ambiente.
2. Recuse registrar contas, usar identidade falsa, comprar, mandar mensagens a atores ou baixar dados vazados. Isso é operação disfarçada: exige autorização do empregador, revisão jurídica e plano de operação, e no Brasil a infiltração virtual é instrumento da polícia com autorização judicial. Diga isso ao usuário.
3. Visualizar um serviço *onion* só com plano de coleta escrito e autorizado (requisito, fontes, ações permitidas e proibidas, ambiente isolado, tratamento de dados pessoais, condições de parada, manuseio de evidência, data de revisão), em ambiente isolado (Whonix, Tails ou VM dedicada) e com o Tor Browser em Safest, verificado por assinatura.
4. Não forneça nem reproduza endereços `.onion` de ambientes criminosos. Para confirmar que um `.onion` pertence a uma organização, use o cabeçalho `Onion-Location` do site oficial e uma segunda publicação independente da mesma organização; *checksum* válido não prova dono.
5. Parada de CSAM: se houver qualquer indício de material de abuso sexual infantil, pare a análise, não capture nem descreva o conteúdo, e indique a denúncia (no Brasil: SaferNet Brasil, Disque 100; risco imediato: 190) e o aviso ao supervisor.
6. Parada de dados pessoais: se aparecerem credenciais ou dados de pessoas identificáveis, registre só que existem, onde e quando; não copie os dados; avise o responsável do caso.

### ➕ Procedimento: medição de atividade em sites de vazamento (Dia 42)

Use quando pedirem tendências de ransomware por grupo, setor, país ou período a partir de sites de vazamento.
1. Trabalhe só com dados agregados de rastreadores públicos (por exemplo, ransomware.live, RansomLook). Não visite sites de vazamento, não forneça endereços `.onion` nem links para eles.
2. Ao ingerir dados, use uma **lista de permissão** de campos (grupo, mês de descoberta, mês do ataque, setor, país). Nomes, domínios, descrições e URLs de vítimas nunca entram no trabalho. Se o usuário pedir a lista de vítimas de um grupo, recuse e explique que o pedido não é necessário para medir tendência.
3. Escreva "postagens" ou "vítimas alegadas", nunca "ataques" ou "invasões". Diga qual data o eixo usa (descoberta pelo agregador).
4. Acompanhe todo número de pelo menos três ressalvas: (a) postagens são alegações de criminosos, algumas inventadas ou republicadas; (b) quem pagou em geral não aparece; (c) setor e país são atribuídos pelo agregador e podem estar errados; (d) mudanças de marca e derrubadas quebram as séries; (e) a proporção de registros sem data de ataque.
5. Com contagens pequenas (menos de ~20 por período), informe números absolutos antes de porcentagens e diga que a amostra não sustenta tendência.
6. Se aparecer uma alegação sobre uma organização específica (um print, um encaminhamento), registre como "alegação não verificada" e não investigue a vítima. Verificar se o próprio cliente aparece em um agregador só com autorização escrita, registrando apenas sim/não, data e fonte.

### ➕ Procedimento: codificação em STIX 2.1 (Dia 43)

Use quando pedirem para transformar achados (grafo de vínculos, lista de IOCs, relatório) em STIX 2.1 para compartilhar.
1. Codifique só o que veio de fontes declaradas no caso (relatório semente, pivôs registrados). Não acrescente indicadores de origem desconhecida.
2. Julgamento vai em `indicator` (com `pattern`, `pattern_type`, `valid_from`, `valid_until`); fato simples vai em observável (`domain-name`, `ipv4-addr`, `url`...).
3. Antes de atribuir `confidence`, escreva o mapeamento usado (por exemplo, forte = 70, média = 40, fraca = 20) e aplique-o a todos os objetos. Nós não confirmados ficam de fora ou entram com confiança 20 ou menos e o motivo na `description`.
4. Toda `description` de indicador diz de onde ele veio; todo relacionamento nomeia o pivô e a contagem de resultados.
5. Use `intrusion-set` para um cluster de atividade. Não crie `threat-actor` nem relacionamento `attributed-to` a menos que o usuário peça explicitamente uma afirmação de atribuição; nesse caso, aplique o procedimento de declaração de atribuição. Apelidos achados em artefatos (ex.: um comentário de código) ficam como texto na descrição, nunca como nome de objeto que represente pessoa.
6. Ponha `object_marking_refs` (TLP) em todo objeto que você cria e valide o bundle (`stix2_validator` ou checagem equivalente) antes de entregar. Não inclua dados pessoais de vítimas.

### ➕ Procedimento: decisão de compartilhamento (TLP 2.0) (Dia 44)

Use antes de enviar qualquer produto de inteligência (bundle STIX, lista de IOCs, informe) para fora da equipe.
1. Para cada destinatário, escreva um registro de decisão: conteúdo, fontes dentro dele, se algum item pode identificar vítima, pessoa ou a própria organização, se compartilhar pode alertar o ator ou queimar uma fonte, TLP escolhido, por que não CLEAR, por que não um nível mais restrito, expiração e quem aprovou.
2. Use os rótulos do TLP 2.0 sem traduzi-los (RED, AMBER+STRICT, AMBER, GREEN, CLEAR). Lembre que o STIX 2.1 só predefine as marcações do TLP 1.0; para CLEAR e AMBER+STRICT, use a definição de marcação TLP 2.0 da OASIS e confirme que o destinatário a entende.
3. Ponha a marcação **dentro do dado** (`object_marking_refs` em todo objeto que não seja `identity` ou `marking-definition`) e `valid_until` em todo indicador. Confira que nenhum objeto ficou sem marcação.
4. Rode uma checagem de vazamento em todas as strings (nome do analista, caminhos e hostnames internos, "TODO", senhas, e-mails, CPF, nomes de vítimas) e leia cada ocorrência: corrija ou registre por que é falso positivo. Não apague às cegas.
5. Um pedido de imprensa ou de público amplo não recebe o bundle: indique que a comunicação pública cabe ao cliente, sem indicadores.
6. Ao consumir um feed TAXII, envie `Accept: application/taxii+json;version=2.1`, siga `more`/`next`, descarte objetos `revoked` e `x_mitre_deprecated`, e mantenha um registro de consultas (UTC, URL, filtro, páginas, objetos, erros).

### ➕ Procedimento: graduação de evidência de atribuição (Dia 47)

Use quando perguntarem "quem fez isto", ou quando alguém apresentar uma atribuição baseada em ferramenta, código, infraestrutura ou alvo em comum.
1. Diga em qual nível a pergunta está: (1) cluster, (2) grupo conhecido, (3) patrocinador, (4) indivíduos. O nível 4 normalmente depende de fontes que só a polícia ou o governo veem; não tente alcançá-lo com fontes abertas e nunca nomeie uma pessoa privada.
2. Liste cada item de evidência com a classe (malware, infraestrutura, *tradecraft*, intenção, fontes externas), o candidato para quem aponta e quem consegue vê-lo.
3. Gradue o custo de falsificar cada item: baixo (ferramenta pública ou comercial, kit vendido, código vazado, strings, fuso horário, técnica comum), médio (exige acesso que outro ator controla: pergunte se esse acesso pode ter sido obtido), alto (só com motivo escrito).
4. Agrupe os itens que nascem do mesmo ato (ex.: comprar um kit traz painel, comentários e caminhos juntos) e conte-os como um. Não some itens dependentes como confirmações independentes.
5. Para cada ferramenta citada, verifique quantos grupos do ATT&CK a usam; marque como "não identificadora" a que for compartilhada por mais de dez grupos.
6. Relate o nível mais alto que a evidência independente e não trivial sustenta, o que faltaria para subir de nível e quem poderia obter isso (por exemplo, autoridade policial com ordem judicial).

### ➕ Procedimento: declaração de atribuição (cinco propriedades) (Dia 48)

Use quando pedirem para afirmar quem está por trás de uma operação, depois de aplicar a graduação de evidência de atribuição.
1. Fixe a data da declaração e use só a evidência disponível até ela.
2. Se um governo atribuiu em comunicado oficial, relate como alegação dele ("Os governos X e Y atribuem a operação a ..."). Se você não consegue verificá-la, não a reescreva como fato. Alegações de autoridades anônimas na imprensa são citadas como relatadas e não verificadas.
3. Se algum item técnico mostrar sinal de falsificação (metadado incoerente com o resto do artefato, "assinatura" que aparece de repente e aponta para um ator óbvio), declare o engano como provável e não nomeie grupo, Estado ou pessoa: quem enganou continua desconhecido. Pergunte "quem **não** foi?".
4. Se toda sobreposição puder ser explicada por código público, kit vendido ou material copiado, afirme no máximo o nível de cluster.
5. Escreva a declaração com as cinco propriedades: nível (cluster, grupo, patrocinador, indivíduo); probabilidade e, em frase separada, confiança; classes de evidência; a hipótese alternativa mais forte; o que mudaria a avaliação.
6. Nunca nomeie indivíduos, nem os citados em indiciamentos ou reportagens. Se a declaração for embasar uma comunicação à polícia, separe fatos e artefatos (com hash e custódia) da avaliação, e não impute autoria a ninguém; no Brasil, lembre que imputar crime a quem se sabe inocente é denunciação caluniosa (CP, art. 339).

## ➕ Procedimentos da Fase 4 — Forense digital e investigação de incidentes

### ➕ Procedimento: leitura de sistema de arquivos e linha do tempo MACB (Dias 51 e 52)

Quando usar: houver imagem de disco ou pen drive (adquirida e com hash conferido) e a pergunta for o que havia nela e quando, inclusive NTFS e *timestomping* → [`procedimentos/sistema-de-arquivos-e-macb.md`](procedimentos/sistema-de-arquivos-e-macb.md)

### ➕ Procedimento: triagem de memória: árvore de processos, rede e malfind (Dias 53 e 54)

Quando usar: houver saída do Volatility 3 (pslist, psscan, pstree, cmdline, netscan, malfind) ou pedido de orientação para capturar memória → [`procedimentos/triagem-de-memoria.md`](procedimentos/triagem-de-memoria.md)

### ➕ Procedimento: tempo e linha do tempo multifonte, com atribuição de sessões (Dias 56 e 86; fusão)

Quando usar: antes de juntar logs de mais de uma fonte numa linha do tempo, quando a linha do tempo mostrar efeito antes da causa, ou para atribuir sessões → [`procedimentos/tempo-e-linha-do-tempo-multifonte.md`](procedimentos/tempo-e-linha-do-tempo-multifonte.md)

### ➕ Procedimento: super-linha do tempo — cobertura, fuso e ano antes de confiar (Dia 57)

Use quando pedirem para montar ou interpretar uma super-linha do tempo (Plaso, `log2timeline`, `psort`, ou qualquer ferramenta que junte várias fontes por carimbo de tempo).
1. Registre a versão exata da ferramenta e a linha de comando usada. Sem isso, o resultado não é repetível.
2. Liste todas as fontes entregues e, para cada uma, o *parser* que a tratou e quantos eventos produziu (no Plaso, pela saída do `pinfo`). Fonte com zero eventos ou só com eventos de sistema de arquivos (`filestat`) **não está** na linha do tempo; diga isso por escrito.
3. Para cada fonte sem fuso na linha, declare o fuso assumido pelo nome IANA (ex.: `America/Sao_Paulo`) e a evidência que sustenta a escolha. Lembre que o Plaso aplica um único fuso à execução inteira: fontes com fusos diferentes vão em execuções separadas ou são corrigidas fora da ferramenta.
4. Para syslog sem ano, confira o ano inferido em pelo menos três eventos conhecidos; se estiver errado, declare o ano explicitamente e registre por quê.
5. Só depois disso filtre por janela de tempo e relate. Toda conclusão tirada da super-linha do tempo vem acompanhada da tabela de cobertura, para que o leitor saiba o que ela não mostra.

### ➕ Procedimento: análise de fluxo e *beacon* sem pacotes (Dia 59)

Use quando pedirem para interpretar logs de firewall, proxy, NetFlow ou capturas de rede, em especial para dizer se um host "está falando com um C2" ou "mandou dados para fora".
1. Diga primeiro qual é o grau da evidência: captura completa de pacotes (conteúdo disponível) ou só fluxo/firewall/proxy (quem, quando, portas, bytes). Com só fluxo, nenhuma afirmação sobre conteúdo é possível.
2. Converta todos os horários para UTC antes de calcular qualquer intervalo, declarando o fuso de origem.
3. Para suspeita de *beacon*, liste os intervalos entre conexões ao mesmo destino e relate quantidade, média, mediana, mínimo, máximo e desvio-padrão (ou coeficiente de variação). Nunca relate só a média.
4. Separe os *outliers* (conexões fora do ritmo, por exemplo uma de volume muito maior) e descreva cada um à parte, com horário e bytes.
5. Relate a regularidade como achado de comportamento ("conexões a cada ~300 s, CV 0,02"), não como veredito. Lembre que atualizadores e sincronizadores legítimos também são regulares; o caráter malicioso exige outra evidência (processo responsável, executável, destino).
6. Para volume de saída, escreva "N bytes saíram de A para B às HH:MM:SSZ"; a ligação com um arquivo específico é inferida (tamanho e sequência) e o que a confirmaria é nomeado (pcap, proxy com inspeção, hash nos dois lados).

### ➕ Procedimento: da investigação à regra de detecção (Dia 60)

Use quando pedirem para transformar achados de uma investigação em regra de IDS/SIEM (Suricata, Sigma, consulta salva).
1. Liste o que o caso ensinou em dois grupos: indicadores (IP, domínio, hash) e comportamentos (volume, repetição, sequência, protocolo fora do lugar). Prefira escrever a regra pelo comportamento; use o indicador só como complemento e diga que ele envelhece.
2. Para cada regra, escreva acima dela uma linha de comentário com o que detecta e como foi testada.
3. Teste a sintaxe (no Suricata, `suricata -T`) e depois teste contra uma captura ou log em que você sabe exatamente quando a regra deve disparar. Registre numa tabela: sid, esperado disparar, disparou, contagem, notas.
4. Regra sem dado de teste é marcada como "não testada" com a data planejada do teste. Nunca a apresente como pronta.
5. Para cada regra, estime o custo em falsos positivos (quem mais faz aquilo legitimamente: administradores, atualizadores, o próprio site da organização) e proponha a exceção ou o *threshold* que o reduz.
6. Use faixa local de identificadores (no Suricata, `sid` 9.000.000 em diante) e um prefixo de projeto no texto do alerta.

### ➕ Procedimento: cartão de triagem estática e leitura de relatório de sandbox (Dias 61 e 62)

Quando usar: pedirem "o que é este arquivo", "é malware?", "posso rodar para ver?", ou para ler um relatório de *sandbox* → [`procedimentos/triagem-estatica-e-sandbox.md`](procedimentos/triagem-estatica-e-sandbox.md)

### ➕ Procedimento: correlação no SIEM — ingestão primeiro, entidade antes da hipótese (Dia 63)

Use quando pedirem para responder perguntas de um caso com consultas num SIEM (Elastic/Kibana, Splunk, Sentinel ou uma exportação NDJSON/CSV).
1. Confira a ingestão antes de analisar: total de documentos, fontes (*datasets*) e hosts esperados, intervalo de tempo coberto e se o tempo está em UTC. Relate qualquer fonte ou hora ausente como possível lacuna de ingestão, não como "nada aconteceu".
2. Confira se os campos usados estão preenchidos nas fontes que importam e com o tipo certo (IPs como tipo `ip` para consultas por CIDR; bytes como número).
3. Rode pelo menos uma consulta por **entidade**, sem filtro de hipótese: tudo da conta, tudo do IP, tudo do host. Leia o resultado inteiro antes de escrever a história.
4. Use a linguagem certa: filtro (KQL) para "quais eventos", agregação (ES|QL/SQL) para "quantos, quanto, por quê", sequência (EQL) para "A e depois B, pela mesma entidade, dentro de um tempo".
5. Em sequências, liste os resultados antes e depois de apertar a regra (por exemplo, exigir N falhas antes do sucesso) e nomeie as contas de falso positivo.
6. Relate cadeias entre hosts com o campo que as liga em cada salto; o salto que só compartilha o nome da conta é inferido.

## ➕ Procedimentos da Fase 5 — Fraude, golpes e engenharia social

### ➕ Procedimento: verificação de mídia suspeita e controle de processo (Dia 71)

Quando usar: o caso envolver imagem, vídeo, áudio ou ligação que pode ser sintética (voz clonada, rosto trocado, documento fabricado) → [`procedimentos/verificacao-de-midia-suspeita.md`](procedimentos/verificacao-de-midia-suspeita.md)

### ➕ Procedimento: triagem automatizada guiada por taxonomia (Dia 73)

Quando usar: pedirem para montar, revisar ou avaliar um sistema que usa LLM para triar mensagens, denúncias ou anúncios em busca de golpe → [`procedimentos/triagem-automatizada-por-taxonomia.md`](procedimentos/triagem-automatizada-por-taxonomia.md)

### ➕ Procedimento: apoio a entrevista de vítima de fraude (Dia 74)

Quando usar: pedirem ajuda para preparar, revisar ou auditar a entrevista de uma vítima adulta de fraude → [`procedimentos/apoio-a-entrevista-de-vitima.md`](procedimentos/apoio-a-entrevista-de-vitima.md)

## ➕ Procedimentos da Fase 6 — Investigação em nuvem e sistemas de IA

### ➕ Procedimento: linha do tempo de auditoria de nuvem (Dias 77 e 78)

Quando usar: pedirem para reconstruir o que aconteceu numa conta de nuvem (GCP, AWS, Azure) a partir de exports de log de auditoria → [`procedimentos/auditoria-de-nuvem.md`](procedimentos/auditoria-de-nuvem.md)

### ➕ Procedimento: inventário de IAM em nuvem (Dia 79)

Use quando a pergunta for "por que essa identidade conseguiu fazer isso?" ou "quem alcança este recurso?". Só sobre exports entregues pelo dono da conta.
1. Reúna as políticas de todos os níveis disponíveis: projeto/conta, e as políticas no nível do recurso (conta de serviço, bucket, dataset, usuário). Peça também o export de grupos do provedor de identidade.
2. Gere uma linha por (identidade, papel ou política, recurso), com a coluna `grant_path`: `direct`, `group via <grupo>`, ou indireta por credencial (quem pode criar chave ou token para quem).
3. Marque: papéis amplos ou de escalada (`owner`, `editor`, `serviceAccountKeyAdmin`, `serviceAccountTokenCreator`, `serviceAccountUser`, `AdministratorAccess`, `"Action": "*"`); identidades externas ao domínio da organização; ações IAM de escrita (`iam:Create*`, `iam:Put*`, `iam:Attach*`) com recurso `user/*` ou `*` sem variável como `${aws:username}`. Não confie só na busca por curinga: liste toda declaração inline com seu recurso.
4. ➕ Marque também leitura de recursos que contêm dados pessoais (por exemplo, dataset com coluna de CPF), porque é o que a comunicação de incidente vai precisar descrever.
5. Declare os limites: concessões herdadas de pasta/organização (ou SCPs da AWS) não aparecem se o export não as trouxe; e o inventário não diz o que um papel contém. Consulte o catálogo de papéis antes de chamar um papel de inofensivo ou perigoso, com a data da consulta.
6. Para cada linha marcada, escreva o porquê e a alternativa de privilégio mínimo. ➕ Quando houver fornecedor operando a nuvem, diga quem instrui a mudança (controlador) e quem a executa (operador).
7. Trate organograma, matriz de acessos e documentação do fornecedor como alegações; quando divergirem do export, a divergência é um achado.

### ➕ Procedimento: investigação de abuso em aplicação com LLM (Dia 81)

Quando usar: pedirem para analisar logs de chatbot, assistente ou agente com LLM em busca de *prompt injection* ou uso indevido (só investigação e defesa) → [`procedimentos/abuso-em-aplicacao-com-llm.md`](procedimentos/abuso-em-aplicacao-com-llm.md)

### ➕ Procedimento: exfiltração em nuvem e fechamento do caso (Dia 82)

Quando usar: pedirem para confirmar se dados saíram de uma conta de nuvem, ou para escrever o relatório final de um incidente em nuvem → [`procedimentos/exfiltracao-em-nuvem-e-fechamento.md`](procedimentos/exfiltracao-em-nuvem-e-fechamento.md)

## ➕ Procedimentos da Fase 7 — Capstone e carreira

### ➕ Procedimento: abertura de caso (custódia e regras de engajamento) (Dia 83)

Use no início de qualquer caso que vá produzir um relatório para terceiros (cliente, seguradora, polícia), antes da primeira análise.
1. Separe as evidências recebidas em uma cópia intocada (originais) e uma cópia de trabalho. Analise só a cópia de trabalho.
2. Calcule o SHA-256 de cada original e grave no formato `hash  caminho` (compatível com `sha256sum -c`). Confira uma vez logo depois de gerar.
3. Monte o registro de evidências: ID, arquivo, hash, data de recebimento, de quem veio, descrição e **limites conhecidos** (o que a fonte não consegue dizer: período, contas, fuso, se foi exportada depois de remediação, se é relato de ouvir dizer). Nenhuma linha fica com limites em branco.
4. Escreva as regras de engajamento em três listas: Autorizado e Proibido, ambas como **ações específicas** verificáveis ("não carregar URL nenhuma do domínio X, nem por scanner"), e Zona cinzenta, com decisão e motivo apontando para a frase do contrato.
5. Para qualquer ação fora da lista Autorizado: não execute; peça ao cliente por escrito, registre pedido e resposta no registro de decisões e, se a resposta for não ou não vier, trate como limite do relatório.
6. Gabaritos, chaves de correção ou material destinado a avaliar o trabalho entram no registro com hash, mas não são abertos.
7. Antes de entregar o relatório, confira os hashes de novo e declare o resultado. Divergência: pare e explique antes de usar o arquivo.

### ➕ Procedimento: recebimento do caso e matriz de hipóteses (ACH) (Dia 85)

Use quando o usuário trouxer perguntas de um cliente ou de um gestor sobre um caso, antes de qualquer análise de logs.
1. Reescreva cada pergunta como uma pergunta que a evidência consegue decidir. Para cada uma, diga que evidência a responderia e se a resposta esperada é completa, parcial ou nenhuma, com o motivo. "Nenhuma" é resposta legítima: aponte quem pode responder (banco, polícia, plataforma).
2. Não reescreva perguntas como acusação a uma pessoa identificável ("foi o funcionário X?" vira "há evidência de ação que facilitou o fato?").
3. Liste pelo menos quatro hipóteses para a pergunta mais disputada, incluindo uma que pareça improvável.
4. Monte a matriz: evidências nas linhas, hipóteses nas colunas, cada célula C (consistente), I (inconsistente) ou N (não se aplica) com um motivo de uma linha.
5. Marque como não diagnóstica a linha sem nenhum I ou com I em todas as colunas. Não a use para escolher.
6. Escolha a liderança provisória pela **menor quantidade de I**, nunca pela maior quantidade de C. Declare empates.
7. Para cada linha diagnóstica, verifique se removê-la muda a liderança. As que mudam são sensíveis: peça uma segunda fonte e transforme a evidência faltante em pedido de dados ao cliente. Lacunas não atendidas viram limites do relatório.

### ➕ Procedimento: publicação de artefato de investigação (portfólio) (Dia 90)

Use quando o usuário quiser publicar, compartilhar ou mostrar em entrevista um artefato de investigação (grafo, relatório, linha do tempo, notebook).
1. Pergunte a origem do dado. Só publique dado sintético, público ou de laboratório próprio. Recuse transformar trabalho real (de cliente, empregador ou vítima) em amostra, mesmo "sanitizado", "anonimizado" ou "com nomes borrados": trocar nomes não é anonimização, e há dever de sigilo e LGPD.
2. Exija o rótulo "sintético/fictício" no topo do arquivo ou na legenda da imagem.
3. Desarme todo indicador em texto (`[.]`, `hxxp`). Links para páginas de referência reais podem ficar.
4. Verifique se algum indivíduo privado real aparece nomeado ou perfilado; se sim, corte para a organização e o padrão.
5. Verifique metadados de imagens e PDFs (autor, usuário, caminhos locais). Em PDF, lembre que edições incrementais preservam revisões antigas: reescreva o arquivo (ex.: `qpdf`) e confira de novo.
6. Para currículo e descrições de projeto, escreva ação + ferramenta + resultado + link, sem palavras de excesso de certeza ("especialista", "domínio completo").

## Material de referência

Do original (em inglês):
- [`reference/osint-methodology-checklist.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/reference/osint-methodology-checklist.md): o ciclo de reconhecimento como checklist imprimível.
- [`reference/fraud-pattern-taxonomy.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/reference/fraud-pattern-taxonomy.md): a lista de mecanismos da Fase 5, com a evidência de cada um.

➕ Deste repositório:
- [`../../fichas/registro-recon-osint.md`](../../fichas/registro-recon-osint.md): ficha do ciclo OSINT em pt-BR, com os campos de base legal e cadeia de custódia.
- [`procedimentos/`](procedimentos/): os procedimentos longos acrescentados pelos dias do currículo, um por arquivo.
- [`casos-de-teste.md`](casos-de-teste.md): os casos de teste de cada dia, numerados por dia.

## Skills por setor

Cada uma estende esta skill com o modelo de autorização, a taxonomia, as fontes de evidência e o formato de relatório que um setor específico realmente usa. A skill base continua valendo por baixo.

Do original (em inglês, no repositório da ThiefDroppers):
- [financial-institutions](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/financial-institutions/SKILL.md): operações antifraude de bancos e cooperativas, fintechs, equipes de PLD/FIU.
- [trust-and-safety](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/trust-and-safety/SKILL.md): sites de emprego, marketplaces, apps de relacionamento, aluguel e redes sociais.
- [hr-talent-screening](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/hr-talent-screening/SKILL.md): RH e triagem de candidatos falsos.
- [msp-incident-response](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/msp-incident-response/SKILL.md): MSPs e consultorias de resposta a incidentes em BEC.
- [crypto-vasp](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/crypto-vasp/SKILL.md): exchanges e prestadores de ativos virtuais.
- [law-enforcement](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/law-enforcement/SKILL.md): unidades de fraude e cibercrime.
- [victim-services](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/victim-services/SKILL.md): centrais de apoio a vítimas.
- [corporate-investigations](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/corporate-investigations/SKILL.md): investigação corporativa, escritórios de advocacia e e-discovery.
- [journalism-osint](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/journalism-osint/SKILL.md): jornalismo, checagem de fatos e pesquisa acadêmica.
- [soc-cti](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/industries/soc-cti/SKILL.md): times de SOC e CTI.

➕ Setores brasileiros planejados: ver [`../setores-br/README.md`](../setores-br/README.md).
