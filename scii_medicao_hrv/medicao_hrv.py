# -*- coding: utf-8 -*-
"""
SCII - Módulo de Medição de Variabilidade da Frequência Cardíaca (HRV)

Este script é responsável por simular a coleta de dados de HRV, capturando
a variabilidade da frequência cardíaca (HRV) ao longo do tempo e armazenando
os dados para análise posterior.

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 11 de Agosto de 2025
"""

import json
import time
import datetime
import random
import argparse

def iniciar_medicao_hrv(duracao_segundos, nome_pratica):
    """
    Inicia a medição de HRV por uma duração específica.

    Args:
        duracao_segundos (int): A duração total da medição em segundos.
        nome_pratica (str): O nome da prática que está sendo realizada.

    Returns:
        str: O caminho do arquivo JSON onde os dados foram salvos.
    """
    print(f"Iniciando medição de HRV para a prática: {nome_pratica}")
    print(f"Duração da medição: {duracao_segundos} segundos")

    # Array para armazenar os dados da medição
    dados_medicao = []

    # Simula a coleta de dados por segundo
    for segundo_atual in range(duracao_segundos):
        # Simula a conexão com um sensor de HRV
        # Em uma versão real, aqui seria a chamada para a biblioteca do sensor
        hrv_simulado = simular_leitura_sensor_hrv()

        # Obtém o timestamp atual
        timestamp = datetime.datetime.now().isoformat()

        # Armazena os dados da medição
        dados_medicao.append({
            "timestamp": timestamp,
            "hrv": hrv_simulado
        })

        # Imprime o progresso da medição
        print(f"Segundo {segundo_atual + 1}/{duracao_segundos} - HRV: {hrv_simulado:.2f} ms")

        # Aguarda 1 segundo para a próxima medição
        time.sleep(1)

    print("\nMedição concluída.")

    # Salva os dados em um arquivo JSON
    caminho_arquivo = salvar_dados_em_json(dados_medicao, nome_pratica)

    return caminho_arquivo

def simular_leitura_sensor_hrv():
    """
    Simula a leitura de um sensor de HRV.

    Retorna um valor de HRV simulado em milissegundos (ms).
    Valores típicos de HRV (RMSSD) variam de 20 a 150 ms.

    Returns:
        float: O valor de HRV simulado.
    """
    # Simula uma leitura de HRV com base em um estado de relaxamento
    # ou estresse, com alguma variação aleatória.
    base_hrv = random.uniform(40.0, 90.0)  # Variação entre relaxamento e atividade leve
    variacao_aleatoria = random.uniform(-5.0, 5.0)
    return base_hrv + variacao_aleatoria

def salvar_dados_em_json(dados, nome_pratica):
    """
    Salva os dados da medição em um arquivo JSON.

    O nome do arquivo é gerado com base no nome da prática e na data/hora
    de execução para garantir que cada medição seja única.

    Args:
        dados (list): A lista de dados da medição a serem salvos.
        nome_pratica (str): O nome da prática realizada.

    Returns:
        str: O caminho do arquivo JSON salvo.
    """
    # Gera um nome de arquivo único
    timestamp_arquivo = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"{nome_pratica}_{timestamp_arquivo}.json"

    # Salva o arquivo na mesma pasta do script
    caminho_completo = f"scii_medicao_hrv/{nome_arquivo}"

    # Escreve os dados no arquivo JSON com formatação legível
    with open(caminho_completo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print(f"Dados salvos com sucesso em: {caminho_completo}")
    return caminho_completo

# Exemplo de uso do módulo
if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="SCII - Módulo de Medição de HRV.")
    parser.add_argument("--duracao", type=int, default=10, help="Duração total da medição em segundos.")
    parser.add_argument("--pratica", type=str, default="Ativacao_Aleph", help="Nome da prática a ser realizada.")

    args = parser.parse_args()

    print("--- Módulo de Medição HRV do SCII ---")

    # Inicia a medição com os parâmetros fornecidos (ou os padrões)
    caminho_resultado = iniciar_medicao_hrv(args.duracao, args.pratica)

    print(f"\nProcesso finalizado. O arquivo de resultado está em: {caminho_resultado}")
