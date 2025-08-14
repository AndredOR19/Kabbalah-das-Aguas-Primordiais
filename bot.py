from flask import Flask, request, jsonify
import openai, json

app = Flask(__name__)

# Sua chave de API da OpenAI
openai.api_key = "SUA_CHAVE_API"

# Carrega a personalidade
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

@app.route("/", methods=["POST"])
def oraculo():
    data = request.json
    pergunta = data.get("pergunta")
    perfil = data.get("perfil")

    contexto = f"""
    Você é o Oráculo-Mestre do Instituto Águas Primordiais.
    Papéis: {config['papel']}
    Estilo: {config['estilo']}
    Limites: {config['limites']}

    Dados do consulente:
    Nome completo: {perfil['nome']}
    Local de nascimento: {perfil['local_nascimento']}
    Local atual: {perfil['local_atual']}
    Data de nascimento: {perfil['data_nascimento']}
    Hora de nascimento: {perfil['hora_nascimento']}

    Pergunta: {pergunta}
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": contexto}]
    )

    return jsonify({"resposta": resposta.choices[0].message["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)