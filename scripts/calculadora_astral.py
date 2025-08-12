#!/usr/bin/env python3
"""
🌟 A CHAVE DOS CÉUS - Calculadora de Mapa Astral Natal
Integração com SCII-Core para análise cósmica completa

Utiliza a biblioteca Kerykeion (Swiss Ephemeris) para cálculos precisos
Gera a "impressão digital cósmica" do usuário em formato JSON
"""

from kerykeion import AstrologicalSubject
import json
import os
import re
from datetime import datetime
from pathlib import Path

class CalculadoraAstral:
    def __init__(self):
        self.dados_usuario = {}
        self.mapa_astral = None
        self.output_dir = Path("mapas_astrais")
        self.output_dir.mkdir(exist_ok=True)
    
    def obter_dados_nascimento(self):
        """
        Função para solicitar e validar os dados de nascimento do usuário.
        Retorna um dicionário com os dados validados.
        """
        print("🌟 === A CHAVE DOS CÉUS ===")
        print("Calculadora de Mapa Astral Natal")
        print("Integração SCII-Core - Impressão Digital Cósmica")
        print("=" * 50)
        
        try:
            # Nome
            nome = input("👤 Nome completo: ").strip()
            if not nome:
                raise ValueError("Nome é obrigatório")
            
            # Data de nascimento
            print("\n📅 Data de Nascimento:")
            ano = self._validar_inteiro("   Ano (ex: 1990): ", 1900, 2030)
            mes = self._validar_inteiro("   Mês (1-12): ", 1, 12)
            dia = self._validar_inteiro("   Dia (1-31): ", 1, 31)
            
            # Validar data
            try:
                datetime(ano, mes, dia)
            except ValueError:
                raise ValueError("Data inválida")
            
            # Hora de nascimento
            print("\n🕐 Hora de Nascimento:")
            hora = self._validar_inteiro("   Hora (0-23): ", 0, 23)
            minuto = self._validar_inteiro("   Minuto (0-59): ", 0, 59)
            
            # Local de nascimento
            print("\n🌍 Local de Nascimento (em inglês):")
            cidade = input("   Cidade: ").strip()
            if not cidade:
                raise ValueError("Cidade é obrigatória")
            
            pais = input("   País: ").strip()
            if not pais:
                raise ValueError("País é obrigatório")
            
            # Obter coordenadas da cidade
            coordenadas = self._obter_coordenadas_cidade(cidade, pais)
            
            # Montar dados para Kerykeion
            self.dados_usuario = {
                "name": nome,
                "year": ano,
                "month": mes,
                "day": dia,
                "hour": hora,
                "minute": minuto,
                "city": cidade,
                "nation": pais,
                "lat": coordenadas['lat'],
                "lng": coordenadas['lng'],
                "tz_str": coordenadas['timezone']
            }
            
            print(f"\n✅ Dados coletados para: {nome}")
            print(f"📅 Nascimento: {dia:02d}/{mes:02d}/{ano} às {hora:02d}:{minuto:02d}")
            print(f"🌍 Local: {cidade}, {pais}")
            
            return self.dados_usuario
            
        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada pelo usuário")
            return None
        except Exception as e:
            print(f"\n❌ Erro na coleta de dados: {e}")
            return None
    
    def _validar_inteiro(self, prompt, min_val, max_val):
        """Valida entrada de número inteiro dentro de um range"""
        while True:
            try:
                valor = int(input(prompt).strip())
                if min_val <= valor <= max_val:
                    return valor
                else:
                    print(f"⚠️ Valor deve estar entre {min_val} e {max_val}")
            except ValueError:
                print("⚠️ Digite um número válido")
            except KeyboardInterrupt:
                raise
    
    def _obter_coordenadas_cidade(self, cidade, pais):
        """Obtém coordenadas geográficas para cidades conhecidas"""
        # Base de dados de cidades principais
        cidades_coordenadas = {
            # Brasil
            ("sao paulo", "brazil"): {"lat": -23.5505, "lng": -46.6333, "timezone": "America/Sao_Paulo"},
            ("rio de janeiro", "brazil"): {"lat": -22.9068, "lng": -43.1729, "timezone": "America/Sao_Paulo"},
            ("brasilia", "brazil"): {"lat": -15.7942, "lng": -47.8822, "timezone": "America/Sao_Paulo"},
            ("salvador", "brazil"): {"lat": -12.9714, "lng": -38.5014, "timezone": "America/Bahia"},
            ("belo horizonte", "brazil"): {"lat": -19.9167, "lng": -43.9345, "timezone": "America/Sao_Paulo"},
            
            # Estados Unidos
            ("new york", "united states"): {"lat": 40.7128, "lng": -74.0060, "timezone": "America/New_York"},
            ("los angeles", "united states"): {"lat": 34.0522, "lng": -118.2437, "timezone": "America/Los_Angeles"},
            ("chicago", "united states"): {"lat": 41.8781, "lng": -87.6298, "timezone": "America/Chicago"},
            ("miami", "united states"): {"lat": 25.7617, "lng": -80.1918, "timezone": "America/New_York"},
            
            # Europa
            ("london", "united kingdom"): {"lat": 51.5074, "lng": -0.1278, "timezone": "Europe/London"},
            ("paris", "france"): {"lat": 48.8566, "lng": 2.3522, "timezone": "Europe/Paris"},
            ("madrid", "spain"): {"lat": 40.4168, "lng": -3.7038, "timezone": "Europe/Madrid"},
            ("rome", "italy"): {"lat": 41.9028, "lng": 12.4964, "timezone": "Europe/Rome"},
            ("berlin", "germany"): {"lat": 52.5200, "lng": 13.4050, "timezone": "Europe/Berlin"},
            ("amsterdam", "netherlands"): {"lat": 52.3676, "lng": 4.9041, "timezone": "Europe/Amsterdam"},
            
            # Ásia
            ("tokyo", "japan"): {"lat": 35.6762, "lng": 139.6503, "timezone": "Asia/Tokyo"},
            ("beijing", "china"): {"lat": 39.9042, "lng": 116.4074, "timezone": "Asia/Shanghai"},
            ("mumbai", "india"): {"lat": 19.0760, "lng": 72.8777, "timezone": "Asia/Kolkata"},
            ("seoul", "south korea"): {"lat": 37.5665, "lng": 126.9780, "timezone": "Asia/Seoul"},
            
            # Outros
            ("sydney", "australia"): {"lat": -33.8688, "lng": 151.2093, "timezone": "Australia/Sydney"},
            ("toronto", "canada"): {"lat": 43.6532, "lng": -79.3832, "timezone": "America/Toronto"},
            ("mexico city", "mexico"): {"lat": 19.4326, "lng": -99.1332, "timezone": "America/Mexico_City"},
            ("buenos aires", "argentina"): {"lat": -34.6118, "lng": -58.3960, "timezone": "America/Argentina/Buenos_Aires"},
        }
        
        # Normalizar entrada
        chave = (cidade.lower().strip(), pais.lower().strip())
        
        # Buscar coordenadas
        if chave in cidades_coordenadas:
            print(f"📍 Coordenadas encontradas para {cidade}, {pais}")
            return cidades_coordenadas[chave]
        
        # Se não encontrar, perguntar ao usuário
        print(f"⚠️ Cidade '{cidade}, {pais}' não encontrada na base de dados")
        print("💡 Você pode:")
        print("   1. Tentar uma cidade próxima mais conhecida")
        print("   2. Fornecer coordenadas manualmente")
        
        opcao = input("Escolha (1/2): ").strip()
        
        if opcao == "1":
            print("\nCidades disponíveis:")
            for i, (c, p) in enumerate(sorted(cidades_coordenadas.keys()), 1):
                if i <= 10:  # Mostrar apenas as primeiras 10
                    print(f"   {c.title()}, {p.title()}")
            print("   ... e mais")
            
            nova_cidade = input("Nova cidade: ").strip()
            novo_pais = input("Novo país: ").strip()
            return self._obter_coordenadas_cidade(nova_cidade, novo_pais)
        
        elif opcao == "2":
            try:
                lat = float(input("Latitude (ex: -23.5505): "))
                lng = float(input("Longitude (ex: -46.6333): "))
                timezone = input("Timezone (ex: America/Sao_Paulo): ").strip()
                
                return {"lat": lat, "lng": lng, "timezone": timezone}
            except ValueError:
                print("❌ Coordenadas inválidas")
                return self._obter_coordenadas_cidade(cidade, pais)
        
        else:
            print("❌ Opção inválida")
            return self._obter_coordenadas_cidade(cidade, pais)
    
    def gerar_mapa_astral(self, dados):
        """
        Calcula o mapa astral e gera os artefatos (resumo e JSON).
        """
        if not dados:
            return False
        
        print(f"\n🔮 Calculando mapa astral para {dados['name']}...")
        print("⏳ Consultando as esferas celestes...")
        
        try:
            # Criar objeto astrológico
            self.mapa_astral = AstrologicalSubject(**dados)
            
            # Exibir resumo no console
            self._exibir_resumo()
            
            # Salvar JSON completo
            nome_arquivo = self._salvar_json()
            
            # Salvar resumo estruturado
            self._salvar_resumo_estruturado(nome_arquivo)
            
            print(f"\n🎉 MAPA ASTRAL GERADO COM SUCESSO!")
            print(f"📁 Arquivos salvos em: {self.output_dir}")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Erro ao gerar o mapa astral: {e}")
            print("💡 Dicas:")
            print("   - Verifique se a cidade e país estão em inglês")
            print("   - Confirme se a data e hora estão corretas")
            print("   - Tente usar nomes de cidades mais conhecidos")
            return False
    
    def _exibir_resumo(self):
        """Exibe resumo formatado do mapa astral"""
        print(f"\n🌟 === MAPA ASTRAL DE {self.mapa_astral.name.upper()} ===")
        print("=" * 60)
        
        # Informações básicas
        print(f"📅 Data: {self.mapa_astral.day:02d}/{self.mapa_astral.month:02d}/{self.mapa_astral.year}")
        print(f"🕐 Hora: {self.mapa_astral.hour:02d}:{self.mapa_astral.minute:02d}")
        print(f"🌍 Local: {self.mapa_astral.city}, {self.mapa_astral.nation}")
        
        print(f"\n✨ LUMINARES E ASCENDENTE:")
        print("-" * 30)
        
        # Sol, Lua e Ascendente
        sol = self.mapa_astral.sun
        lua = self.mapa_astral.moon
        asc = self.mapa_astral.first_house
        
        print(f"☉ Sol: {sol.sign} {sol.abs_pos:.1f}° (Casa {sol.house})")
        print(f"☽ Lua: {lua.sign} {lua.abs_pos:.1f}° (Casa {lua.house})")
        print(f"⬆ Ascendente: {asc.sign} {asc.abs_pos:.1f}°")
        
        print(f"\n🪐 PLANETAS:")
        print("-" * 30)
        
        # Planetas principais
        planetas_ordem = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
        simbolos = {
            'mercury': '☿', 'venus': '♀', 'mars': '♂', 'jupiter': '♃',
            'saturn': '♄', 'uranus': '♅', 'neptune': '♆', 'pluto': '♇'
        }
        
        for planeta in planetas_ordem:
            if hasattr(self.mapa_astral, planeta):
                info = getattr(self.mapa_astral, planeta)
                simbolo = simbolos.get(planeta, '●')
                nome = planeta.capitalize()
                print(f"{simbolo} {nome}: {info.sign} {info.abs_pos:.1f}° (Casa {info.house})")
        
        print(f"\n🏠 CASAS ASTROLÓGICAS:")
        print("-" * 30)
        
        # Casas importantes
        casas_importantes = [1, 4, 7, 10]  # Angular houses
        nomes_casas = {1: "Ascendente", 4: "Fundo do Céu", 7: "Descendente", 10: "Meio do Céu"}
        
        for i in casas_importantes:
            if i == 1:
                casa = self.mapa_astral.first_house
            elif i == 4:
                casa = self.mapa_astral.fourth_house
            elif i == 7:
                casa = self.mapa_astral.seventh_house
            elif i == 10:
                casa = self.mapa_astral.tenth_house
            else:
                continue
            
            nome = nomes_casas[i]
            print(f"Casa {i} ({nome}): {casa.sign} {casa.abs_pos:.1f}°")
    
    def _salvar_json(self):
        """Salva o mapa astral completo em JSON"""
        # Nome do arquivo sanitizado
        nome_limpo = re.sub(r'[^\w\s-]', '', self.mapa_astral.name.lower())
        nome_limpo = re.sub(r'[-\s]+', '_', nome_limpo)
        nome_arquivo = f"mapa_natal_{nome_limpo}.json"
        caminho_completo = self.output_dir / nome_arquivo
        
        # Salvar usando método nativo do Kerykeion
        try:
            # Tentar método mais recente
            if hasattr(self.mapa_astral, 'json_dump'):
                self.mapa_astral.json_dump(str(caminho_completo))
            elif hasattr(self.mapa_astral, 'to_json'):
                self.mapa_astral.to_json(str(caminho_completo))
            else:
                # Fallback: salvar dados básicos manualmente
                dados_basicos = {
                    "name": self.mapa_astral.name,
                    "year": self.mapa_astral.year,
                    "month": self.mapa_astral.month,
                    "day": self.mapa_astral.day,
                    "hour": self.mapa_astral.hour,
                    "minute": self.mapa_astral.minute,
                    "city": self.mapa_astral.city,
                    "nation": self.mapa_astral.nation,
                    "sun": {"sign": self.mapa_astral.sun.sign, "abs_pos": self.mapa_astral.sun.abs_pos, "house": self.mapa_astral.sun.house},
                    "moon": {"sign": self.mapa_astral.moon.sign, "abs_pos": self.mapa_astral.moon.abs_pos, "house": self.mapa_astral.moon.house},
                    "first_house": {"sign": self.mapa_astral.first_house.sign, "abs_pos": self.mapa_astral.first_house.abs_pos}
                }
                
                with open(caminho_completo, 'w', encoding='utf-8') as f:
                    json.dump(dados_basicos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Aviso: Erro ao salvar JSON completo: {e}")
            print("📄 Salvando dados essenciais...")
        
        print(f"📄 Mapa completo salvo: {nome_arquivo}")
        return nome_arquivo
    
    def _salvar_resumo_estruturado(self, nome_base):
        """Salva um resumo estruturado para integração com SCII-Core"""
        nome_resumo = nome_base.replace('.json', '_resumo.json')
        caminho_resumo = self.output_dir / nome_resumo
        
        # Criar estrutura resumida para SCII-Core
        resumo = {
            "metadata": {
                "nome": self.mapa_astral.name,
                "data_nascimento": f"{self.mapa_astral.day:02d}/{self.mapa_astral.month:02d}/{self.mapa_astral.year}",
                "hora_nascimento": f"{self.mapa_astral.hour:02d}:{self.mapa_astral.minute:02d}",
                "local": f"{self.mapa_astral.city}, {self.mapa_astral.nation}",
                "timestamp_calculo": datetime.now().isoformat(),
                "versao_scii": "5.0"
            },
            "luminares": {
                "sol": {
                    "signo": self.mapa_astral.sun.sign,
                    "graus": round(self.mapa_astral.sun.abs_pos, 2),
                    "casa": self.mapa_astral.sun.house,
                    "elemento": self._obter_elemento(self.mapa_astral.sun.sign),
                    "modalidade": self._obter_modalidade(self.mapa_astral.sun.sign)
                },
                "lua": {
                    "signo": self.mapa_astral.moon.sign,
                    "graus": round(self.mapa_astral.moon.abs_pos, 2),
                    "casa": self.mapa_astral.moon.house,
                    "elemento": self._obter_elemento(self.mapa_astral.moon.sign),
                    "modalidade": self._obter_modalidade(self.mapa_astral.moon.sign)
                },
                "ascendente": {
                    "signo": self.mapa_astral.first_house.sign,
                    "graus": round(self.mapa_astral.first_house.abs_pos, 2),
                    "elemento": self._obter_elemento(self.mapa_astral.first_house.sign),
                    "modalidade": self._obter_modalidade(self.mapa_astral.first_house.sign)
                }
            },
            "planetas": {},
            "elementos_dominantes": self._calcular_elementos_dominantes(),
            "modalidades_dominantes": self._calcular_modalidades_dominantes(),
            "assinatura_cosmica": self._gerar_assinatura_cosmica()
        }
        
        # Adicionar planetas
        planetas = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
        for planeta in planetas:
            if hasattr(self.mapa_astral, planeta):
                info = getattr(self.mapa_astral, planeta)
                resumo["planetas"][planeta] = {
                    "signo": info.sign,
                    "graus": round(info.abs_pos, 2),
                    "casa": info.house,
                    "elemento": self._obter_elemento(info.sign),
                    "modalidade": self._obter_modalidade(info.sign)
                }
        
        # Salvar resumo
        with open(caminho_resumo, 'w', encoding='utf-8') as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)
        
        print(f"📋 Resumo SCII-Core salvo: {nome_resumo}")
    
    def _obter_elemento(self, signo):
        """Retorna o elemento do signo"""
        elementos = {
            'Ari': 'Fogo', 'Leo': 'Fogo', 'Sag': 'Fogo',
            'Tau': 'Terra', 'Vir': 'Terra', 'Cap': 'Terra',
            'Gem': 'Ar', 'Lib': 'Ar', 'Aqu': 'Ar',
            'Can': 'Água', 'Sco': 'Água', 'Pis': 'Água'
        }
        return elementos.get(signo, 'Desconhecido')
    
    def _obter_modalidade(self, signo):
        """Retorna a modalidade do signo"""
        modalidades = {
            'Ari': 'Cardinal', 'Can': 'Cardinal', 'Lib': 'Cardinal', 'Cap': 'Cardinal',
            'Tau': 'Fixo', 'Leo': 'Fixo', 'Sco': 'Fixo', 'Aqu': 'Fixo',
            'Gem': 'Mutável', 'Vir': 'Mutável', 'Sag': 'Mutável', 'Pis': 'Mutável'
        }
        return modalidades.get(signo, 'Desconhecido')
    
    def _calcular_elementos_dominantes(self):
        """Calcula a distribuição dos elementos"""
        elementos = {'Fogo': 0, 'Terra': 0, 'Ar': 0, 'Água': 0}
        
        # Contar luminares (peso 2)
        elementos[self._obter_elemento(self.mapa_astral.sun.sign)] += 2
        elementos[self._obter_elemento(self.mapa_astral.moon.sign)] += 2
        elementos[self._obter_elemento(self.mapa_astral.first_house.sign)] += 2
        
        # Contar planetas (peso 1)
        planetas = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
        for planeta in planetas:
            if hasattr(self.mapa_astral, planeta):
                info = getattr(self.mapa_astral, planeta)
                elementos[self._obter_elemento(info.sign)] += 1
        
        return elementos
    
    def _calcular_modalidades_dominantes(self):
        """Calcula a distribuição das modalidades"""
        modalidades = {'Cardinal': 0, 'Fixo': 0, 'Mutável': 0}
        
        # Contar luminares (peso 2)
        modalidades[self._obter_modalidade(self.mapa_astral.sun.sign)] += 2
        modalidades[self._obter_modalidade(self.mapa_astral.moon.sign)] += 2
        modalidades[self._obter_modalidade(self.mapa_astral.first_house.sign)] += 2
        
        # Contar planetas (peso 1)
        planetas = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
        for planeta in planetas:
            if hasattr(self.mapa_astral, planeta):
                info = getattr(self.mapa_astral, planeta)
                modalidades[self._obter_modalidade(info.sign)] += 1
        
        return modalidades
    
    def _gerar_assinatura_cosmica(self):
        """Gera uma assinatura cósmica única baseada no mapa"""
        sol_signo = self.mapa_astral.sun.sign
        lua_signo = self.mapa_astral.moon.sign
        asc_signo = self.mapa_astral.first_house.sign
        
        # Elementos dominantes
        elementos = self._calcular_elementos_dominantes()
        elemento_dominante = max(elementos, key=elementos.get)
        
        # Modalidades dominantes
        modalidades = self._calcular_modalidades_dominantes()
        modalidade_dominante = max(modalidades, key=modalidades.get)
        
        return {
            "trindade_principal": f"{sol_signo}-{lua_signo}-{asc_signo}",
            "elemento_dominante": elemento_dominante,
            "modalidade_dominante": modalidade_dominante,
            "codigo_cosmico": f"{sol_signo[:3]}{lua_signo[:3]}{asc_signo[:3]}".upper()
        }
    
    def executar_calculo_completo(self):
        """Executa o processo completo de cálculo astral"""
        print("🌟 Iniciando cálculo da impressão digital cósmica...")
        
        # Obter dados
        dados = self.obter_dados_nascimento()
        if not dados:
            return False
        
        # Gerar mapa
        sucesso = self.gerar_mapa_astral(dados)
        
        if sucesso:
            print(f"\n🎊 CHAVE DOS CÉUS FORJADA COM SUCESSO!")
            print("=" * 50)
            print("✨ Sua impressão digital cósmica foi calculada")
            print("📁 Arquivos disponíveis para integração SCII-Core")
            print("🔮 Pronto para análises astrológicas avançadas")
        
        return sucesso

def main():
    """Função principal - interface de linha de comando"""
    calculadora = CalculadoraAstral()
    
    try:
        calculadora.executar_calculo_completo()
    except KeyboardInterrupt:
        print("\n\n👋 Cálculo astral interrompido pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("🔧 Verifique a instalação do Kerykeion e tente novamente")

if __name__ == "__main__":
    main()