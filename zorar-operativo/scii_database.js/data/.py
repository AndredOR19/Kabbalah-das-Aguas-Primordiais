import json
with open('scii_database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data['letras']['Aleph']['comando_ritualistico'])
