"""
verificar_repo.py — confere se cada dia escrito segue o guia de produção.

Uso:
    python scripts/verificar_repo.py          # todos os dias que têm pasta
    python scripts/verificar_repo.py 2 3 4    # só esses

Para cada dia confere:
    1. README.md, dia-NN.ipynb e _skill-delta.md existem;
    2. as seções obrigatórias do guia estão no README;
    3. o notebook é um JSON válido;
    4. os links relativos do README apontam para arquivos que existem;
    5. fidelidade ao original (heurística): o README tem pelo menos tantos
       blocos de código e linhas de tabela quanto o original, e não é
       muito mais curto que ele.

Não roda os notebooks (para isso, use testar_notebook.py).
Só stdlib.
"""

import json
import re
import sys
from comum import FASES, RAIZ, ler_mapa, pasta_do_dia

SECOES = ["## 🎬", "## 📖 Conceito", "## 📚 Recursos", "## 🛠️", "## ✅ Checkpoint",
          "## ⚖️", "## 🧠", "## 🤖", "## 💡", "## 📝"]


def contar(texto):
    blocos = texto.count("```") // 2
    tabelas = sum(1 for l in texto.splitlines() if l.strip().startswith("|"))
    return blocos, tabelas


def verificar(dia, fase):
    problemas = []
    pasta = pasta_do_dia(dia, fase)
    readme = pasta / "README.md"
    nb = pasta / f"dia-{dia:02d}.ipynb"
    delta = pasta / "_skill-delta.md"
    for arq in (readme, nb, delta):
        if not arq.exists():
            problemas.append(f"falta {arq.name}")
    if not readme.exists():
        return problemas

    texto = readme.read_text(encoding="utf-8")
    for s in SECOES:
        if s not in texto:
            problemas.append(f"seção ausente: {s}")
    if "TODO" in texto:
        problemas.append(f"{texto.count('TODO')} TODO(s) no README")

    if nb.exists():
        try:
            json.loads(nb.read_text(encoding="utf-8"))
        except ValueError as e:
            problemas.append(f"notebook inválido: {e}")

    # Links dentro de blocos de código (``` ... ```) são exemplo, não link de verdade.
    sem_codigo = re.sub(r"```.*?```", "", texto, flags=re.S)
    for link in re.findall(r"\]\(([^)#\s]+)", sem_codigo):
        if link.startswith(("http", "mailto")):
            continue
        if not (pasta / link).exists():
            problemas.append(f"link quebrado: {link}")

    original = RAIZ / "upstream" / "curriculum" / FASES[fase][1] / f"day-{dia:02d}.md"
    if original.exists():
        o = original.read_text(encoding="utf-8")
        ob, ot = contar(o)
        rb, rt = contar(texto)
        if rb < ob:
            problemas.append(f"blocos de código: {rb} no README < {ob} no original")
        if rt < ot:
            problemas.append(f"linhas de tabela: {rt} no README < {ot} no original")
        if len(texto) < 0.95 * len(o):
            problemas.append(f"README ({len(texto)} car.) mais curto que o original ({len(o)} car.)")
    return problemas


def main():
    pedidos = {int(a) for a in sys.argv[1:]}
    total = com_problema = 0
    for linha in ler_mapa():
        dia, fase = int(linha["dia"]), int(linha["fase"])
        if pedidos and dia not in pedidos:
            continue
        if not pedidos and not pasta_do_dia(dia, fase).exists():
            continue
        total += 1
        p = verificar(dia, fase)
        if p:
            com_problema += 1
            print(f"⚠️  Dia {dia:02d}: " + "; ".join(p))
        else:
            print(f"✅ Dia {dia:02d}")
    print(f"\n{total - com_problema}/{total} dias sem pendências.")
    sys.exit(1 if com_problema else 0)


if __name__ == "__main__":
    main()
