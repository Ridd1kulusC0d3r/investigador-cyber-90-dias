"""
listar_pendencias.py — junta todos os TODOs dos dias em PENDENCIAS.md.

Uso:
    python scripts/listar_pendencias.py

Os TODOs ficam escondidos nos READMEs como comentários HTML
(<!-- TODO jurídico: ... -->), então não aparecem no GitHub.
Este script os reúne num só lugar, por dia, para você conferir na fonte.

Só stdlib.
"""

import re
from comum import RAIZ, ler_mapa, pasta_do_dia

PADRAO = re.compile(r"<!--\s*(TODO[^:]*):\s*(.*?)\s*-->", re.S)


def main():
    linhas = [
        "# Pendências para conferir",
        "",
        "<!-- Arquivo gerado por scripts/listar_pendencias.py. Não edite à mão. -->",
        "",
        "Pontos que os autores dos dias preferiram **não afirmar sem conferir na fonte** "
        "(número de artigo, prazo de resolução, jurisprudência, nome de norma). "
        "Ficam como comentário HTML no README do dia; resolva na fonte oficial, "
        "edite o trecho e apague o comentário.",
        "",
    ]
    total = 0
    for d in ler_mapa():
        n, f = int(d["dia"]), int(d["fase"])
        readme = pasta_do_dia(n, f) / "README.md"
        if not readme.exists():
            continue
        achados = PADRAO.findall(readme.read_text(encoding="utf-8"))
        if not achados:
            continue
        rel = readme.relative_to(RAIZ).as_posix()
        linhas.append(f"## Dia {n:02d} — [{d['titulo_ptbr']}]({rel})")
        linhas.append("")
        for tipo, texto in achados:
            linhas.append(f"- [ ] **{tipo.strip()}**: {' '.join(texto.split())}")
            total += 1
        linhas.append("")
    linhas.insert(4, f"**Total:** {total} pendências.")
    linhas.insert(5, "")
    (RAIZ / "PENDENCIAS.md").write_text("\n".join(linhas), encoding="utf-8")
    print(f"PENDENCIAS.md atualizado — {total} pendências.")


if __name__ == "__main__":
    main()
