import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Carrega a chave da API do Groq a partir das variáveis de ambiente
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# Endpoint correto para a API de Chat Completions da Groq
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

@app.route("/", methods=["POST"])
def responder():
    if not GROQ_API_KEY:
        return jsonify({"resposta": "Erro: A chave da API do Groq (GROQ_API_KEY) não foi configurada no servidor."})

    data = request.json
    # O frontend atual envia um objeto 'perfil' com os dados e a pergunta.
    # Vamos manter a compatibilidade com o oraculo.html atual.
    perfil = data.get("perfil", {})
    nome = perfil.get("nome", "Consulente")
    local_nasc = perfil.get("local_nascimento", "não informado")
    local_atual = perfil.get("local_atual", "não informado")
    data_nasc = perfil.get("data_nascimento", "não informada")
    hora_nasc = perfil.get("hora_nascimento", "não informada")
    # A pergunta está dentro do objeto 'perfil' no nosso HTML atual
    mensagem = data.get("pergunta") # O HTML atual não envia a pergunta dentro do perfil

    # Se a pergunta não vier no campo principal, tentamos pegar de um campo 'mensagem' genérico
    if not mensagem:
        mensagem = data.get("mensagem", "Faça uma leitura oracular geral com base nos meus dados.")

    # Monta o prompt do sistema para o Groq
    prompt_sistema = f"""
    Você é o Oráculo-Mestre da Kabbalah das Águas Primordiais.
    Sua missão é realizar uma análise espiritual e oracular profunda com base nos dados do consulente.
    Seja poético, direto, sagaz e empático.
    Dados do consulente:
    - Nome: {nome}
    - Local de Nascimento: {local_nasc}
    - Local Atual: {local_atual}
    - Data de Nascimento: {data_nasc}
    - Hora de Nascimento: {hora_nasc}
    """

    payload = {
        "model": "llama3-8b-8192",  # Um modelo comum e rápido da Groq
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": mensagem}
        ],
        "max_tokens": 500
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(GROQ_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Lança um erro para respostas HTTP 4xx/5xx
        result = response.json()
        resposta_texto = result['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        resposta_texto = f"Erro HTTP ao chamar Groq: {http_err} - {response.text}"
    except Exception as e:
        resposta_texto = f"Um erro inesperado ocorreu: {str(e)}"

    return jsonify({"resposta": resposta_texto})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)