#!/usr/bin/env python3
"""
🌟 INTEGRADOR ASTRAL-SCII
Conecta A Chave dos Céus com o Sistema SCII-Core
Análise de correspondências astrológicas com letras hebraicas
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Adicionar caminho do psico_collect
sys.path.append('git_psychodiagnostic/scripts')

class IntegradorAstralSCII:
    def __init__(self):
        self.scii_data = None
        self.mapa_astral = None
        self.correspondencias_astrais = {}
        self.carregar_scii_core()
    
    def carregar_scii_core(self):
        """Carrega o SCII-Core database"""
        scii_path = Path("scii_database.js/data/scii_database.json")
        
        try:
            with open(scii_path, 'r', encoding='utf-8') as f:
                self.scii_data = json.load(f)
            print("✅ SCII-Core carregado com sucesso")
        except Exception as e:
            print(f"❌ Erro ao carregar SCII-Core: {e}")
            sys.exit(1)
    
    def carregar_mapa_astral(self, caminho_mapa):
        """Carrega um mapa astral do arquivo JSON"""
        try:
            with open(caminho_mapa, 'r', encoding='utf-8') as f:
                self.mapa_astral = json.load(f)
            print(f"✅ Mapa astral carregado: {self.mapa_astral['metadata']['nome']}")
            return True
        except Exception as e:
            print(f"❌ Erro ao carregar mapa astral: {e}")
            return False
    
    def mapear_signos_letras_hebraicas(self):
        """Mapeia signos astrológicos com letras hebraicas"""
        # Correspondências tradicionais da Cabala
        mapeamento_signos = {
            'Ari': 'ה',  # He - Áries
            'Tau': 'ו',  # Vav - Touro  
            'Gem': 'ז',  # Zayin - Gêmeos
            'Can': 'ח',  # Chet - Câncer
            'Leo': 'ט',  # Tet - Leão
            'Vir': 'י',  # Yod - Virgem
            'Lib': 'ל',  # Lamed - Libra
            'Sco': 'נ',  # Nun - Escorpião
            'Sag': 'ס',  # Samech - Sagitário
            'Cap': 'ע',  # Ayin - Capricórnio
            'Aqu': 'צ',  # Tzade - Aquário
            'Pis': 'ק'   # Qoph - Peixes
        }
        
        return mapeamento_signos
    
    def mapear_planetas_letras_hebraicas(self):
        """Mapeia planetas com letras hebraicas"""
        # Correspondências tradicionais da Cabala
        mapeamento_planetas = {
            'sun': 'ר',      # Resh - Sol
            'moon': 'ג',     # Gimel - Lua
            'mercury': 'ב',  # Beth - Mercúrio
            'venus': 'ד',    # Daleth - Vênus
            'mars': 'פ',     # Pe - Marte
            'jupiter': 'כ',  # Kaph - Júpiter
            'saturn': 'ת',   # Tav - Saturno
            'uranus': 'א',   # Aleph - Urano
            'neptune': 'מ',  # Mem - Netuno
            'pluto': 'ש'     # Shin - Plutão
        }
        
        return mapeamento_planetas
    
    def analisar_correspondencias_astrais(self):
        """Analisa correspondências entre mapa astral e SCII-Core"""
        if not self.mapa_astral:
            print("❌ Nenhum mapa astral carregado")
            return
        
        print(f"\n🔮 ANÁLISE ASTRAL-SCII PARA {self.mapa_astral['metadata']['nome'].upper()}")
        print("=" * 70)
        
        mapeamento_signos = self.mapear_signos_letras_hebraicas()
        mapeamento_planetas = self.mapear_planetas_letras_hebraicas()
        
        # Analisar luminares
        print("\n✨ LUMINARES E CORRESPONDÊNCIAS:")
        print("-" * 40)
        
        luminares = self.mapa_astral['luminares']
        
        for luminar, dados in luminares.items():
            signo = dados['signo']
            letra_signo = mapeamento_signos.get(signo, '?')
            
            # Buscar letra no SCII-Core
            letra_scii = self.buscar_letra_scii(letra_signo)
            
            print(f"☉ {luminar.capitalize()}: {signo} → {letra_signo}")
            if letra_scii:
                # Buscar nome da letra (chave do dicionário)
                nome_letra = None
                for nome, dados in self.scii_data['letras'].items():
                    if dados.get('letra_hebraica') == letra_signo:
                        nome_letra = nome
                        break
                
                print(f"   🔤 Letra SCII: {nome_letra} ({letra_scii['letra_hebraica']})")
                print(f"   🫀 Sistema: {letra_scii['nome_anatomico']}")
                print(f"   ✨ Função: {letra_scii.get('funcao_espiritual', 'N/A')}")
        
        # Analisar planetas
        print(f"\n🪐 PLANETAS E CORRESPONDÊNCIAS:")
        print("-" * 40)
        
        planetas = self.mapa_astral['planetas']
        
        for planeta, dados in planetas.items():
            signo = dados['signo']
            letra_planeta = mapeamento_planetas.get(planeta, '?')
            letra_signo = mapeamento_signos.get(signo, '?')
            
            # Buscar letras no SCII-Core
            letra_planeta_scii = self.buscar_letra_scii(letra_planeta)
            letra_signo_scii = self.buscar_letra_scii(letra_signo)
            
            print(f"♂ {planeta.capitalize()}: {signo}")
            print(f"   🌟 Planeta → {letra_planeta} | Signo → {letra_signo}")
            
            if letra_planeta_scii:
                nome_planeta = self.obter_nome_letra(letra_planeta)
                print(f"   🔤 Planeta SCII: {nome_planeta} → {letra_planeta_scii['nome_anatomico']}")
            
            if letra_signo_scii:
                nome_signo = self.obter_nome_letra(letra_signo)
                print(f"   🔤 Signo SCII: {nome_signo} → {letra_signo_scii['nome_anatomico']}")
        
        # Análise de dominâncias
        self.analisar_dominancias()
        
        # Gerar perfil integrado
        self.gerar_perfil_integrado()
    
    def buscar_letra_scii(self, letra_hebraica):
        """Busca uma letra hebraica no SCII-Core"""
        if not self.scii_data or 'letras' not in self.scii_data:
            return None
        
        for nome_letra, dados in self.scii_data['letras'].items():
            if dados.get('letra_hebraica') == letra_hebraica:
                return dados
        
        return None
    
    def obter_nome_letra(self, letra_hebraica):
        """Obtém o nome da letra hebraica"""
        if not self.scii_data or 'letras' not in self.scii_data:
            return None
        
        for nome_letra, dados in self.scii_data['letras'].items():
            if dados.get('letra_hebraica') == letra_hebraica:
                return nome_letra
        
        return None
    
    def analisar_dominancias(self):
        """Analisa elementos e modalidades dominantes"""
        print(f"\n🌊 ANÁLISE DE DOMINÂNCIAS:")
        print("-" * 40)
        
        elementos = self.mapa_astral['elementos_dominantes']
        modalidades = self.mapa_astral['modalidades_dominantes']
        
        elemento_dominante = max(elementos, key=elementos.get)
        modalidade_dominante = max(modalidades, key=modalidades.get)
        
        print(f"🔥 Elemento Dominante: {elemento_dominante} ({elementos[elemento_dominante]} pontos)")
        print(f"⚡ Modalidade Dominante: {modalidade_dominante} ({modalidades[modalidade_dominante]} pontos)")
        
        # Correspondências elementais com SCII
        correspondencias_elementos = {
            'Fogo': ['ר', 'ש', 'ט'],  # Resh, Shin, Tet
            'Água': ['מ', 'נ', 'ח'],  # Mem, Nun, Chet  
            'Ar': ['א', 'ז', 'צ'],    # Aleph, Zayin, Tzade
            'Terra': ['ה', 'ו', 'י', 'ע']  # He, Vav, Yod, Ayin
        }
        
        letras_elemento = correspondencias_elementos.get(elemento_dominante, [])
        print(f"🔤 Letras do elemento {elemento_dominante}: {', '.join(letras_elemento)}")
        
        # Buscar sistemas anatômicos correspondentes
        sistemas_elemento = []
        for letra in letras_elemento:
            letra_scii = self.buscar_letra_scii(letra)
            if letra_scii:
                sistemas_elemento.append(letra_scii['nome_anatomico'])
        
        if sistemas_elemento:
            print(f"🫀 Sistemas anatômicos relacionados: {', '.join(sistemas_elemento)}")
    
    def gerar_perfil_integrado(self):
        """Gera perfil integrado Astral-SCII"""
        print(f"\n🌟 PERFIL INTEGRADO ASTRAL-SCII:")
        print("=" * 50)
        
        assinatura = self.mapa_astral['assinatura_cosmica']
        
        print(f"👤 Nome: {self.mapa_astral['metadata']['nome']}")
        print(f"📅 Nascimento: {self.mapa_astral['metadata']['data_nascimento']} às {self.mapa_astral['metadata']['hora_nascimento']}")
        print(f"🌍 Local: {self.mapa_astral['metadata']['local']}")
        print(f"🔮 Código Cósmico: {assinatura['codigo_cosmico']}")
        print(f"🌊 Assinatura Elemental: {assinatura['elemento_dominante']}-{assinatura['modalidade_dominante']}")
        
        # Salvar perfil integrado
        self.salvar_perfil_integrado()
    
    def salvar_perfil_integrado(self):
        """Salva o perfil integrado em JSON"""
        nome_arquivo = f"perfil_astral_scii_{self.mapa_astral['metadata']['nome'].lower().replace(' ', '_')}.json"
        caminho_arquivo = Path("mapas_astrais") / nome_arquivo
        
        mapeamento_signos = self.mapear_signos_letras_hebraicas()
        mapeamento_planetas = self.mapear_planetas_letras_hebraicas()
        
        perfil_integrado = {
            "metadata": {
                "nome": self.mapa_astral['metadata']['nome'],
                "data_nascimento": self.mapa_astral['metadata']['data_nascimento'],
                "hora_nascimento": self.mapa_astral['metadata']['hora_nascimento'],
                "local": self.mapa_astral['metadata']['local'],
                "timestamp_integracao": datetime.now().isoformat(),
                "versao_scii": "5.0"
            },
            "assinatura_cosmica": self.mapa_astral['assinatura_cosmica'],
            "correspondencias_luminares": {},
            "correspondencias_planetas": {},
            "sistemas_anatomicos_ativados": [],
            "letras_hebraicas_dominantes": [],
            "perfil_psicossomatico": {}
        }
        
        # Mapear luminares
        for luminar, dados in self.mapa_astral['luminares'].items():
            signo = dados['signo']
            letra_signo = mapeamento_signos.get(signo, '?')
            letra_scii = self.buscar_letra_scii(letra_signo)
            
            perfil_integrado["correspondencias_luminares"][luminar] = {
                "signo": signo,
                "letra_hebraica": letra_signo,
                "sistema_anatomico": letra_scii['nome_anatomico'] if letra_scii else None,
                "funcao_espiritual": letra_scii.get('funcao_espiritual') if letra_scii else None
            }
            
            if letra_scii:
                perfil_integrado["sistemas_anatomicos_ativados"].append(letra_scii['nome_anatomico'])
                perfil_integrado["letras_hebraicas_dominantes"].append(letra_signo)
        
        # Mapear planetas
        for planeta, dados in self.mapa_astral['planetas'].items():
            signo = dados['signo']
            letra_planeta = mapeamento_planetas.get(planeta, '?')
            letra_signo = mapeamento_signos.get(signo, '?')
            
            letra_planeta_scii = self.buscar_letra_scii(letra_planeta)
            letra_signo_scii = self.buscar_letra_scii(letra_signo)
            
            perfil_integrado["correspondencias_planetas"][planeta] = {
                "signo": signo,
                "letra_planeta": letra_planeta,
                "letra_signo": letra_signo,
                "sistema_planeta": letra_planeta_scii['nome_anatomico'] if letra_planeta_scii else None,
                "sistema_signo": letra_signo_scii['nome_anatomico'] if letra_signo_scii else None
            }
        
        # Remover duplicatas
        perfil_integrado["sistemas_anatomicos_ativados"] = list(set(perfil_integrado["sistemas_anatomicos_ativados"]))
        perfil_integrado["letras_hebraicas_dominantes"] = list(set(perfil_integrado["letras_hebraicas_dominantes"]))
        
        # Salvar arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(perfil_integrado, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 Perfil integrado salvo: {nome_arquivo}")
    
    def listar_mapas_disponiveis(self):
        """Lista mapas astrais disponíveis"""
        mapas_dir = Path("mapas_astrais")
        
        if not mapas_dir.exists():
            print("❌ Diretório de mapas astrais não encontrado")
            return []
        
        mapas_resumo = list(mapas_dir.glob("*_resumo.json"))
        
        if not mapas_resumo:
            print("❌ Nenhum mapa astral encontrado")
            return []
        
        print("📋 Mapas astrais disponíveis:")
        for i, mapa in enumerate(mapas_resumo, 1):
            try:
                with open(mapa, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                nome = dados['metadata']['nome']
                data = dados['metadata']['data_nascimento']
                print(f"   {i}. {nome} ({data}) - {mapa.name}")
            except:
                print(f"   {i}. {mapa.name} (erro ao ler)")
        
        return mapas_resumo
    
    def executar_integracao_interativa(self):
        """Executa integração interativa"""
        print("🌟 INTEGRADOR ASTRAL-SCII")
        print("Conectando A Chave dos Céus com SCII-Core")
        print("=" * 50)
        
        # Listar mapas disponíveis
        mapas = self.listar_mapas_disponiveis()
        
        if not mapas:
            print("\n💡 Dica: Execute primeiro 'python3 scripts/calculadora_astral.py' para gerar mapas")
            return
        
        try:
            escolha = int(input(f"\nEscolha um mapa (1-{len(mapas)}): ")) - 1
            
            if 0 <= escolha < len(mapas):
                mapa_escolhido = mapas[escolha]
                
                if self.carregar_mapa_astral(mapa_escolhido):
                    self.analisar_correspondencias_astrais()
                else:
                    print("❌ Erro ao carregar mapa astral")
            else:
                print("❌ Escolha inválida")
                
        except ValueError:
            print("❌ Digite um número válido")
        except KeyboardInterrupt:
            print("\n👋 Integração cancelada")

def main():
    """Função principal"""
    integrador = IntegradorAstralSCII()
    integrador.executar_integracao_interativa()

if __name__ == "__main__":
    main()