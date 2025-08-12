#!/usr/bin/env python3
"""
🌟 VALIDADOR COMPLETO DO SISTEMA SCII-CORE EXPANDIDO
Valida todas as funcionalidades: Ponte, Atlas 3D, Chave dos Céus e Integração Astral
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

def validar_ponte_scii():
    """Valida a Ponte SCII-Core original"""
    print("🔍 Validando Ponte SCII-Core...")
    
    try:
        # Validar SCII database
        scii_path = Path("scii_database.js/data/scii_database.json")
        if not scii_path.exists():
            return False, "SCII database não encontrado"
        
        # Validar psico_collect
        psico_path = Path("git_psychodiagnostic/scripts/psico_collect.py")
        if not psico_path.exists():
            return False, "psico_collect.py não encontrado"
        
        # Validar Atlas 3D
        atlas_path = Path("atlas_anatomico_3d.html")
        if not atlas_path.exists():
            return False, "Atlas 3D não encontrado"
        
        return True, "Ponte SCII-Core operacional"
        
    except Exception as e:
        return False, f"Erro na validação: {e}"

def validar_chave_dos_ceus():
    """Valida A Chave dos Céus"""
    print("🔍 Validando A Chave dos Céus...")
    
    try:
        # Validar calculadora astral
        calc_path = Path("scripts/calculadora_astral.py")
        if not calc_path.exists():
            return False, "calculadora_astral.py não encontrado"
        
        # Validar diretório de mapas
        mapas_dir = Path("mapas_astrais")
        if not mapas_dir.exists():
            return False, "Diretório mapas_astrais não encontrado"
        
        # Contar mapas existentes
        mapas_resumo = list(mapas_dir.glob("*_resumo.json"))
        mapas_completos = list(mapas_dir.glob("mapa_natal_*.json"))
        
        return True, f"Chave dos Céus operacional ({len(mapas_resumo)} mapas gerados)"
        
    except Exception as e:
        return False, f"Erro na validação: {e}"

def validar_integrador_astral():
    """Valida o Integrador Astral-SCII"""
    print("🔍 Validando Integrador Astral-SCII...")
    
    try:
        # Validar integrador
        integrador_path = Path("scripts/integrador_astral_scii.py")
        if not integrador_path.exists():
            return False, "integrador_astral_scii.py não encontrado"
        
        # Validar perfis integrados
        mapas_dir = Path("mapas_astrais")
        perfis_integrados = list(mapas_dir.glob("perfil_astral_scii_*.json"))
        
        return True, f"Integrador Astral-SCII operacional ({len(perfis_integrados)} perfis gerados)"
        
    except Exception as e:
        return False, f"Erro na validação: {e}"

def validar_dependencias():
    """Valida dependências do sistema"""
    print("🔍 Validando Dependências...")
    
    try:
        # Testar Kerykeion
        import kerykeion
        kerykeion_ok = True
    except ImportError:
        kerykeion_ok = False
    
    # Testar outras dependências
    dependencias = {
        "json": True,
        "pathlib": True,
        "datetime": True,
        "kerykeion": kerykeion_ok
    }
    
    falhas = [dep for dep, ok in dependencias.items() if not ok]
    
    if falhas:
        return False, f"Dependências ausentes: {', '.join(falhas)}"
    else:
        return True, "Todas as dependências instaladas"

def testar_funcionalidade_completa():
    """Testa funcionalidade completa do sistema"""
    print("🔍 Testando Funcionalidade Completa...")
    
    try:
        # Testar carregamento SCII-Core
        sys.path.append('git_psychodiagnostic/scripts')
        from psico_collect import PsicoCollector
        
        collector = PsicoCollector()
        if not collector.scii_data:
            return False, "SCII-Core não carregou"
        
        # Testar mapeamento de emoção
        correspondence = collector.find_emotion_correspondence('frustração')
        if not correspondence:
            return False, "Mapeamento de emoções falhou"
        
        # Testar criação de estado
        collector.create_estado_atual(correspondence)
        estado_path = Path("estado_atual.json")
        if not estado_path.exists():
            return False, "Criação de estado falhou"
        
        # Limpar estado
        collector.create_estado_atual(None)
        
        return True, "Funcionalidade completa testada com sucesso"
        
    except Exception as e:
        return False, f"Erro no teste: {e}"

def gerar_relatorio_sistema():
    """Gera relatório completo do sistema"""
    print("\n📊 GERANDO RELATÓRIO DO SISTEMA...")
    
    # Coletar estatísticas
    stats = {
        "timestamp": datetime.now().isoformat(),
        "versao_scii": "5.0",
        "componentes": {},
        "arquivos_gerados": {},
        "capacidades": []
    }
    
    # Contar arquivos por categoria
    mapas_dir = Path("mapas_astrais")
    if mapas_dir.exists():
        stats["arquivos_gerados"]["mapas_astrais"] = len(list(mapas_dir.glob("mapa_natal_*.json")))
        stats["arquivos_gerados"]["resumos_astrais"] = len(list(mapas_dir.glob("*_resumo.json")))
        stats["arquivos_gerados"]["perfis_integrados"] = len(list(mapas_dir.glob("perfil_astral_scii_*.json")))
    
    # Verificar componentes
    componentes_principais = {
        "ponte_scii": Path("validar_ponte_completa.py").exists(),
        "atlas_3d": Path("atlas_anatomico_3d.html").exists(),
        "chave_dos_ceus": Path("scripts/calculadora_astral.py").exists(),
        "integrador_astral": Path("scripts/integrador_astral_scii.py").exists(),
        "servidor_atlas": Path("servidor_atlas.py").exists(),
        "demo_completa": Path("demo_ponte_completa.py").exists()
    }
    
    stats["componentes"] = componentes_principais
    
    # Capacidades do sistema
    capacidades = [
        "Mapeamento emocional → anatômico",
        "Visualização 3D em tempo real",
        "Cálculo de mapas astrais natais",
        "Integração astrologia → cabala → anatomia",
        "Análise de correspondências cósmicas",
        "Perfis psicossomáticos integrados",
        "Biofeedback visual emocional",
        "Servidor web para Atlas 3D"
    ]
    
    stats["capacidades"] = capacidades
    
    # Salvar relatório
    relatorio_path = Path("relatorio_sistema_scii.json")
    with open(relatorio_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"📄 Relatório salvo: {relatorio_path}")
    return stats

def main():
    """Executa validação completa do sistema"""
    print("🌟 VALIDADOR COMPLETO DO SISTEMA SCII-CORE EXPANDIDO")
    print("=" * 70)
    print("Validando: Ponte + Atlas 3D + Chave dos Céus + Integração Astral")
    print("=" * 70)
    
    validacoes = [
        ("Ponte SCII-Core", validar_ponte_scii),
        ("A Chave dos Céus", validar_chave_dos_ceus),
        ("Integrador Astral-SCII", validar_integrador_astral),
        ("Dependências", validar_dependencias),
        ("Funcionalidade Completa", testar_funcionalidade_completa)
    ]
    
    resultados = []
    
    for nome, funcao_validacao in validacoes:
        try:
            sucesso, mensagem = funcao_validacao()
            resultados.append((nome, sucesso, mensagem))
            
            status = "✅ PASSOU" if sucesso else "❌ FALHOU"
            print(f"{status:12} | {nome}: {mensagem}")
            
        except Exception as e:
            resultados.append((nome, False, f"Erro crítico: {e}"))
            print(f"❌ FALHOU    | {nome}: Erro crítico: {e}")
    
    # Gerar relatório
    stats = gerar_relatorio_sistema()
    
    # Resumo final
    print("\n" + "=" * 70)
    print("📊 RESUMO FINAL DA VALIDAÇÃO")
    print("=" * 70)
    
    sucessos = sum(1 for _, sucesso, _ in resultados if sucesso)
    total = len(resultados)
    
    print(f"📈 RESULTADO GERAL: {sucessos}/{total} validações passaram")
    print(f"🎯 Taxa de Sucesso: {(sucessos/total)*100:.1f}%")
    
    if sucessos == total:
        print("\n🎉 SISTEMA SCII-CORE EXPANDIDO TOTALMENTE OPERACIONAL!")
        print("🚀 Todas as funcionalidades validadas com sucesso")
        print("\n🌟 CAPACIDADES DISPONÍVEIS:")
        for capacidade in stats["capacidades"]:
            print(f"   ✨ {capacidade}")
        
        print(f"\n📊 ESTATÍSTICAS:")
        print(f"   🗂️ Mapas astrais: {stats['arquivos_gerados'].get('mapas_astrais', 0)}")
        print(f"   📋 Resumos SCII: {stats['arquivos_gerados'].get('resumos_astrais', 0)}")
        print(f"   🔮 Perfis integrados: {stats['arquivos_gerados'].get('perfis_integrados', 0)}")
        
        print(f"\n💡 PRÓXIMOS PASSOS:")
        print("   1. Execute: python3 servidor_atlas.py")
        print("   2. Execute: python3 scripts/calculadora_astral.py")
        print("   3. Execute: python3 scripts/integrador_astral_scii.py")
        print("   4. Execute: python3 demo_ponte_completa.py demo")
        print("   5. Explore as correspondências cósmicas! 🌌")
        
    else:
        print("\n⚠️ SISTEMA PARCIALMENTE OPERACIONAL")
        print("🔧 Corrija os problemas identificados acima")
        
        falhas = [nome for nome, sucesso, _ in resultados if not sucesso]
        print(f"❌ Componentes com falhas: {', '.join(falhas)}")
    
    return sucessos == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)