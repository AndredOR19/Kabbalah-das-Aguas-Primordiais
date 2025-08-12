#!/usr/bin/env python3
"""
Coletor de dados psicossomáticos para integração com Git
Suporta: entrada manual + webcam (opcional)
"""

import json
import datetime
import os
from pathlib import Path

class PsicoCollector:
    def __init__(self):
        self.data_dir = Path(".gitpsychodata")
        self.data_dir.mkdir(exist_ok=True)
        
    def collect_manual_data(self):
        """Coleta dados via entrada manual no terminal"""
        print("\n🧠 === COLETA PSICOSSOMÁTICA ===")
        print("Digite os valores (pressione Enter para pular):\n")
        
        data = {
            "hr": self._get_int_input("Frequência cardíaca (bpm): "),
            "hrv": self._get_int_input("HRV: "),
            "resp_rate": self._get_int_input("Respiração (rpm): "),
            "focus": self._get_int_input("Foco (0-100%): "),
            "mood": input("Humor (feliz/neutro/triste/ansioso/calmo): ").lower() or "neutro",
            "note": input("Observações: ") or ""
        }
        
        # Filtrar valores None
        return {k: v for k, v in data.items() if v is not None}
    
    def _get_int_input(self, prompt):
        """Obtém entrada inteira segura"""
        try:
            value = input(prompt).strip()
            return int(value) if value else None
        except ValueError:
            print(f"⚠️ Valor inválido para {prompt}")
            return None
    
    def save_data(self, data):
        """Salva dados em formato JSON"""
        timestamp = datetime.datetime.now()
        filename = f"psico_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        filepath = self.data_dir / filename
        
        # Adicionar timestamp
        data["timestamp"] = timestamp.isoformat()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Dados salvos em: {filepath}")
        return filepath
    
    def generate_commit_suffix(self, data):
        """Gera sufixo para mensagem de commit"""
        suffix = f" | hr={data.get('hr', 'N/A')} hrv={data.get('hrv', 'N/A')} foco={data.get('focus', 'N/A')}% humor={data.get('mood', 'N/A')}"
        return suffix
    
    def run(self):
        """Executa coleta completa"""
        print("🎯 Iniciando coleta de dados psicossomáticos...")
        
        # Coletar dados
        data = self.collect_manual_data()
        
        if not data:
            print("❌ Nenhum dado coletado")
            return None
        
        # Salvar dados
        filepath = self.save_data(data)
        
        # Gerar sufixo para commit
        suffix = self.generate_commit_suffix(data)
        
        # Salvar também como current_psico.json para fácil acesso
        current_file = self.data_dir / "current_psico.json"
        with open(current_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n📋 Sufixo para commit: {suffix}")
        return data

if __name__ == "__main__":
    collector = PsicoCollector()
    collector.run()
