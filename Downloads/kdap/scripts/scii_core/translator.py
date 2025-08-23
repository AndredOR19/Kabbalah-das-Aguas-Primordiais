# translator.py - Núcleo do SCII
def translate(word):
    mapping = {
        "I": ("י", 10, "Yod - Semente", 20, "Potencial criativo"),
        "S": ("ס", 60, "Samekh - Suporte", 25, "Confiança"),
        "A": ("א", 1, "Aleph - Sopro", 11, "Unificação do início")
    }

    result = {
        "input": word,
        "hebrew": [],
        "values": [],
        "archetypes": [],
        "paths": [],
        "tikun": [],
        "gematria_total": 0
    }

    total = 0
    for char in word.upper():
        if char in mapping:
            heb, val, arch, path, tik = mapping[char]
            result["hebrew"].append(heb)
            result["values"].append(val)
            result["archetypes"].append(arch)
            result["paths"].append(path)
            result["tikun"].append(tik)
            total += val

    result["hebrew"] = " ".join(result["hebrew"])
    result["gematria_total"] = total
    return result
