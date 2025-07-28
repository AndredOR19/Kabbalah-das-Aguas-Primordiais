"""
Módulo de Diagnóstico do SCII.

Coordena o processamento das informações de entrada (nome, data, sintomas) através
dos módulos de gematria e astrologia, realiza mapeamentos simplificados com as
bases de dados de sintomas e retorna um dicionário com o diagnóstico, letras
desequilibradas, sefirot afetadas e ritual sugerido.
"""
from typing import Dict, List

from .gematria import GematriaCalculator
from .astrology import calcular_mapa_basico
import json
import os

# Caminho para a base de dados no mesmo pacote.
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def _carregar_mapa_sintomas() -> Dict:
    """Carrega o mapeamento de sintomas para letras e sefirot."""
    path = os.path.join(BASE_DIR, "symptoms_map.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def diagnosticar_scii(input_data: Dict) -> Dict:
    """
    Processa dados através da malha SCII simplificada.

    Args:
        input_data (dict): Deve conter 'nome', 'data_nascimento' e 'sintomas' (lista).

    Returns:
        dict: Informações de diagnóstico e ritual.
    """
    nome = input_data.get("nome", "")
    data_nascimento = input_data.get("data_nascimento", "")
    sintomas: List[str] = input_data.get("sintomas", [])

    gematria = GematriaCalculator()
    gematria_result = gematria.nome_para_hebraico(nome)
    astrologia_result = calcular_mapa_basico(data_nascimento) if data_nascimento else {}

    sintomas_map = _carregar_mapa_sintomas()

    letras_desequilibradas: List[str] = []
    sefirot_afetadas: List[str] = []
    rituais: List[str] = []

    for sintoma in sintomas:
        chave = sintoma.lower()
        if chave in sintomas_map:
            entry = sintomas_map[chave]
            letras_desequilibradas.extend(entry.get("letters", []))
            sefirot_afetadas.extend(entry.get("sefirot", []))
            ritual = entry.get("ritual")
            if ritual:
                rituais.append(ritual)

    # Se nada encontrado, sugere letra dominante como equilíbrio.
    if not letras_desequilibradas and gematria_result.get("letra_dominante"):
        letras_desequilibradas.append(gematria_result["letra_dominante"]["letra"])
    if not sefirot_afetadas and gematria_result.get("sefira_correspondente"):
        sefirot_afetadas.append(gematria_result["sefira_correspondente"]["nome"])

    return {
        'letras_desequilibradas': list(set(letras_desequilibradas)),
        'sefirot_afetadas': list(set(sefirot_afetadas)),
        'rituais': rituais or ["Medite com a letra dominante e visualize equilíbrio."],
        'gematria': gematria_result,
        'astrologia': astrologia_result,
    }