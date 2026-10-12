"""
gerar_indice.py — reescreve curriculo/README.md a partir do mapa dos 90 dias.

Uso:
    python scripts/gerar_indice.py

Mostra, por fase, cada dia com: status, título em pt-BR, link para o
nosso estudo (se já existe) e link para o original.

Só stdlib.
"""

from comum import RAIZ, FASES, ler_mapa, pasta_do_dia, link_original

ICONE = {"estudado": "✅", "em-andamento": "🟡", "pendente": "⬜"}


def main():
    dias = ler_mapa()
    feitos = sum(1 for d in dias if d["status"] == "estudado")

    # Barra de progresso em texto: 20 blocos = 90 dias
    cheios = round(feitos / len(dias) * 20)
    barra = "█" * cheios + "░" * (20 - cheios)

    linhas = [
        "# Currículo — os 90 dias",
        "",
        "<!-- Arquivo gerado por scripts/gerar_indice.py. Edite o mapa-dos-dias.csv, não este arquivo. -->",
        "",
        f"**Progresso:** `{barra}` {feitos}/{len(dias)} dias",
        "",
        "Legenda: ✅ estudado · 🟡 em andamento · ⬜ pendente. "
        "Cada dia segue o [`_modelo-do-dia.md`](_modelo-do-dia.md).",
        "",
    ]

    for num, (pasta_br, _, nome) in FASES.items():
        da_fase = [d for d in dias if int(d["fase"]) == num]
        primeiro, ultimo = da_fase[0]["dia"], da_fase[-1]["dia"]
        linhas += [
            f"## Fase {num}. {nome} (dias {primeiro} a {ultimo})",
            "",
            "| | Dia | Tema | Original |",
            "|---|---|---|---|",
        ]
        for d in da_fase:
            n = int(d["dia"])
            pasta = pasta_do_dia(n, num)
            tema = d["titulo_ptbr"]
            if (pasta / "README.md").exists():
                tema = f"[{tema}]({pasta_br}/dia-{n:02d}/)"
            linhas.append(
                f"| {ICONE.get(d['status'], '⬜')} | {n:02d} | {tema} | "
                f"[EN]({link_original(n, num)}) |"
            )
        linhas.append("")

    (RAIZ / "curriculo" / "README.md").write_text("\n".join(linhas), encoding="utf-8")
    print(f"curriculo/README.md atualizado — {feitos}/{len(dias)} estudados.")


if __name__ == "__main__":
    main()
