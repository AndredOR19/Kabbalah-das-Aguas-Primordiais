# Git Psychodiagnostic Module
Módulo de diagnóstico psicossomático integrado ao Git para VS Code.

## 🚀 Como Usar

### Instalação Rápida
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar Git hooks
python setup_hooks.py

# 3. Coletar dados
python scripts/psico_collect.py

# 4. Visualizar dashboard
python dashboard/app.py
```

### Fluxo de Trabalho
1. **Coleta Manual**: Digite valores diretamente
2. **Coleta Webcam**: Análise automática de expressões
3. **Commit Inteligente**: Dados embutidos automaticamente
4. **Dashboard**: Visualização temporal dos padrões

## 📊 Dados Coletados
- HR (Heart Rate)
- HRV (Heart Rate Variability)
- Respiração (rpm)
- Foco (%)
- Humor (manual/detectado)
- Observações livres

## 🔧 Arquitetura
```
git_psychodiagnostic/
├── scripts/          # Coleta de dados
├── dashboard/        # Visualização
├── hooks/           # Git hooks
├── templates/       # Templates de commit
└── data/           # Armazenamento local
