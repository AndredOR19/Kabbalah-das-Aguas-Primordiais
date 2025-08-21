#!/usr/bin/env python3
"""
Dashboard de Visualização - Monitor Psicossomático Git
"""

import streamlit as st
import pandas as pd
import json
import os
import glob
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Git Psycho Monitor Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Dashboard - Monitor Psicossomático Git")
st.markdown("Análise temporal dos estados psicossomáticos durante commits")

def load_data():
    """Carrega todos os dados psicossomáticos"""
    data_dir = ".gitpsychodata"
    if not os.path.exists(data_dir):
        st.error("Diretório de dados não encontrado. Execute o monitor primeiro.")
        return pd.DataFrame()
    
    files = glob.glob(os.path.join(data_dir, "psychodata_*.json"))
    if not files:
        st.warning("Nenhum dado encontrado. Execute o monitor para coletar dados.")
        return pd.DataFrame()
    
    all_data = []
    for file in sorted(files):
        with open(file, 'r') as f:
            data = json.load(f)
            data['filename'] = os.path.basename(file)
            all_data.append(data)
    
    return pd.json_normalize(all_data)

def create_visualizations(df):
    """Cria visualizações dos dados"""
    if df.empty:
        return
    
    # Preparar dados
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total de Registros", len(df))
    
    with col2:
        if 'metrics.foco' in df.columns:
            avg_foco = df['metrics.foco'].mean()
            st.metric("Foco Médio", f"{avg_foco:.1f}")
    
    with col3:
        if 'metrics.energia' in df.columns:
            avg_energia = df['metrics.energia'].mean()
            st.metric("Energia Média", f"{avg_energia:.1f}")
    
    with col4:
        if 'metrics.humor' in df.columns:
            humor_counts = df['metrics.humor'].value_counts()
            top_humor = humor_counts.index[0]
            st.metric("Humor Predominante", top_humor)
    
    # Gráfico de linha temporal
    st.subheader("📈 Evolução Temporal")
    
    metrics_to_plot = ['metrics.foco', 'metrics.energia', 'metrics.qualidade_sono']
    available_metrics = [m for m in metrics_to_plot if m in df.columns]
    
    if available_metrics:
        fig = go.Figure()
        
        for metric in available_metrics:
            metric_name = metric.replace('metrics.', '')
            fig.add_trace(go.Scatter(
                x=df['timestamp'],
                y=df[metric],
                mode='lines+markers',
                name=metric_name.title()
            ))
        
        fig.update_layout(
            title="Métricas ao Longo do Tempo",
            xaxis_title="Data/Hora",
            yaxis_title="Valor",
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Distribuição de humores
    if 'metrics.humor' in df.columns:
        st.subheader("😊 Distribuição de Humores")
        
        humor_counts = df['metrics.humor'].value_counts()
        fig_pie = px.pie(
            values=humor_counts.values,
            names=humor_counts.index,
            title="Distribuição de Estados Emocionais"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Correlações
    numeric_cols = [col for col in df.columns if col.startswith('metrics.') and df[col].dtype in ['int64', 'float64']]
    if len(numeric_cols) > 1:
        st.subheader("🔗 Correlações entre Métricas")
        
        corr_data = df[numeric_cols].corr()
        fig_corr = px.imshow(
            corr_data,
            labels=dict(color="Correlação"),
            title="Matriz de Correlação",
            color_continuous_scale="RdBu_r"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    
    # Tabela de dados
    st.subheader("📊 Dados Detalhados")
    
    # Preparar dados para exibição
    display_df = df.copy()
    
    # Renomear colunas para melhor visualização
    column_mapping = {
        'timestamp': 'Data/Hora',
        'metrics.foco': 'Foco',
        'metrics.energia': 'Energia',
        'metrics.humor': 'Humor',
        'metrics.qualidade_sono': 'Qualidade do Sono',
        'metrics.cafeina': 'Cafeína',
        'metrics.observacoes': 'Observações'
    }
    
    display_df = display_df.rename(columns=column_mapping)
    
    # Selecionar colunas para exibição
    display_columns = [col for col in column_mapping.values() if col in display_df.columns]
    if display_columns:
        st.dataframe(display_df[display_columns], use_container_width=True)

def main():
    """Função principal do dashboard"""
    st.sidebar.title("⚙️ Configurações")
    
    # Carregar dados
    df = load_data()
    
    if not df.empty:
        # Filtros
        st.sidebar.subheader("📅 Filtros")
        
        # Filtro de data
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            min_date = df['timestamp'].min()
            max_date = df['timestamp'].max()
            
            date_range = st.sidebar.date_input(
                "Período",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date
            )
            
            if len(date_range) == 2:
                mask = (df['timestamp'].dt.date >= date_range[0]) & (df['timestamp'].dt.date <= date_range[1])
                df = df[mask]
        
        # Criar visualizações
        create_visualizations(df)
        
        # Exportar dados
        st.sidebar.subheader("📤 Exportar")
        if st.sidebar.button("Exportar CSV"):
            csv = df.to_csv(index=False)
            st.sidebar.download_button(
                label="Baixar CSV",
                data=csv,
                file_name=f"psychodata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    else:
        st.info("💡 Execute o monitor para coletar dados primeiro:")
        st.code("python git_psycho_monitor/monitor_psico.py")

if __name__ == "__main__":
    main()
