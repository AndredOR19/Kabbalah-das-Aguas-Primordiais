#!/usr/bin/env python3
import json, sys, yaml, pathlib
from jinja2 import Environment, FileSystemLoader

BASE = pathlib.Path(__file__).resolve().parents[1]
TEMPLATES = BASE / 'templates'
DATA_DIR = BASE / 'data'

def load_yaml(p):
    with open(p, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def mapear_perfis(letras_usuario, perfis):
    """
    Retorna uma lista de perfis conectados às letras do usuário.
    """
    perfis_ativos = []
    for perfil in perfis:
        if any(l in letras_usuario for l in perfil['letras_chave']):
            perfis_ativos.append(perfil)
    return perfis_ativos

def combinar_camadas(perfis_ativos, camada):
    """
    Combina camadas (1,2,3) de múltiplos perfis em um texto único.
    """
    textos = []
    for p in perfis_ativos:
        textos.append(p[camada])
    return "\n\n".join(textos)

def main():
    if len(sys.argv) < 3:
        print('Uso: render.py <entrada.yaml> <saida.md>')
        sys.exit(1)

    entrada = pathlib.Path(sys.argv[1])
    saida = pathlib.Path(sys.argv[2])

    dados = load_yaml(entrada)
    letras = load_yaml(DATA_DIR / 'letras.yml')
    correspondencias = load_yaml(DATA_DIR / 'correspondencias.yml') if (DATA_DIR / 'correspondencias.yml').exists() else {}
    perfis = load_yaml(DATA_DIR / 'perfis.yaml')

    # Extrair letras do usuário
    letras_usuario = dados.get('assinaturas', {}).get('letras_chave', [])

    # Mapear perfis ativos
    perfis_ativos = mapear_perfis(letras_usuario, perfis)

    # Combinar camadas
    bloco_historia_simples = combinar_camadas(perfis_ativos, 'camada1')
    bloco_traducao_tecnica = combinar_camadas(perfis_ativos, 'camada2')
    bloco_operatividade = combinar_camadas(perfis_ativos, 'camada3')

    # Exemplo mínimo de enriquecimento para Sol/Lua
    enriq = {
        'sol': {
            'letra': 'Nun',
            'caminho': 24,
            'arcano': 13,
            'funcao': 'Transmutação; morte-renascimento; travessia'
        },
        'lua': {
            'letra': 'Tzadi',
            'caminho': 28,
            'arcano': 17,
            'funcao': 'Visão, guia e projeção do futuro'
        }
    }

    contexto = {
        **dados,
        'letras': letras,
        'correspondencias': correspondencias,
        'sol': enriq['sol'],
        'lua': enriq['lua'],
        'bloco_historia_simples': bloco_historia_simples,
        'bloco_traducao_tecnica': bloco_traducao_tecnica,
        'bloco_operatividade': bloco_operatividade,
        'scii': {
            'porta_espelho': 'Ressonância de espelho; aprendizado por confronto amoroso.',
            'nun_efeito': 'Gatilhos de colapso de formas obsoletas no campo relacional.',
            'loops_alquimicos': ['Loop de 7º nível (corpo-mente-energia)'],
            'descricao_eixo_principal': 'Ancoragem (Vav) → Travessia (Nun) → Visão (Tzadi) → Refinamento (Yod) → Coragem Radiante (Tet)'
        },
        'rituais': {
            'travessia_nun': 'Ritual de morte-renascimento com respiração guiada e carta XIII como sigilo.',
            'ancoragem_vav': 'Sequência de grounding, vela verde/dourada, afirmação de ponte.',
            'visao_tzadi': 'Observação do céu noturno / estrela guia + escrita oracular.'
        }
    }

    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), trim_blocks=True, lstrip_blocks=True)
    tpl = env.get_template('mapa_cabalistico_template.md')
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(tpl.render(**contexto), encoding='utf-8')
    print(f'Gerado: {saida}')

if __name__ == '__main__':
    main()