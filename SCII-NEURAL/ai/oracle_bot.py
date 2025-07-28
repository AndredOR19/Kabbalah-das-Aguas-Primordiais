"""
Componente de Chatbot Oracular.

Define a classe `OracleBot` que integra o GematriaCalculator, astrologia e
diagnóstico para interagir com usuários de forma dialogal. Este módulo serve
como um exemplo de como encapsular contexto de conversa e gerar respostas
oraculares; a implementação real deve incluir tratamento de múltiplos turnos e
persistência de histórico.
"""

from typing import Dict
from ..core.diagnosis import diagnosticar_scii
from ..core.ritual_generator import gerar_rituais

class OracleBot:
    def __init__(self) -> None:
        self.conversation_context: Dict[str, Dict] = {}

    def process_user_input(self, message: str, user_data: Dict) -> Dict:
        """
        Processa o input do usuário através do SCII.

        Args:
            message (str): Mensagem textual do usuário.
            user_data (dict): Dados estruturados (nome, data_nascimento, sintomas).

        Returns:
            Dict: Conteúdo oracular com diagnóstico e rituais.
        """
        # Diagnostica a partir dos dados fornecidos
        resultado = diagnosticar_scii(user_data)
        letras = resultado.get('letras_desequilibradas', [])
        sefirot = resultado.get('sefirot_afetadas', [])
        # Gera rituais adicionais
        rituais = gerar_rituais(letras, sefirot)
        resultado['rituais'] = rituais
        # Incluir mensagem oracular simples
        resultado['mensagem_oracular'] = (
            "Que a sabedoria das letras te conduza. "
            "Siga os rituais e observe as transformações."
        )
        return resultado