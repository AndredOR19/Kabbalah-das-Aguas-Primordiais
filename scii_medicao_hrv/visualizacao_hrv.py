# -*- coding: utf-8 -*-
"""
SCII - Módulo de Visualização de Dados de HRV

Este script lê um arquivo JSON de medição de HRV e gera um gráfico
de linha para visualizar a flutuação da variabilidade da frequência
cardíaca ao longo do tempo.

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 11 de Agosto de 2025
"""

import json
import argparse
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def visualizar_dados_hrv(caminho_arquivo):
    """
    Gera e salva um gráfico a partir de um arquivo de dados de HRV.

    Args:
        caminho_arquivo (str): O caminho para o arquivo JSON de medição.
    """
    print(f"\n--- Gerando Gráfico de Visualização de HRV ---")
    print(f"Lendo dados de: {caminho_arquivo}")

    # 1. Ler e carregar o arquivo JSON
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_medicao = json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo de medição não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro: O arquivo de medição está em um formato JSON inválido.")
        return

    if not dados_medicao:
        print("Erro: O arquivo de medição não contém dados.")
        return

    # 2. Extrair dados para os eixos do gráfico
    timestamps_str = [item['timestamp'] for item in dados_medicao]
    valores_hrv = [item['hrv'] for item in dados_medicao]

    # Converte as strings de timestamp para objetos datetime
    timestamps_dt = [datetime.fromisoformat(ts) for ts in timestamps_str]

    # 3. Configurar e gerar o gráfico
    plt.style.use('seaborn-v0_8-darkgrid') # Estilo visual do gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plotar os dados
    ax.plot(timestamps_dt, valores_hrv, marker='o', linestyle='-', color='cyan', label='HRV (ms)')

    # Formatar o eixo X para mostrar a hora de forma legível
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")

    # Adicionar títulos e legendas
    nome_pratica = os.path.basename(caminho_arquivo).split('_')[0]
    data_medicao = timestamps_dt[0].strftime("%Y-%m-%d")
    ax.set_title(f'Assinatura Vibracional (HRV) - Prática: {nome_pratica}\nData: {data_medicao}', fontsize=16, color='white')
    ax.set_xlabel('Tempo (HH:MM:SS)', fontsize=12, color='white')
    ax.set_ylabel('HRV (RMSSD em ms)', fontsize=12, color='white')
    ax.legend()
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Mudar a cor do fundo e dos eixos
    fig.patch.set_facecolor('#2c2c2c')
    ax.set_facecolor('#3c3c3c')
    ax.tick_params(colors='white', which='both')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')

    # 4. Salvar o gráfico como uma imagem
    caminho_grafico = caminho_arquivo.replace('.json', '_grafico.png')
    plt.savefig(caminho_grafico, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())

    print(f"Gráfico salvo com sucesso em: {caminho_grafico}")
    plt.close()

# Exemplo de uso do módulo
if __name__ == "__main__":
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="SCII - Módulo de Visualização de Dados de HRV.")
    parser.add_argument("caminho_arquivo", type=str, help="Caminho para o arquivo JSON de medição de HRV.")

    args = parser.parse_args()

    # Gera o gráfico a partir do arquivo fornecido
    visualizar_dados_hrv(args.caminho_arquivo)
