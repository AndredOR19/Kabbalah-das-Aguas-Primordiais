"""
Módulo de Gematria e Correspondências Hebraicas.

Este módulo oferece uma classe `GematriaCalculator` capaz de converter um nome
português para a estrutura cabalística hebraica: transliteração, cálculo de
gematria, redução numerológica, determinação de Sefirá, letra dominante e
análise vibracional dos elementos e planetas presentes. É a porta de entrada
para o processamento do SCII.
"""

import re
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum

@dataclass
class HebrewLetter:
    """Representa uma letra hebraica com suas correspondências básicas."""
    name: str
    hebrew: str
    value: int
    meaning: str
    sefira: str
    planet: str
    element: str
    body_part: str
    sound: str
    color: str
    ritual_function: str

class Sefira(Enum):
    """Enumeração das 10 Sefirot com seus atributos essenciais."""
    KETHER = (1, "Kether", "Coroa", "Divindade")
    CHOKMAH = (2, "Chokmah", "Sabedoria", "Pai Superno")
    BINAH = (3, "Binah", "Entendimento", "Mãe Superna")
    CHESED = (4, "Chesed", "Misericórdia", "Água")
    GEBURAH = (5, "Geburah", "Severidade", "Fogo")
    TIFERET = (6, "Tiferet", "Beleza", "Ar")
    NETZACH = (7, "Netzach", "Vitória", "Vênus")
    HOD = (8, "Hod", "Glória", "Mercúrio")
    YESOD = (9, "Yesod", "Fundamento", "Lua")
    MALKUTH = (10, "Malkuth", "Reino", "Terra")

class GematriaCalculator:
    """
    Classe principal para cálculos gemátricos e correspondências.

    Usa um mapeamento fonético simples para transliterar nomes em letras
    hebraicas e calcula a gematria total, redução numerológica, sefirá
    correspondente e letra dominante. Também agrega informações
    vibracionais baseadas em elementos e planetas.
    """

    def __init__(self) -> None:
        self.hebrew_letters = self._load_hebrew_letters()
        self.phonetic_map = self._create_phonetic_map()

    def _load_hebrew_letters(self) -> Dict[str, HebrewLetter]:
        """Carrega a definição das 22 letras hebraicas."""
        letters_data: Dict[str, HebrewLetter] = {
            "Aleph": HebrewLetter("Aleph", "א", 1, "Boi, Ar", "Kether", "Ar", "Ar", "Pulmões", "A", "Branco",
                                  "União dos opostos"),
            "Bet": HebrewLetter("Bet", "ב", 2, "Casa", "Chokmah", "Mercúrio", "Ar", "Boca", "B", "Amarelo",
                                "Construção, comunicação"),
            "Gimel": HebrewLetter("Gimel", "ג", 3, "Camelo", "Luna", "Lua", "Água", "Estômago", "G", "Azul",
                                  "Movimento, nutrição"),
            "Dalet": HebrewLetter("Dalet", "ד", 4, "Porta", "Vênus", "Vênus", "Terra", "Seios", "D", "Verde",
                                  "Receptividade, amor"),
            "Heh": HebrewLetter("Heh", "ה", 5, "Janela", "Áries", "Marte", "Fogo", "Útero", "H", "Vermelho",
                                "Visão, revelação"),
            "Vav": HebrewLetter("Vav", "ו", 6, "Prego", "Touro", "Taurus", "Terra", "Coração", "V", "Laranja",
                                "Conexão, fixação"),
            "Zain": HebrewLetter("Zain", "ז", 7, "Espada", "Gêmeos", "Gêmeos", "Ar", "Braços", "Z", "Violeta",
                                 "Discriminação"),
            "Cheth": HebrewLetter("Cheth", "ח", 8, "Cerca", "Câncer", "Câncer", "Água", "Fígado", "Ch", "Marrom",
                                  "Proteção, limites"),
            "Teth": HebrewLetter("Teth", "ט", 9, "Serpente", "Leão", "Sol", "Fogo", "Intestinos", "T", "Dourado",
                                 "Força interior"),
            "Yod": HebrewLetter("Yod", "י", 10, "Mão", "Virgem", "Virgem", "Terra", "Mãos", "Y", "Verde-amarelo",
                                "Manifestação"),
            "Kaph": HebrewLetter("Kaph", "כ", 20, "Palma", "Júpiter", "Júpiter", "Fogo", "Fígado", "K", "Azul-royal",
                                 "Expansão"),
            "Lamed": HebrewLetter("Lamed", "ל", 30, "Aguilhão", "Libra", "Vênus", "Ar", "Rins", "L", "Rosa",
                                  "Ensino, equilíbrio"),
            "Mem": HebrewLetter("Mem", "מ", 40, "Água", "Águas", "Água", "Água", "Sangue", "M", "Azul-mar",
                                "Fluidez, morte/renascimento"),
            "Nun": HebrewLetter("Nun", "נ", 50, "Peixe", "Escorpião", "Marte", "Água",
                                "Órgãos reprodutivos", "N", "Azul-escuro", "Transformação"),
            "Samech": HebrewLetter("Samech", "ס", 60, "Suporte", "Sagitário", "Júpiter", "Fogo", "Quadris", "S",
                                   "Azul-claro", "Sustentação"),
            "Ayin": HebrewLetter("Ayin", "ע", 70, "Olho", "Capricórnio", "Saturno", "Terra", "Joelhos", "O", "Índigo",
                                 "Percepção profunda"),
            "Pei": HebrewLetter("Pei", "פ", 80, "Boca", "Marte", "Marte", "Fogo", "Língua", "P", "Escarlate",
                                "Comunicação do poder"),
            "Tzade": HebrewLetter("Tzade", "צ", 90, "Anzol", "Aquário", "Urano", "Ar", "Tornozelos", "Tz",
                                  "Violeta", "Pesca, busca espiritual"),
            "Qoph": HebrewLetter("Qoph", "ק", 100, "Nuca", "Peixes", "Netuno", "Água", "Pés", "Q", "Carmesim",
                                 "Ilusão/Iluminação"),
            "Resh": HebrewLetter("Resh", "ר", 200, "Cabeça", "Sol", "Sol", "Fogo", "Cabeça", "R", "Laranja-dourado",
                                 "Liderança, princípio"),
            "Shin": HebrewLetter("Shin", "ש", 300, "Dente", "Fogo", "Fogo", "Fogo", "Sistema nervoso", "Sh",
                                 "Vermelho-fogo", "Transformação espiritual"),
            "Tav": HebrewLetter("Tav", "ת", 400, "Cruz", "Saturno", "Saturno", "Terra", "Esqueleto", "T", "Preto",
                                "Cristalização, forma final"),
        }
        return letters_data

    def _create_phonetic_map(self) -> Dict[str, str]:
        """Cria um mapeamento fonético simples de caracteres latinos para letras hebraicas."""
        return {
            'A': 'Aleph', 'B': 'Bet', 'C': 'Kaph', 'D': 'Dalet',
            'E': 'Heh', 'F': 'Pei', 'G': 'Gimel', 'H': 'Heh',
            'I': 'Yod', 'J': 'Yod', 'K': 'Kaph', 'L': 'Lamed',
            'M': 'Mem', 'N': 'Nun', 'O': 'Ayin', 'P': 'Pei',
            'Q': 'Qoph', 'R': 'Resh', 'S': 'Samech', 'T': 'Teth',
            'U': 'Vav', 'V': 'Vav', 'W': 'Vav', 'X': 'Samech',
            'Y': 'Yod', 'Z': 'Zain'
        }

    def nome_para_hebraico(self, nome: str) -> Dict:
        """
        Converte um nome português para dados cabalísticos completos.

        Args:
            nome (str): Nome completo da pessoa.

        Returns:
            Dict: informações gemátricas e vibracionais.
        """
        # Normaliza e remove caracteres não alfabéticos
        nome_limpo = re.sub(r'[^A-Za-zÀ-ÿ]', '', nome.upper())
        nome_limpo = self._normalizar_acentos(nome_limpo)

        letras_hebraicas: List[str] = []
        transliteracao: List[str] = []
        valor_total = 0
        correspondencias: List[Dict] = []

        for char in nome_limpo:
            if char in self.phonetic_map:
                letra_nome = self.phonetic_map[char]
                letra_obj = self.hebrew_letters[letra_nome]
                letras_hebraicas.append(letra_obj.hebrew)
                transliteracao.append(letra_nome)
                valor_total += letra_obj.value
                correspondencias.append({
                    'letra': letra_nome,
                    'hebraico': letra_obj.hebrew,
                    'valor': letra_obj.value,
                    'significado': letra_obj.meaning,
                    'corpo': letra_obj.body_part,
                    'cor': letra_obj.color,
                })

        reducao = self._reduzir_numero(valor_total)
        sefira = self._determinar_sefira(reducao)
        letra_dominante = self._encontrar_letra_dominante(transliteracao) if transliteracao else None

        return {
            'nome_original': nome,
            'nome_limpo': nome_limpo,
            'transliteracao_hebraica': ' '.join(letras_hebraicas),
            'letras_nomes': transliteracao,
            'gematria_total': valor_total,
            'reducao_numerologica': reducao,
            'sefira_correspondente': sefira,
            'letra_dominante': letra_dominante,
            'correspondencias_detalhadas': correspondencias,
            'analise_vibracional': self._analisar_vibracao(correspondencias),
        }

    def _normalizar_acentos(self, texto: str) -> str:
        """Remove acentos e cedilhas de um texto latino."""
        acentos = {
            'À': 'A', 'Á': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A',
            'È': 'E', 'É': 'E', 'Ê': 'E', 'Ë': 'E',
            'Ì': 'I', 'Í': 'I', 'Î': 'I', 'Ï': 'I',
            'Ò': 'O', 'Ó': 'O', 'Ô': 'O', 'Õ': 'O', 'Ö': 'O',
            'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U',
            'Ç': 'C', 'Ñ': 'N'
        }
        for acento, normal in acentos.items():
            texto = texto.replace(acento, normal)
        return texto

    def _reduzir_numero(self, numero: int) -> int:
        """Reduz um número à sua raiz numerológica, preservando mestres (11, 22, 33)."""
        while numero > 9 and numero not in (11, 22, 33):
            numero = sum(int(d) for d in str(numero))
        return numero

    def _determinar_sefira(self, numero: int) -> Dict:
        """Mapeia a redução numerológica à Sefirá correspondente."""
        sefirot_map = {
            1: Sefira.KETHER,
            2: Sefira.CHOKMAH,
            3: Sefira.BINAH,
            4: Sefira.CHESED,
            5: Sefira.GEBURAH,
            6: Sefira.TIFERET,
            7: Sefira.NETZACH,
            8: Sefira.HOD,
            9: Sefira.YESOD,
            10: Sefira.MALKUTH,
            11: Sefira.KETHER,
            22: Sefira.CHOKMAH,
            33: Sefira.BINAH,
        }
        sefira = sefirot_map.get(numero, Sefira.KETHER)
        return {
            'numero': sefira.value[0],
            'nome': sefira.value[1],
            'significado': sefira.value[2],
            'arquetipo': sefira.value[3],
        }

    def _encontrar_letra_dominante(self, letras: List[str]) -> Dict:
        """Encontra a letra mais frequente na transliteração."""
        from collections import Counter
        contador = Counter(letras)
        letra_mais_comum, freq = contador.most_common(1)[0]
        letra_obj = self.hebrew_letters[letra_mais_comum]
        return {
            'letra': letra_mais_comum,
            'hebraico': letra_obj.hebrew,
            'frequencia': freq,
            'significado': letra_obj.meaning,
            'funcao_ritual': letra_obj.ritual_function,
            'parte_corpo': letra_obj.body_part,
            'planeta': letra_obj.planet,
            'cor': letra_obj.color,
        }

    def _analisar_vibracao(self, correspondencias: List[Dict]) -> Dict:
        """Analisa distribuição de elementos, planetas e partes do corpo."""
        elementos = {'Fogo': 0, 'Água': 0, 'Ar': 0, 'Terra': 0}
        planetas: Dict[str, int] = {}
        partes_corpo: List[str] = []

        for corr in correspondencias:
            letra_obj = self.hebrew_letters[corr['letra']]
            # Incrementa contagem de elementos
            if letra_obj.element in elementos:
                elementos[letra_obj.element] += 1
            # Incrementa contagem de planetas
            planeta = letra_obj.planet
            planetas[planeta] = planetas.get(planeta, 0) + 1
            # Coleta partes do corpo
            partes_corpo.append(letra_obj.body_part)

        elemento_dominante = max(elementos, key=elementos.get) if elementos else None
        planeta_dominante = max(planetas, key=planetas.get) if planetas else None

        return {
            'elemento_dominante': elemento_dominante,
            'distribuicao_elementos': elementos,
            'planeta_dominante': planeta_dominante,
            'distribuicao_planetas': planetas,
            'partes_corpo_influenciadas': list(set(partes_corpo)),
        }