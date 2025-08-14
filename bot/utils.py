import json

def carregar_configuracao():
    """Carrega as configurações do bot."""
    with open('bot/config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def carregar_base_conhecimento():
    """Carrega a base de conhecimento."""
    with open('base_conhecimento.json', 'r', encoding='utf-8') as f:
        return json.load(f)