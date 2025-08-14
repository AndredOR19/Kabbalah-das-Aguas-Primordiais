from flask import Flask, request, jsonify
import openai, json, os

app = Flask(__name__)

# Chave da API da OpenAI (lida a partir das variáveis de ambiente)
# IMPORTANTE: No Render, a variável de ambiente deve se chamar OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

# Carrega a personalidade
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

@app.route("/", methods=["POST"])
def oraculo():
    data = request.json
    pergunta = data.get("pergunta")
    perfil = data.get("perfil")

    if not openai.api_key:
        return jsonify({"resposta": "Erro: A chave da API da OpenAI não foi configurada no servidor."})

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
        resposta = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": contexto}]
        )
        return jsonify({"resposta": resposta.choices[0].message["content"]})
    except Exception as e:
        return jsonify({"resposta": f"Ocorreu um erro ao contatar o Oráculo: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))