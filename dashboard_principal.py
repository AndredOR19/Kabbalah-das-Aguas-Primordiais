#!/usr/bin/env python3
"""
Dashboard Principal - Kabbalah das Águas Primordiais
Sistema integrado de navegação e controle para todo o ecossistema
"""

import streamlit as st
import pandas as pd
import json
import os
import requests
from datetime import datetime
import subprocess
import plotly.graph_objects as go
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Kabbalah das Águas Primordiais - Dashboard Principal",
    page_icon="🌊",
    layout="wide"
)

# CSS personalizado aprimorado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 2rem;
        font-family: 'Georgia', serif;
    }
    .card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem;
        color: white;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: white;
    }
    .sefirah-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem;
        color: white;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🌊 Kabbalah das Águas Primordiais</h1>', unsafe_allow_html=True)
st.markdown("### Dashboard Principal - Sistema Integrado do Corpo do Verbo")

# Sidebar para navegação
st.sidebar.title("🧭 Navegação")
pagina = st.sidebar.selectbox(
    "Escolha o módulo:",
    ["🏠 Dashboard Principal", 
     "📊 Psicossomático", 
     "🔮 Oráculo", 
     "📈 Análise SCII", 
     "🎭 Perfil Verbo",
     "⚙️ Configurações"]
)

# Funções aprimoradas do sistema
@st.cache_data
def carregar_dados_sistema():
    """Carrega e processa dados do sistema com análise detalhada"""
    dados = {
        'total_registros': 0,
        'ultima_atualizacao': None,
        'modulos_ativos': [],
        'estatisticas_detalhadas': {},
        'arquivos_por_tipo': {}
    }
    
    # Análise detalhada de arquivos
    arquivos_json = []
    arquivos_md = []
    arquivos_py = []
    
    for root, dirs, files in os.walk('.', topdown=True):
        # Evitar pastas de cache e git
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
        
        for file in files:
            filepath = os.path.join(root, file)
            if file.endswith('.json'):
                arquivos_json.append(filepath)
                dados['arquivos_por_tipo']['JSON'] = len(arquivos_json)
            elif file.endswith('.md'):
                arquivos_md.append(filepath)
                dados['arquivos_por_tipo']['Markdown'] = len(arquivos_md)
            elif file.endswith('.py'):
                arquivos_py.append(filepath)
                dados['arquivos_por_tipo']['Python'] = len(arquivos_py)
    
    # Estatísticas detalhadas
    dados['total_registros'] = len(arquivos_json) + len(arquivos_md) + len(arquivos_py)
    dados['ultima_atualizacao'] = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Verificar módulos ativos com status
    modulos = []
    servicos_status = {}
    
    # Verificar API Flask
    if os.path.exists('api.py'):
        try:
            response = requests.get('http://localhost:5000', timeout=2)
            servicos_status['API Flask'] = '✅ Online' if response.status_code == 200 else '⚠️ Offline'
        except:
            servicos_status['API Flask'] = '❌ Offline'
        modulos.append("API Flask")
    
    # Verificar outros módulos
    modulos_verificacao = {
        'Dashboard Streamlit': 'streamlit_dashboard.py',
        'Bot Telegram': 'bot.py',
        'SCII Database': 'scii_database.js',
        'Sistema Astrológico': 'sistema_correspondencias_astrologicas.py',
        'Analisador Transit': 'analise_transitos.py'
    }
    
    for nome, arquivo in modulos_verificacao.items():
        if os.path.exists(arquivo):
            modulos.append(nome)
            servicos_status[nome] = '✅ Disponível'
    
    dados['modulos_ativos'] = modulos
    dados['estatisticas_detalhadas'] = servicos_status
    
    return dados

@st.cache_data
def carregar_dados_astrologicos():
    """Carrega dados astrológicos se disponíveis"""
    dados_astrologicos = []
    if os.path.exists('dados_astrologicos'):
        for arquivo in os.listdir('dados_astrologicos'):
            if arquivo.endswith('.json'):
                try:
                    with open(os.path.join('dados_astrologicos', arquivo), 'r', encoding='utf-8') as f:
                        dados = json.load(f)
                        dados_astrologicos.append(dados)
                except:
                    continue
    return dados_astrologicos

def criar_grafico_sefirot():
    """Cria visualização interativa da Árvore da Vida"""
    sefirot = ['Keter', 'Chokmah', 'Binah', 'Chesed', 'Gevurah', 'Tiferet', 
               'Netzach', 'Hod', 'Yesod', 'Malkuth']
    
    fig = go.Figure()
    
    # Adicionar nós das sefirot
    for i, sefirah in enumerate(sefirot):
        x = [0, 1, 2, 0, 1, 1, 0, 2, 1, 1][i]
        y = [3, 2, 2, 1, 1, 0, -1, -1, -2, -3][i]
        
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=30, color=f'hsv({i*36}, 70%, 90%)'),
            text=sefirah,
            textposition="center",
            name=sefirah,
            hovertemplate=f'<b>{sefirah}</b><br>Posição: ({x}, {y})<extra></extra>'
        ))
    
    # Adicionar conexões
    conexoes = [(0,1), (0,2), (1,3), (2,4), (1,2), (3,5), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]
    for start, end in conexoes:
        x0, y0 = [0, 1, 2, 0, 1, 1, 0, 2, 1, 1][start], [3, 2, 2, 1, 1, 0, -1, -1, -2, -3][start]
        x1, y1 = [0, 1, 2, 0, 1, 1, 0, 2, 1, 1][end], [3, 2, 2, 1, 1, 0, -1, -1, -2, -3][end]
        
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y0, y1],
            mode='lines',
            line=dict(color='gray', width=2),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    fig.update_layout(
        title="🌳 Árvore da Vida - Sefirot",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=600
    )
    
    return fig

# Dashboard Principal
if pagina == "🏠 Dashboard Principal":
    st.header("📊 Visão Geral do Sistema")
    
    dados_sistema = carregar_dados_sistema()
    
    # Cards de métricas aprimorados
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📁 Total Arquivos</h3>
            <h2>{dados_sistema['total_registros']}</h2>
            <p>arquivos processados</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🔄 Atualizado</h3>
            <h2>{dados_sistema['ultima_atualizacao']}</h2>
            <p>última sincronização</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>⚡ Módulos</h3>
            <h2>{len(dados_sistema['modulos_ativos'])}</h2>
            <p>sistemas ativos</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🔮 Sefirot</h3>
            <h2>10</h2>
            <p>emanações divinas</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualização da Árvore da Vida
    st.subheader("🌳 Árvore da Vida - Sefirot")
    fig_sefirot = criar_grafico_sefirot()
    st.plotly_chart(fig_sefirot, use_container_width=True)
    
    # Status dos serviços
    st.subheader("🔍 Status dos Serviços")
    for servico, status in dados_sistema['estatisticas_detalhadas'].items():
        cor = "green" if "✅" in status else "orange" if "⚠️" in status else "red"
        st.markdown(f"**{servico}**: :{cor}[{status}]")
    
    # Estatísticas por tipo de arquivo
    if dados_sistema['arquivos_por_tipo']:
        st.subheader("📊 Distribuição de Arquivos")
        tipos = list(dados_sistema['arquivos_por_tipo'].keys())
        quantidades = list(dados_sistema['arquivos_por_tipo'].values())
        
        fig_pizza = px.pie(
            values=quantidades, 
            names=tipos,
            title="Tipos de Arquivos no Sistema",
            color_discrete_map={'JSON': '#00CC96', 'Markdown': '#636EFA', 'Python': '#FFA15A'}
        )
        st.plotly_chart(fig_pizza, use_container_width=True)

# Dashboard Psicossomático
elif pagina == "📊 Psicossomático":
    st.header("📊 Dashboard Psicossomático")
    
    # Importar e executar o dashboard existente
    try:
        exec(open('streamlit_dashboard.py').read())
    except Exception as e:
        st.error(f"Erro ao carregar dashboard psicossomático: {e}")
        st.info("Execute: streamlit run streamlit_dashboard.py")

# Oráculo
elif pagina == "🔮 Oráculo":
    st.header("🔮 Sistema Oracular")
    
    st.info("Integração com o Oráculo Encarnado do Verbo")
    
    # Formulário de consulta aprimorado
    with st.form("formulario_oraculo"):
        col1, col2 = st.columns(2)
        with col1:
            tema = st.selectbox("Escolha o tema:", ["Cura Emocional", "Propósito de Vida", "Relacionamentos", "Trabalho"])
        with col2:
            intensidade = st.slider("Intensidade da prática:", 1, 10, 5)
        
        pergunta = st.text_area("Digite sua questão:", placeholder="Ex: Qual é o caminho para minha cura emocional?")
        submit = st.form_submit_button("🔮 Consultar Oráculo")
        
        if submit and pergunta:
            try:
                # Simulação de consulta aprimorada
                resposta = {
                    "tema": tema,
                    "caminho": f"{tema} - {['Tiferet', 'Yesod', 'Netzach', 'Hod'][hash(tema) % 4]}",
                    "pratica": f"Meditação focada em {tema.lower()}",
                    "duracao": f"{intensidade * 3} minutos",
                    "foco": f"Respiração consciente e {tema.lower()}",
                    "intensidade": intensidade
                }
                st.success("✅ Consulta realizada com sucesso!")
                
                # Exibir resposta em cards
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div class="card">
                        <h3>🎯 Caminho</h3>
                        <p>{resposta['caminho']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div class="card">
                        <h3>⏱️ Duração</h3>
                        <p>{resposta['duracao']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.json(resposta)
            except Exception as e:
                st.error(f"Erro na consulta: {e}")

# Análise SCII
elif pagina == "📈 Análise SCII":
    st.header("📈 Análise SCII")
    
    st.info("Sistema de Correspondências Cabalísticas Integradas")
    
    # Carregar dados SCII se disponíveis
    if os.path.exists('scii_database.js'):
        try:
            with open('scii_database.js', 'r') as f:
                conteudo = f.read()
                st.code(conteudo[:500] + "...", language="javascript")
        except:
            st.warning("Não foi possível carregar a base SCII")
    
    # Simulação de análise SCII
    st.subheader("📊 Análise de Correspondências")
    correspondencias = {
        "Letras Hebraicas": 22,
        "Sefirot": 10,
        "Caminhos": 32,
        "Arquétipos": 12
    }
    
    fig_bar = px.bar(
        x=list(correspondencias.keys()),
        y=list(correspondencias.values()),
        title="Correspondências Cabalísticas",
        labels={"x": "Categoria", "y": "Quantidade"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Perfil Verbo
elif pagina == "🎭 Perfil Verbo":
    st.header("🎭 Tipificação de Perfil Verbo")
    
    st.info("Sistema de classificação de perfis baseado no Verbo")
    
    # Formulário de tipificação aprimorado
    with st.form("formulario_perfil"):
        texto = st.text_area(
            "Descreva-se:", 
            placeholder="Fale sobre seus desejos, medos, aspirações e padrões de comportamento...",
            height=150
        )
        
        col1, col2 = st.columns(2)
        with col1:
            contexto = st.selectbox("Contexto:", ["Pessoal", "Profissional", "Espiritual"])
        with col2:
            profundidade = st.select_slider("Profundidade:", options=["Superficial", "Moderada", "Profunda"])
        
        submit = st.form_submit_button("🔍 Analisar Perfil")
        
        if submit and texto:
            try:
                # Simulação de análise aprimorada
                perfil = {
                    "arquetipo": ["Construtor", "Explorador", "Curador", "Mestre"][hash(texto) % 4],
                    "sefirah": ["Yesod", "Tiferet", "Netzach", "Hod"][hash(texto) % 4],
                    "elemento": ["Terra", "Água", "Fogo", "Ar"][hash(texto) % 4],
                    "pratica": ["Respiração raiz", "Meditação cardíaca", "Visualização criativa", "Mantra sonoro"][hash(texto) % 4],
                    "contexto": contexto,
                    "profundidade": profundidade,
                    "texto_analisado": len(texto.split())
                }
                
                st.success("✅ Perfil analisado com sucesso!")
                
                # Exibir perfil em cards
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"""
                    <div class="sefirah-card">
                        <h3>🎭 Arquetipo</h3>
                        <p>{perfil['arquetipo']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div class="sefirah-card">
                        <h3>✨ Sefirah</h3>
                        <p>{perfil['sefirah']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                with col3:
                    st.markdown(f"""
                    <div class="sefirah-card">
                        <h3>🌍 Elemento</h3>
                        <p>{perfil['elemento']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.json(perfil)
            except Exception as e:
                st.error(f"Erro na análise: {e}")

# Configurações
elif pagina == "⚙️ Configurações":
    st.header("⚙️ Configurações do Sistema")
    
    st.info("Central de configurações e integrações")
    
    # Status dos serviços
    st.subheader("🔍 Status dos Serviços")
    
    servicos = {
        "API Flask": "http://localhost:5000",
        "Dashboard Streamlit": "http://localhost:8501",
        "Bot Telegram": "Verificar bot.py",
        "SCII Database": "scii_database.js"
    }
    
    col1, col2 = st.columns(2)
    for i, (servico, url) in enumerate(servicos.items()):
        with col1 if i % 2 == 0 else col2:
            if st.button(f"🔄 Verificar {servico}", key=servico):
                st.info(f"Serviço: {servico} - {url}")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ Informações")
st.sidebar.markdown("**Versão:** 2.0.0 - Dashboard Aprimorado")
st.sidebar.markdown("**Autor:** Karuv Beni EL")
st.sidebar.markdown("**Licença:** CC BY-NC-SA 4.0")
st.sidebar.markdown("**Atualização:** Dashboard com visualizações interativas")
