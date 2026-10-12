"""
comum.py — pedaços compartilhados pelos scripts do repo.

Só biblioteca padrão (stdlib). Nada para instalar.
"""

import csv          # lê o mapa dos 90 dias
from pathlib import Path  # caminhos que funcionam igual no Windows, Linux e Mac

# Raiz do repositório = a pasta acima de scripts/
RAIZ = Path(__file__).resolve().parent.parent
MAPA = RAIZ / "curriculo" / "mapa-dos-dias.csv"

# Cada fase tem DOIS nomes de pasta:
#   - o nosso (pt-BR), em curriculo/
#   - o do original (ThiefDroppers), em upstream/curriculum/
# Mantemos os dois lado a lado para nunca perder a ligação com o original.
FASES = {
    1: ("fase-1-fundamentos", "phase-1-foundations", "Fundamentos"),
    2: ("fase-2-osint-pegada-digital", "phase-2-osint-digital-footprint", "OSINT e pegada digital"),
    3: ("fase-3-inteligencia-de-ameacas", "phase-3-cyber-threat-intelligence", "Inteligência de ameaças cibernéticas"),
    4: ("fase-4-forense-e-resposta", "phase-4-digital-forensics-incident-investigation", "Forense digital e investigação de incidentes"),
    5: ("fase-5-fraude-e-engenharia-social", "phase-5-fraud-social-engineering", "Fraude, golpes e engenharia social"),
    6: ("fase-6-nuvem-e-sistemas-de-ia", "phase-6-cloud-ai-system-investigation", "Investigação em nuvem e sistemas de IA"),
    7: ("fase-7-capstone-e-carreira", "phase-7-capstone-career", "Capstone e carreira"),
}

URL_ORIGINAL = "https://github.com/thiefdroppers/cyber-investigator-skills/blob/main/curriculum"


def ler_mapa():
    """Devolve a lista de dias (um dicionário por linha do CSV)."""
    with MAPA.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pasta_do_dia(dia: int, fase: int) -> Path:
    """Ex.: curriculo/fase-1-fundamentos/dia-01"""
    return RAIZ / "curriculo" / FASES[fase][0] / f"dia-{dia:02d}"


def link_original(dia: int, fase: int) -> str:
    """Link direto para o dia no repositório original."""
    return f"{URL_ORIGINAL}/{FASES[fase][1]}/day-{dia:02d}.md"
