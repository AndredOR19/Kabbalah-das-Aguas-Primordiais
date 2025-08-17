"""
CLI simples para consultas SCII.
Exemplos:
  python -m src.scii_cli --emocao "ansiedade"
  python src/scii_cli.py --emocao "unidade"
"""
from __future__ import annotations
import argparse
from scii_core import SCII

def main() -> int:
    parser = argparse.ArgumentParser(description="SCII CLI - consulta por emoção/sintoma")
    parser.add_argument("--emocao", "--sintoma", dest="emocao", required=True)
    args = parser.parse_args()
    scii = SCII()
    resultados = scii.diagnostico_por_emocao(args.emocao)
    if not resultados:
        print("Nenhuma correspondência encontrada.")
        return 1
    for r in resultados:
        print(f"- Letra: {r['letra']} | Órgão: {r.get('orgao') or '-'} | Arquétipo: {r.get('arquétipo') or '-'}")
        print(f"  Tratamento: {r['tratamento_sugerido']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())