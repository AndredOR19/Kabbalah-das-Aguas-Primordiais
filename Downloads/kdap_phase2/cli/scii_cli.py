import argparse
from scripts.scii_core.core import SCIIEngine

def main():
    parser = argparse.ArgumentParser(description="Consulta ao SCII - Kabbalah das Águas Primordiais")
    parser.add_argument("palavra", type=str, help="Palavra ou nome para análise")
    args = parser.parse_args()

    engine = SCIIEngine()
    resultado = engine.analyze(args.palavra)

    print("=== Consulta SCII ===")
    print(f"Entrada: {resultado['input']}")
    print(f"Letras Hebraicas: {' '.join(resultado['letters'])}")
    print(f"Valores: {resultado['values']}")
    print(f"Arquétipos: {resultado['arquétipos']}")
    print(f"Caminhos: {resultado['caminhos']}")
    print(f"Tikun: {resultado['tikun']}")
    print(f"Gematria Total: {resultado['gematria_total']}")

if __name__ == "__main__":
    main()
