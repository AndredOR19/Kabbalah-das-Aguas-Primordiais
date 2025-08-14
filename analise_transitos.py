# -*- coding: utf-8 -*-

"""
Módulo de Análise de Trânsitos - Kabbalah das Águas Primordiais
Sistema avançado para análise de trânsitos planetários e suas correspondências cabalísticas

Este módulo implementa:
- Cálculo de trânsitos planetários
- Análise de janelas temporais
- Correspondências cabalísticas dos trânsitos
- Rituais específicos para cada período
- Integração com o Sistema SCII
"""

import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import json

# ============================================================================
# CICLOS PLANETÁRIOS E CORRESPONDÊNCIAS
# ============================================================================

CICLOS_PLANETARIOS = {
    "Lua": {
        "ciclo_completo": 29.5,  # dias
        "tipo": "Emocional/Receptivo",
        "sefira": "Yesod",
        "funcao": "Espelhamento da Alma"
    },
    "Mercúrio": {
        "ciclo_completo": 88,  # dias
        "tipo": "Mental/Comunicativo", 
        "sefira": "Hod",
        "funcao": "Ponte do Verbo"
    },
    "Vênus": {
        "ciclo_completo": 225,  # dias
        "tipo": "Harmônico/Estético",
        "sefira": "Netzach", 
        "funcao": "Beleza e Atração"
    },
    "Sol": {
        "ciclo_completo": 365.25,  # dias
        "tipo": "Vital/Central",
        "sefira": "Tiferet",
        "funcao": "Irradiação do Ser"
    },
    "Marte": {
        "ciclo_completo": 687,  # dias (1.88 anos)
        "tipo": "Ativo/Assertivo",
        "sefira": "Gevurah",
        "funcao": "Força de Vontade"
    },
    "Júpiter": {
        "ciclo_completo": 4333,  # dias (11.86 anos)
        "tipo": "Expansivo/Benéfico",
        "sefira": "Chesed",
        "funcao": "Misericórdia e Crescimento"
    },
    "Saturno": {
        "ciclo_completo": 10759,  # dias (29.46 anos)
        "tipo": "Estrutural/Limitador",
        "sefira": "Binah",
        "funcao": "Cristalização e Disciplina"
    },
    "Urano": {
        "ciclo_completo": 30687,  # dias (84.01 anos)
        "tipo": "Revolucionário/Libertador",
        "sefira": "Keter",
        "funcao": "Iluminação Súbita"
    },
    "Netuno": {
        "ciclo_completo": 60190,  # dias (164.8 anos)
        "tipo": "Dissolutivo/Inspirador",
        "sefira": "Chokmah",
        "funcao": "Sabedoria Intuitiva"
    },
    "Plutão": {
        "ciclo_completo": 90560,  # dias (248 anos)
        "tipo": "Transformador/Regenerador",
        "sefira": "Gevurah Oculta",
        "funcao": "Morte e Renascimento"
    }
}

# ============================================================================
# TIPOS DE TRÂNSITOS E SUAS INTERPRETAÇÕES
# ============================================================================

TIPOS_TRANSITOS = {
    "Conjunção": {
        "orbe": 8,
        "natureza": "Fusão de Energias",
        "interpretacao": "Novo ciclo iniciático, fusão de potenciais",
        "ritual_base": "Meditação de Síntese",
        "duracao_media": "3-7 dias (planetas rápidos), 1-3 anos (planetas lentos)"
    },
    "Sextil": {
        "orbe": 6,
        "natureza": "Oportunidade Harmônica",
        "interpretacao": "Abertura de caminhos, facilidade de manifestação",
        "ritual_base": "Trabalho Cooperativo",
        "duracao_media": "2-5 dias (planetas rápidos), 6 meses-1 ano (planetas lentos)"
    },
    "Quadratura": {
        "orbe": 8,
        "natureza": "Tensão Criativa",
        "interpretacao": "Desafio evolutivo, catalisador de crescimento",
        "ritual_base": "Exercício de Superação",
        "duracao_media": "3-7 dias (planetas rápidos), 1-2 anos (planetas lentos)"
    },
    "Trígono": {
        "orbe": 8,
        "natureza": "Fluxo Natural",
        "interpretacao": "Manifestação espontânea, talentos ativados",
        "ritual_base": "Contemplação Fluida",
        "duracao_media": "3-7 dias (planetas rápidos), 1-2 anos (planetas lentos)"
    },
    "Oposição": {
        "orbe": 8,
        "natureza": "Polarização Integrativa",
        "interpretacao": "Busca de equilíbrio, consciência dos opostos",
        "ritual_base": "Meditação dos Opostos",
        "duracao_media": "3-7 dias (planetas rápidos), 1-3 anos (planetas lentos)"
    }
}

# ============================================================================
# FASES ESPECÍFICAS DOS TRÂNSITOS
# ============================================================================

FASES_SATURNO = {
    "Primeira Quadratura (7 anos)": {
        "significado": "Primeira crise de estrutura",
        "desafio": "Estabelecer limites pessoais",
        "oportunidade": "Desenvolver disciplina",
        "ritual": "Exercícios de Foco e Concentração"
    },
    "Oposição (14-15 anos)": {
        "significado": "Crise da adolescência",
        "desafio": "Questionar autoridades",
        "oportunidade": "Encontrar autoridade interior",
        "ritual": "Rituais de Passagem"
    },
    "Segunda Quadratura (21-22 anos)": {
        "significado": "Crise de responsabilidade",
        "desafio": "Assumir papel adulto",
        "oportunidade": "Cristalizar propósito",
        "ritual": "Compromissos Sagrados"
    },
    "Primeiro Retorno (29-30 anos)": {
        "significado": "Maturidade espiritual",
        "desafio": "Integrar lições da juventude",
        "oportunidade": "Estabelecer fundações sólidas",
        "ritual": "Ritual de Maturidade"
    },
    "Segundo Retorno (58-60 anos)": {
        "significado": "Sabedoria da experiência",
        "desafio": "Aceitar limitações físicas",
        "oportunidade": "Tornar-se mentor",
        "ritual": "Transmissão de Sabedoria"
    }
}

FASES_JUPITER = {
    "Primeiro Retorno (12 anos)": {
        "significado": "Expansão da consciência infantil",
        "oportunidade": "Descobrir talentos naturais",
        "ritual": "Celebração dos Dons"
    },
    "Segundo Retorno (24 anos)": {
        "significado": "Expansão da consciência adulta",
        "oportunidade": "Estabelecer filosofia de vida",
        "ritual": "Definição de Propósito"
    },
    "Terceiro Retorno (36 anos)": {
        "significado": "Expansão da sabedoria",
        "oportunidade": "Ensinar e compartilhar",
        "ritual": "Abertura para o Ensino"
    },
    "Quarto Retorno (48 anos)": {
        "significado": "Expansão da compreensão",
        "oportunidade": "Integrar experiências",
        "ritual": "Síntese da Jornada"
    }
}

# ============================================================================
# CLASSES PRINCIPAIS
# ============================================================================

@dataclass
class Transito:
    """Representa um trânsito planetário específico"""
    planeta_transitante: str
    planeta_natal: str
    tipo_aspecto: str
    data_inicio: datetime.datetime
    data_exata: datetime.datetime
    data_fim: datetime.datetime
    orbe_atual: float
    intensidade: str  # "Aproximação", "Exato", "Separação"
    
@dataclass
class JanelaTransito:
    """Representa uma janela temporal de influência"""
    nome: str
    periodo_inicio: datetime.datetime
    periodo_fim: datetime.datetime
    planetas_envolvidos: List[str]
    temas_principais: List[str]
    rituais_recomendados: List[str]
    intensidade_geral: str

class AnalisadorTransitos:
    """Classe principal para análise de trânsitos"""
    
    def __init__(self):
        self.ciclos = CICLOS_PLANETARIOS
        self.tipos_transitos = TIPOS_TRANSITOS
        self.fases_saturno = FASES_SATURNO
        self.fases_jupiter = FASES_JUPITER
    
    def calcular_fase_saturno(self, idade_atual: float) -> Dict:
        """Calcula a fase atual do ciclo de Saturno"""
        ciclo_saturno = 29.46
        posicao_no_ciclo = idade_atual % ciclo_saturno
        
        if 6 <= posicao_no_ciclo <= 8:
            return {
                "fase": "Primeira Quadratura",
                "detalhes": self.fases_saturno["Primeira Quadratura (7 anos)"],
                "posicao_exata": posicao_no_ciclo
            }
        elif 13 <= posicao_no_ciclo <= 16:
            return {
                "fase": "Oposição",
                "detalhes": self.fases_saturno["Oposição (14-15 anos)"],
                "posicao_exata": posicao_no_ciclo
            }
        elif 20 <= posicao_no_ciclo <= 23:
            return {
                "fase": "Segunda Quadratura", 
                "detalhes": self.fases_saturno["Segunda Quadratura (21-22 anos)"],
                "posicao_exata": posicao_no_ciclo
            }
        elif 28 <= posicao_no_ciclo <= 1 or posicao_no_ciclo <= 1:
            return {
                "fase": "Retorno de Saturno",
                "detalhes": self.fases_saturno["Primeiro Retorno (29-30 anos)"],
                "posicao_exata": posicao_no_ciclo
            }
        else:
            return {
                "fase": "Período de Integração",
                "detalhes": {
                    "significado": "Período de assimilação das lições",
                    "oportunidade": "Aplicar estruturas aprendidas",
                    "ritual": "Prática Consistente"
                },
                "posicao_exata": posicao_no_ciclo
            }
    
    def calcular_fase_jupiter(self, idade_atual: float) -> Dict:
        """Calcula a fase atual do ciclo de Júpiter"""
        ciclo_jupiter = 11.86
        numero_retornos = int(idade_atual // ciclo_jupiter)
        posicao_no_ciclo = idade_atual % ciclo_jupiter
        
        retornos_proximos = []
        for i in range(1, 6):
            idade_retorno = i * ciclo_jupiter
            if abs(idade_atual - idade_retorno) <= 0.5:  # Dentro de 6 meses
                retornos_proximos.append({
                    "numero": i,
                    "idade": idade_retorno,
                    "detalhes": self.fases_jupiter.get(f"{self._ordinal(i)} Retorno ({int(idade_retorno)} anos)", {})
                })
        
        return {
            "retornos_completos": numero_retornos,
            "posicao_atual": posicao_no_ciclo,
            "retornos_proximos": retornos_proximos,
            "fase_atual": self._determinar_fase_jupiter(posicao_no_ciclo)
        }
    
    def _ordinal(self, n: int) -> str:
        """Converte número em ordinal"""
        ordinais = {1: "Primeiro", 2: "Segundo", 3: "Terceiro", 4: "Quarto", 5: "Quinto"}
        return ordinais.get(n, f"{n}º")
    
    def _determinar_fase_jupiter(self, posicao: float) -> Dict:
        """Determina a fase atual dentro do ciclo de Júpiter"""
        if 0 <= posicao <= 3:
            return {
                "nome": "Semeadura",
                "significado": "Plantio de novas possibilidades",
                "acao": "Explorar e expandir horizontes"
            }
        elif 3 < posicao <= 6:
            return {
                "nome": "Crescimento",
                "significado": "Desenvolvimento das oportunidades",
                "acao": "Nutrir e desenvolver projetos"
            }
        elif 6 < posicao <= 9:
            return {
                "nome": "Florescimento",
                "significado": "Manifestação dos frutos",
                "acao": "Colher resultados e compartilhar"
            }
        else:
            return {
                "nome": "Preparação",
                "significado": "Preparação para novo ciclo",
                "acao": "Integrar aprendizados e preparar terreno"
            }
    
    def analisar_transitos_periodo(self, data_inicio: datetime.datetime, 
                                 data_fim: datetime.datetime,
                                 dados_natais: Dict) -> Dict:
        """Analisa trânsitos para um período específico"""
        
        # Esta função seria implementada com dados de efemérides reais
        # Por ora, retorna estrutura base para demonstração
        
        analise = {
            "periodo": {
                "inicio": data_inicio.strftime("%d/%m/%Y"),
                "fim": data_fim.strftime("%d/%m/%Y"),
                "duracao_dias": (data_fim - data_inicio).days
            },
            "transitos_principais": self._simular_transitos_principais(data_inicio, data_fim),
            "janelas_temporais": self._identificar_janelas_temporais(data_inicio, data_fim),
            "rituais_periodo": self._recomendar_rituais_periodo(data_inicio, data_fim),
            "temas_dominantes": self._identificar_temas_dominantes(data_inicio, data_fim)
        }
        
        return analise
    
    def _simular_transitos_principais(self, inicio: datetime.datetime, fim: datetime.datetime) -> List[Dict]:
        """Simula trânsitos principais para demonstração"""
        # Em implementação real, usaria efemérides
        transitos = [
            {
                "planeta": "Júpiter",
                "aspecto": "Trígono",
                "planeta_natal": "Sol",
                "data_exata": inicio + datetime.timedelta(days=30),
                "interpretacao": "Período de expansão solar, crescimento da autoestima",
                "oportunidades": ["Reconhecimento profissional", "Crescimento pessoal"],
                "rituais": ["Meditação Solar Matinal", "Afirmações de Abundância"]
            },
            {
                "planeta": "Saturno",
                "aspecto": "Quadratura",
                "planeta_natal": "Lua",
                "data_exata": inicio + datetime.timedelta(days=45),
                "interpretacao": "Reestruturação emocional, disciplina dos sentimentos",
                "desafios": ["Controle emocional", "Responsabilidade afetiva"],
                "rituais": ["Jejum Emocional", "Meditação da Disciplina"]
            }
        ]
        return transitos
    
    def _identificar_janelas_temporais(self, inicio: datetime.datetime, fim: datetime.datetime) -> List[JanelaTransito]:
        """Identifica janelas temporais importantes"""
        janelas = [
            JanelaTransito(
                nome="Portal de Expansão Jupiteriana",
                periodo_inicio=inicio + datetime.timedelta(days=25),
                periodo_fim=inicio + datetime.timedelta(days=35),
                planetas_envolvidos=["Júpiter", "Sol"],
                temas_principais=["Crescimento", "Reconhecimento", "Abundância"],
                rituais_recomendados=["Ritual Solar", "Oferendas de Gratidão"],
                intensidade_geral="Alta"
            ),
            JanelaTransito(
                nome="Reestruturação Saturnina",
                periodo_inicio=inicio + datetime.timedelta(days=40),
                periodo_fim=inicio + datetime.timedelta(days=50),
                planetas_envolvidos=["Saturno", "Lua"],
                temas_principais=["Disciplina", "Estrutura", "Responsabilidade"],
                rituais_recomendados=["Meditação Silenciosa", "Exercícios de Foco"],
                intensidade_geral="Média-Alta"
            )
        ]
        return janelas
    
    def _recomendar_rituais_periodo(self, inicio: datetime.datetime, fim: datetime.datetime) -> Dict:
        """Recomenda rituais específicos para o período"""
        return {
            "rituais_diarios": [
                "Meditação matinal com letra hebraica do dia",
                "Respiração consciente ao meio-dia",
                "Contemplação noturna dos trânsitos"
            ],
            "rituais_semanais": [
                "Domingo: Ritual Solar (Resh ר)",
                "Segunda: Ritual Lunar (Gimel ג)",
                "Terça: Ritual Marciano (Peh פ)",
                "Quarta: Ritual Mercurial (Bet ב)",
                "Quinta: Ritual Jupiteriano (Kaph כ)",
                "Sexta: Ritual Venusiano (Dalet ד)",
                "Sábado: Ritual Saturnino (Tav ת)"
            ],
            "rituais_especiais": [
                {
                    "data": inicio + datetime.timedelta(days=30),
                    "nome": "Ritual de Expansão Jupiteriana",
                    "descricao": "Cerimônia de abertura para abundância"
                },
                {
                    "data": inicio + datetime.timedelta(days=45),
                    "nome": "Ritual de Estruturação Saturnina",
                    "descricao": "Cerimônia de disciplina e foco"
                }
            ]
        }
    
    def _identificar_temas_dominantes(self, inicio: datetime.datetime, fim: datetime.datetime) -> List[Dict]:
        """Identifica temas dominantes do período"""
        return [
            {
                "tema": "Expansão e Crescimento",
                "planeta_regente": "Júpiter",
                "sefira": "Chesed",
                "manifestacao": "Oportunidades de crescimento profissional e pessoal",
                "desafio": "Não se dispersar em muitas direções",
                "ritual_chave": "Meditação da Abundância Focada"
            },
            {
                "tema": "Estruturação e Disciplina",
                "planeta_regente": "Saturno",
                "sefira": "Binah",
                "manifestacao": "Necessidade de organizar e disciplinar aspectos da vida",
                "desafio": "Não se tornar rígido demais",
                "ritual_chave": "Exercícios de Flexibilidade Estruturada"
            }
        ]
    
    def gerar_relatorio_transitos(self, dados_natais: Dict, periodo_dias: int = 90) -> str:
        """Gera relatório completo de trânsitos"""
        
        data_atual = datetime.datetime.now()
        data_fim = data_atual + datetime.timedelta(days=periodo_dias)
        
        # Calcular idade atual (aproximada)
        if 'data_nascimento' in dados_natais:
            idade = (data_atual - dados_natais['data_nascimento']).days / 365.25
        else:
            idade = 35  # Valor padrão para demonstração
        
        fase_saturno = self.calcular_fase_saturno(idade)
        fase_jupiter = self.calcular_fase_jupiter(idade)
        analise_periodo = self.analisar_transitos_periodo(data_atual, data_fim, dados_natais)
        
        relatorio = f"""
# RELATÓRIO DE TRÂNSITOS - O VERBO EM MOVIMENTO
## Período: {data_atual.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}

---

## I. CICLOS PLANETÁRIOS ATUAIS

### Saturno - O Mestre da Estrutura
**Idade Atual**: {idade:.1f} anos
**Fase do Ciclo**: {fase_saturno['fase']}
**Posição no Ciclo**: {fase_saturno['posicao_exata']:.1f} anos

**Significado**: {fase_saturno['detalhes']['significado']}
**Desafio Principal**: {fase_saturno['detalhes'].get('desafio', 'Integração das lições')}
**Oportunidade**: {fase_saturno['detalhes'].get('oportunidade', 'Crescimento através da disciplina')}
**Ritual Recomendado**: {fase_saturno['detalhes']['ritual']}

### Júpiter - O Benfeitor Expansivo
**Retornos Completos**: {fase_jupiter['retornos_completos']}
**Posição Atual**: {fase_jupiter['posicao_atual']:.1f} anos no ciclo
**Fase Atual**: {fase_jupiter['fase_atual']['nome']}

**Significado**: {fase_jupiter['fase_atual']['significado']}
**Ação Recomendada**: {fase_jupiter['fase_atual']['acao']}

---

## II. TRÂNSITOS PRINCIPAIS DO PERÍODO

"""
        
        for transito in analise_periodo['transitos_principais']:
            relatorio += f"""
### {transito['planeta']} {transito['aspecto']} {transito['planeta_natal']}
**Data Exata**: {transito['data_exata'].strftime('%d/%m/%Y')}

**Interpretação**: {transito['interpretacao']}

"""
            if 'oportunidades' in transito:
                relatorio += "**Oportunidades**:\n"
                for op in transito['oportunidades']:
                    relatorio += f"- {op}\n"
            
            if 'desafios' in transito:
                relatorio += "**Desafios**:\n"
                for desafio in transito['desafios']:
                    relatorio += f"- {desafio}\n"
            
            relatorio += "**Rituais Específicos**:\n"
            for ritual in transito['rituais']:
                relatorio += f"- {ritual}\n"
            relatorio += "\n"
        
        relatorio += """
---

## III. JANELAS TEMPORAIS ESPECIAIS

"""
        
        for janela in analise_periodo['janelas_temporais']:
            relatorio += f"""
### {janela.nome}
**Período**: {janela.periodo_inicio.strftime('%d/%m/%Y')} a {janela.periodo_fim.strftime('%d/%m/%Y')}
**Intensidade**: {janela.intensidade_geral}
**Planetas Envolvidos**: {', '.join(janela.planetas_envolvidos)}

**Temas Principais**: {', '.join(janela.temas_principais)}

**Rituais Recomendados**:
"""
            for ritual in janela.rituais_recomendados:
                relatorio += f"- {ritual}\n"
            relatorio += "\n"
        
        relatorio += """
---

## IV. PROTOCOLO RITUAL DO PERÍODO

### Práticas Diárias
"""
        for ritual in analise_periodo['rituais_periodo']['rituais_diarios']:
            relatorio += f"- {ritual}\n"
        
        relatorio += "\n### Práticas Semanais\n"
        for ritual in analise_periodo['rituais_periodo']['rituais_semanais']:
            relatorio += f"- {ritual}\n"
        
        relatorio += "\n### Rituais Especiais\n"
        for ritual in analise_periodo['rituais_periodo']['rituais_especiais']:
            relatorio += f"""
**{ritual['data'].strftime('%d/%m/%Y')}** - {ritual['nome']}
{ritual['descricao']}
"""
        
        relatorio += """
---

## V. TEMAS DOMINANTES

"""
        
        for tema in analise_periodo['temas_dominantes']:
            relatorio += f"""
### {tema['tema']}
**Planeta Regente**: {tema['planeta_regente']} (Sefira: {tema['sefira']})

**Manifestação**: {tema['manifestacao']}
**Desafio**: {tema['desafio']}
**Ritual Chave**: {tema['ritual_chave']}

"""
        
        relatorio += """
---

## CONCLUSÃO - O TEMPO SAGRADO

Este período representa uma janela única em sua jornada evolutiva. Os trânsitos não são eventos externos que acontecem "para você", mas sim ativações internas que emergem "através de você". Cada aspecto, cada janela temporal, cada ritual recomendado é uma oportunidade de alinhar sua consciência com o fluxo cósmico.

Use este mapa temporal como um navegador usa as correntes do oceano - não para ser levado por elas, mas para navegar conscientemente em direção ao seu destino espiritual.

O Verbo se move através do tempo, e você é o instrumento através do qual Ele se manifesta.

---
*Relatório gerado pelo Sistema de Análise de Trânsitos*
*Kabbalah das Águas Primordiais - SCII 5.0*
"""
        
        return relatorio

# ============================================================================
# EXEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Dados de exemplo
    dados_exemplo = {
        'nome': 'André de Oliveira Rodrigues',
        'data_nascimento': datetime.datetime(1985, 3, 15),
        'planetas_natais': {
            'Sol': 'Peixes',
            'Lua': 'Gêmeos',
            'Ascendente': 'Capricórnio'
        }
    }
    
    # Criar analisador e gerar relatório
    analisador = AnalisadorTransitos()
    relatorio = analisador.gerar_relatorio_transitos(dados_exemplo, 90)
    
    # Salvar relatório
    with open("/home/andre/Kabbalah-das-Aguas-Primordiais/relatorio_transitos_exemplo.md", "w", encoding="utf-8") as f:
        f.write(relatorio)
    
    print("Módulo de Análise de Trânsitos criado com sucesso!")
    print("Relatório de exemplo salvo em: relatorio_transitos_exemplo.md")