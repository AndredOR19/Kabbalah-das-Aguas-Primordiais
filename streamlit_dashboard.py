import streamlit as st
import glob
import json
import pandas as pd
from datetime import datetime

st.title("Painel Psicossomático - Kabbalah das Águas Primordiais")

# Busca todos os arquivos JSON
files = sorted(glob.glob(".gitpsychodata/entries/*.json"))

if not files:
    st.warning("Nenhuma entrada psicossomática encontrada. Faça um commit com dados PSICO_JSON primeiro.")
    st.stop()

data = []
for f in files:
    with open(f, "r", encoding="utf-8") as jf:
        try:
            entry = json.load(jf)
            data.append(entry)
        except:
            continue

df = pd.DataFrame(data)

# Convertendo timestamp para datetime
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce')
else:
    df["timestamp"] = pd.NaT

st.write("### Dados brutos")
st.dataframe(df)

# Gráfico de HR, HRV e foco ao longo do tempo
if {"timestamp", "hr", "hrv", "focus"}.issubset(df.columns):
    st.write("### Evolução dos sinais vitais")
    df_plot = df.dropna(subset=["timestamp", "hr", "hrv", "focus"])
    df_plot = df_plot.sort_values("timestamp")
    st.line_chart(df_plot.set_index("timestamp")[["hr", "hrv", "focus"]])
else:
    st.info("Dados insuficientes para gráfico de sinais vitais.")

# Humor detectado
if "mood" in df.columns or "mood_detected" in df.columns:
    st.write("### Humor ao longo do tempo")
    mood_col = "mood" if "mood" in df.columns else "mood_detected"
    mood_counts = df[mood_col].value_counts()
    st.bar_chart(mood_counts)
else:
    st.info("Nenhum dado de humor disponível.")

# Análise de padrões por dia da semana
if "timestamp" in df.columns:
    st.write("### Padrões por dia da semana")
    df["day_of_week"] = df["timestamp"].dt.day_name()
    daily_patterns = df.groupby("day_of_week").agg({
        "hr": "mean",
        "hrv": "mean",
        "focus": "mean"
    }).round(2)
    st.dataframe(daily_patterns)

# Estatísticas gerais
st.write("### Estatísticas gerais")
if not df.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de registros", len(df))
    with col2:
        if "hr" in df.columns:
            st.metric("HR médio", f"{df['hr'].mean():.1f}")
    with col3:
        if "hrv" in df.columns:
            st.metric("HRV médio", f"{df['hrv'].mean():.1f}")

# Filtros interativos
st.sidebar.header("Filtros")
if "mood" in df.columns:
    selected_mood = st.sidebar.multiselect(
        "Filtrar por humor",
        options=df["mood"].unique(),
        default=df["mood"].unique()
    )
    filtered_df = df[df["mood"].isin(selected_mood)]
    st.write("### Dados filtrados por humor")
    st.dataframe(filtered_df)
