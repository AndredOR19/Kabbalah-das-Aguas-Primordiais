"""
Módulo de Astrologia Básica para o SCII.

Este módulo expõe uma função `calcular_mapa_basico` que recebe data, hora e local
de nascimento e retorna um mapeamento simples das regências planetárias. Para
prototipagem, utiliza um algoritmo simplificado ou valores fixos. Para uso real,
integre uma biblioteca de efemérides ou API externa.
"""

from datetime import datetime
from typing import Dict

def calcular_mapa_basico(data: str, hora: str = "12:00", local: str = "") -> Dict:
    """
    Extrai regências planetárias essenciais a partir de data e hora.

    Args:
        data (str): Data de nascimento no formato DD/MM/AAAA.
        hora (str): Hora de nascimento no formato HH:MM (opcional).
        local (str): Localidade (opcional).

    Returns:
        Dict: Signos solares, lunares e ascendente simplificados.
    """
    # Esta função é apenas uma aproximação. Em um MVP real, utilize
    # uma biblioteca como `astral` ou APIs de astrologia.
    try:
        dia, mes, ano = map(int, data.split('/'))
    except Exception:
        raise ValueError("Data deve estar no formato DD/MM/AAAA")

    # Determinação simplificada do signo solar pelo mês.
    signos = [
        (20, "Capricórnio"), (19, "Aquário"), (20, "Peixes"), (20, "Áries"),
        (20, "Touro"), (20, "Gêmeos"), (22, "Câncer"), (22, "Leão"),
        (22, "Virgem"), (22, "Libra"), (21, "Escorpião"), (21, "Sagitário"),
        (19, "Capricórnio"),
    ]
    signo_solar = "Capricórnio"
    if 1 <= mes <= 12:
        limite, signo_solar = signos[mes - 1]
        if dia > limite:
            signo_solar = signos[mes][1]

    # Para simplificar, definimos o signo lunar como oposto e ascendente como o mesmo.
    opostos = {
        "Áries": "Libra", "Touro": "Escorpião", "Gêmeos": "Sagitário",
        "Câncer": "Capricórnio", "Leão": "Aquário", "Virgem": "Peixes",
        "Libra": "Áries", "Escorpião": "Touro", "Sagitário": "Gêmeos",
        "Capricórnio": "Câncer", "Aquário": "Leão", "Peixes": "Virgem",
    }
    signo_lunar = opostos.get(signo_solar, "Peixes")
    ascendente = signo_solar

    # Regente do dia baseado na data (segunda-feira = Lua, etc.)
    regentes = ["Sol", "Lua", "Marte", "Mercúrio", "Júpiter", "Vênus", "Saturno"]
    try:
        data_obj = datetime(ano, mes, dia)
        regente_dia = regentes[data_obj.weekday()]
    except Exception:
        regente_dia = "Sol"

    return {
        'sol': signo_solar,
        'lua': signo_lunar,
        'ascendente': ascendente,
        'regente_dia': regente_dia,
    }