#!/usr/bin/env python3
"""
Gerador de Trovões Harmônicos
- Entrada: frequência (Hz) e estação (string)
- Saída: arquivo WAV em tempestades_geradas/

Uso:
    python3 thunder_generator.py 528 PRIMAVERA

Dependências:
    numpy (para síntese de sinal)

Observações:
    - Duração e taxa de amostragem podem ser definidas via variáveis de ambiente:
        DURACAO_TROVAO (segundos, float) [default 3.0]
        SAMPLE_RATE (Hz, int)            [default 44100]
"""

import os
import sys
import math
import time
import wave
import struct
from datetime import datetime

try:
    import numpy as np
except Exception as e:
    print(f"[ERRO] Numpy não disponível: {e}")
    print("Instale com: pip3 install numpy")
    sys.exit(1)


def gerar_trovao(frequencia_hz: float, duracao_s: float, sample_rate: int = 44100) -> np.ndarray:
    """Gera um sinal de áudio tipo 'trovão' usando seno + ruído com decaimento exponencial."""
    t = np.linspace(0, duracao_s, int(sample_rate * duracao_s), endpoint=False)

    # Componente senoidal base
    seno = np.sin(2 * np.pi * frequencia_hz * t)

    # Ruído branco suave para textura de trovão
    ruido = np.random.normal(0, 0.4, size=t.shape)

    # Envoltória com ataque curto e decaimento exponencial
    ataque_s = max(0.02, duracao_s * 0.05)
    ataque = np.clip(t / ataque_s, 0, 1)
    decaimento = np.exp(-3 * t / duracao_s)
    envoltoria = ataque * decaimento

    sinal = (0.6 * seno + 0.4 * ruido) * envoltoria

    # Normalização para int16
    sinal = sinal / (np.max(np.abs(sinal)) + 1e-12)
    return (sinal * 32767).astype(np.int16)


def salvar_wav(caminho: str, dados: np.ndarray, sample_rate: int):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with wave.open(caminho, 'wb') as wf:
        wf.setnchannels(1)  # mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        # Escreve em blocos para evitar uso excessivo de memória
        frames = struct.pack('<' + 'h' * len(dados), *dados.tolist())
        wf.writeframes(frames)


def main():
    if len(sys.argv) < 3:
        print("Uso: python3 thunder_generator.py <frequencia_hz> <ESTACAO>")
        sys.exit(2)

    try:
        freq = float(sys.argv[1])
    except ValueError:
        print("[ERRO] Frequência inválida. Ex: 528")
        sys.exit(2)

    estacao = str(sys.argv[2]).upper()

    # Parâmetros via ambiente (opcionais)
    duracao = float(os.getenv('DURACAO_TROVAO', '3.0'))
    sample_rate = int(os.getenv('SAMPLE_RATE', '44100'))

    print(f"[⚡] Gerando trovão: {freq:.0f}Hz | Estação: {estacao} | Duração: {duracao}s | SR: {sample_rate}")

    dados = gerar_trovao(freq, duracao, sample_rate)

    carimbo = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f"tempestades_geradas/trovao_{estacao.lower()}_{int(freq)}Hz_{carimbo}.wav"

    salvar_wav(nome_arquivo, dados, sample_rate)
    print(f"[✅] Trovão salvo em: {nome_arquivo}")


if __name__ == '__main__':
    main()