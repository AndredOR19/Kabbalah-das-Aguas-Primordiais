#!/bin/bash
# Protocolo Vivaldi - Neurostorm Script
# Script mestre de ativação do Protocolo Vivaldi

# Carrega configurações cabalísticas
source ./assets/data/il_grosso_mogul.yaml

# Determina estação atual
ESTACAO=$(python -c "from datetime import datetime; print(['INVERNO','PRIMAVERA','VERAO','OUTONO'][(datetime.now().month % 12)//3])")

# Obtém frequência base do mapeamento
FREQUENCIA=$(grep "$ESTACAO" ./assets/data/quattro_stagioni.map | awk -F: '/frequencia_base/ {print $2}')

# Gera trovão harmônico
python ./scripts/thunder_generator.py $FREQUENCIA $ESTACAO

# Inicia interface
echo "Iniciando Protocolo Vivaldi..."
echo "Estação atual: $ESTACAO"
echo "Frequência base: $FREQUENCIA Hz"
echo "Ativando interface..."
echo "Acesse: http://localhost:8000/vortex_player.html"

# Inicia servidor local (opcional)
# python -m http.server 8000
