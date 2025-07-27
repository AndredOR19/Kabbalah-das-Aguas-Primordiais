#!/usr/bin/env python3
"""
Ferramenta simples para cálculo de gematria hebraica.

Este script define um dicionário de valores gemátricos das letras hebraicas e
oferece funções para somar o valor numérico de uma palavra ou frase.  
Pode ser utilizado de forma interativa ou incorporado a outros módulos.

Exemplo de uso:

    $ python3 calculate_gematria.py "שלום"
    Valor gemátrico de 'שלום': 376

Autor: Equipe O Corpo do Verbo
"""

import sys
import unicodedata

# Mapeamento de letras hebraicas para valores gemátricos (sistema padrão)
GEMATRIA_MAP = {
    'א': 1,
    'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10,
    'כ': 20, 'ך': 20,
    'ל': 30,
    'מ': 40, 'ם': 40,
    'נ': 50, 'ן': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80, 'ף': 80,
    'צ': 90, 'ץ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400
}


def remove_niqqud(text: str) -> str:
    """Remove vogais e sinais diacríticos (niqqud) de um texto hebraico."""
    return ''.join(c for c in text if not unicodedata.combining(c))


def calcular_gematria(palavra: str) -> int:
    """
    Calcula o valor gemátrico de uma palavra ou frase hebraica.
    Letras que não estiverem no dicionário são ignoradas.
    """
    soma = 0
    palavra_limpa = remove_niqqud(palavra)
    for letra in palavra_limpa:
        if letra in GEMATRIA_MAP:
            soma += GEMATRIA_MAP[letra]
    return soma


def main(args: list[str]) -> None:
    if not args:
        print("Uso: python3 calculate_gematria.py <palavra ou frase hebraica>")
        return
    entrada = ' '.join(args)
    valor = calcular_gematria(entrada)
    print(f"Valor gemátrico de '{entrada}': {valor}")


if __name__ == '__main__':
    main(sys.argv[1:])
