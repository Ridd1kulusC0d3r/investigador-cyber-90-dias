"""
registrar_evidencia.py — cadeia de custódia mínima, em uma linha de comando.

Uso:
    python scripts/registrar_evidencia.py caminho/do/arquivo "descrição curta"

O que faz:
    1. Calcula o SHA-256 do arquivo (a "impressão digital" dele).
    2. Anota a hora em UTC (fuso neutro, o mesmo para qualquer perito).
    3. Acrescenta uma linha em notas/registro-de-custodia.csv.

Por que importa: se o arquivo mudar 1 byte, o hash muda inteiro.
Quem receber sua evidência recalcula o hash e confere que é o mesmo arquivo.
É o começo do que o CPP chama de cadeia de custódia (arts. 158-A a 158-F).

Só stdlib.
"""

import csv
import hashlib                       # SHA-256
import sys
from datetime import datetime, timezone
from pathlib import Path

from comum import RAIZ

REGISTRO = RAIZ / "notas" / "registro-de-custodia.csv"
CAMPOS = ["utc", "arquivo", "sha256", "bytes", "descricao"]


def sha256_do_arquivo(caminho: Path) -> str:
    """Lê o arquivo em pedaços de 64 KB (funciona até com arquivos enormes)."""
    h = hashlib.sha256()
    with caminho.open("rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()


def main():
    if len(sys.argv) < 2:
        print('Uso: python scripts/registrar_evidencia.py <arquivo> "descrição"')
        sys.exit(1)

    arquivo = Path(sys.argv[1])
    if not arquivo.is_file():
        print(f"Arquivo não encontrado: {arquivo}")
        sys.exit(1)

    linha = {
        # isoformat com 'Z' no fim = UTC, sem ambiguidade de fuso
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "arquivo": str(arquivo),
        "sha256": sha256_do_arquivo(arquivo),
        "bytes": arquivo.stat().st_size,
        "descricao": " ".join(sys.argv[2:]) or "(sem descrição)",
    }

    REGISTRO.parent.mkdir(exist_ok=True)
    novo = not REGISTRO.exists()
    # "a" = append: nunca apaga o que já foi registrado
    with REGISTRO.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if novo:
            w.writeheader()
        w.writerow(linha)

    print(f"{linha['utc']}  {linha['sha256']}  {arquivo}")


if __name__ == "__main__":
    main()
