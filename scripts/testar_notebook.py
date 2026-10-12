"""
testar_notebook.py — roda todas as células de código de um notebook, fora do Colab.

Uso:
    python scripts/testar_notebook.py curriculo/fase-1-fundamentos/dia-01/dia-01.ipynb [...]

Simula o aluno:
    - input() responde automaticamente (alterna "S", "1", "a", "N"...);
    - google.colab não existe (as células precisam tratar o ImportError);
    - a rede pode falhar: células que baixam algo precisam ter plano B offline;
    - linhas que começam com "!" ou "%" (comandos de shell do Colab) são puladas.

Roda cada notebook numa pasta temporária, para não sujar o repositório.
Sai com código 1 se alguma célula der erro.

Só stdlib.
"""

import builtins
import contextlib
import io
import itertools
import json
import os
import sys
import tempfile
import traceback
from pathlib import Path

RESPOSTAS = ["S", "1", "a", "N", "2", "b", "sim", "3", "c", "0"]


def rodar(caminho: Path) -> bool:
    nb = json.loads(caminho.read_text(encoding="utf-8"))
    respostas = itertools.cycle(RESPOSTAS)
    original_input = builtins.input
    builtins.input = lambda prompt="": next(respostas)
    escopo = {"__name__": "__main__"}
    ok = True
    pasta_antes = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            n = 0
            for i, celula in enumerate(nb["cells"], start=1):
                if celula["cell_type"] != "code":
                    continue
                n += 1
                linhas = celula["source"] if isinstance(celula["source"], list) else celula["source"].splitlines(True)
                codigo = "".join(l for l in linhas if not l.lstrip().startswith(("!", "%")))
                saida = io.StringIO()
                try:
                    with contextlib.redirect_stdout(saida):
                        exec(compile(codigo, f"{caminho.name}[célula {i}]", "exec"), escopo)
                except SystemExit:
                    pass
                except Exception:
                    ok = False
                    print(f"  ❌ célula {i} falhou:")
                    print("     " + traceback.format_exc().replace("\n", "\n     "))
            print(f"{'✅' if ok else '❌'} {caminho} — {n} células de código")
        finally:
            os.chdir(pasta_antes)
            builtins.input = original_input
    return ok


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/testar_notebook.py <notebook.ipynb> [...]")
        sys.exit(1)
    resultados = [rodar(Path(p).resolve()) for p in sys.argv[1:]]
    sys.exit(0 if all(resultados) else 1)


if __name__ == "__main__":
    main()
