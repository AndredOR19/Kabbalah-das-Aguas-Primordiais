#!/usr/bin/env python3
"""
VALIDADOR COMPLETO DA PONTE SCII-CORE
Verifica se todos os componentes estão funcionando corretamente
"""

import json
import sys
import os
from pathlib import Path

# Adicionar caminho do psico_collect
sys.path.append('git_psychodiagnostic/scripts')

def validar_scii_database():
    """Valida o SCII-Core database"""
    print("🔍 Validando SCII-Core Database...")
    
    scii_path = Path("scii_database.js/data/scii_database.json")
    
    if not scii_path.exists():
        print(f"❌ SCII database não encontrado: {scii_path}")
        return False
    
    try:
        with open(scii_path, 'r', encoding='utf-8') as f:
            scii_data = json.load(f)
        
        # Verificar estrutura essencial
        required_keys = ['letras', 'ponte_sismografo_atlas']
        for key in required_keys:
            if key not in scii_data:
                print(f"❌ Chave obrigatória ausente: {key}")
                return False
        
        # Verificar letras
        letras = scii_data['letras']
        letras_completas = 0
        
        for nome_letra, dados in letras.items():
            required_fields = ['id', 'letra_hebraica', 'nome_anatomico', 'id_mesh_3d']
            if all(field in dados for field in required_fields):
                letras_completas += 1
        
        print(f"✅ SCII Database válido")
        print(f"   📚 Letras completas: {letras_completas}/22")
        
        # Verificar ponte
        ponte = scii_data['ponte_sismografo_atlas']
        mapeamento = ponte.get('mapeamento_emocoes_anatomia', {})
        print(f"   🌉 Emoções mapeadas: {len(mapeamento)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao validar SCII database: {e}")
        return False

def validar_sistema1():
    """Valida o Sistema 1 (Sismógrafo)"""
    print("\n🔍 Validando Sistema 1 (Sismógrafo)...")
    
    psico_collect_path = Path("git_psychodiagnostic/scripts/psico_collect.py")
    
    if not psico_collect_path.exists():
        print(f"❌ Script psico_collect.py não encontrado: {psico_collect_path}")
        return False
    
    try:
        from psico_collect import PsicoCollector
        
        collector = PsicoCollector()
        
        # Testar carregamento do SCII
        if not collector.scii_data:
            print("❌ Sistema 1 não conseguiu carregar SCII-Core")
            return False
        
        # Testar mapeamento de emoção
        test_emotion = 'frustração'
        correspondence = collector.find_emotion_correspondence(test_emotion)
        
        if not correspondence:
            print(f"❌ Sistema 1 não conseguiu mapear emoção: {test_emotion}")
            return False
        
        # Testar criação de estado
        collector.create_estado_atual(correspondence)
        estado_path = Path("estado_atual.json")
        
        if not estado_path.exists():
            print("❌ Sistema 1 não conseguiu criar estado_atual.json")
            return False
        
        print("✅ Sistema 1 (Sismógrafo) funcionando")
        print(f"   🎭 Teste de emoção: {test_emotion} → {correspondence['sistema_anatomico']}")
        print(f"   📄 Estado atual criado: {estado_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao validar Sistema 1: {e}")
        return False

def validar_sistema2():
    """Valida o Sistema 2 (Atlas 3D)"""
    print("\n🔍 Validando Sistema 2 (Atlas 3D)...")
    
    atlas_path = Path("atlas_anatomico_3d.html")
    
    if not atlas_path.exists():
        print(f"❌ Atlas 3D não encontrado: {atlas_path}")
        return False
    
    try:
        with open(atlas_path, 'r', encoding='utf-8') as f:
            atlas_content = f.read()
        
        # Verificar componentes essenciais
        required_components = [
            'three.min.js',
            'checkEstadoAtual',
            'applyVisualEffect',
            'anatomyMeshes',
            'estado_atual.json'
        ]
        
        missing_components = []
        for component in required_components:
            if component not in atlas_content:
                missing_components.append(component)
        
        if missing_components:
            print(f"❌ Componentes ausentes no Atlas: {missing_components}")
            return False
        
        print("✅ Sistema 2 (Atlas 3D) estruturalmente válido")
        print(f"   📄 Arquivo: {atlas_path}")
        print(f"   🎮 Three.js: Integrado")
        print(f"   🔄 Monitoramento de estado: Implementado")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao validar Sistema 2: {e}")
        return False

def validar_ponte_comunicacao():
    """Valida a comunicação entre os sistemas"""
    print("\n🔍 Validando Comunicação da Ponte...")
    
    try:
        from psico_collect import PsicoCollector
        
        collector = PsicoCollector()
        
        # Testar sequência completa
        test_emotions = ['frustração', 'ansiedade', 'ego_inflado']
        
        for emotion in test_emotions:
            # Sistema 1: Mapear emoção
            correspondence = collector.find_emotion_correspondence(emotion)
            
            if not correspondence:
                print(f"❌ Falha no mapeamento: {emotion}")
                return False
            
            # Sistema 1: Criar estado
            collector.create_estado_atual(correspondence)
            
            # Verificar se Sistema 2 pode ler
            estado_path = Path("estado_atual.json")
            if not estado_path.exists():
                print(f"❌ Estado não criado para: {emotion}")
                return False
            
            with open(estado_path, 'r', encoding='utf-8') as f:
                estado_data = json.load(f)
            
            # Verificar campos essenciais para o Atlas
            required_fields = ['sistema_anatomico', 'id_mesh_3d', 'letra_hebraica']
            if not all(field in estado_data for field in required_fields):
                print(f"❌ Estado incompleto para: {emotion}")
                return False
        
        # Limpar estado final
        collector.create_estado_atual(None)
        
        print("✅ Comunicação da Ponte funcionando")
        print(f"   🔄 Emoções testadas: {len(test_emotions)}")
        print(f"   📡 Protocolo estado_atual.json: OK")
        print(f"   🌉 Ciclo completo: Funcional")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao validar comunicação: {e}")
        return False

def validar_arquivos_auxiliares():
    """Valida arquivos auxiliares"""
    print("\n🔍 Validando Arquivos Auxiliares...")
    
    arquivos_esperados = [
        "demo_ponte_completa.py",
        "servidor_atlas.py",
        "validar_ponte_scii.py"
    ]
    
    arquivos_encontrados = 0
    
    for arquivo in arquivos_esperados:
        if Path(arquivo).exists():
            arquivos_encontrados += 1
            print(f"   ✅ {arquivo}")
        else:
            print(f"   ⚠️ {arquivo} (opcional)")
    
    print(f"✅ Arquivos auxiliares: {arquivos_encontrados}/{len(arquivos_esperados)} encontrados")
    return True

def main():
    """Executa validação completa"""
    print("🌟 VALIDADOR COMPLETO DA PONTE SCII-CORE")
    print("=" * 60)
    print("Verificando integração Sistema 1 ↔ Sistema 2")
    print("=" * 60)
    
    validacoes = [
        ("SCII-Core Database", validar_scii_database),
        ("Sistema 1 (Sismógrafo)", validar_sistema1),
        ("Sistema 2 (Atlas 3D)", validar_sistema2),
        ("Comunicação da Ponte", validar_ponte_comunicacao),
        ("Arquivos Auxiliares", validar_arquivos_auxiliares)
    ]
    
    resultados = []
    
    for nome, funcao_validacao in validacoes:
        try:
            resultado = funcao_validacao()
            resultados.append((nome, resultado))
        except Exception as e:
            print(f"❌ Erro crítico em {nome}: {e}")
            resultados.append((nome, False))
    
    # Resumo final
    print("\n" + "=" * 60)
    print("📊 RESUMO DA VALIDAÇÃO")
    print("=" * 60)
    
    sucessos = 0
    for nome, resultado in resultados:
        status = "✅ PASSOU" if resultado else "❌ FALHOU"
        print(f"{status:12} | {nome}")
        if resultado:
            sucessos += 1
    
    print("-" * 60)
    print(f"📈 RESULTADO GERAL: {sucessos}/{len(resultados)} validações passaram")
    
    if sucessos == len(resultados):
        print("\n🎉 PONTE SCII-CORE TOTALMENTE FUNCIONAL!")
        print("🚀 Pronta para uso em produção")
        print("\n💡 Próximos passos:")
        print("   1. Execute: python3 servidor_atlas.py")
        print("   2. Execute: python3 demo_ponte_completa.py demo")
        print("   3. Observe a magia acontecer! ✨")
    else:
        print("\n⚠️ PONTE PARCIALMENTE FUNCIONAL")
        print("🔧 Corrija os problemas identificados acima")
    
    return sucessos == len(resultados)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)