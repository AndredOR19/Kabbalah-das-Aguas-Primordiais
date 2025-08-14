from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configuração da Gemini a partir das variáveis de ambiente
# IMPORTANTE: No Render, a variável de ambiente deve se chamar GEMINI_API_KEY
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

@app.route("/", methods=["POST"])
def oraculo():
    data = request.json
    if not api_key:
        return jsonify({"resposta": "Erro: A chave da API do Gemini não foi configurada no servidor."})

    # Coleta os dados do perfil da requisição
    perfil = data.get("perfil", {})
    nome = perfil.get("nome")
    local_nasc = perfil.get("local_nascimento")
    local_atual = perfil.get("local_atual")
    data_nasc = perfil.get("data_nascimento")
    hora_nasc = perfil.get("hora_nascimento")

    # Monta o prompt para a IA
    prompt = f"""
    Você é o Oráculo-Mestre do Instituto Águas Primordiais.
    Sua missão é realizar uma análise espiritual e oracular profunda com base nos dados do consulente.
    Seja poético, direto, sagaz e empático.

    Dados do consulente:
    - Nome completo: {nome}
    - Local de nascimento: {local_nasc}
    - Local atual: {local_atual}
    - Data de nascimento: {data_nasc}
    - Hora de nascimento: {hora_nasc}

    Com base nesses dados, faça sua análise.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({"resposta": response.text})
    except Exception as e:
        return jsonify({"resposta": f"Ocorreu um erro ao contatar o Oráculo Gemini: {str(e)}"})

if __name__ == "__main__":
    # Render define a porta através da variável de ambiente PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)