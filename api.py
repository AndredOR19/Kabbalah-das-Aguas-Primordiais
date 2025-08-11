# -*- coding: utf-8 -*-
"""
SCII - API Oracular Universal

Este script cria uma API web usando Flask para expor o ciclo de
calibração de HRV como um serviço acessível pela rede. Ele serve como
a espinha dorsal para futuras aplicações web e móveis.

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 12 de Agosto de 2025
"""

from flask import Flask, request, jsonify
import subprocess
import json
import os

# Inicializa a aplicação Flask
app = Flask(__name__)

# --- ENDPOINT PRINCIPAL DA API ---

@app.route('/api/calibrar', methods=['POST'])
def calibrar_pratica():
    """
    Endpoint para executar o ciclo completo de calibração de HRV.

    Recebe um JSON com os parâmetros da prática e retorna um JSON
    com o resultado completo da análise e feedback.

    JSON de Entrada (Exemplo):
    {
        "duracao": 20,
        "pratica": "Meditacao_Tiferet"
    }

    JSON de Saída (Exemplo):
    {
        "status": "sucesso",
        "relatorio_analise": "... texto do relatório ...",
        "feedback_pratico": "... texto do feedback ...",
        "caminho_grafico": "scii_medicao_hrv/Meditacao_Tiferet_..._grafico.png"
    }
    """
    print("Recebida requisição em /api/calibrar")

    # 1. Validar a entrada
    dados_entrada = request.json
    if not dados_entrada or 'duracao' not in dados_entrada or 'pratica' not in dados_entrada:
        return jsonify({"status": "erro", "mensagem": "Parâmetros 'duracao' e 'pratica' são obrigatórios."}), 400

    duracao = dados_entrada['duracao']
    pratica = dados_entrada['pratica']

    try:
        # --- ETAPA 1: MEDIÇÃO ---
        # Executa o script de medição como um processo separado
        # para obter o nome do arquivo de resultado dinamicamente.
        resultado_medicao = subprocess.run(
            ['python3', 'scii_medicao_hrv/medicao_hrv.py', f'--duracao={duracao}', f'--pratica={pratica}'],
            capture_output=True, text=True, check=True
        )
        # Extrai o caminho do arquivo da última linha da saída
        caminho_arquivo_medicao = resultado_medicao.stdout.strip().split('\n')[-1].split(': ')[-1]
        print(f"Medição concluída. Arquivo gerado: {caminho_arquivo_medicao}")

        # --- ETAPA 2: ANÁLISE ---
        resultado_analise = subprocess.run(
            ['python3', 'scii_medicao_hrv/analise_hrv.py', caminho_arquivo_medicao, f'--pratica={pratica}'],
            capture_output=True, text=True, check=True
        )
        relatorio_analise = resultado_analise.stdout
        print("Análise concluída.")

        # --- ETAPA 3: FEEDBACK ---
        resultado_feedback = subprocess.run(
            ['python3', 'scii_medicao_hrv/feedback_pratico.py', f'--pratica={pratica}'],
            input=relatorio_analise, capture_output=True, text=True, check=True
        )
        feedback_pratico = resultado_feedback.stdout
        print("Feedback gerado.")

        # --- ETAPA 4: VISUALIZAÇÃO ---
        subprocess.run(
            ['python3', 'scii_medicao_hrv/visualizacao_hrv.py', caminho_arquivo_medicao],
            capture_output=True, text=True, check=True
        )
        caminho_grafico = caminho_arquivo_medicao.replace('.json', '_grafico.png')
        print(f"Visualização gerada: {caminho_grafico}")

        # 5. Montar a resposta final
        resposta = {
            "status": "sucesso",
            "relatorio_analise": relatorio_analise,
            "feedback_pratico": feedback_pratico,
            "caminho_grafico": caminho_grafico
        }
        return jsonify(resposta), 200

    except subprocess.CalledProcessError as e:
        # Se qualquer um dos scripts falhar, retorna um erro detalhado
        print(f"Erro ao executar subprocesso: {e.stderr}")
        return jsonify({"status": "erro", "mensagem": "Falha ao executar o ciclo de calibração.", "detalhes": e.stderr}), 500
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        return jsonify({"status": "erro", "mensagem": "Ocorreu um erro inesperado no servidor.", "detalhes": str(e)}), 500

# --- Rota de Teste ---

@app.route('/')
def index():
    """Rota principal para verificar se a API está no ar."""
    return "API do Oráculo Universal SCII está no ar. Use o endpoint /api/calibrar para interagir."

# --- Execução da API ---

if __name__ == '__main__':
    # Executa o servidor Flask. O host '0.0.0.0' torna a API acessível
    # a partir de outras máquinas na mesma rede.
    app.run(host='0.0.0.0', port=5000, debug=True)
