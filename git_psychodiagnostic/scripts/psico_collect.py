#!/usr/bin/env python3
"""
Coletor de dados psicossomáticos para integração com Git
Suporta: entrada manual + webcam (opcional)
INTEGRAÇÃO SCII-CORE: Ponte com Atlas Anatômico 3D
"""

import json
import datetime
import os
from pathlib import Path

class PsicoCollector:
    def __init__(self):
        self.data_dir = Path(".gitpsychodata")
        self.data_dir.mkdir(exist_ok=True)
        
        # SCII-Core Integration
        self.scii_database_path = Path("scii_database.js/data/scii_database.json")
        self.estado_atual_path = Path("estado_atual.json")
        self.scii_data = self.load_scii_database()
    
    def load_scii_database(self):
        """Carrega o SCII-Core database"""
        try:
            if self.scii_database_path.exists():
                with open(self.scii_database_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print("✅ SCII-Core carregado com sucesso")
                    return data
            else:
                print(f"⚠️ SCII database não encontrado em: {self.scii_database_path}")
                return None
        except Exception as e:
            print(f"❌ Erro ao carregar SCII database: {e}")
            return None
    
    def find_emotion_correspondence(self, emotion):
        """Encontra correspondência anatômica para uma emoção no SCII-Core"""
        if not self.scii_data:
            return None
        
        # Buscar na ponte sismógrafo-atlas
        ponte = self.scii_data.get('ponte_sismografo_atlas', {})
        mapeamento = ponte.get('mapeamento_emocoes_anatomia', {})
        
        # Busca direta
        if emotion in mapeamento:
            return mapeamento[emotion]
        
        # Busca por palavras-chave nas emoções das letras
        letras = self.scii_data.get('letras', {})
        for nome_letra, dados_letra in letras.items():
            emocoes_associadas = dados_letra.get('emocoes_associadas', [])
            if emotion in emocoes_associadas:
                return {
                    'sistema_anatomico': dados_letra.get('nome_anatomico'),
                    'letra_hebraica': dados_letra.get('letra_hebraica'),
                    'nome_letra': nome_letra,
                    'id_mesh_3d': dados_letra.get('id_mesh_3d'),
                    'funcao_espiritual': dados_letra.get('funcao_espiritual'),
                    'pratica_sugerida': dados_letra.get('pratica_sugerida'),
                    'intensidade_base': 0.7,
                    'cor_visualizacao': '#FF6B35'  # Cor padrão
                }
        
        return None
    
    def create_estado_atual(self, emotion_data):
        """Cria ou atualiza o arquivo estado_atual.json"""
        try:
            if emotion_data:
                with open(self.estado_atual_path, 'w', encoding='utf-8') as f:
                    json.dump(emotion_data, f, ensure_ascii=False, indent=2)
                print(f"🌉 Estado atual criado: {emotion_data['sistema_anatomico']} ({emotion_data['nome_letra']})")
            else:
                # Limpar estado se não há emoção detectada
                if self.estado_atual_path.exists():
                    self.estado_atual_path.unlink()
                    print("🌙 Estado atual limpo (neutro)")
        except Exception as e:
            print(f"❌ Erro ao criar estado atual: {e}")
        
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
            "emotion": input("Emoção específica (frustração/ansiedade/medo/etc): ").lower().strip(),
            "note": input("Observações: ") or ""
        }
        
        # Filtrar valores None e strings vazias
        filtered_data = {}
        for k, v in data.items():
            if v is not None and v != "":
                filtered_data[k] = v
        
        return filtered_data
    
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
        """Executa coleta completa com integração SCII-Core"""
        print("🎯 Iniciando coleta de dados psicossomáticos...")
        
        # Coletar dados
        data = self.collect_manual_data()
        
        if not data:
            print("❌ Nenhum dado coletado")
            self.create_estado_atual(None)  # Limpar estado
            return None
        
        # INTEGRAÇÃO SCII-CORE: Processar emoção
        emotion_correspondence = None
        if 'emotion' in data and data['emotion']:
            print(f"\n🔍 Buscando correspondência para emoção: '{data['emotion']}'")
            emotion_correspondence = self.find_emotion_correspondence(data['emotion'])
            
            if emotion_correspondence:
                print(f"✅ Correspondência encontrada:")
                print(f"   🫀 Sistema: {emotion_correspondence['sistema_anatomico']}")
                print(f"   🔤 Letra: {emotion_correspondence['letra_hebraica']} ({emotion_correspondence['nome_letra']})")
                print(f"   🎯 Função: {emotion_correspondence.get('funcao_espiritual', 'N/A')}")
                print(f"   🧘 Prática: {emotion_correspondence.get('pratica_sugerida', 'N/A')}")
            else:
                print(f"⚠️ Nenhuma correspondência encontrada para '{data['emotion']}'")
        
        # Criar sinal de estado para o Atlas
        self.create_estado_atual(emotion_correspondence)
        
        # Salvar dados
        filepath = self.save_data(data)
        
        # Gerar sufixo para commit
        suffix = self.generate_commit_suffix(data)
        
        # Salvar também como current_psico.json para fácil acesso
        current_file = self.data_dir / "current_psico.json"
        with open(current_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n📋 Sufixo para commit: {suffix}")
        
        if emotion_correspondence:
            print(f"🌉 PONTE ATIVA: Atlas deve iluminar {emotion_correspondence['id_mesh_3d']}")
        
        return data

if __name__ == "__main__":
    collector = PsicoCollector()
    collector.run()
