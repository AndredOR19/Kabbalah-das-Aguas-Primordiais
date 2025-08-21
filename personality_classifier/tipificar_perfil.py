# -*- coding: utf-8 -*-
"""
SCII - Motor de Predição de Perfil Arquetípico

Este script carrega o modelo treinado e seus artefatos para realizar
a predição de um perfil arquetípico a partir de um novo texto.

Ele é projetado para ser chamado pela API, recebendo um texto e
retornando o "Perfil-Verbo" completo.

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 12 de Agosto de 2025
"""

import pickle
import pandas as pd
import re
from nltk.stem import WordNetLemmatizer

# --- CARREGAMENTO DOS ARTEFATOS DO MODELO ---

# Caminhos para os arquivos salvos
MODEL_PATH = 'personality_classifier/scii_model.pkl'
VECTORIZER_PATH = 'personality_classifier/scii_vectorizer.pkl'
LABEL_ENCODER_PATH = 'personality_classifier/scii_label_encoder.pkl'
DATASET_PATH = 'personality_classifier/scii_dataset_template.csv'

try:
    # Carregar o modelo treinado
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("Modelo (scii_model.pkl) carregado com sucesso.")

    # Carregar o vetorizador
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
    print("Vetorizador (scii_vectorizer.pkl) carregado com sucesso.")

    # Carregar o codificador de rótulos
    with open(LABEL_ENCODER_PATH, 'rb') as f:
        label_encoder = pickle.load(f)
    print("Codificador de Rótulos (scii_label_encoder.pkl) carregado com sucesso.")

    # Carregar o dataset para mapeamento reverso
    df_mapa = pd.read_csv(DATASET_PATH)
    print("Dataset de mapeamento carregado com sucesso.")

except FileNotFoundError as e:
    print(f"Erro crítico ao carregar artefatos do modelo: {e}")
    print("Por favor, execute o script 'treinar_modelo_scii.py' primeiro.")
    model = None # Garante que o script não funcione se os modelos não forem carregados

# --- FUNÇÃO DE LIMPEZA DE TEXTO (deve ser idêntica à do treinamento) ---
def limpar_texto_predicao(texto):
    """
Aplica a mesma limpeza do treinamento em um único texto.
    """
    lemmatizer = WordNetLemmatizer()
    
    texto = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', texto)
    texto = re.sub(r'[^a-zA-Z\s]', '', texto, re.I|re.A)
    texto = texto.lower()
    
    palavras = texto.split()
    palavras_lematizadas = [lemmatizer.lemmatize(palavra) for palavra in palavras]
    texto_limpo = " ".join(palavras_lematizadas)
    
    return texto_limpo

# --- FUNÇÃO PRINCIPAL DE TIPIFICAÇÃO ---
def obter_perfil_verbo(texto_usuario):
    """
    Processa um texto de usuário e retorna o Perfil-Verbo completo.

    Args:
        texto_usuario (str): O texto fornecido pelo usuário.

    Returns:
        dict: Um dicionário contendo o Perfil-Verbo completo ou um erro.
    """
    if model is None:
        return {"erro": "O modelo de tipificação não está carregado. Execute o treinamento."}

    print(f"\nRecebido texto para tipificação: '{texto_usuario[:50]}...'")

    # 1. Limpar o texto de entrada
    texto_limpo = limpar_texto_predicao(texto_usuario)
    print(f"Texto limpo: '{texto_limpo[:50]}...'")

    # 2. Vetorizar o texto usando o mesmo vetorizador do treinamento
    vetor_texto = vectorizer.transform([texto_limpo]).toarray()

    # 3. Fazer a predição com o modelo
    predicao_numerica = model.predict(vetor_texto)

    # 4. Decodificar a predição para obter o diagnóstico_chave
    diagnostico_chave_predito = label_encoder.inverse_transform(predicao_numerica)[0]
    print(f"Diagnóstico Chave Predito: {diagnostico_chave_predito}")

    # 5. Mapear o diagnóstico para as outras informações do SCII
    # Pega a primeira correspondência encontrada no dataset original
    perfil_completo = df_mapa[df_mapa['diagnostico_chave'] == diagnostico_chave_predito].iloc[0].to_dict()

    # Adiciona o texto original e o diagnóstico para clareza
    perfil_final = {
        "texto_original": texto_usuario,
        "diagnostico_predito": perfil_completo
    }

    print(f"Perfil-Verbo completo gerado: {perfil_final}")
    return perfil_final

# --- Ponto de Entrada para Teste ---
if __name__ == "__main__":
    print("\n--- Testando o Motor de Predição de Perfil Arquetípico ---")
    
    # Este texto de exemplo deve ser classificado com base no seu dataset treinado.
    # O resultado dependerá dos exemplos que você forneceu no .csv.
    texto_exemplo = "Eu busco estabilidade e ordem. Quero construir uma base sólida para o meu futuro, com disciplina e responsabilidade. O tempo é meu aliado."
    
    perfil_resultante = obter_perfil_verbo(texto_exemplo)

    if "erro" in perfil_resultante:
        print(f"\nFalha no teste: {perfil_resultante['erro']}")
    else:
        print("\n--- RESULTADO DA TIPIFICAÇÃO EXEMPLO ---")
        for chave, valor in perfil_resultante['diagnostico_predito'].items():
            print(f"- {chave.replace('_', ' ').title()}: {valor}")
        print("-----------------------------------------")
