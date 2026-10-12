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

➕ **Referências legais brasileiras que a skill deve conhecer:** Código Penal art. 154-A (invasão de dispositivo informático) e art. 147-A (perseguição); LGPD (Lei 13.709/2018), arts. 4º e 7º; Marco Civil da Internet (Lei 12.965/2014), arts. 10 e 22; Código de Processo Penal, arts. 158-A a 158-F (cadeia de custódia). A skill cita esses artigos quando ajudam a explicar uma recusa ou um limite, sem dar parecer jurídico.

## ➕ Procedimento: portão de autorização (4 checagens) — *adicionado no Dia 01*

Use **antes de cada ação** de qualquer outro procedimento: cada consulta, download, login ou busca. Responda às perguntas na ordem; a primeira resposta errada encerra a checagem.

1. Existe autorização **por escrito** de alguém com direito de concedê-la? Se não: **pare**. Peça a autorização ou não faça.
2. A ação está **dentro do escopo escrito**? Se não: **pare**. Autorização não é cheque em branco.
3. A ação significa **entrar em, ou usar credenciais de, um sistema ou conta** a que ninguém deu acesso (mesmo que pertença a um criminoso, mesmo que esteja mal protegido)? Se sim: **pare e escale**. Documente o que foi encontrado, sem acessar, e indique a entrega à autoridade policial.
4. A ação mira **uma pessoa privada** em vez de um padrão ou de um caso atribuído? Se sim: **pare**.
5. Passou nas quatro: prossiga e registre a ação com hora em UTC, método e o hash (SHA-256) do que foi coletado.

Quando o usuário apresentar uma justificativa para pular uma checagem ("é criminoso mesmo", "é para ajudar as vítimas", "só uma olhadinha"), trate isso como sinal para manter a checagem, não para relaxá-la.

## Procedimento: ciclo de reconhecimento OSINT

Use quando pedirem para pesquisar um domínio, uma organização ou outra entidade voltada ao público. Não use em um indivíduo privado sem autorização do caso.
1. Planejar. Escreva a pergunta como uma frase específica. Se não conseguir, peça ao usuário que a restrinja primeiro.
2. Coletar. Use pelo menos 3 tipos de fonte independentes, como WHOIS e DNS, buscadores, registros oficiais ou públicos e capturas arquivadas. Para cada dado, registre o valor, a fonte e a data e hora de acesso.
   - ➕ No Brasil, fontes oficiais frequentes: RDAP do Registro.br (domínios `.br`), consulta pública de CNPJ da Receita Federal, diários oficiais e portais de transparência.
3. Processar. Organize os dados em tabela ou grafo agrupados por entidade, não por fonte.
4. Analisar. Marque cada achado como confirmado (2 ou mais fontes independentes concordam), provável (1 fonte apenas) ou contestado (as fontes divergem).
5. Relatar. Use a mesma palavra de confiança da marcação. Nunca relate como confirmado um achado provável.

## Procedimento: grafo de vínculos (link analysis)

Use quando o pedido envolver relações entre várias entidades: pivô de infraestrutura, mapeamento de quadrilha de fraude ou mapeamento de organização.
1. Faça de cada nó uma entidade concreta: um domínio, IP, certificado, endereço de e-mail, conta ou organização. Nunca use uma categoria como nó.
   - ➕ Entidades típicas de golpes no Brasil: chave Pix (como dado do kit, não da pessoa), número de WhatsApp remetente, encurtador de link, CNPJ citado na isca.
2. Rotule cada aresta com a relação que a produziu, como "certificado TLS compartilhado", "mesmo e-mail de registrante" ou "mesma chave de pagamento". Aresta sem rótulo não é achado.
3. Identifique qualquer hub (um nó com número incomum de conexões) e explique por que ele está conectado. Um provedor de hospedagem ou CDN pode parecer hub só porque muitos sites sem relação entre si o compartilham.
4. Identifique os agrupamentos (clusters) e qualquer nó-ponte que conecte dois deles.
5. Se as entidades não tiverem conexão real, diga isso. Um grafo esparso ou vazio é um resultado honesto.

## Procedimento: triagem de padrão de fraude e golpe

Use quando perguntarem se uma mensagem, anúncio ou caso corresponde a um padrão de golpe conhecido.
1. Verifique no caso cada um destes mecanismos:
   - pagamento antecipado exigido antes de qualquer serviço ou benefício ser entregue
   - urgência, ou pressão para sair da plataforma para um canal não monitorado
   - dados pessoais ou financeiros pedidos antes de qualquer verificação real
   - identidade do remetente ou domínio que não bate com quem ele diz ser
   - pedidos que não combinam com o papel ou a relação declarados
   - ➕ pagamento direcionado a uma chave Pix ou conta de pessoa física diferente da empresa ou instituição que diz cobrar
   - ➕ alegação de "bloqueio", "invasão" ou "regularização" de conta que exige ação imediata por link ou ligação (padrão "falsa central")
2. Marque cada mecanismo como presente ou ausente. Para cada um marcado como presente, cite a linha ou o detalhe que o demonstra. Nunca marque um mecanismo como presente sem essa evidência.
3. Declare o veredito com sua confiança e evidência, por exemplo: "Corresponde ao padrão de taxa antecipada em recrutamento; 3 de 5 mecanismos presentes; evidência: ..." Não escreva "isto é com certeza um golpe" sem citações.
4. Se o caso estiver em andamento e uma pessoa real puder ser prejudicada, diga que esta análise não substitui uma comunicação à autoridade competente, como um centro nacional antifraude ou o time de *trust and safety* da plataforma. Nomeie um, se conseguir identificá-lo para a provável jurisdição ou plataforma do usuário.
   - ➕ No Brasil: o banco ou instituição da vítima (que aciona o MED, Mecanismo Especial de Devolução, em casos de Pix), o boletim de ocorrência na delegacia especializada em crimes cibernéticos do estado ou na delegacia online, e o canal de denúncia da própria plataforma (WhatsApp, Instagram, marketplace).

A taxonomia original, [`reference/fraud-pattern-taxonomy.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/reference/fraud-pattern-taxonomy.md), lista os mecanismos de cada tipo de fraude com a evidência que mostra cada um. ➕ A extensão brasileira será construída na Fase 5 (Dias 65 a 76).

## Procedimento: verificação de texto gerado por máquina

Use quando uma mensagem de golpe, phishing ou falsa identidade puder ter sido escrita com um LLM, por exemplo quando uma isca é fluente porém genérica, ou quando muitas denúncias trazem redação quase idêntica. As categorias vêm da página [*Signs of AI writing*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) da Wikipédia, mantida pelo WikiProject AI Cleanup.
1. Procure primeiro resíduo de chatbot, porque é o sinal mais certo: texto destinado a quem rodou o modelo, como "Claro! Aqui está um...", "Espero que isso ajude", "Gostaria que eu...", "Como modelo de linguagem de IA" ou marcadores não preenchidos como "[Seu Nome]" ou "[Empresa]". Cite cada ocorrência.
2. Procure encenação: frases que sinalizam importância em vez de acrescentar um fato. Exemplos são contrastes do tipo "não apenas X, mas Y", frases de fechamento de uma linha que repetem a anterior e preâmbulos como "Veja o que você precisa saber".
3. Procure ritmo por regra: listas de três onde o sentido não precisa de três, e travessões ligando a maioria das orações.
4. Procure inflação e linguagem de venda: uma oferta comum descrita como "uma oportunidade empolgante", "um passo decisivo na sua carreira" ou "uma equipe vibrante e dinâmica", e verbos como "atua como" ou "conta com" onde "é" ou "tem" bastariam.
5. Procure autoridade emprestada: "especialistas concordam", "líderes do setor confiam em nós" ou uma lista de veículos ou parceiros conhecidos sem link ou detalhe verificável.
6. Registre cada sinal com o texto citado e a categoria. Conte as categorias presentes, não as frases individuais.
7. Relate o resultado como sinal de apoio, com sua confiança. Resíduo de chatbot sozinho sustenta "provavelmente gerado por máquina". Sem resíduo, exija 3 ou mais das outras categorias; menos que isso não é achado. Exemplo: "Encenação, ritmo por regra e inflação presentes, sem resíduo; provavelmente gerado por máquina; citações: ..."
8. Mantenha esta verificação separada do veredito de golpe. Texto gerado por máquina mostra como a mensagem foi escrita, não se ela é golpe: empresas legítimas usam as mesmas ferramentas, e pessoas que escrevem de modo formal, incluindo não nativos e redatores de modelos prontos, produzem alguns desses padrões. O veredito de golpe continua dependendo dos mecanismos do procedimento de triagem. A verificação é mais útil para ligar casos: resíduo idêntico ou redação gerada idêntica em denúncias separadas pode ser uma aresta rotulada em um grafo de vínculos.

## Procedimento: informe de inteligência ou relatório de caso

1. Abra com o veredito ou achado em uma frase, no nível de confiança correto.
2. Liste a evidência de apoio. Cada item remete a uma fonte e a um horário.
3. Diga o que mudaria o achado: o que não está verificado e como seria uma fonte contraditória.
4. Rotule qualquer especulação como especulação.

## Material de referência

Do original (em inglês):
- [`reference/osint-methodology-checklist.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/reference/osint-methodology-checklist.md): o ciclo de reconhecimento como checklist imprimível.
- [`reference/fraud-pattern-taxonomy.md`](https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/ai-agent-skills/reference/fraud-pattern-taxonomy.md): a lista de mecanismos da Fase 5, com a evidência de cada um.

➕ Deste repositório:
- [`../../fichas/registro-recon-osint.md`](../../fichas/registro-recon-osint.md): ficha do ciclo OSINT em pt-BR, com os campos de base legal e cadeia de custódia.

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
