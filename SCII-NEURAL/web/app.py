"""
Aplicação Web do Oráculo SCII.

Um servidor Flask simples que expõe uma interface para o usuário submeter dados e
receber diagnósticos oraculares em formato JSON. Esta é uma implementação
mínima para demonstração.
"""

from flask import Flask, render_template, request, jsonify
from ..core.diagnosis import diagnosticar_scii

app = Flask(__name__)

@app.route("/")
def home():
    """Rota principal que serve a página de consulta."""
    return render_template("oracle_interface.html")

@app.route("/consulta", methods=["POST"])
def nova_consulta():
    """Recebe dados do cliente em JSON e retorna diagnóstico."""
    dados = request.get_json(force=True)
    diagnostico = diagnosticar_scii(dados)
    return jsonify(diagnostico)

if __name__ == "__main__":
    app.run(debug=True)