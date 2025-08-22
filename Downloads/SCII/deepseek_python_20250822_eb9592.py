#!/usr/bin/env python3
"""
Sistema Automático de Diagnóstico 12-7-3
Interface conversacional para identificação de desequilíbrios
Autor: André de Oliveira Rodrigues
Data: 2024-03-20
Versão: 1.0
"""

import json
from datetime import datetime

class DiagnosticoAuto:
    def __init__(self):
        # Carregar perguntas de um arquivo JSON para facilitar customização
        with open('data/perguntas_diagnostico.json', 'r', encoding='utf-8') as f:
            self.perguntas = json.load(f)
        
        # Carregar correspondências das letras
        with open('data/correspondencias.json', 'r', encoding='utf-8') as f:
            self.correspondencias = json.load(f)
        
        self.resultados = {12: 0, 7: 0, 3: 0}
        self.respostas_detalhadas = []

    def executar_diagnostico(self):
        print("=== DIAGNÓSTICO AUTOMÁTICO 12-7-3 ===")
        print("Este sistema ajudará a identificar desequilíbrios nas camadas da sua realidade.")
        print("Responda cada pergunta honestamente para receber uma análise personalizada.\n")
        
        for i, pergunta in enumerate(self.perguntas, 1):
            print(f"\nPergunta {i} de {len(self.perguntas)}:")
            print(f"{pergunta['texto']}")
            
            for j, opcao in enumerate(pergunta['opcoes'], 1):
                print(f"   {j}. {opcao['texto']}")
            
            while True:
                try:
                    resposta = int(input("\nSua resposta (número): "))
                    if 1 <= resposta <= len(pergunta['opcoes']):
                        break
                    else:
                        print(f"Por favor, digite um número entre 1 e {len(pergunta['opcoes'])}.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            
            # Registrar a resposta
            opcao_escolhida = pergunta['opcoes'][resposta - 1]
            self.resultados[pergunta['camada']] += opcao_escolhida['valor']
            self.respostas_detalhadas.append({
                'pergunta': pergunta['texto'],
                'resposta': opcao_escolhida['texto'],
                'camada': pergunta['camada'],
                'valor': opcao_escolhida['valor']
            })
        
        return self.gerar_relatorio()

    def gerar_relatorio(self):
        # Identificar camada com maior desequilíbrio
        camada_principal = max(self.resultados, key=self.resultados.get)
        camada_nome = {12: "Mente", 7: "Matéria", 3: "Força"}[camada_principal]
        
        # Gerar recomendações baseadas nas respostas
        recomendacoes = self.gerar_recomendacoes()
        
        relatorio = {
            'data': datetime.now().isoformat(),
            'pontuacao': self.resultados,
            'desequilíbrio_principal': camada_principal,
            'nome_desequilíbrio': camada_nome,
            'recomendacoes': recomendacoes,
            'respostas_detalhadas': self.respostas_detalhadas
        }
        
        # Salvar relatório em arquivo
        with open(f'reports/diagnostico_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json', 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, ensure_ascii=False, indent=2)
        
        return relatorio

    def gerar_recomendacoes(self):
        recomendacoes = []
        
        # Recomendações para camada 12 (Mente)
        if self.resultados[12] > 15:
            recomendacoes.append({
                'camada': 12,
                'prioridade': 'alta',
                'acao': 'Fortalecer a estrutura mental',
                'ritual': 'Meditação da Roda dos 12',
                'letras': ['ה', 'ז', 'ל'],
                'duracao': '15 minutos diários',
                'descricao': 'Foque em visualizar a completude dos 12 arquétipos para estabilizar a mente.'
            })
        
        # Recomendações para camada 7 (Matéria)
        if self.resultados[7] > 15:
            recomendacoes.append({
                'camada': 7,
                'prioridade': 'alta',
                'acao': 'Desbloquear fluxo material',
                'ritual': 'Ritual do Fluxo Contínuo',
                'letras': ['ב', 'פ', 'ת'],
                'duracao': '20 minutos a cada 3 dias',
                'descricao': 'Trabalhe com as letras duplas para destravar processos estagnados.'
            })
        
        # Recomendações para camada 3 (Força)
        if self.resultados[3] > 10:
            recomendacoes.append({
                'camada': 3,
                'prioridade': 'alta',
                'acao': 'Conectar com forças primordiais',
                'ritual': 'Meditação das 3 Forças',
                'letras': ['א', 'מ', 'ש'],
                'duracao': '10 minutos diários',
                'descricao': 'Alinhe-se com as forças do Ar, Água e Fogo para restabelecer o propósito.'
            })
        
        # Recomendações gerais baseadas na combinação de camadas
        if self.resultados[12] > 10 and self.resultados[7] > 10:
            recomendacoes.append({
                'camada': '12+7',
                'prioridade': 'media',
                'acao': 'Integrar mente e matéria',
                'ritual': 'Ritual de Unificação',
                'letras': ['ה', 'ב'],  # Exemplo de combinação
                'duracao': '25 minutos semanais',
                'descricao': 'Equilibre a estrutura mental com a ação material para manifestação eficaz.'
            })
        
        return recomendacoes

    def mostrar_relatorio(self, relatorio):
        print("\n" + "="*50)
        print("RELATÓRIO DE DIAGNÓSTICO")
        print("="*50)
        print(f"Data: {relatorio['data']}")
        print(f"Pontuação: Mente {relatorio['pontuacao'][12]}, Matéria {relatorio['pontuacao'][7]}, Força {relatorio['pontuacao'][3]}")
        print(f"Desequilíbrio principal: {relatorio['nome_desequilíbrio']} (Camada {relatorio['desequilíbrio_principal']})")
        
        print("\nRECOMENDAÇÕES:")
        for i, rec in enumerate(relatorio['recomendacoes'], 1):
            print(f"{i}. {rec['acao']}")
            print(f"   Ritual: {rec['ritual']}")
            print(f"   Letras: {', '.join(rec['letras'])}")
            print(f"   Duração: {rec['duracao']}")
            print(f"   Descrição: {rec['descricao']}\n")

# Arquivo de configuração: data/perguntas_diagnostico.json
"""
[
  {
    "texto": "Como você descreve seu estado mental atual?",
    "camada": 12,
    "opcoes": [
      {"texto": "Claro e focado", "valor": 1},
      {"texto": "Confuso e disperso", "valor": 5},
      {"texto": "Criativo mas não concretizado", "valor": 3}
    ]
  },
  {
    "texto": "Como está seu fluxo de ação e realização?",
    "camada": 7,
    "opcoes": [
      {"texto": "Fluido e constante", "valor": 1},
      {"texto": "Bloqueado e interrompido", "valor": 5},
      {"texto": "Alternando entre fluxo e bloqueio", "valor": 3}
    ]
  },
  {
    "texto": "Como você sente sua conexão com o propósito?",
    "camada": 3,
    "opcoes": [
      {"texto": "Forte e alinhada", "valor": 1},
      {"texto": "Fraca e desconectada", "valor": 5},
      {"texto": "Variável, mas presente", "valor": 3}
    ]
  }
]
"""

if __name__ == "__main__":
    diagnostico = DiagnosticoAuto()
    relatorio = diagnostico.executar_diagnostico()
    diagnostico.mostrar_relatorio(relatorio)