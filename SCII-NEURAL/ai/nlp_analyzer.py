"""
Analisador de Linguagem Natural Espiritual.

Este módulo oferece uma função `extrair_padroes_vibrationais` que
identifica arquétipos ou padrões vibracionais em um texto. A versão inicial
conta apenas a frequência de palavras-chave predefinidas; futuras iterações
podem usar modelos de PLN mais sofisticados.
"""

from typing import Dict

def extrair_padroes_vibrationais(texto: str) -> Dict:
    """
    Identifica arquétipos e desequilíbrios através da linguagem.

    Args:
        texto (str): Texto fornecido pelo usuário.

    Returns:
        Dict: Dados com arquétipo dominante, sefirot ativadas e palavras chave.
    """
    texto_lower = texto.lower()
    palavras_chave = []
    arquetipo = "Neutro"
    sefirot = []

    # Exemplos de gatilhos simples
    if "julgamento" in texto_lower:
        arquetipo = "Geburah"
        sefirot.append("Geburah")
        palavras_chave.append("julgamento")
    if "amor" in texto_lower:
        arquetipo = "Chesed"
        sefirot.append("Chesed")
        palavras_chave.append("amor")

    return {
        'arquetipo_dominante': arquetipo,
        'sefirot_ativadas': sefirot,
        'nivel_equilibrio': 0.5,
        'palavras_chave': palavras_chave,
    }