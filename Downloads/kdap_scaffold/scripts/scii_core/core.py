"""SCII Core — Kabbalah das Águas Primordiais
MVP: análise mínima de um termo em estrutura SCII.

Este módulo é deliberadamente simples. Ele define:
- Um schema estável (dataclass) para retorno
- Uma função `analisar_termo` que tokeniza o input e soma valores

TODOs (Fase 1):
- Transliteração pt-BR → Hebraico (configurável)
- Gematria adequada (e variações)
- Caminhos, Arquétipos e Tikun mapeados por letra
"""
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import unicodedata
import json

# --- Schema ---
@dataclass
class SchemaSCII:
    termo: str
    tokens: List[Dict[str, Any]]
    valor_total: int
    caminhos: List[str]
    arquetipos: List[str]
    tikun: List[str]

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)

# --- Config protótipo ---
# Proto-gematria simples (A=1..Z=26), só para MVP rodar.
# Substituir por tabela oficial na sequência da Fase 1.
PROTO_VALORES = {chr(c): i for i, c in enumerate(range(ord('A'), ord('Z')+1), start=1)}

def normalizar_str(s: str) -> str:
    """Remove acentos e normaliza para ASCII básico para o protótipo."""
    nfkd = unicodedata.normalize('NFKD', s)
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])

def analisar_termo(termo: str) -> SchemaSCII:
    if not isinstance(termo, str) or not termo.strip():
        raise ValueError("`termo` deve ser uma string não vazia.")

    bruto = termo.strip()
    base = normalizar_str(bruto).upper()

    tokens = []
    soma = 0
    for ch in base:
        if ch.isalpha():
            val = PROTO_VALORES.get(ch, 0)
            soma += val
            tokens.append({
                "char": ch,
                "valor": val,
                "letra": None,          # TODO: mapear para letra hebraica
                "caminho": None,        # TODO
                "arquétipo": None,      # TODO
                "tikun": None           # TODO
            })

    schema = SchemaSCII(
        termo=bruto,
        tokens=tokens,
        valor_total=soma,
        caminhos=[],     # TODO: inferir por letra
        arquetipos=[],   # TODO
        tikun=[]         # TODO
    )
    return schema
