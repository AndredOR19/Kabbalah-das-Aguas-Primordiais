from flask import Flask, request, jsonify
import google.generativeai as genai
import json
import os

app = Flask(__name__)

# Chave da API do Google Gemini (lida a partir das variáveis de ambiente)
# IMPORTANTE: No Render, a variável de ambiente deve se chamar GEMINI_API_KEY
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Carrega a personalidade
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

@app.route("/", methods=["POST"])
def oraculo():
    data = request.json
    pergunta = data.get("pergunta")
    perfil = data.get("perfil")

    if not api_key:
        return jsonify({"resposta": "Erro: A chave da API do Gemini não foi configurada no servidor."})

    # Constrói o prompt para o Gemini
    contexto = f"""
    Você é o Oráculo-Mestre do Instituto Águas Primordiais.
    Seus papéis são: {config['papel']}
    Seu estilo é: {config['estilo']}
    Suas regras são: {config['limites']}

    A seguir, os dados do consulente que faz a pergunta. Use esses dados para dar uma resposta mais profunda e personalizada.
    - Nome completo: {perfil['nome']}
    - Local de nascimento: {perfil['local_nascimento']}
    - Local atual: {perfil['local_atual']}
    - Data de nascimento: {perfil['data_nascimento']}
    - Hora de nascimento: {perfil['hora_nascimento']}

    Responda à seguinte pergunta: "{pergunta}"
    """

    try:
        # Inicializa o modelo e gera o conteúdo
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(contexto)
        return jsonify({"resposta": response.text})
    except Exception as e:
        # Retorna uma mensagem de erro mais detalhada para depuração
        return jsonify({"resposta": f"Ocorreu um erro ao contatar o Oráculo Gemini: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))