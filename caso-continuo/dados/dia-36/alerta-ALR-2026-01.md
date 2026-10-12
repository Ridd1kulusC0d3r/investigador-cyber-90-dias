<!-- Documento 100% FICTÍCIO da Operação Isca (Investigador Cyber 90 Dias, Dia 36).
     Domínios .example (RFC 2606), IPs de documentação (RFC 5737), telefones no formato inexistente +55 00.
     Nenhuma pessoa, empresa ou caso real. -->

# ALR-2026-01 — Alerta conjunto: campanha "Pix bloqueado" (IscaKit) contra cooperativas de crédito

**Emitido por:** Vigia (MSSP) com o grupo de segurança das cooperativas mineiras (fictício)
**Data:** 2026-10-12 · **TLP:AMBER** · **Versão:** 1.0

## Resumo

[S01] Entre 5 e 11 de outubro de 2026, cinco cooperativas de crédito de Minas Gerais (Serra Azul, CoopVale, CredMinas, Unicoop Sul e Cooperouro) foram alvo de uma mesma campanha de phishing por SMS que se passa pela própria cooperativa.
[S02] O conjunto de ferramentas usado, apelidado internamente de IscaKit, é um kit de phishing conhecido por oferecer módulos de captura de código de SMS (OTP) e de envio automático de mensagens por WhatsApp.

## Atividade observada

[S03] Os operadores registraram domínios imitação para cada cooperativa, como serraazul-pix[.]example e coopvale-pix[.]example, entre um e dez dias antes de cada disparo.
[S04] Para cada domínio, os operadores obtiveram um certificado TLS gratuito de uma autoridade certificadora pública, em geral na véspera do disparo.
[S05] Os operadores enviaram SMS aos celulares de cooperados com o texto "sua chave Pix foi bloqueada por segurança" e um link encurtado (lnk[.]example/sa7) que redirecionava para o domínio imitação.
[S06] A página servida no domínio imitação reproduzia o internet banking da cooperativa e enviava ao servidor dos operadores o usuário e a senha digitados pelo cooperado.
[S07] Com as credenciais capturadas, os operadores entraram no internet banking legítimo da cooperativa e iniciaram transferências Pix para contas de terceiros.
[S08] Na Serra Azul, três cooperados tiveram transferências Pix não reconhecidas em 5 de outubro.
[S09] Os operadores mantiveram presença na infraestrutura ao longo da semana.
[S10] Um perfil de Instagram (@serraazul.oficial), criado pelos operadores, respondia a reclamações de cooperados com o mesmo link do SMS.
[S11] A página falsa usa um arquivo JavaScript em que aparece o comentário "// pescador", o que reforça que se trata do mesmo kit em todos os domínios.

## Recomendações

[S12] As cooperativas devem bloquear os domínios listados no anexo e orientar os cooperados a nunca digitar a senha a partir de links recebidos por SMS.
