#!/usr/bin/env python3
"""
Validador da Ponte SCII-Core
Verifica a integridade e completude do arquivo scii_database.json
"""

import json
import sys
from pathlib import Path

def carregar_scii_core():
    """Carrega o arquivo SCII-Core"""
    caminho = Path("scii_database.js/data/scii_database.json")
    if not caminho.exists():
        print(f"❌ Arquivo não encontrado: {caminho}")
        return None
    
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Erro no JSON: {e}")
        return None

def validar_estrutura_letra(nome_letra, dados_letra):
    """Valida se uma letra possui todos os campos essenciais"""
    campos_obrigatorios = [
        'id', 'valor_gemátrico', 'letra_hebraica', 'nome_anatomico', 
        'id_mesh_3d', 'emocoes_associadas', 'estados_chave', 
        'funcao_espiritual', 'pratica_sugerida'
    ]
    
    campos_faltando = []
    for campo in campos_obrigatorios:
        if campo not in dados_letra:
            campos_faltando.append(campo)
    
    return campos_faltando

def validar_ponte(scii_data):
    """Valida a seção da ponte"""
    if 'ponte_sismografo_atlas' not in scii_data:
        return ["Seção 'ponte_sismografo_atlas' não encontrada"]
    
    ponte = scii_data['ponte_sismografo_atlas']
    erros = []
    
    # Verificar seções obrigatórias
    secoes_obrigatorias = ['mapeamento_emocoes_anatomia', 'estados_fisiologicos', 'configuracao_ponte']
    for secao in secoes_obrigatorias:
        if secao not in ponte:
            erros.append(f"Seção '{secao}' não encontrada na ponte")
    
    return erros

def validar_consistencia_mapeamento(scii_data):
    """Valida consistência entre letras e mapeamento"""
    if 'letras' not in scii_data or 'ponte_sismografo_atlas' not in scii_data:
        return ["Estrutura básica incompleta"]
    
    letras = scii_data['letras']
    mapeamento = scii_data['ponte_sismografo_atlas'].get('mapeamento_emocoes_anatomia', {})
    
    erros = []
    
    # Verificar se todas as emoções mapeadas existem nas letras
    for emocao, dados in mapeamento.items():
        letra_hebraica = dados.get('letra_hebraica')
        id_mesh = dados.get('id_mesh_3d')
        
        # Encontrar a letra correspondente
        letra_encontrada = None
        for nome_letra, dados_letra in letras.items():
            if dados_letra.get('letra_hebraica') == letra_hebraica:
                letra_encontrada = dados_letra
                break
        
        if not letra_encontrada:
            erros.append(f"Emoção '{emocao}' mapeia para letra '{letra_hebraica}' que não existe")
            continue
        
        # Verificar consistência do mesh_id
        if letra_encontrada.get('id_mesh_3d') != id_mesh:
            erros.append(f"Inconsistência no mesh_id para emoção '{emocao}'")
        
        # Verificar se a emoção está listada na letra
        emocoes_letra = letra_encontrada.get('emocoes_associadas', [])
        if emocao not in emocoes_letra:
            erros.append(f"Emoção '{emocao}' não está listada na letra '{letra_hebraica}'")
    
    return erros

def main():
    print("🔍 Validando SCII-Core...")
    print("=" * 50)
    
    # Carregar dados
    scii_data = carregar_scii_core()
    if not scii_data:
        sys.exit(1)
    
    print("✅ Arquivo JSON carregado com sucesso")
    
    # Validar estrutura básica
    if 'letras' not in scii_data:
        print("❌ Seção 'letras' não encontrada")
        sys.exit(1)
    
    # Validar cada letra
    letras_completas = 0
    letras_incompletas = 0
    
    print("\n📝 Validando letras hebraicas...")
    for nome_letra, dados_letra in scii_data['letras'].items():
        campos_faltando = validar_estrutura_letra(nome_letra, dados_letra)
        if campos_faltando:
            print(f"⚠️  {nome_letra}: Faltam campos {campos_faltando}")
            letras_incompletas += 1
        else:
            print(f"✅ {nome_letra}: Completa")
            letras_completas += 1
    
    print(f"\n📊 Resumo das letras:")
    print(f"   ✅ Completas: {letras_completas}")
    print(f"   ⚠️  Incompletas: {letras_incompletas}")
    print(f"   📈 Total: {letras_completas + letras_incompletas}")
    
    # Validar ponte
    print("\n🌉 Validando ponte...")
    erros_ponte = validar_ponte(scii_data)
    if erros_ponte:
        for erro in erros_ponte:
            print(f"❌ {erro}")
    else:
        print("✅ Estrutura da ponte válida")
    
    # Validar consistência
    print("\n🔗 Validando consistência...")
    erros_consistencia = validar_consistencia_mapeamento(scii_data)
    if erros_consistencia:
        for erro in erros_consistencia:
            print(f"❌ {erro}")
    else:
        print("✅ Mapeamento consistente")
    
    # Estatísticas da ponte
    if 'ponte_sismografo_atlas' in scii_data:
        ponte = scii_data['ponte_sismografo_atlas']
        num_emocoes = len(ponte.get('mapeamento_emocoes_anatomia', {}))
        num_estados = len(ponte.get('estados_fisiologicos', {}))
        
        print(f"\n📈 Estatísticas da ponte:")
        print(f"   🎭 Emoções mapeadas: {num_emocoes}")
        print(f"   🫀 Estados fisiológicos: {num_estados}")
    
    # Resultado final
    total_erros = len(erros_ponte) + len(erros_consistencia) + letras_incompletas
    
    print("\n" + "=" * 50)
    if total_erros == 0:
        print("🎉 SCII-Core está COMPLETO e VÁLIDO!")
        print("🚀 Pronto para integração Sismógrafo-Atlas")
    else:
        print(f"⚠️  SCII-Core tem {total_erros} problemas para resolver")
        print("🔧 Revise os itens marcados acima")
    
    return 0 if total_erros == 0 else 1

if __name__ == "__main__":
    sys.exit(main())