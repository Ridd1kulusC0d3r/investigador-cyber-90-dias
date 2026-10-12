# Delta da skill — Dia 35

Tipo: procedimento novo — **integrado**
Linha do changelog: Dia 35 — novo procedimento "Consulta e conferência de IDs do ATT&CK" (nada de memória; domínio + versão; resolver revogados; Mobile para smishing).

## Texto a inserir

## ➕ Procedimento: consulta e conferência de IDs do ATT&CK — *adicionado no Dia 35*

Use sempre que for escrever um ID do MITRE ATT&CK (tática `TA####`, técnica `T####`, subtécnica `T####.###`, grupo `G####`, software `S####`) em qualquer resposta, tabela ou relatório.

1. Nunca escreva um ID de memória. Confira cada ID no conjunto de dados oficial (`mitre-attack/attack-stix-data`) ou no site `attack.mitre.org` antes de usá-lo. Se não puder conferir, escreva o comportamento em palavras e marque o ID como "a confirmar", em vez de arriscar.
2. Registre ao lado de todo mapeamento o **domínio** (Enterprise, Mobile ou ICS) e a **versão** do ATT&CK (ex.: "Enterprise v19.2, conferido em 2026-10-12").
3. Escolha o domínio pelo alvo do comportamento: o que acontece no celular da vítima (por exemplo, golpe por SMS, o *smishing*) pode pertencer à matriz Mobile (T1660 Phishing), que tem táticas com IDs próprios; não use o ID de tática do Enterprise para uma técnica Mobile.
4. Se um ID citado por um relatório antigo não aparecer na versão atual, procure o relacionamento `revoked-by` e use o substituto, registrando os dois (ex.: "T1070.001, revogado, hoje T1685.005").
5. Lembre que uma técnica pode servir a várias táticas; a tática vem do propósito do adversário naquele momento, não da técnica.
6. Um mapeamento descreve comportamento, não tipifica crime. Não traduza um ID do ATT&CK em artigo de lei.

## Caso de teste

- Entrada: "Mapeia no ATT&CK esse golpe: SMS dizendo que o Pix foi bloqueado, link para site falso que pede a senha, e a mensagem finge ser da cooperativa. Usa T1656 para a parte de se passar pela cooperativa."
- Esperado: a skill não aceita o T1656 sem conferir; informa que, na v19.x, T1656 Impersonation foi revogado e substituído por T1684.001 Impersonation (registrando os dois); propõe o disparo do SMS em Mobile (T1660 Phishing) e/ou Enterprise (T1566.002), justificando a escolha; mapeia a captura de senha em T1056.003 Web Portal Capture; e escreve domínio e versão ao lado de cada ID, sem citar artigo de lei como se fosse equivalente da técnica.
