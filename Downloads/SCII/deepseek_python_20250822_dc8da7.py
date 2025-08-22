#!/usr/bin/env python3
"""
Sistema de Notificações Inteligentes
Baseado em correspondências astrológicas e ciclos cósmicos
Autor: André de Oliveira Rodrigues
Data: 2024-03-20
Versão: 1.0
"""

import schedule
import time
import json
from datetime import datetime, timedelta
import logging
from astral import LocationInfo
from astral.sun import sun
import pytz

# Configurar logging
logging.basicConfig(filename='logs/notificacoes.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class NotificadorInteligente:
    def __init__(self):
        self.carregar_configuracoes()
        self.carregar_horarios_otimos()
        
    def carregar_configuracoes(self):
        with open('config/notificacoes_config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        # Configuração de localização para cálculos astrológicos
        self.localizacao = LocationInfo(
            self.config['localizacao']['nome'],
            self.config['localizacao']['regiao'],
            self.config['localizacao']['fuso_horario'],
            self.config['localizacao']['latitude'],
            self.config['localizacao']['longitude']
        )
        
    def carregar_horarios_otimos(self):
        with open('data/horarios_magicos.json', 'r', encoding='utf-8') as f:
            self.horarios_magicos = json.load(f)
    
    def calcular_horarios_astrologicos(self):
        """Calcula horários baseados na posição do sol e astrologia"""
        cidade = pytz.timezone(self.localizacao.timezone)
        agora = datetime.now(cidade)
        s = sun(self.localizacao.observer, date=agora.date(), tzinfo=cidade)
        
        horarios = {
            'amanhecer': s['sunrise'],
            'meio_dia': s['noon'],
            'por_do_sol': s['sunset'],
            'meia_noite': agora.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        }
        
        return horarios
    
    def determinar_melhor_horario(self, tipo_pratica):
        """Determina o melhor horário para uma prática baseado em múltiplos fatores"""
        horarios_astrologicos = self.calcular_horarios_astrologicos()
        horarios_magicos = self.horarios_magicos[tipo_pratica]
        
        # Combinar horários astrológicos com correspondências mágicas
        if tipo_pratica == "meditacao":
            return horarios_astrologicos['amanhecer'] + timedelta(minutes=30)
        elif tipo_pratica == "ritual_12":
            return horarios_astrologicos['meio_dia']
        elif tipo_pratica == "ritual_7":
            return horarios_astrologicos['por_do_sol'] - timedelta(hours=1)
        elif tipo_pratica == "ritual_3":
            return horarios_astrologicos['meia_noite'] - timedelta(hours=2)
        else:
            return datetime.now() + timedelta(hours=1)
    
    def gerar_mensagem_notificacao(self, tipo_pratica):
        """Gera mensagem personalizada baseada no tipo de prática"""
        mensagens = {
            "meditacao": "Hora ideal para meditação. Conecte-se com a quietude interior.",
            "ritual_12": "Momento propício para trabalhar a estrutura mental. Ative a Roda dos 12.",
            "ritual_7": "Energia favorável para manifestação material. Realize o Ritual do Fluxo.",
            "ritual_3": "Conexão ampliada com as forças primordiais. Alinhe-se com o propósito."
        }
        return mensagens.get(tipo_pratica, "Hora de praticar.")
    
    def agendar_notificacoes_diarias(self):
        """Agenda notificações para o dia atual"""
        praticas = ["meditacao", "ritual_12", "ritual_7", "ritual_3"]
        
        for pratica in praticas:
            horario = self.determinar_melhor_horario(pratica)
            mensagem = self.gerar_mensagem_notificacao(pratica)
            
            # Converter para formato schedule
            horario_str = horario.strftime("%H:%M")
            
            schedule.every().day.at(horario_str).do(
                self.enviar_notificacao, mensagem, pratica
            )
            
            logging.info(f"Notificação agendada para {horario_str}: {pratica}")
    
    def enviar_notificacao(self, mensagem, tipo_pratica):
        """Envia notificação de acordo com o sistema operacional"""
        try:
            # Para Windows
            import winsound
            winsound.Beep(1000, 500)  # Beep sonoro
        except ImportError:
            pass
        
        # Para Linux/Mac (notificação visual)
        import os
        os.system(f'echo "{mensagem}" | wall')
        
        # Registrar no log
        logging.info(f"Notificação enviada: {mensagem}")
        
        # Aqui você pode integrar com APIs de notificação mobile se desejar
        print(f"\n🔔 NOTIFICAÇÃO: {mensagem}\n")
    
    def verificar_mudancas_astrologicas(self):
        """Verifica mudanças astrológicas importantes e ajusta horários"""
        # Esta função pode ser expandida para considerar trânsitos planetários
        pass
    
    def executar(self):
        """Loop principal do sistema de notificações"""
        print("Iniciando Sistema de Notificações Inteligentes...")
        print("Press Ctrl+C para parar.")
        
        self.agendar_notificacoes_diarias()
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Verificar a cada minuto
                
                # Recalcular horários se passar da meia-noite
                if datetime.now().hour == 0 and datetime.now().minute == 0:
                    self.agendar_notificacoes_diarias()
                    
        except KeyboardInterrupt:
            print("Sistema de notificações encerrado.")

# Arquivo de configuração: config/notificacoes_config.json
"""
{
  "localizacao": {
    "nome": "São Paulo",
    "regiao": "BR",
    "fuso_horario": "America/Sao_Paulo",
    "latitude": -23.5505,
    "longitude": -46.6333
  },
  "notificacoes_ativas": true,
  "tipos_pratica": ["meditacao", "ritual_12", "ritual_7", "ritual_3"]
}
"""

# Arquivo de dados: data/horarios_magicos.json
"""
{
  "meditacao": {
    "melhor_horario": "amanhecer",
    "planeta_regente": "Sol",
    "elemento": "Ar",
    "intensidade": "suave"
  },
  "ritual_12": {
    "melhor_horario": "meio_dia",
    "planeta_regente": "Mercúrio",
    "elemento": "Éter",
    "intensidade": "media"
  },
  "ritual_7": {
    "melhor_horario": "tarde",
    "planeta_regente": "Vênus",
    "elemento": "Água",
    "intensidade": "media"
  },
  "ritual_3": {
    "melhor_horario": "meia_noite",
    "planeta_regente": "Lua",
    "elemento": "Fogo",
    "intensidade": "forte"
  }
}
"""

if __name__ == "__main__":
    notificador = NotificadorInteligente()
    notificador.executar()