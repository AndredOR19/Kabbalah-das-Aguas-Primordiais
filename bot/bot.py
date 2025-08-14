import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
# Supondo que você usará a API da OpenAI
# import openai

# Carregar a chave da API (deve ser configurada como uma variável de ambiente)
# openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios (como o seu GitHub Pages)

def carregar_json(caminho_arquivo):
    """Carrega um arquivo JSON."""
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

# Carregar a base de conhecimento e a configuração do bot
base_conhecimento = carregar_json('base_conhecimento.json')
config_bot = carregar_json('config.json')

@app.route('/perguntar', methods=['POST'])
def perguntar_ao_oraculo():
    """Endpoint da API para receber perguntas e retornar respostas."""
    dados = request.get_json()
    pergunta = dados.get('pergunta')

    if not pergunta:
        return jsonify({"erro": "Nenhuma pergunta fornecida."}), 400

    # --- Lógica de Geração de Resposta ---
    # Aqui entraria a chamada para a API da OpenAI ou outro modelo de linguagem.
    # O prompt seria construído com a personalidade do bot, a base de conhecimento e a pergunta do usuário.

    # Exemplo de prompt (simplificado):
    prompt = f"""
    Você é o Oráculo-Mestre do Instituto Águas Primordiais.
    Seu papel é: {config_bot['papel']}.
    Seu estilo é: {config_bot['estilo']}.
    Suas regras são: {config_bot['limites']}.

    Base de conhecimento relevante:
    {json.dumps(base_conhecimento, indent=2, ensure_ascii=False)}

    Com base em tudo isso, responda à seguinte pergunta de um buscador:
    "{pergunta}"
    """

    # Exemplo de resposta mockada (sem chamada real à API):
    # Em um cenário real, você faria a chamada aqui:
    # response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=250)
    # resposta_gerada = response.choices[0].text.strip()
    
    resposta_gerada = f"Esta é uma resposta de exemplo para a pergunta: '{pergunta}'. A API real ainda precisa ser implementada e hospedada."

    # Salvar a pergunta e a resposta (opcional, para registro)
    with open('log_perguntas.jsonl', 'a', encoding='utf-8') as f:
        log_entry = {"pergunta": pergunta, "resposta": resposta_gerada}
        f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')

    return jsonify({"resposta": resposta_gerada})

if __name__ == '__main__':
    # Para rodar localmente: python bot/bot.py
    # Para produção, use um servidor WSGI como Gunicorn.
    app.run(debug=True, port=5000)