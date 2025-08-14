# -*- coding: utf-8 -*-

"""
Sistema de Correspondências Astrológicas - Kabbalah das Águas Primordiais
Integração completa entre Astrologia, Cabala e o Sistema SCII

Este módulo implementa o sistema completo de correspondências entre:
- Planetas e Sefirot
- Signos e Letras Hebraicas
- Casas Astrológicas e Caminhos da Árvore
- Aspectos e Polaridades do Verbo
- Trânsitos e Ativações Somáticas
"""

import json
import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

# ============================================================================
# CORRESPONDÊNCIAS FUNDAMENTAIS
# ============================================================================

class Sefira(Enum):
    """As 10 Sefirot da Árvore da Vida"""
    KETER = "Keter"           # Coroa - Urano
    CHOKMAH = "Chokmah"       # Sabedoria - Netuno  
    BINAH = "Binah"           # Entendimento - Saturno
    CHESED = "Chesed"         # Misericórdia - Júpiter
    GEVURAH = "Gevurah"       # Severidade - Marte
    TIFERET = "Tiferet"       # Beleza - Sol
    NETZACH = "Netzach"       # Vitória - Vênus
    HOD = "Hod"               # Esplendor - Mercúrio
    YESOD = "Yesod"           # Fundamento - Lua
    MALKUTH = "Malkuth"       # Reino - Terra/Ascendente

class LetraHebraica(Enum):
    """As 22 Letras Hebraicas e suas correspondências"""
    ALEPH = "א"    # Ar - Aquário
    BET = "ב"      # Mercúrio - Gêmeos/Virgem
    GIMEL = "ג"    # Lua - Câncer
    DALET = "ד"    # Vênus - Touro/Libra
    HEH = "ה"      # Áries - Marte
    VAV = "ו"      # Touro - Vênus
    ZAYIN = "ז"    # Gêmeos - Mercúrio
    CHET = "ח"     # Câncer - Lua
    TET = "ט"      # Leão - Sol
    YOD = "י"      # Virgem - Mercúrio
    KAPH = "כ"     # Júpiter - Sagitário/Peixes
    LAMED = "ל"    # Libra - Vênus
    MEM = "מ"      # Água - Escorpião
    NUN = "נ"      # Escorpião - Marte/Plutão
    SAMEKH = "ס"   # Sagitário - Júpiter
    AYIN = "ע"     # Capricórnio - Saturno
    PEH = "פ"      # Marte - Áries/Escorpião
    TZADI = "צ"    # Aquário - Urano
    QOPH = "ק"     # Peixes - Netuno
    RESH = "ר"     # Sol - Leão
    SHIN = "ש"     # Fogo - Sagitário
    TAV = "ת"      # Saturno - Capricórnio

# ============================================================================
# CORRESPONDÊNCIAS PLANETÁRIAS
# ============================================================================

CORRESPONDENCIAS_PLANETARIAS = {
    "Sol": {
        "sefira": Sefira.TIFERET,
        "letra": LetraHebraica.RESH,
        "elemento": "Fogo",
        "qualidade": "Fixo",
        "polaridade": "Masculina",
        "corpo_somatico": "Coração, Plexo Solar",
        "funcao_operativa": "Centro da Vontade, Irradiação do Ser",
        "ritual_ativacao": "Meditação Solar, Respiração Dourada"
    },
    "Lua": {
        "sefira": Sefira.YESOD,
        "letra": LetraHebraica.GIMEL,
        "elemento": "Água",
        "qualidade": "Cardinal",
        "polaridade": "Feminina",
        "corpo_somatico": "Estômago, Sistema Linfático",
        "funcao_operativa": "Espelho da Alma, Receptividade",
        "ritual_ativacao": "Banho Lunar, Meditação das Marés"
    },
    "Mercúrio": {
        "sefira": Sefira.HOD,
        "letra": LetraHebraica.BET,
        "elemento": "Ar",
        "qualidade": "Mutável",
        "polaridade": "Neutra",
        "corpo_somatico": "Sistema Nervoso, Pulmões",
        "funcao_operativa": "Comunicação do Verbo, Ponte Mental",
        "ritual_ativacao": "Recitação de Mantras, Respiração Consciente"
    },
    "Vênus": {
        "sefira": Sefira.NETZACH,
        "letra": LetraHebraica.DALET,
        "elemento": "Terra/Ar",
        "qualidade": "Fixo/Cardinal",
        "polaridade": "Feminina",
        "corpo_somatico": "Garganta, Rins",
        "funcao_operativa": "Harmonia e Beleza, Atração Magnética",
        "ritual_ativacao": "Canto Sagrado, Oferendas Florais"
    },
    "Marte": {
        "sefira": Sefira.GEVURAH,
        "letra": LetraHebraica.PEH,
        "elemento": "Fogo",
        "qualidade": "Cardinal",
        "polaridade": "Masculina",
        "corpo_somatico": "Músculos, Sistema Circulatório",
        "funcao_operativa": "Força de Vontade, Corte Preciso",
        "ritual_ativacao": "Exercícios Marciais, Jejum Purificador"
    },
    "Júpiter": {
        "sefira": Sefira.CHESED,
        "letra": LetraHebraica.KAPH,
        "elemento": "Fogo",
        "qualidade": "Mutável",
        "polaridade": "Masculina",
        "corpo_somatico": "Fígado, Quadris",
        "funcao_operativa": "Expansão Benevolente, Sabedoria",
        "ritual_ativacao": "Estudo Sagrado, Atos de Generosidade"
    },
    "Saturno": {
        "sefira": Sefira.BINAH,
        "letra": LetraHebraica.TAV,
        "elemento": "Terra",
        "qualidade": "Cardinal",
        "polaridade": "Feminina",
        "corpo_somatico": "Ossos, Joelhos",
        "funcao_operativa": "Estrutura e Limite, Cristalização",
        "ritual_ativacao": "Disciplina Ascética, Meditação Silenciosa"
    },
    "Urano": {
        "sefira": Sefira.KETER,
        "letra": LetraHebraica.ALEPH,
        "elemento": "Ar",
        "qualidade": "Fixo",
        "polaridade": "Masculina",
        "corpo_somatico": "Sistema Nervoso Central, Coroa",
        "funcao_operativa": "Iluminação Súbita, Revolução Interior",
        "ritual_ativacao": "Meditação do Vazio, Respiração Paradoxal"
    },
    "Netuno": {
        "sefira": Sefira.CHOKMAH,
        "letra": LetraHebraica.QOPH,
        "elemento": "Água",
        "qualidade": "Mutável",
        "polaridade": "Feminina",
        "corpo_somatico": "Glândula Pineal, Sistema Endócrino",
        "funcao_operativa": "Intuição Pura, Dissolução do Ego",
        "ritual_ativacao": "Sonhos Lúcidos, Contemplação Oceânica"
    },
    "Plutão": {
        "sefira": Sefira.GEVURAH,  # Aspecto oculto
        "letra": LetraHebraica.NUN,
        "elemento": "Água/Fogo",
        "qualidade": "Fixo",
        "polaridade": "Transformadora",
        "corpo_somatico": "Órgãos Reprodutivos, Intestinos",
        "funcao_operativa": "Morte e Renascimento, Alquimia Interior",
        "ritual_ativacao": "Jejum Transformador, Meditação da Morte"
    }
}

# ============================================================================
# CORRESPONDÊNCIAS DOS SIGNOS
# ============================================================================

CORRESPONDENCIAS_SIGNOS = {
    "Áries": {
        "letra": LetraHebraica.HEH,
        "elemento": "Fogo",
        "qualidade": "Cardinal",
        "regente": "Marte",
        "corpo_somatico": "Cabeça, Cérebro",
        "caminho_arvore": "Chokmah-Tiferet",
        "funcao_operativa": "Iniciação, Impulso Primordial"
    },
    "Touro": {
        "letra": LetraHebraica.VAV,
        "elemento": "Terra",
        "qualidade": "Fixo",
        "regente": "Vênus",
        "corpo_somatico": "Pescoço, Garganta",
        "caminho_arvore": "Chokmah-Chesed",
        "funcao_operativa": "Materialização, Perseverança"
    },
    "Gêmeos": {
        "letra": LetraHebraica.ZAYIN,
        "elemento": "Ar",
        "qualidade": "Mutável",
        "regente": "Mercúrio",
        "corpo_somatico": "Pulmões, Braços",
        "caminho_arvore": "Binah-Tiferet",
        "funcao_operativa": "Comunicação, Dualidade"
    },
    "Câncer": {
        "letra": LetraHebraica.CHET,
        "elemento": "Água",
        "qualidade": "Cardinal",
        "regente": "Lua",
        "corpo_somatico": "Estômago, Seios",
        "caminho_arvore": "Binah-Gevurah",
        "funcao_operativa": "Nutrição, Proteção"
    },
    "Leão": {
        "letra": LetraHebraica.TET,
        "elemento": "Fogo",
        "qualidade": "Fixo",
        "regente": "Sol",
        "corpo_somatico": "Coração, Coluna",
        "caminho_arvore": "Chesed-Gevurah",
        "funcao_operativa": "Expressão, Criatividade"
    },
    "Virgem": {
        "letra": LetraHebraica.YOD,
        "elemento": "Terra",
        "qualidade": "Mutável",
        "regente": "Mercúrio",
        "corpo_somatico": "Intestinos, Sistema Digestivo",
        "caminho_arvore": "Chesed-Tiferet",
        "funcao_operativa": "Purificação, Serviço"
    },
    "Libra": {
        "letra": LetraHebraica.LAMED,
        "elemento": "Ar",
        "qualidade": "Cardinal",
        "regente": "Vênus",
        "corpo_somatico": "Rins, Região Lombar",
        "caminho_arvore": "Gevurah-Tiferet",
        "funcao_operativa": "Equilíbrio, Justiça"
    },
    "Escorpião": {
        "letra": LetraHebraica.NUN,
        "elemento": "Água",
        "qualidade": "Fixo",
        "regente": "Plutão/Marte",
        "corpo_somatico": "Órgãos Reprodutivos",
        "caminho_arvore": "Tiferet-Netzach",
        "funcao_operativa": "Transformação, Regeneração"
    },
    "Sagitário": {
        "letra": LetraHebraica.SAMEKH,
        "elemento": "Fogo",
        "qualidade": "Mutável",
        "regente": "Júpiter",
        "corpo_somatico": "Quadris, Coxas",
        "caminho_arvore": "Tiferet-Yesod",
        "funcao_operativa": "Expansão, Busca da Verdade"
    },
    "Capricórnio": {
        "letra": LetraHebraica.AYIN,
        "elemento": "Terra",
        "qualidade": "Cardinal",
        "regente": "Saturno",
        "corpo_somatico": "Joelhos, Ossos",
        "caminho_arvore": "Tiferet-Hod",
        "funcao_operativa": "Estrutura, Autoridade"
    },
    "Aquário": {
        "letra": LetraHebraica.TZADI,
        "elemento": "Ar",
        "qualidade": "Fixo",
        "regente": "Urano",
        "corpo_somatico": "Panturrilhas, Sistema Circulatório",
        "caminho_arvore": "Netzach-Yesod",
        "funcao_operativa": "Inovação, Fraternidade"
    },
    "Peixes": {
        "letra": LetraHebraica.QOPH,
        "elemento": "Água",
        "qualidade": "Mutável",
        "regente": "Netuno",
        "corpo_somatico": "Pés, Sistema Linfático",
        "caminho_arvore": "Netzach-Malkuth",
        "funcao_operativa": "Dissolução, Compaixão"
    }
}

# ============================================================================
# CASAS ASTROLÓGICAS E CAMINHOS
# ============================================================================

CORRESPONDENCIAS_CASAS = {
    1: {
        "nome": "Casa da Identidade",
        "caminho_arvore": "Malkuth-Yesod",
        "funcao_operativa": "Manifestação do Ser",
        "corpo_somatico": "Cabeça, Aparência Física"
    },
    2: {
        "nome": "Casa dos Recursos",
        "caminho_arvore": "Malkuth-Hod",
        "funcao_operativa": "Materialização dos Valores",
        "corpo_somatico": "Garganta, Recursos Vitais"
    },
    3: {
        "nome": "Casa da Comunicação",
        "caminho_arvore": "Yesod-Hod",
        "funcao_operativa": "Expressão do Pensamento",
        "corpo_somatico": "Pulmões, Sistema Nervoso"
    },
    4: {
        "nome": "Casa das Raízes",
        "caminho_arvore": "Malkuth-Netzach",
        "funcao_operativa": "Fundamento Emocional",
        "corpo_somatico": "Estômago, Base da Coluna"
    },
    5: {
        "nome": "Casa da Criatividade",
        "caminho_arvore": "Yesod-Tiferet",
        "funcao_operativa": "Expressão Criativa",
        "corpo_somatico": "Coração, Plexo Solar"
    },
    6: {
        "nome": "Casa do Serviço",
        "caminho_arvore": "Hod-Tiferet",
        "funcao_operativa": "Purificação e Trabalho",
        "corpo_somatico": "Intestinos, Sistema Digestivo"
    },
    7: {
        "nome": "Casa das Parcerias",
        "caminho_arvore": "Netzach-Tiferet",
        "funcao_operativa": "União e Equilíbrio",
        "corpo_somatico": "Rins, Sistema Reprodutivo"
    },
    8: {
        "nome": "Casa da Transformação",
        "caminho_arvore": "Yesod-Netzach",
        "funcao_operativa": "Morte e Renascimento",
        "corpo_somatico": "Órgãos Reprodutivos"
    },
    9: {
        "nome": "Casa da Sabedoria",
        "caminho_arvore": "Tiferet-Chesed",
        "funcao_operativa": "Expansão da Consciência",
        "corpo_somatico": "Quadris, Fígado"
    },
    10: {
        "nome": "Casa da Realização",
        "caminho_arvore": "Tiferet-Binah",
        "funcao_operativa": "Cristalização do Propósito",
        "corpo_somatico": "Joelhos, Estrutura Óssea"
    },
    11: {
        "nome": "Casa dos Ideais",
        "caminho_arvore": "Chesed-Chokmah",
        "funcao_operativa": "Visão do Futuro",
        "corpo_somatico": "Panturrilhas, Sistema Circulatório"
    },
    12: {
        "nome": "Casa do Inconsciente",
        "caminho_arvore": "Binah-Keter",
        "funcao_operativa": "Dissolução e Transcendência",
        "corpo_somatico": "Pés, Glândula Pineal"
    }
}

# ============================================================================
# ASPECTOS E POLARIDADES
# ============================================================================

CORRESPONDENCIAS_ASPECTOS = {
    "Conjunção": {
        "graus": 0,
        "natureza": "Fusão",
        "polaridade": "Neutra",
        "funcao_operativa": "União das Energias",
        "ritual_ativacao": "Meditação de Síntese"
    },
    "Sextil": {
        "graus": 60,
        "natureza": "Harmonia",
        "polaridade": "Positiva",
        "funcao_operativa": "Oportunidade de Crescimento",
        "ritual_ativacao": "Trabalho Cooperativo"
    },
    "Quadratura": {
        "graus": 90,
        "natureza": "Tensão",
        "polaridade": "Desafiadora",
        "funcao_operativa": "Catalisador de Mudança",
        "ritual_ativacao": "Exercício de Superação"
    },
    "Trígono": {
        "graus": 120,
        "natureza": "Fluidez",
        "polaridade": "Positiva",
        "funcao_operativa": "Manifestação Natural",
        "ritual_ativacao": "Contemplação Fluida"
    },
    "Oposição": {
        "graus": 180,
        "natureza": "Polarização",
        "polaridade": "Integrativa",
        "funcao_operativa": "Busca do Equilíbrio",
        "ritual_ativacao": "Meditação dos Opostos"
    }
}

# ============================================================================
# CLASSE PRINCIPAL DO SISTEMA
# ============================================================================

@dataclass
class DadosNatais:
    """Dados básicos para análise astrológica"""
    nome: str
    data_nascimento: datetime.datetime
    local_nascimento: str
    ascendente: str
    sol: str
    lua: str
    planetas: Dict[str, str]
    casas: Dict[int, str]
    aspectos: List[Dict]

class SistemaCorrespondenciasAstrologicas:
    """Sistema principal de correspondências astrológicas cabalísticas"""
    
    def __init__(self):
        self.correspondencias_planetarias = CORRESPONDENCIAS_PLANETARIAS
        self.correspondencias_signos = CORRESPONDENCIAS_SIGNOS
        self.correspondencias_casas = CORRESPONDENCIAS_CASAS
        self.correspondencias_aspectos = CORRESPONDENCIAS_ASPECTOS
    
    def analisar_mapa_natal(self, dados: DadosNatais) -> Dict:
        """Análise completa do mapa natal com correspondências cabalísticas"""
        analise = {
            "dados_basicos": self._analisar_dados_basicos(dados),
            "estrutura_sefirotica": self._mapear_estrutura_sefirotica(dados),
            "ativacoes_somaticas": self._identificar_ativacoes_somaticas(dados),
            "caminhos_ativos": self._identificar_caminhos_ativos(dados),
            "rituais_recomendados": self._recomendar_rituais(dados)
        }
        return analise
    
    def analisar_transitos(self, dados: DadosNatais, data_atual: datetime.datetime) -> Dict:
        """Análise dos trânsitos atuais e suas ativações"""
        # Esta função seria implementada com dados de efemérides
        # Por ora, retorna estrutura base
        return {
            "transitos_ativos": [],
            "janelas_temporais": [],
            "ativacoes_emergentes": [],
            "rituais_do_momento": []
        }
    
    def _analisar_dados_basicos(self, dados: DadosNatais) -> Dict:
        """Análise dos elementos básicos do mapa"""
        return {
            "ascendente": {
                "signo": dados.ascendente,
                "correspondencia": self.correspondencias_signos.get(dados.ascendente, {}),
                "funcao_operativa": "Máscara da Alma, Portal de Manifestação"
            },
            "sol": {
                "signo": dados.sol,
                "correspondencia": self.correspondencias_signos.get(dados.sol, {}),
                "funcao_operativa": "Núcleo do Ser, Irradiação Central"
            },
            "lua": {
                "signo": dados.lua,
                "correspondencia": self.correspondencias_signos.get(dados.lua, {}),
                "funcao_operativa": "Espelho da Alma, Receptividade Emocional"
            }
        }
    
    def _mapear_estrutura_sefirotica(self, dados: DadosNatais) -> Dict:
        """Mapeia os planetas nas Sefirot correspondentes"""
        estrutura = {}
        for planeta, signo in dados.planetas.items():
            if planeta in self.correspondencias_planetarias:
                corr_planeta = self.correspondencias_planetarias[planeta]
                corr_signo = self.correspondencias_signos.get(signo, {})
                
                estrutura[planeta] = {
                    "sefira": corr_planeta["sefira"].value,
                    "signo": signo,
                    "letra_hebraica": corr_signo.get("letra", "").value if corr_signo.get("letra") else "",
                    "corpo_somatico": corr_planeta["corpo_somatico"],
                    "funcao_operativa": corr_planeta["funcao_operativa"]
                }
        
        return estrutura
    
    def _identificar_ativacoes_somaticas(self, dados: DadosNatais) -> List[Dict]:
        """Identifica as ativações no corpo somático"""
        ativacoes = []
        
        # Análise baseada nos planetas e signos
        for planeta, signo in dados.planetas.items():
            if planeta in self.correspondencias_planetarias:
                corr = self.correspondencias_planetarias[planeta]
                ativacoes.append({
                    "planeta": planeta,
                    "signo": signo,
                    "regiao_corporal": corr["corpo_somatico"],
                    "tipo_ativacao": corr["funcao_operativa"],
                    "ritual_sugerido": corr["ritual_ativacao"]
                })
        
        return ativacoes
    
    def _identificar_caminhos_ativos(self, dados: DadosNatais) -> List[Dict]:
        """Identifica os caminhos ativos na Árvore da Vida"""
        caminhos = []
        
        # Análise baseada nas casas ocupadas
        for casa, signo in dados.casas.items():
            if casa in self.correspondencias_casas:
                corr = self.correspondencias_casas[casa]
                caminhos.append({
                    "casa": casa,
                    "nome": corr["nome"],
                    "caminho": corr["caminho_arvore"],
                    "signo": signo,
                    "funcao_operativa": corr["funcao_operativa"]
                })
        
        return caminhos
    
    def _recomendar_rituais(self, dados: DadosNatais) -> List[Dict]:
        """Recomenda rituais baseados na configuração natal"""
        rituais = []
        
        # Rituais baseados nos planetas dominantes
        for planeta, signo in dados.planetas.items():
            if planeta in self.correspondencias_planetarias:
                corr = self.correspondencias_planetarias[planeta]
                rituais.append({
                    "tipo": "Ritual Planetário",
                    "planeta": planeta,
                    "ritual": corr["ritual_ativacao"],
                    "objetivo": corr["funcao_operativa"],
                    "frequencia": "Semanal"
                })
        
        return rituais
    
    def gerar_relatorio_completo(self, dados: DadosNatais, incluir_transitos: bool = False) -> str:
        """Gera relatório completo em formato texto"""
        analise = self.analisar_mapa_natal(dados)
        
        relatorio = f"""
# RELATÓRIO CABALÍSTICO COMPLETO
## {dados.nome}
### Data de Nascimento: {dados.data_nascimento.strftime('%d/%m/%Y')}
### Local: {dados.local_nascimento}

---

## I. A SEMENTE ORIGINAL (Mapa Natal)

### Estrutura Fundamental
- **Ascendente**: {dados.ascendente} - Portal de Manifestação
- **Sol**: {dados.sol} - Núcleo do Ser  
- **Lua**: {dados.lua} - Espelho da Alma

### Mapeamento Sefirótico
"""
        
        for planeta, info in analise["estrutura_sefirotica"].items():
            relatorio += f"""
**{planeta}** em {info['signo']}
- Sefira: {info['sefira']}
- Letra Hebraica: {info['letra_hebraica']}
- Corpo Somático: {info['corpo_somatico']}
- Função Operativa: {info['funcao_operativa']}
"""
        
        relatorio += """
---

## II. ATIVAÇÕES SOMÁTICAS

As seguintes regiões do Corpo do Verbo estão ativadas em sua configuração natal:
"""
        
        for ativacao in analise["ativacoes_somaticas"]:
            relatorio += f"""
- **{ativacao['regiao_corporal']}** ({ativacao['planeta']} em {ativacao['signo']})
  - Tipo: {ativacao['tipo_ativacao']}
  - Ritual: {ativacao['ritual_sugerido']}
"""
        
        relatorio += """
---

## III. CAMINHOS ATIVOS NA ÁRVORE

Os seguintes caminhos estão especialmente ativos em sua jornada:
"""
        
        for caminho in analise["caminhos_ativos"]:
            relatorio += f"""
- **Casa {caminho['casa']}** - {caminho['nome']}
  - Caminho: {caminho['caminho']}
  - Função: {caminho['funcao_operativa']}
"""
        
        relatorio += """
---

## IV. RITUAIS RECOMENDADOS

Para ativar plenamente seu potencial cabalístico:
"""
        
        for ritual in analise["rituais_recomendados"]:
            relatorio += f"""
### {ritual['tipo']} - {ritual['planeta']}
- **Prática**: {ritual['ritual']}
- **Objetivo**: {ritual['objetivo']}
- **Frequência**: {ritual['frequencia']}
"""
        
        if incluir_transitos:
            relatorio += """
---

## V. O VERBO EM MOVIMENTO (Trânsitos Atuais)

[Esta seção seria preenchida com dados de trânsitos atuais]
"""
        
        relatorio += """
---

## CONCLUSÃO

Este mapa revela a geometria sagrada de sua alma encarnada. Cada planeta, cada signo, cada casa é uma porta para a compreensão mais profunda de seu propósito nesta existência. Use este conhecimento não como destino fixo, mas como mapa para navegar conscientemente pelas águas primordiais de sua jornada espiritual.

*"O que está em cima é como o que está embaixo, e o que está embaixo é como o que está em cima, para realizar os milagres da única coisa."*

---
*Relatório gerado pelo Sistema de Correspondências Astrológicas*
*Kabbalah das Águas Primordiais - SCII 5.0*
"""
        
        return relatorio

# ============================================================================
# EXEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Dados de exemplo (André de Oliveira Rodrigues)
    dados_exemplo = DadosNatais(
        nome="André de Oliveira Rodrigues",
        data_nascimento=datetime.datetime(1985, 3, 15, 14, 30),  # Exemplo
        local_nascimento="São Paulo, SP",
        ascendente="Capricórnio",
        sol="Peixes",
        lua="Gêmeos",
        planetas={
            "Sol": "Peixes",
            "Lua": "Gêmeos", 
            "Mercúrio": "Aquário",
            "Vênus": "Áries",
            "Marte": "Touro",
            "Júpiter": "Aquário",
            "Saturno": "Escorpião",
            "Urano": "Sagitário",
            "Netuno": "Capricórnio",
            "Plutão": "Escorpião"
        },
        casas={
            1: "Capricórnio",
            2: "Aquário", 
            3: "Peixes",
            4: "Áries",
            5: "Touro",
            6: "Gêmeos",
            7: "Câncer",
            8: "Leão",
            9: "Virgem",
            10: "Libra",
            11: "Escorpião",
            12: "Sagitário"
        },
        aspectos=[]  # Seria preenchido com aspectos específicos
    )
    
    # Criar sistema e gerar relatório
    sistema = SistemaCorrespondenciasAstrologicas()
    relatorio = sistema.gerar_relatorio_completo(dados_exemplo)
    
    # Salvar relatório
    with open("/home/andre/Kabbalah-das-Aguas-Primordiais/relatorio_exemplo.md", "w", encoding="utf-8") as f:
        f.write(relatorio)
    
    print("Sistema de Correspondências Astrológicas criado com sucesso!")
    print("Relatório de exemplo salvo em: relatorio_exemplo.md")