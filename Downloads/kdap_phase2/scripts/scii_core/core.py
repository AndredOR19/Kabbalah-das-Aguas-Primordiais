import json
import os

class SCIIEngine:
    def __init__(self):
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'transliteracao.json')
        with open(data_path, 'r', encoding='utf-8') as f:
            self.translit = json.load(f)

    def analyze(self, word):
        result = {
            "input": word,
            "letters": [],
            "values": [],
            "arquétipos": [],
            "caminhos": [],
            "tikun": []
        }

        # Percorrer cada caractere do input (simplesmente, pode ser refinado com regex)
        for char in word:
            entry = self.translit.get(char.upper()) or self.translit.get(char.lower())
            if entry:
                result["letters"].append(entry.get("hebraico", char))
                result["values"].append(entry.get("valor", None))
                result["arquétipos"].append(entry.get("arquetipo", None))
                result["caminhos"].append(entry.get("caminho", None))
                result["tikun"].append(entry.get("tikun", None))
            else:
                result["letters"].append(char)
                result["values"].append(None)
                result["arquétipos"].append(None)
                result["caminhos"].append(None)
                result["tikun"].append(None)

        # Soma do valor total
        result["gematria_total"] = sum(v for v in result["values"] if v is not None)
        return result
