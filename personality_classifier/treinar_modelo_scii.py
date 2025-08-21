# -*- coding: utf-8 -*-
"""
SCII - Treinamento do Motor de Tipificação Arquetípica

Este script adapta o fluxo de trabalho do classificador de personalidade
original para treinar um novo modelo baseado no dataset do Corpo do Verbo.

O processo inclui:
1. Carregar o dataset SCII.
2. Limpar e pré-processar os textos.
3. Vetorizar os textos usando CountVectorizer.
4. Codificar os rótulos (diagnósticos-chave).
5. Balancear o dataset com SMOTE.
6. Treinar um modelo RandomForestClassifier.
7. Salvar o modelo treinado e o vetorizador para uso na API.

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 12 de Agosto de 2025
"""

import pandas as pd
import re
import pickle
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report

# --- 1. FUNÇÃO DE LIMPEZA DE TEXTO ---
def limpar_texto(textos):
    """
Aplica uma série de limpezas nos textos de entrada.
    """
    dados_limpos = []
    lemmatizer = WordNetLemmatizer()
    
    for texto in textos:
        # Remove URLs e caracteres especiais
        texto = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', texto)
        texto = re.sub(r'[^a-zA-Z\s]', '', texto, re.I|re.A)
        texto = texto.lower()
        
        # Lematização
        palavras = texto.split()
        palavras_lematizadas = [lemmatizer.lemmatize(palavra) for palavra in palavras]
        texto_limpo = " ".join(palavras_lematizadas)
        
        dados_limpos.append(texto_limpo)
        
    return dados_limpos

# --- 2. FUNÇÃO PRINCIPAL DE TREINAMENTO ---
def treinar_e_salvar_modelo(caminho_dataset):
    """
    Executa o pipeline completo de treinamento e salva os artefatos.
    """
    print("--- Iniciando Treinamento do Modelo SCII ---")

    # Carregar o dataset SCII
    try:
        df = pd.read_csv(caminho_dataset)
        print(f"Dataset '{caminho_dataset}' carregado com sucesso. {len(df)} registros encontrados.")
    except FileNotFoundError:
        print(f"Erro: Dataset não encontrado em '{caminho_dataset}'. Certifique-se de que o arquivo existe.")
        return

    # Define a coluna alvo (o que queremos prever)
    coluna_alvo = 'diagnostico_chave'
    print(f"Coluna alvo para classificação: '{coluna_alvo}'")

    # Limpar os textos
    print("Limpando e pré-processando os textos...")
    df['texto_limpo'] = limpar_texto(df['texto'])

    # Vetorizar os textos
    print("Vetorizando os textos com CountVectorizer...")
    vectorizer = CountVectorizer(max_features=5000, ngram_range=(1, 2)) # Usando unigramas e bigramas
    X = vectorizer.fit_transform(df['texto_limpo']).toarray()

    # Codificar os rótulos
    print("Codificando os rótulos da coluna alvo...")
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(df[coluna_alvo])

    # Balancear o dataset com SMOTE
    # SMOTE precisa de pelo menos 2 amostras por classe para funcionar
    if df[coluna_alvo].nunique() > 1 and all(df[coluna_alvo].value_counts() > 1):
        print("Balanceando o dataset com SMOTE...")
        smote = SMOTE(random_state=42)
        X_sm, y_sm = smote.fit_resample(X, y)
    else:
        print("Aviso: SMOTE não aplicado. Número de amostras ou classes insuficiente.")
        X_sm, y_sm = X, y

    # Dividir em treino e teste
    print("Dividindo os dados em conjuntos de treino e teste...")
    X_train, X_test, y_train, y_test = train_test_split(X_sm, y_sm, test_size=0.2, random_state=42)

    # Treinar o modelo RandomForest
    print("Treinando o modelo RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=150, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)

    # Avaliar o modelo
    print("\nAvaliando o modelo treinado...")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_, zero_division=0))

    # Salvar os artefatos (modelo, vetorizador e codificador de rótulos)
    print("Salvando os artefatos do modelo...")
    with open('personality_classifier/scii_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('personality_classifier/scii_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    with open('personality_classifier/scii_label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)

    print("\n--- Treinamento Concluído! ---")
    print("Modelo salvo em: personality_classifier/scii_model.pkl")
    print("Vetorizador salvo em: personality_classifier/scii_vectorizer.pkl")
    print("Codificador de Rótulos salvo em: personality_classifier/scii_label_encoder.pkl")

# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    caminho_do_dataset = 'personality_classifier/scii_dataset_template.csv'
    treinar_e_salvar_modelo(caminho_do_dataset)
