def calcular_indice_imanencia(pontuacoes):
    """
    pontuacoes: dicionário com pesos atribuídos às variáveis.
    Exemplo:
    {
      "linguagem": 0.6,
      "nível de abstração": 0.4,
      "valor atribuído ao sagrado": 0.8,
      "uso de analogias científicas": 0.3,
      "presença de despersonalização cósmica": 0.7
    }
    """
    pesos = {
      "linguagem": 0.20,
      "nível de abstração": 0.20,
      "valor atribuído ao sagrado": 0.25,
      "uso de analogias científicas": 0.15,
      "presença de despersonalização cósmica": 0.20
    }
    soma = sum(pontuacoes[chave] * pesos[chave] for chave in pesos)
    return round(soma, 2)
