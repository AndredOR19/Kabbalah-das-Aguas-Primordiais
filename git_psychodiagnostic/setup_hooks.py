#!/usr/bin/env python3
"""
Script de configuração automática dos Git hooks
"""

import os
import stat
from pathlib import Path

def setup_git_hooks():
    """Configura hooks do Git automaticamente"""
    
    # Diretório de hooks
    hooks_dir = Path(".git/hooks")
    if not hooks_dir.exists():
        print("❌ Não é um repositório Git")
        return False
    
    # Conteúdo do pre-commit hook
    pre_commit_content = '''#!/bin/sh
# Git Psychodiagnostic Pre-commit Hook
# Coleta dados psicossomáticos antes de cada commit

echo "🔍 Coletando dados psicossomáticos..."
python3 git_psychodiagnostic/scripts/psico_collect.py

# Verificar se o arquivo current_psico.json existe
if [ -f ".gitpsychodata/current_psico.json" ]; then
    echo "✅ Dados psicossomáticos coletados"
    git add .gitpsychodata/current_psico.json
else
    echo "⚠️ Nenhum dado psicossomático encontrado"
fi
'''
    
    # Escrever pre-commit hook
    pre_commit_file = hooks_dir / "pre-commit"
    with open(pre_commit_file, 'w') as f:
        f.write(pre_commit_content)
    
    # Tornar executável
    os.chmod(pre_commit_file, 0o755)
    
    print("✅ Hooks do Git configurados com sucesso!")
    print("   - Pre-commit hook ativado")
    print("   - Coleta automática de dados psicossomáticos")
    
    return True

if __name__ == "__main__":
    setup_git_hooks()
