"""
CLI simples para consultas SCII.
Exemplos:
  python -m src.scii_cli --emocao "ansiedade"
  python src/scii_cli.py --emocao "unidade" --json
  python src/scii_cli.py --emocao "ansiedade" --filtro-orgao "Respiratório"
  python src/scii_cli.py --emocao "ansiedade" --filtro-arquetipo "Tarot"
"""
from __future__ import annotations
import argparse
import json
import sys
from typing import List, Dict, Any
from scii_core import SCII

def aplica_filtros(resultados: List[Dict[str, Any]], filtro_orgao: str | None, filtro_arquetipo: str | None):
    def ok(r: Dict[str, Any]) -> bool:
        if filtro_orgao and not ((r.get("orgao") or "").lower().find(filtro_orgao.lower()) >= 0):
            return False
        if filtro_arquetipo and not ((r.get("arquétipo") or "").lower().find(filtro_arquetipo.lower()) >= 0):
            return False
        return True
    return [r for r in resultados if ok(r)]

def main() -> int:
    parser = argparse.ArgumentParser(description="SCII CLI - consulta por emoção/sintoma")
    parser.add_argument("--emocao", "--sintoma", dest="emocao", required=True, help="termo a buscar (ex: ansiedade)")
    parser.add_argument("--filtro-orgao", dest="filtro_orgao", help="filtra pelo nome do órgão (substring)")
    parser.add_argument("--filtro-arquetipo", dest="filtro_arquetipo", help="filtra pelo arquétipo (substring)")
    parser.add_argument("--json", action="store_true", help="saida em JSON")
    args = parser.parse_args()

    scii = SCII()
    resultados = scii.diagnostico_por_emocao(args.emocao)
    resultados = aplica_filtros(resultados, args.filtro_orgao, args.filtro_arquetipo)

    if not resultados:
        msg = "Nenhuma correspondência encontrada."
        if args.json:
            json.dump({"resultados": [], "mensagem": msg}, sys.stdout, ensure_ascii=False)
            print()
        else:
            print(msg)
        return 1

    if args.json:
        json.dump({"resultados": resultados}, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return 0

    for r in resultados:
        print(f"- Letra: {r['letra']} | Órgão: {r.get('orgao') or '-'} | Arquétipo: {r.get('arquétipo') or '-'}")
        print(f"  Tratamento: {r['tratamento_sugerido']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())