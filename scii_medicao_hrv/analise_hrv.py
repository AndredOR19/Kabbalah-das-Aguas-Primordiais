# -*- coding: utf-8 -*-
"""
SCII - Módulo de Análise de Assinatura Vibracional (HRV)

Este script analisa os dados de HRV coletados pelo módulo de medição,
compara-os com uma assinatura arquetípica de referência e gera um
relatório de alinhamento.

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 11 de Agosto de 2025
"""

import json
import numpy as np
import argparse

# --- BANCO DE DADOS DE ASSINATURAS ARQUETÍPICAS ---
ASSINATURAS = {
    "Ativacao_Aleph": {
        "hrv_media_ideal": 60.0,
        "desvio_padrao_ideal": 15.0
    },
    "Meditacao_Tiferet": {
        "hrv_media_ideal": 75.0,
        "desvio_padrao_ideal": 12.0
    },
    "Contemplacao_Binah": {
        "hrv_media_ideal": 80.0,
        "desvio_padrao_ideal": 8.0
    },
    "Default": {
        "hrv_media_ideal": 65.0,
        "desvio_padrao_ideal": 10.0
    }
}

def analisar_assinatura_vibracional(caminho_arquivo, assinatura_arquetipica):
    """
    Analisa a assinatura vibracional de uma medição de HRV.

    Args:
        caminho_arquivo (str): O caminho para o arquivo JSON de dados de HRV.
        assinatura_arquetipica (dict): Dicionário com os valores ideais de referência.

    Returns:
        str: O relatório de análise textual.
    """
    print(f"\n--- Iniciando Análise da Assinatura Vibracional ---")
    print(f"Analisando arquivo: {caminho_arquivo}")

    # 1. Ler e carregar o arquivo JSON
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_medicao = json.load(f)
    except FileNotFoundError:
        return "Erro: Arquivo de medição não encontrado."
    except json.JSONDecodeError:
        return "Erro: O arquivo de medição está em um formato JSON inválido."

    # Extrai apenas os valores de HRV para cálculo
    valores_hrv = [medicao['hrv'] for medicao in dados_medicao]

    if not valores_hrv:
        return "Erro: O arquivo de medição não contém dados de HRV."

    # 2. Calcular a média e o desvio padrão
    hrv_media_calculada = np.mean(valores_hrv)
    hrv_desvio_padrao_calculado = np.std(valores_hrv)

    # 3. Comparar com a assinatura arquetípica
    hrv_media_ideal = assinatura_arquetipica.get("hrv_media_ideal", 0)
    hrv_desvio_padrao_ideal = assinatura_arquetipica.get("desvio_padrao_ideal", 0)

    # Define uma margem de tolerância para o alinhamento (ex: 10%)
    margem_tolerancia = 0.10

    # Verifica se a média e o desvio padrão estão dentro da tolerância
    alinhamento_media = abs(hrv_media_calculada - hrv_media_ideal) <= (hrv_media_ideal * margem_tolerancia)
    alinhamento_desvio = abs(hrv_desvio_padrao_calculado - hrv_desvio_padrao_ideal) <= (hrv_desvio_padrao_ideal * margem_tolerancia)

    status_alinhamento = "Alinhado" if alinhamento_media and alinhamento_desvio else "Não Alinhado"

    # 4. Gerar o relatório de análise
    relatorio = f"""
    ==================================================
    RELATÓRIO DE ANÁLISE VIBRACIONAL - SCII
    ==================================================

    [ DADOS CALCULADOS ]
    - Média HRV: {hrv_media_calculada:.2f} ms
    - Desvio Padrão HRV: {hrv_desvio_padrao_calculado:.2f} ms

    [ ASSINATURA ARQUETÍPICA DE REFERÊNCIA ]
    - Média HRV Ideal: {hrv_media_ideal:.2f} ms
    - Desvio Padrão Ideal: {hrv_desvio_padrao_ideal:.2f} ms

    [ AVALIAÇÃO DE ALINHAMENTO ]
    - Status: {status_alinhamento}

    [ FEEDBACK DO SISTEMA ]
    - {gerar_feedback_textual(status_alinhamento)}

    ==================================================
    """

    return relatorio

def gerar_feedback_textual(status):
    """
    Gera um feedback textual com base no status de alinhamento.

    Args:
        status (str): O status de alinhamento ("Alinhado" ou "Não Alinhado").

    Returns:
        str: A mensagem de feedback.
    """
    if status == "Alinhado":
        return "O sistema indica um bom alinhamento com a energia da prática. A ressonância foi estabelecida com sucesso."
    else:
        return "O sistema detectou um desvio da assinatura ideal. Verifique a intenção, o ambiente e o foco durante a prática."

# Exemplo de uso do módulo
if __name__ == "__main__":
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="SCII - Módulo de Análise de Assinatura Vibracional.")
    parser.add_argument("caminho_arquivo", type=str, help="Caminho para o arquivo JSON de medição de HRV.")
    parser.add_argument("--pratica", type=str, default="Default", help="Nome da prática para selecionar a assinatura arquetípica correta.")

    args = parser.parse_args()

    # Seleciona a assinatura arquetípica com base no nome da prática
    assinatura = ASSINATURAS.get(args.pratica, ASSINATURAS["Default"])

    # Analisa os dados do arquivo fornecido
    relatorio_final = analisar_assinatura_vibracional(args.caminho_arquivo, assinatura)

    # Imprime o relatório final
    print(relatorio_final)
