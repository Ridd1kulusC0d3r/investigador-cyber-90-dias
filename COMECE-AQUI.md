# 🚀 Comece aqui

## Para estudar (5 minutos)

1. Leia a seção **Ética e regras do jogo** do [README](README.md).
2. Abra o [Dia 01](curriculo/fase-1-fundamentos/dia-01/).
3. Clique no botão **Open in Colab** do dia. Rode as células de cima para baixo com **Shift+Enter**. Não precisa instalar nada.
4. Faça a prática até ter o artefato do dia. Só então o dia conta.

## Para manter o seu repositório (quando você estudar um dia novo)

Você precisa só de Python 3 instalado. Nada mais.

```bash
# 1. Cria a pasta do dia 2 já com título, link do original e badge do Colab
python scripts/novo_dia.py 2

# 2. Estude, traduza e some a camada BR no README.md que foi criado

# 3. No curriculo/mapa-dos-dias.csv, mude o status do dia para "estudado"

# 4. Atualiza o índice com a barra de progresso
python scripts/gerar_indice.py

# 5. Registra o hash e a hora UTC de qualquer evidência/artefato
python scripts/registrar_evidencia.py notas/meu-artefato.png "descrição"
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
