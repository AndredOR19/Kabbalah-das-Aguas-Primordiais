#!/usr/bin/env python3
"""CLI mínimo para consulta SCII (protótipo).

Uso:
  python scripts/cli_scii.py "Issá"
"""
import sys, json
from scii_core import analisar_termo

def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/cli_scii.py \"TERMO\"")
        sys.exit(1)
    termo = " ".join(sys.argv[1:])
    resultado = analisar_termo(termo)
    print(resultado.to_json())

if __name__ == "__main__":
    main()
