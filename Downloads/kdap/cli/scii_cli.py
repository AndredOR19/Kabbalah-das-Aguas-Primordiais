# scii_cli.py - CLI para consultas ao SCII
import sys
from scripts.scii_core import translate

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scii_cli.py 'Palavra'")
    else:
        word = sys.argv[1]
        result = translate(word)
        print(f"Entrada: {result['input']}")
        print(f"Hebraico: {result['hebrew']}")
        print(f"Valores: {result['values']}")
        print(f"Arquétipos: {result['archetypes']}")
        print(f"Caminhos: {result['paths']}")
        print(f"Tikun: {result['tikun']}")
        print(f"Gematria Total: {result['gematria_total']}")
