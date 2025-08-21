#!/usr/bin/env python3
# Thunder Generator - Gerador de Áudio de Trovão
# Protocolo Vivaldi

import numpy as np
import wave
import sys
import argparse
from datetime import datetime

class ThunderGenerator:
    def __init__(self, base_frequency=528, duration=10, sample_rate=44100):
        self.base_frequency = base_frequency
        self.duration = duration
        self.sample_rate = sample_rate
        self.harmonics = [1, 1.5, 2, 2.5, 3]
        
    def generate_thunder_wave(self, season='primavera'):
        """Gera onda de trovão harmônico baseada na estação"""
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration))
        
        # Frequência base para cada estação
        season_frequencies = {
            'primavera': 396,
            'estate': 417,
            'autunno': 528,
            'inverno': 639
        }
        
        base_freq = season_frequencies.get(season.lower(), self.base_frequency)
        
        # Gera harmônicos
        wave_data = np.zeros_like(t)
        for i, harmonic in enumerate(self.harmonics):
            freq = base_freq * harmonic
            amplitude = 1 / (i + 1)  # Amplitude decrescente
            wave_data += amplitude * np.sin(2 * np.pi * freq * t)
        
        # Adiciona ruído de trovão
        noise = np.random.normal(0, 0.1, len(t))
        wave_data += noise
        
        # Aplica envelope de trovão
        envelope = self.generate_envelope(t)
        wave_data *= envelope
        
        # Normaliza
        wave_data = wave_data / np.max(np.abs(wave_data))
        
        return wave_data
    
    def generate_envelope(self, t):
        """Gera envelope de trovão"""
        # Começa suave, aumenta, depois decai
        attack = 0.1
        decay = 0.3
        sustain = 0.4
        release = 0.2
        
        envelope = np.zeros_like(t)
        
        attack_samples = int(len(t) * attack)
        decay_samples = int(len(t) * decay)
        sustain_samples = int(len(t) * sustain)
        release_samples = len(t) - attack_samples - decay_samples - sustain_samples
        
        # Attack
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
        
        # Decay
        envelope[attack_samples:attack_samples+decay_samples] = np.linspace(1, 0.7, decay_samples)
        
        # Sustain
        envelope[attack_samples+decay_samples:attack_samples+decay_samples+sustain_samples] = 0.7
        
        # Release
        envelope[-release_samples:] = np.linspace(0.7, 0, release_samples)
        
        return envelope
    
    def save_wave(self, wave_data, filename):
        """Salva arquivo de áudio"""
        wave_data = (wave_data * 32767).astype(np.int16)
        
        with wave.open(filename, 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16 bits
            wav_file.setframerate(self.sample_rate)
            wav_file.writeframes(wave_data.tobytes())
    
    def generate_seasonal_thunder(self, season):
        """Gera trovão para uma estação específica"""
        wave_data = self.generate_thunder_wave(season)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"thunder_{season}_{timestamp}.wav"
        self.save_wave(wave_data, filename)
        return filename

def main():
    parser = argparse.ArgumentParser(description='Gerador de trovão harmônico')
    parser.add_argument('frequency', type=int, help='Frequência base')
    parser.add_argument('season', type=str, help='Estação (primavera/estate/autunno/inverno)')
    parser.add_argument('--duration', type=int, default=10, help='Duração em segundos')
    parser.add_argument('--output', type=str, default='thunder.wav', help='Arquivo de saída')
    
    args = parser.parse_args()
    
    generator = ThunderGenerator(args.frequency, args.duration)
    filename = generator.generate_seasonal_thunder(args.season)
    
    print(f"Trovão gerado: {filename}")
    print(f"Frequência: {args.frequency} Hz")
    print(f"Estação: {args.season}")

if __name__ == "__main__":
    main()
