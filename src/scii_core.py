"""
SCII Core Loader and Query Utilities
- Loads SCII JSON database
- Provides minimal diagnostic query by emotion keyword
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "scii_database.js" / "data" / "scii_database.json"

class SCII:
    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = Path(db_path) if db_path else DB_PATH
        if not self.db_path.exists():
            raise FileNotFoundError(f"SCII database not found: {self.db_path}")
        with self.db_path.open("r", encoding="utf-8") as f:
            self.data: Dict[str, Any] = json.load(f)
        # Expect structure { metadata, letras: { "Aleph": {...}, ... } }
        self.letras: Dict[str, Dict[str, Any]] = self.data.get("letras", {})

    def diagnostico_por_emocao(self, termo: str) -> List[Dict[str, Any]]:
        termo_lc = termo.strip().lower()
        resultados: List[Dict[str, Any]] = []
        for letra, info in self.letras.items():
            emoc = info.get("emocoes_associadas") or info.get("emocao")
            if not emoc:
                continue
            # normalize to list of strings
            if isinstance(emoc, str):
                lista = [emoc]
            else:
                lista = [str(e) for e in emoc]
            match = any(termo_lc in e.lower() for e in lista)
            if match:
                orgao = info.get("nome_anatomico") or (info.get("corpo") or {}).get("orgao")
                arquetipo = info.get("astro_secundario") or info.get("arquétipo")
                resultados.append({
                    "letra": letra,
                    "orgao": orgao,
                    "arquétipo": arquetipo,
                    "tratamento_sugerido": self._tratamento(letra, orgao),
                })
        return resultados

    @staticmethod
    def _tratamento(letra: str, orgao: str | None) -> str:
        alvo = f" + atenção ao {orgao}" if orgao else ""
        return f"Meditação na letra {letra}{alvo}"

if __name__ == "__main__":
    import argparse, pprint
    parser = argparse.ArgumentParser(description="Diagnóstico SCII por emoção/sintoma")
    parser.add_argument("--emocao", "--sintoma", dest="emocao", required=True, help="termo a buscar (ex: ansiedade)")
    args = parser.parse_args()
    scii = SCII()
    pp = pprint.PrettyPrinter(indent=2, width=100, sort_dicts=False)
    pp.pprint(scii.diagnostico_por_emocao(args.emocao))