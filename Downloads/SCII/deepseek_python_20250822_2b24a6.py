#!/usr/bin/env python3
"""
Sistema Automático de Diagnóstico 12-7-3
Interface conversacional para identificação de desequilíbrios
"""

class DiagnosticoAuto:
    def __init__(self):
        self.perguntas = [
            {
                "pergunta": "Como você descreve seu estado mental atual?",
                "opcoes": ["Claro e focado", "Confuso e disperso", "Criativo mas não concretizado"],
                "camada": 12
            },
            {
                "pergunta": "Como está seu fluxo de ação e realização?",
                "opcoes": ["Fluido e constante", "Bloqueado e interrompido", "Alternando entre fluxo e bloqueio"],
                "camada": 7
            },
            # Adicionar mais 10-15 perguntas...
        ]
    
    def executar_diagnostico(self):
        print("=== DIAGNÓSTICO AUTOMÁTICO 12-7-3 ===")
        print("Responda as perguntas para receber uma análise personalizada\n")
        
        resultados = {12: 0, 7: 0, 3: 0}
        
        for i, pergunta in enumerate(self.perguntas, 1):
            print(f"\n{i}. {pergunta['pergunta']}")
            for j, opcao in enumerate(pergunta['opcoes'], 1):
                print(f"   {j}. {opcao}")
            
            resposta = int(input("\nSua resposta (número): "))
            resultados[pergunta['camada']] += resposta
        
        return self.analisar_resultados(resultados)
    
    def analisar_resultados(self, resultados):
        # Lógica de análise complexa aqui
        return {
            "desequilíbrio_principal": max(resultados, key=resultados.get),
            "pontuacao": resultados,
            "recomendacoes": self.gerar_recomendacoes(resultados)
        }

# Interface web simples usando Flask
from flask import Flask, request, jsonify

app = Flask(__name__)
diagnostico = DiagnosticoAuto()

@app.route('/diagnostico', methods=['POST'])
def api_diagnostico():
    respostas = request.json
    resultado = diagnostico.analisar_respostas(respostas)
    return jsonify(resultado)