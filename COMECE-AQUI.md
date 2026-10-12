# 🚀 Comece aqui

## Para estudar (5 minutos)

1. Leia a seção **Ética e regras do jogo** do [README](README.md).
2. Abra o [Dia 01](curriculo/fase-1-fundamentos/dia-01/).
3. Clique no botão **Open in Colab** do dia. Rode as células de cima para baixo com **Shift+Enter**. Não precisa instalar nada.
4. Faça a prática até ter o artefato do dia. Só então o dia conta.

## Para manter o seu repositório

Os 90 dias já estão escritos. Você precisa só de Python 3 instalado. Ao estudar cada dia:

```bash
# 1. Faça a prática do dia (README + notebook) e registre o artefato com hash e hora UTC
python scripts/registrar_evidencia.py notas/meu-artefato.png "descrição"

# 2. No curriculo/mapa-dos-dias.csv, mude o status do dia de "rascunho" para "estudado"
#    (rascunho = conteúdo pronto; estudado = você fez a prática e o artefato existe)

# 3. Atualize o índice com a barra de progresso
python scripts/gerar_indice.py

# 4. Ao reescrever ou acrescentar algo num dia, siga o guia de produção:
#    curriculo/_GUIA-DE-PRODUCAO.md
#    (para um dia novo do zero, python scripts/novo_dia.py NN cria a pasta sem sobrescrever nada)
```

Para trazer as atualizações do original da ThiefDroppers:

```bash
git submodule update --init --remote upstream
```

## Checklist de um dia completo

- [ ] Tradução fiel do original (Conceito, Recursos, Prática, Checkpoint)
- [ ] 🎬 Abertura do caso (Operação Isca)
- [ ] ➕ Prática BR
- [ ] ⚖️ Camada jurídica BR
- [ ] 🧠 Camada 8
- [ ] 🤖 Skill do dia + linha no `CHANGELOG-DA-SKILL.md`
- [ ] 💡 Inovação OSINT do dia
- [ ] 📓 Notebook Colab testado
- [ ] Artefato produzido e registrado

## Verificações (rode antes de cada commit)

```bash
python scripts/verificar_repo.py          # estrutura, seções, links e fidelidade ao original
python scripts/testar_notebook.py curriculo/fase-1-fundamentos/dia-01/dia-01.ipynb
python scripts/listar_pendencias.py       # atualiza PENDENCIAS.md
```
