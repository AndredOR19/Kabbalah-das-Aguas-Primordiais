#!/usr/bin/env python3
"""
Teste da integração SCII-Core no Sistema 1
"""

import sys
import os
sys.path.append('git_psychodiagnostic/scripts')

from psico_collect import PsicoCollector

def test_emotion_mapping():
    """Testa o mapeamento de emoções"""
    collector = PsicoCollector()
    
    # Testar emoções conhecidas
    emotions_to_test = [
        'frustração',
        'ansiedade', 
        'medo_da_mudança',
        'ego_inflado',
        'materialismo',
        'emoção_inexistente'
    ]
    
    print("🧪 TESTE: Mapeamento de Emoções SCII-Core")
    print("=" * 50)
    
    for emotion in emotions_to_test:
        print(f"\n🔍 Testando: '{emotion}'")
        correspondence = collector.find_emotion_correspondence(emotion)
        
        if correspondence:
            print(f"✅ Encontrado:")
            print(f"   🫀 Sistema: {correspondence['sistema_anatomico']}")
            print(f"   🔤 Letra: {correspondence['letra_hebraica']} ({correspondence['nome_letra']})")
            print(f"   🎯 Mesh ID: {correspondence['id_mesh_3d']}")
            
            # Criar estado atual para teste
            collector.create_estado_atual(correspondence)
        else:
            print(f"❌ Não encontrado")
            collector.create_estado_atual(None)
    
    print("\n🎉 Teste concluído!")

if __name__ == "__main__":
    test_emotion_mapping()