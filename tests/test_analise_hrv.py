# -*- coding: utf-8 -*-
"""
Testes Unitários para o Módulo de Análise de HRV do SCII

Este script verifica a corretude da função analisar_assinatura_vibracional,
garantindo que ela retorne os resultados esperados para diferentes cenários
de dados de entrada (Alinhado e Não Alinhado).

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 11 de Agosto de 2025
"""

import json
import os
import pytest
from scii_medicao_hrv.analise_hrv import analisar_assinatura_vibracional

# --- Fixtures para os Testes ---

@pytest.fixture
def assinatura_arquetipica_exemplo():
    """Fornece uma assinatura arquetípica padrão para os testes."""
    return {
        "hrv_media_ideal": 70.0,
        "desvio_padrao_ideal": 10.0
    }

@pytest.fixture
def criar_arquivo_json_temporario(tmp_path):
    """Cria um arquivo JSON temporário com dados de HRV para um teste."""
    def _criar_arquivo(dados, nome_arquivo="teste.json"):
        caminho_arquivo = tmp_path / nome_arquivo
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4)
        return str(caminho_arquivo)
    return _criar_arquivo

# --- Testes de Cenários ---

def test_analise_alinhada(criar_arquivo_json_temporario, assinatura_arquetipica_exemplo):
    """
    Testa o cenário onde os dados de HRV estão ALINHADOS com a assinatura.
    A média e o desvio padrão estão dentro da margem de tolerância de 10%.
    """
    # Dados que resultam em média ~70.2 e desvio padrão ~9.8 (dentro da tolerância)
    dados_alinhados = [
        {"timestamp": "2025-08-11T12:00:00", "hrv": 60.0},
        {"timestamp": "2025-08-11T12:00:01", "hrv": 82.0},
        {"timestamp": "2025-08-11T12:00:02", "hrv": 71.0},
        {"timestamp": "2025-08-11T12:00:03", "hrv": 58.0},
        {"timestamp": "2025-08-11T12:00:04", "hrv": 80.0}
    ]
    caminho_arquivo = criar_arquivo_json_temporario(dados_alinhados)

    # Executa a análise
    relatorio = analisar_assinatura_vibracional(caminho_arquivo, assinatura_arquetipica_exemplo)

    # Verifica se o relatório contém a avaliação correta
    assert "Status: Alinhado" in relatorio
    assert "bom alinhamento" in relatorio

def test_analise_nao_alinhada(criar_arquivo_json_temporario, assinatura_arquetipica_exemplo):
    """
    Testa o cenário onde os dados de HRV NÃO ESTÃO ALINHADOS com a assinatura.
    A média está muito abaixo do ideal, fora da margem de tolerância.
    """
    # Dados que resultam em média ~50, muito abaixo do ideal de 70
    dados_nao_alinhados = [
        {"timestamp": "2025-08-11T12:00:00", "hrv": 45.0},
        {"timestamp": "2025-08-11T12:00:01", "hrv": 55.0},
        {"timestamp": "2025-08-11T12:00:02", "hrv": 48.0},
        {"timestamp": "2025-08-11T12:00:03", "hrv": 52.0}
    ]
    caminho_arquivo = criar_arquivo_json_temporario(dados_nao_alinhados)

    # Executa a análise
    relatorio = analisar_assinatura_vibracional(caminho_arquivo, assinatura_arquetipica_exemplo)

    # Verifica se o relatório contém a avaliação correta
    assert "Status: Não Alinhado" in relatorio
    assert "detectou um desvio" in relatorio

# --- Testes de Casos Especiais (Edge Cases) ---

def test_arquivo_nao_encontrado():
    """Testa o comportamento quando o arquivo de entrada não existe."""
    relatorio = analisar_assinatura_vibracional("arquivo_inexistente.json", {})
    assert "Erro: Arquivo de medição não encontrado" in relatorio

def test_arquivo_json_invalido(criar_arquivo_json_temporario):
    """Testa o comportamento quando o arquivo JSON está mal formatado."""
    caminho_arquivo = criar_arquivo_json_temporario([], nome_arquivo="invalido.json")
    # Corrompe o arquivo JSON
    with open(caminho_arquivo, 'w') as f:
        f.write('{"chave": "valor",}') # JSON inválido com vírgula extra

    relatorio = analisar_assinatura_vibracional(caminho_arquivo, {})
    assert "formato JSON inválido" in relatorio

def test_arquivo_sem_dados_hrv(criar_arquivo_json_temporario):
    """Testa o comportamento quando o arquivo não contém medições de HRV."""
    caminho_arquivo = criar_arquivo_json_temporario([])
    relatorio = analisar_assinatura_vibracional(caminho_arquivo, {})
    assert "não contém dados de HRV" in relatorio
