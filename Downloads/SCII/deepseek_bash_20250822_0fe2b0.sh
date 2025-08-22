#!/bin/bash

echo "Instalando Sistema Kabbalah das Águas Primordiais..."
echo "==================================================="

# Criar estrutura de pastas
mkdir -p {scripts,data,logs,reports}

# Instalar dependências Python
pip install -r requirements.txt

# Configurar banco de dados local
python scripts/init_db.py

# Configurar agendamento de backups
echo "0 2 * * * python scripts/backup.py" >> /etc/crontab

# Configurar permissões
chmod +x scripts/*.py

echo "Instalação concluída!"
echo "Execute: python scripts/sistema_principal.py"