import matplotlib.pyplot as plt
import json
from datetime import datetime

class DashboardProgresso:
    def __init__(self):
        self.dados = self.carregar_dados()
    
    def carregar_dados(self):
        try:
            with open('dados_progresso.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"meditacoes": [], "rituais": [], "avaliacoes": []}
    
    def gerar_relatorio_mensal(self):
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        
        # Gráfico de frequência de práticas
        axs[0,0].plot([d['data'] for d in self.dados['meditacoes']], 
                     [d['duracao'] for d in self.dados['meditacoes']])
        axs[0,0].set_title('Evolução da Prática Meditativa')
        
        # Gráfico de camadas trabalhadas
        camadas = [12, 7, 3]
        contagem = [sum(1 for r in self.dados['rituais'] if r['camada'] == c) for c in camadas]
        axs[0,1].pie(contagem, labels=['Mente', 'Matéria', 'Força'], autopct='%1.1f%%')
        axs[0,1].set_title('Distribuição por Camadas')
        
        plt.savefig('relatorio_mensal.png')
        return 'relatorio_mensal.png'