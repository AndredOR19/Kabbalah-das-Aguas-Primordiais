# -*- coding: utf-8 -*-

"""
Processador de Apostila Astrológica Cabalística
Sistema para processar materiais de referência e criar apostila integrada

Este módulo analisa os materiais disponíveis e cria uma apostila única que integra:
- Astrologia tradicional (fundamentos técnicos)
- Cabala operativa (correspondências e práticas)
- Sistema SCII (integração com Kabbalah das Águas Primordiais)
"""

import os
import json
import datetime
from typing import Dict, List, Optional
import subprocess

class ProcessadorApostila:
    """Classe principal para processar materiais e criar apostila integrada"""
    
    def __init__(self, diretorio_base: str = "/home/andre/Kabbalah-das-Aguas-Primordiais/documentos/materiais-referencia"):
        self.diretorio_base = diretorio_base
        self.diretorio_processados = os.path.join(diretorio_base, "materiais-processados")
        
        # Materiais prioritários identificados
        self.materiais_prioritarios = {
            "astrologia_basica": [
                "Astrologia Basica - NANS.pdf",
                "Marion D. March e Joan McEvers_Curso Básico de Astrologia - Vol. 1.pdf",
                "Marion D. March e Joan McEvers_Curso Básico de Astrologia - Vol. 2.pdf",
                "Marion D. March e Joan McEvers_Curso Basico de Astrologia - Vol. 3.pdf",
                "Ciça Bueno e Márcia Mattos_Curso de Astrologia.pdf"
            ],
            "astrologia_avancada": [
                "Alexandre Volguine_A Técnica das Revoluções Solares.pdf",
                "Alexandre Volguine_Astrologia Lunar.pdf",
                "Howard Sasportas_As Doze Casas.pdf",
                "Dane Rudhyar_A Prática da Astrologia.pdf"
            ],
            "astrologia_esoterica": [
                "Master E K_Spiritual Astrology.pdf",
                "Papus_Iniciação astrológica.pdf",
                "Maria Eugênia de Castro_Astrologia e as Dimensões do ser.pdf"
            ],
            "cabala_astrologica": [
                "Rav Philip S. Berg_Astrologia Cabalística.pdf",
                "Rav Berg_Astrologia Cabalística.pdf"
            ],
            "cabala_pratica": [
                "Dion Fortune_ A Cabala Mística.pdf",
                "MacGregor Mathers_A Cabala Revelada.pdf",
                "Franz Bardon_A Chave para a Verdadeira Cabala.pdf",
                "Ali Al Khan S I Manual Magico de Kabbala Pratica.pdf"
            ],
            "correspondencias": [
                "Glossário da Cabala.pdf",
                "Luiz Trevizani_Numerologia Cabalística.pdf"
            ]
        }
    
    def criar_estrutura_apostila(self) -> Dict:
        """Cria a estrutura base da apostila integrada"""
        
        estrutura = {
            "titulo": "APOSTILA DE ASTROLOGIA CABALÍSTICA",
            "subtitulo": "Sistema Integrado Kabbalah das Águas Primordiais",
            "versao": "1.0",
            "data_criacao": datetime.datetime.now().isoformat(),
            
            "partes": {
                "I": {
                    "titulo": "FUNDAMENTOS ASTROLÓGICOS",
                    "descricao": "Base técnica sólida da astrologia tradicional",
                    "capitulos": {
                        1: "Introdução à Astrologia - História e Princípios",
                        2: "Os Planetas - Arquétipos Cósmicos",
                        3: "Os Signos - Qualidades e Elementos", 
                        4: "As Casas - Campos de Experiência",
                        5: "Os Aspectos - Relações Dinâmicas",
                        6: "Interpretação Básica do Mapa Natal"
                    }
                },
                
                "II": {
                    "titulo": "CORRESPONDÊNCIAS CABALÍSTICAS",
                    "descricao": "Integração entre Astrologia e Cabala",
                    "capitulos": {
                        7: "A Árvore da Vida e os Planetas",
                        8: "As 22 Letras Hebraicas e o Zodíaco",
                        9: "Sefirot e Correspondências Planetárias",
                        10: "Caminhos da Árvore e Casas Astrológicas",
                        11: "Aspectos como Polaridades do Verbo",
                        12: "O Corpo Somático do Verbo"
                    }
                },
                
                "III": {
                    "titulo": "ANÁLISE DINÂMICA - TRÂNSITOS E CICLOS",
                    "descricao": "O Verbo em movimento através do tempo",
                    "capitulos": {
                        13: "Ciclos Planetários e Desenvolvimento Espiritual",
                        14: "Trânsitos como Ativações Cabalísticas",
                        15: "Retornos Planetários e Iniciações",
                        16: "Progressões e Direções Espirituais",
                        17: "Timing Sagrado e Astrologia Eletiva"
                    }
                },
                
                "IV": {
                    "titulo": "SISTEMA OPERATIVO SCII",
                    "descricao": "Aplicação prática do conhecimento",
                    "capitulos": {
                        18: "Análise Completa do Mapa Cabalístico",
                        19: "Protocolo Ritual Personalizado",
                        20: "Práticas de Ativação Planetária",
                        21: "Meditações e Exercícios Somáticos",
                        22: "Integração com o Sistema SCII"
                    }
                },
                
                "V": {
                    "titulo": "CASOS PRÁTICOS E EXEMPLOS",
                    "descricao": "Aplicação real do sistema",
                    "capitulos": {
                        23: "Análise de Mapas Exemplares",
                        24: "Estudos de Caso de Trânsitos",
                        25: "Protocolos Rituais Específicos",
                        26: "Desenvolvimento de Operadores SCII"
                    }
                }
            },
            
            "apendices": {
                "A": "Tabelas de Correspondências Completas",
                "B": "Efemérides e Cálculos",
                "C": "Glossário Astrológico-Cabalístico",
                "D": "Bibliografia e Referências",
                "E": "Exercícios Práticos"
            }
        }
        
        return estrutura
    
    def gerar_capitulo_introducao(self) -> str:
        """Gera o capítulo de introdução da apostila"""
        
        capitulo = """
# CAPÍTULO 1: INTRODUÇÃO À ASTROLOGIA CABALÍSTICA
## História, Princípios e Visão Integrada

---

### 🌟 A SÍNTESE DAS TRADIÇÕES

*"Como em cima, assim embaixo; como embaixo, assim em cima, para realizar os milagres da única coisa."*

Esta apostila representa uma síntese única entre duas das mais antigas e profundas tradições de conhecimento da humanidade: a **Astrologia** e a **Cabala**. Não se trata de uma mera justaposição de sistemas, mas de uma **integração orgânica** que revela as correspondências ocultas entre a geometria cósmica e a estrutura da consciência humana.

### 🔮 O QUE É ASTROLOGIA CABALÍSTICA?

A Astrologia Cabalística é um sistema que reconhece que:

1. **Os planetas são manifestações das Sefirot** - as emanações divinas da Árvore da Vida
2. **Os signos correspondem às 22 Letras Hebraicas** - os arquétipos fundamentais da criação
3. **As casas representam os Caminhos da Árvore** - os campos de experiência da consciência
4. **Os aspectos são polaridades do Verbo** - as tensões criativas que geram evolução
5. **Os trânsitos são ativações somáticas** - momentos de despertar espiritual

### 📚 FUNDAMENTOS HISTÓRICOS

#### Origens Antigas
A conexão entre Astrologia e Cabala remonta aos primórdios de ambas as tradições:

- **Babilônia (2000 a.C.)**: Primeiras correspondências entre planetas e divindades
- **Egito Antigo**: Integração entre astronomia e cosmologia sagrada  
- **Grécia Clássica**: Sistematização astrológica com Ptolomeu
- **Tradição Judaica**: Desenvolvimento da Cabala e suas correspondências
- **Renascimento**: Síntese hermética com Pico della Mirandola e outros

#### Desenvolvimento Moderno
- **Século XIX**: Ressurgimento do interesse esotérico
- **Golden Dawn**: Sistematização das correspondências
- **Século XX**: Astrologia psicológica e abordagens espirituais
- **Século XXI**: Integração com sistemas contemporâneos

### 🎯 OBJETIVOS DESTA APOSTILA

Esta apostila foi criada para:

1. **Ensinar os fundamentos** da astrologia tradicional com rigor técnico
2. **Revelar as correspondências** cabalísticas de cada elemento astrológico
3. **Integrar com o Sistema SCII** da Kabbalah das Águas Primordiais
4. **Fornecer práticas operativas** para desenvolvimento espiritual
5. **Formar operadores qualificados** do sistema integrado

### 🔧 METODOLOGIA DE ESTUDO

#### Estrutura Progressiva
- **Parte I**: Base técnica sólida (astrologia tradicional)
- **Parte II**: Correspondências cabalísticas (integração)
- **Parte III**: Análise dinâmica (trânsitos e ciclos)
- **Parte IV**: Sistema operativo (práticas e rituais)
- **Parte V**: Casos práticos (aplicação real)

#### Abordagem Integrada
Cada conceito astrológico será apresentado em três níveis:
1. **Técnico**: Definição precisa e características
2. **Cabalístico**: Correspondências e significados esotéricos
3. **Operativo**: Aplicações práticas e rituais

### 🌊 A KABBALAH DAS ÁGUAS PRIMORDIAIS

Esta apostila integra-se ao sistema maior da **Kabbalah das Águas Primordiais**, que reconhece:

- **O Corpo Somático do Verbo**: A manifestação física das energias espirituais
- **O Sistema SCII**: Correspondência Integrada e Inteligente
- **As Águas Primordiais**: O estado original de potencialidade pura
- **O Verbo Encarnado**: A palavra divina manifestada na matéria

### 🎓 PARA QUEM É ESTA APOSTILA?

#### Iniciantes
- Base sólida em astrologia tradicional
- Introdução gradual às correspondências cabalísticas
- Exercícios práticos para fixação

#### Intermediários
- Aprofundamento das correspondências
- Técnicas avançadas de interpretação
- Integração com práticas espirituais

#### Avançados
- Sistema completo de análise cabalística
- Formação como operador SCII
- Desenvolvimento de protocolos personalizados

### 🔮 PRINCÍPIOS FUNDAMENTAIS

#### 1. Correspondência Universal
*"Tudo que está em cima corresponde ao que está embaixo"*
- Cada elemento astrológico tem sua correspondência cabalística
- O macrocosmo se reflete no microcosmo
- A geometria cósmica espelha a estrutura da consciência

#### 2. Vibração e Ressonância
*"Nada está parado, tudo vibra"*
- Planetas são centros de vibração específica
- Signos são qualidades vibratórias
- Aspectos são relações harmônicas ou dissonantes

#### 3. Polaridade e Complementaridade
*"Tudo é duplo, tudo tem dois polos"*
- Cada planeta tem sua polaridade oculta
- Signos opostos se complementam
- Aspectos tensos geram crescimento

#### 4. Ritmo e Ciclos
*"Tudo flui, tudo tem suas marés"*
- Trânsitos seguem ritmos cósmicos
- Ciclos planetários marcam fases evolutivas
- Timing é fundamental para a manifestação

#### 5. Causa e Efeito
*"Toda causa tem seu efeito, todo efeito tem sua causa"*
- Configurações natais indicam potenciais
- Trânsitos ativam possibilidades
- Livre arbítrio opera dentro das leis cósmicas

#### 6. Gênero e Polaridade
*"O gênero está em tudo, tudo tem seus princípios masculino e feminino"*
- Planetas expressam polaridades ativas ou receptivas
- Signos alternam entre masculinos e femininos
- Equilíbrio entre polaridades gera harmonia

### 🚀 COMO USAR ESTA APOSTILA

#### Estudo Sequencial
1. **Leia cada capítulo** na ordem apresentada
2. **Pratique os exercícios** propostos
3. **Consulte as tabelas** de correspondências
4. **Aplique em mapas reais** (seu próprio primeiro)
5. **Desenvolva protocolos** personalizados

#### Consulta Rápida
- **Índice detalhado** para localizar temas específicos
- **Tabelas de correspondências** para consulta imediata
- **Glossário** para esclarecimento de termos
- **Bibliografia** para aprofundamento

#### Prática Operativa
- **Exercícios graduais** em cada capítulo
- **Protocolos rituais** específicos
- **Casos práticos** para análise
- **Sistema de avaliação** do progresso

### 🎯 RESULTADOS ESPERADOS

Ao completar esta apostila, você será capaz de:

1. **Interpretar mapas astrológicos** com profundidade cabalística
2. **Identificar correspondências** entre planetas, signos e Sefirot
3. **Analisar trânsitos** como ativações espirituais
4. **Criar protocolos rituais** personalizados
5. **Operar o Sistema SCII** com competência
6. **Ensinar e transmitir** o conhecimento integrado

### 🌟 CONVITE À JORNADA

*"Conhece-te a ti mesmo e conhecerás o universo e os deuses."*

Esta apostila é mais que um manual técnico - é um **mapa da alma** que revela como a geometria cósmica se manifesta em sua jornada pessoal. Cada planeta em seu mapa é uma faceta de sua divindade interior, cada aspecto uma lição a ser integrada, cada trânsito uma oportunidade de crescimento.

Prepare-se para uma jornada que transformará não apenas sua compreensão da astrologia, mas sua percepção de si mesmo como ser cósmico encarnado na matéria para realizar a Grande Obra.

**O Verbo se fez carne em você. Agora, faça a carne se tornar Verbo.**

---

*Próximo Capítulo: Os Planetas - Arquétipos Cósmicos*

"""
        
        return capitulo
    
    def gerar_capitulo_planetas(self) -> str:
        """Gera o capítulo sobre planetas e suas correspondências"""
        
        capitulo = """
# CAPÍTULO 2: OS PLANETAS - ARQUÉTIPOS CÓSMICOS
## Correspondências Cabalísticas e Manifestações Somáticas

---

### 🌟 OS PLANETAS COMO SEFIROT ENCARNADAS

Na Astrologia Cabalística, os planetas não são meramente corpos celestes distantes, mas **emanações vivas das Sefirot** - os aspectos fundamentais da divindade que se manifestam através da geometria cósmica. Cada planeta é um **centro de consciência** que vibra em uma frequência específica, ativando correspondências precisas no Corpo Somático do Verbo.

### ☉ SOL - TIFERET (תפארת)
*"O Centro Radiante do Ser"*

#### Correspondências Fundamentais
- **Sefira**: Tiferet (Beleza/Harmonia)
- **Letra Hebraica**: Resh (ר) - "A Cabeça Cósmica"
- **Elemento**: Fogo Central
- **Qualidade**: Fixo/Radiante
- **Polaridade**: Masculina/Ativa

#### Manifestação Somática
- **Órgãos**: Coração, Plexo Solar, Coluna Vertebral
- **Sistema**: Circulatório, Vitalidade Geral
- **Chakra**: Manipura (Plexo Solar) e Anahata (Coração)
- **Glândula**: Timo

#### Função Operativa
O Sol representa o **Centro da Vontade** - o núcleo radiante da personalidade que irradia sua essência única. Em Tiferet, ele harmoniza todas as outras energias planetárias, sendo o ponto de equilíbrio entre Misericórdia (Chesed) e Severidade (Gevurah).

#### Rituais de Ativação Solar
- **Manhã**: Saudação ao Sol com respiração dourada
- **Meio-dia**: Meditação no Plexo Solar
- **Domingo**: Ritual completo de irradiação solar
- **Mantra**: "Adonai" (אדני) - "Meu Senhor"

### ☽ LUA - YESOD (יסוד)
*"O Espelho da Alma"*

#### Correspondências Fundamentais
- **Sefira**: Yesod (Fundamento)
- **Letra Hebraica**: Gimel (ג) - "O Camelo que Atravessa"
- **Elemento**: Água Receptiva
- **Qualidade**: Cardinal/Mutável
- **Polaridade**: Feminina/Receptiva

#### Manifestação Somática
- **Órgãos**: Estômago, Útero, Sistema Linfático
- **Sistema**: Reprodutivo, Digestivo, Emocional
- **Chakra**: Svadhisthana (Sacral)
- **Glândula**: Ovários/Testículos

#### Função Operativa
A Lua é o **Espelho da Alma** que reflete e amplifica todas as influências recebidas. Em Yesod, ela serve como fundamento etérico que conecta o mundo espiritual (Sefirot superiores) com a manifestação física (Malkuth).

#### Rituais de Ativação Lunar
- **Lua Nova**: Ritual de intenções e novos ciclos
- **Lua Cheia**: Ritual de manifestação e gratidão
- **Segunda-feira**: Meditação das marés emocionais
- **Mantra**: "Shaddai El Chai" (שדי אל חי) - "Deus Todo-Poderoso Vivente"

### ☿ MERCÚRIO - HOD (הוד)
*"A Ponte do Verbo"*

#### Correspondências Fundamentais
- **Sefira**: Hod (Esplendor/Glória)
- **Letra Hebraica**: Bet (ב) - "A Casa do Verbo"
- **Elemento**: Ar Mental
- **Qualidade**: Mutável/Adaptável
- **Polaridade**: Neutra/Andrógina

#### Manifestação Somática
- **Órgãos**: Pulmões, Sistema Nervoso, Mãos
- **Sistema**: Respiratório, Nervoso, Comunicativo
- **Chakra**: Vishuddha (Garganta)
- **Glândula**: Tireoide

#### Função Operativa
Mercúrio é a **Ponte do Verbo** que traduz pensamentos em palavras e conecta diferentes níveis de consciência. Em Hod, ele representa a inteligência analítica que organiza e comunica o conhecimento.

#### Rituais de Ativação Mercurial
- **Quarta-feira**: Recitação de mantras e estudos
- **Respiração**: Pranayama consciente
- **Escrita**: Journaling e correspondências sagradas
- **Mantra**: "Elohim Tzabaoth" (אלהים צבאות) - "Deus dos Exércitos"

### ♀ VÊNUS - NETZACH (נצח)
*"A Harmonia Magnética"*

#### Correspondências Fundamentais
- **Sefira**: Netzach (Vitória/Eternidade)
- **Letra Hebraica**: Dalet (ד) - "A Porta da Beleza"
- **Elemento**: Terra/Ar (Touro/Libra)
- **Qualidade**: Fixo/Cardinal
- **Polaridade**: Feminina/Atrativa

#### Manifestação Somática
- **Órgãos**: Garganta, Rins, Órgãos Reprodutivos
- **Sistema**: Endócrino, Urinário, Estético
- **Chakra**: Anahata (Coração) e Svadhisthana (Sacral)
- **Glândula**: Paratireoide, Suprarrenais

#### Função Operativa
Vênus representa a **Harmonia Magnética** que atrai e harmoniza através da beleza e do amor. Em Netzach, ela é a força que vence através da atração e da persistência amorosa.

#### Rituais de Ativação Venusiana
- **Sexta-feira**: Oferendas florais e canto sagrado
- **Arte**: Criação e contemplação da beleza
- **Relacionamentos**: Práticas de amor consciente
- **Mantra**: "YHVH Tzabaoth" (יהוה צבאות) - "Senhor dos Exércitos"

### ♂ MARTE - GEVURAH (גבורה)
*"A Força de Vontade"*

#### Correspondências Fundamentais
- **Sefira**: Gevurah (Severidade/Força)
- **Letra Hebraica**: Peh (פ) - "A Boca que Fala"
- **Elemento**: Fogo Ativo
- **Qualidade**: Cardinal/Iniciador
- **Polaridade**: Masculina/Assertiva

#### Manifestação Somática
- **Órgãos**: Músculos, Sistema Circulatório, Cabeça
- **Sistema**: Muscular, Imunológico, Motor
- **Chakra**: Manipura (Plexo Solar) e Muladhara (Base)
- **Glândula**: Suprarrenais

#### Função Operativa
Marte é a **Força de Vontade** que corta através dos obstáculos e estabelece limites necessários. Em Gevurah, ele representa o aspecto severo mas justo da divindade que disciplina e purifica.

#### Rituais de Ativação Marciana
- **Terça-feira**: Exercícios marciais e jejum purificador
- **Disciplina**: Práticas de autocontrole
- **Proteção**: Rituais de estabelecimento de limites
- **Mantra**: "Elohim Gibor" (אלהים גבור) - "Deus Forte"

### ♃ JÚPITER - CHESED (חסד)
*"A Expansão Benevolente"*

#### Correspondências Fundamentais
- **Sefira**: Chesed (Misericórdia/Bondade)
- **Letra Hebraica**: Kaph (כ) - "A Palma Aberta"
- **Elemento**: Fogo Expansivo
- **Qualidade**: Mutável/Generoso
- **Polaridade**: Masculina/Benéfica

#### Manifestação Somática
- **Órgãos**: Fígado, Quadris, Coxas
- **Sistema**: Digestivo Superior, Metabólico
- **Chakra**: Manipura (Plexo Solar) expandido
- **Glândula**: Pâncreas

#### Função Operativa
Júpiter representa a **Expansão Benevolente** que cresce através da generosidade e sabedoria. Em Chesed, ele é a misericórdia divina que abençoa e expande sem limites.

#### Rituais de Ativação Jupiteriana
- **Quinta-feira**: Estudo sagrado e atos de generosidade
- **Abundância**: Práticas de gratidão e prosperidade
- **Ensino**: Compartilhamento de conhecimento
- **Mantra**: "El" (אל) - "Deus"

### ♄ SATURNO - BINAH (בינה)
*"A Estrutura Cristalizadora"*

#### Correspondências Fundamentais
- **Sefira**: Binah (Entendimento/Compreensão)
- **Letra Hebraica**: Tav (ת) - "O Selo Final"
- **Elemento**: Terra Estrutural
- **Qualidade**: Cardinal/Limitador
- **Polaridade**: Feminina/Receptiva

#### Manifestação Somática
- **Órgãos**: Ossos, Joelhos, Pele
- **Sistema**: Esquelético, Estrutural
- **Chakra**: Muladhara (Base)
- **Glândula**: Paratireoide

#### Função Operativa
Saturno é a **Estrutura Cristalizadora** que dá forma e limite às energias expansivas. Em Binah, ele representa o entendimento profundo que vem através da experiência e da disciplina.

#### Rituais de Ativação Saturnina
- **Sábado**: Meditação silenciosa e disciplina ascética
- **Estrutura**: Organização e planejamento
- **Tempo**: Práticas de paciência e persistência
- **Mantra**: "YHVH Elohim" (יהוה אלהים) - "Senhor Deus"

### ♅ URANO - KETER (כתר)
*"A Iluminação Súbita"*

#### Correspondências Fundamentais
- **Sefira**: Keter (Coroa)
- **Letra Hebraica**: Aleph (א) - "O Sopro Primordial"
- **Elemento**: Ar Elétrico
- **Qualidade**: Fixo/Revolucionário
- **Polaridade**: Transcendente

#### Manifestação Somática
- **Órgãos**: Sistema Nervoso Central, Coroa
- **Sistema**: Elétrico, Intuitivo
- **Chakra**: Sahasrara (Coroa)
- **Glândula**: Pineal

#### Função Operativa
Urano representa a **Iluminação Súbita** que quebra padrões e revela verdades superiores. Em Keter, ele é a coroa da consciência que conecta com o divino.

#### Rituais de Ativação Uraniana
- **Meditação**: Do vazio e respiração paradoxal
- **Inovação**: Práticas criativas e revolucionárias
- **Liberdade**: Quebra de padrões limitantes
- **Mantra**: "Eheieh" (אהיה) - "Eu Sou"

### ♆ NETUNO - CHOKMAH (חכמה)
*"A Sabedoria Intuitiva"*

#### Correspondências Fundamentais
- **Sefira**: Chokmah (Sabedoria)
- **Letra Hebraica**: Qoph (ק) - "O Olho da Agulha"
- **Elemento**: Água Cósmica
- **Qualidade**: Mutável/Dissolutivo
- **Polaridade**: Masculina/Inspiradora

#### Manifestação Somática
- **Órgãos**: Glândula Pineal, Sistema Endócrino
- **Sistema**: Psíquico, Intuitivo
- **Chakra**: Ajna (Terceiro Olho)
- **Glândula**: Pineal, Pituitária

#### Função Operativa
Netuno é a **Sabedoria Intuitiva** que dissolve as ilusões e revela a unidade subjacente. Em Chokmah, ele é a sabedoria primordial que precede o entendimento.

#### Rituais de Ativação Netuniana
- **Sonhos**: Trabalho com sonhos lúcidos
- **Contemplação**: Meditação oceânica
- **Compaixão**: Práticas de dissolução do ego
- **Mantra**: "Yah" (יה) - "Deus"

### ♇ PLUTÃO - GEVURAH OCULTA
*"A Morte e Renascimento"*

#### Correspondências Fundamentais
- **Sefira**: Gevurah Oculta (Aspecto Transformador)
- **Letra Hebraica**: Nun (נ) - "O Peixe que Nada"
- **Elemento**: Água/Fogo Alquímico
- **Qualidade**: Fixo/Transformador
- **Polaridade**: Regenerativa

#### Manifestação Somática
- **Órgãos**: Órgãos Reprodutivos, Intestinos
- **Sistema**: Eliminatório, Regenerativo
- **Chakra**: Svadhisthana (Sacral) profundo
- **Glândula**: Gônadas

#### Função Operativa
Plutão representa a **Morte e Renascimento** - o processo alquímico que transforma chumbo em ouro. Ele é o aspecto oculto de Gevurah que destrói para regenerar.

#### Rituais de Ativação Plutoniana
- **Transformação**: Jejum transformador e meditação da morte
- **Alquimia**: Práticas de transmutação interior
- **Regeneração**: Rituais de morte e renascimento
- **Mantra**: "Elohim Gibor" (אלהים גבור) - aspecto transformador

### 🔮 SÍNTESE PLANETÁRIA

#### Planetas Pessoais (Sol, Lua, Mercúrio, Vênus, Marte)
- Representam aspectos da **personalidade individual**
- Manifestam-se através do **ego consciente**
- Ciclos rápidos (dias a 2 anos)
- Influência **direta e imediata**

#### Planetas Sociais (Júpiter, Saturno)
- Representam a **integração social**
- Manifestam-se através de **papéis sociais**
- Ciclos médios (12 a 29 anos)
- Influência **estrutural e educativa**

#### Planetas Transpessoais (Urano, Netuno, Plutão)
- Representam **forças coletivas**
- Manifestam-se através de **transformações geracionais**
- Ciclos longos (84 a 248 anos)
- Influência **evolutiva e transcendente**

### 🎯 EXERCÍCIOS PRÁTICOS

#### 1. Identificação Planetária Pessoal
- Identifique seu planeta dominante no mapa natal
- Observe suas manifestações somáticas
- Pratique o ritual de ativação correspondente

#### 2. Meditação Planetária Semanal
- Segunda: Lua - Receptividade emocional
- Terça: Marte - Força de vontade
- Quarta: Mercúrio - Comunicação clara
- Quinta: Júpiter - Expansão benevolente
- Sexta: Vênus - Harmonia e beleza
- Sábado: Saturno - Disciplina e estrutura
- Domingo: Sol - Irradiação central

#### 3. Observação de Trânsitos
- Acompanhe os trânsitos planetários atuais
- Observe suas manifestações em sua vida
- Correlacione com as correspondências cabalísticas

---

*Próximo Capítulo: Os Signos - Qualidades e Elementos*

"""
        
        return capitulo
    
    def salvar_capitulo(self, nome_arquivo: str, conteudo: str):
        """Salva um capítulo processado"""
        
        caminho_arquivo = os.path.join(self.diretorio_processados, nome_arquivo)
        
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        return caminho_arquivo
    
    def gerar_apostila_completa(self) -> str:
        """Gera a apostila completa baseada nos materiais processados"""
        
        print("Iniciando geração da apostila completa...")
        
        # Criar estrutura
        estrutura = self.criar_estrutura_apostila()
        
        # Gerar capítulos principais
        cap1 = self.gerar_capitulo_introducao()
        cap2 = self.gerar_capitulo_planetas()
        
        # Salvar capítulos
        self.salvar_capitulo("capitulo_01_introducao.md", cap1)
        self.salvar_capitulo("capitulo_02_planetas.md", cap2)
        
        # Salvar estrutura
        estrutura_arquivo = os.path.join(self.diretorio_processados, "estrutura_apostila.json")
        with open(estrutura_arquivo, 'w', encoding='utf-8') as f:
            json.dump(estrutura, f, indent=2, ensure_ascii=False)
        
        # Gerar índice da apostila
        indice = self._gerar_indice_apostila(estrutura)
        self.salvar_capitulo("indice_apostila.md", indice)
        
        return "Apostila base gerada com sucesso!"
    
    def _gerar_indice_apostila(self, estrutura: Dict) -> str:
        """Gera o índice completo da apostila"""
        
        indice = f"""
# {estrutura['titulo']}
## {estrutura['subtitulo']}

**Versão**: {estrutura['versao']}
**Data**: {datetime.datetime.fromisoformat(estrutura['data_criacao']).strftime('%d/%m/%Y')}

---

## 📚 ÍNDICE COMPLETO

"""
        
        for parte_num, parte in estrutura['partes'].items():
            indice += f"""
### PARTE {parte_num}: {parte['titulo']}
*{parte['descricao']}*

"""
            for cap_num, cap_titulo in parte['capitulos'].items():
                indice += f"**Capítulo {cap_num}**: {cap_titulo}\n"
            indice += "\n"
        
        indice += """
---

## 📖 APÊNDICES

"""
        
        for ap_letra, ap_titulo in estrutura['apendices'].items():
            indice += f"**Apêndice {ap_letra}**: {ap_titulo}\n"
        
        indice += """
---

## 🎯 COMO USAR ESTA APOSTILA

### Para Iniciantes
1. Comece pela **Parte I** (Fundamentos Astrológicos)
2. Pratique os exercícios de cada capítulo
3. Consulte o **Apêndice C** (Glossário) quando necessário

### Para Intermediários
1. Foque na **Parte II** (Correspondências Cabalísticas)
2. Integre com conhecimento astrológico prévio
3. Desenvolva práticas da **Parte IV**

### Para Avançados
1. Estude todo o sistema integrado
2. Aplique em casos práticos (**Parte V**)
3. Desenvolva protocolos personalizados

---

## 🔮 OBJETIVOS DE APRENDIZAGEM

Ao completar esta apostila, você será capaz de:

- ✅ Interpretar mapas astrológicos com profundidade cabalística
- ✅ Identificar correspondências entre planetas e Sefirot
- ✅ Analisar trânsitos como ativações espirituais
- ✅ Criar protocolos rituais personalizados
- ✅ Operar o Sistema SCII com competência
- ✅ Ensinar e transmitir o conhecimento integrado

---

*"O conhecimento sem prática é estéril; a prática sem conhecimento é perigosa. A síntese de ambos é sabedoria."*

**Kabbalah das Águas Primordiais - SCII 5.0**
"""
        
        return indice

# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    processador = ProcessadorApostila()
    resultado = processador.gerar_apostila_completa()
    
    print(resultado)
    print("\nArquivos gerados:")
    print("- estrutura_apostila.json")
    print("- indice_apostila.md") 
    print("- capitulo_01_introducao.md")
    print("- capitulo_02_planetas.md")
    print("\nPróximos passos: Continuar gerando os demais capítulos baseados nos materiais de referência.")