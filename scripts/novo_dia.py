"""
novo_dia.py — abre a pasta de um dia novo a partir do modelo.

Uso:
    python scripts/novo_dia.py 2

O que faz:
    1. Procura o dia no mapa (curriculo/mapa-dos-dias.csv).
    2. Cria curriculo/<fase>/dia-NN/README.md já preenchido com
       título, link do original, rank Jutsu e badge do Colab.
    3. NÃO sobrescreve nada que já exista (regra: somar, nunca substituir).

Só stdlib.
"""

import sys
from comum import RAIZ, FASES, ler_mapa, pasta_do_dia, link_original

REPO = "Ridd1kulusC0d3r/investigador-cyber-90-dias"


def rank_jutsu(fase: int) -> str:
    """
    As 7 fases viram ranks do Formato Jutsu.
    Fases 1-2 = D/C (base), 3-4 = B, 5-6 = A, 7 = S (o caso completo).
    """
    return {1: "D", 2: "C", 3: "B", 4: "B", 5: "A", 6: "A", 7: "S"}[fase]


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Uso: python scripts/novo_dia.py <número do dia, 1 a 90>")
        sys.exit(1)

    dia = int(sys.argv[1])
    linha = next((l for l in ler_mapa() if int(l["dia"]) == dia), None)
    if linha is None:
        print(f"Dia {dia} não está no mapa.")
        sys.exit(1)

    fase = int(linha["fase"])
    pasta = pasta_do_dia(dia, fase)
    destino = pasta / "README.md"

    # Regra de ouro do repo: se já existe, não mexe.
    if destino.exists():
        print(f"Já existe: {destino.relative_to(RAIZ)} — nada foi alterado.")
        return

    pasta.mkdir(parents=True, exist_ok=True)
    modelo = (RAIZ / "curriculo" / "_modelo-do-dia.md").read_text(encoding="utf-8")

    caminho_nb = f"curriculo/{FASES[fase][0]}/dia-{dia:02d}/dia-{dia:02d}.ipynb"
    texto = modelo.format(
        dia=dia,
        dia_nn=f"{dia:02d}",
        titulo_ptbr=linha["titulo_ptbr"],
        titulo_original=linha["titulo_original"],
        link_original=link_original(dia, fase),
        fase=fase,
        nome_fase=FASES[fase][2],
        rank=rank_jutsu(fase),
        link_colab=f"https://colab.research.google.com/github/{REPO}/blob/main/{caminho_nb}",
    )
    destino.write_text(texto, encoding="utf-8")
    print(f"Criado: {destino.relative_to(RAIZ)}")
    print("Lembre de mudar o status no mapa-dos-dias.csv e rodar scripts/gerar_indice.py")


if __name__ == "__main__":
    main()
