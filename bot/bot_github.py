#!/usr/bin/env python3
"""
Mestre Digital - Integração com GitHub Issues
Responde automaticamente a issues e comentários no GitHub
"""

import openai
import json
import os
import sys
from github import Github

# Configurações
REPOSITORY = os.getenv('REPOSITORY')
ISSUE_NUMBER = int(os.getenv('ISSUE_NUMBER', 0))
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Inicializar clientes
g = Github(GITHUB_TOKEN)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Carregar configurações
with open('bot/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

with open('base_conhecimento.json', 'r', encoding='utf-8') as f:
    base_conhecimento = json.load(f)

def carregar_contexto_instituto():
    """Carrega todo o contexto do instituto"""
    contexto = []
    
    # Adicionar base de conhecimento
    contexto.append("=== BASE DE CONHECIMENTO DO INSTITUTO ===")
    contexto.append(json.dumps(base_conhecimento, ensure_ascii=False, indent=2))
    
    # Adicionar configurações do mestre
    contexto.append("\n=== CONFIGURAÇÃO DO MESTRE DIGITAL ===")
    contexto.append(json.dumps(config, ensure_ascii=False, indent=2))
    
    return "\n".join(contexto)

def gerar_resposta_github(pergunta, contexto_issue=None):
    """Gera resposta específica para issues do GitHub"""
    
    contexto_instituto = carregar_contexto_instituto()
    
    system_prompt = f"""
    Você é o Mestre Digital do Instituto Águas Primordiais, respondendo automaticamente a issues no GitHub.
    
    {config['personalidade']}
    
    {contexto_instituto}
    
    INSTRUÇÕES IMPORTANTES:
    - Responda de forma clara, profunda e espiritualmente alinhada
    - Use linguagem acessível mas mantendo a profundidade kabbalística
    - Seja acolhedor e orientador
    - Inclua referências aos ensinamentos quando relevante
    - Mantenha um tom que combine sabedoria ancestral com linguagem contemporânea
    
    FORMATO DA RESPOSTA:
    - Comece com uma saudação espiritual
    - Desenvolva a resposta com profundidade
    - Finalize com uma bênção ou orientação prática
    """
    
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    if contexto_issue:
        messages.append({"role": "system", "content": f"Contexto da issue: {contexto_issue}"})
    
    messages.append({"role": "user", "content": pergunta})
    
    response = client.chat.completions.create(
        model=config.get('modelo', 'gpt-4o-mini'),
        messages=messages,
        max_tokens=config.get('max_tokens', 1500),
        temperature=config.get('temperature', 0.7)
    )
    
    return response.choices[0].message.content

def responder_issue_github():
    """Responde automaticamente a uma issue do GitHub"""
    
    if not all([REPOSITORY, ISSUE_NUMBER, GITHUB_TOKEN]):
        print("Variáveis de ambiente não configuradas corretamente")
        return
    
    try:
        # Obter repositório e issue
        repo = g.get_repo(REPOSITORY)
        issue = repo.get_issue(number=ISSUE_NUMBER)
        
        # Preparar contexto
        contexto = f"""
        Título: {issue.title}
        Autor: {issue.user.login}
        Tipo: {'Issue' if issue.pull_request is None else 'Pull Request'}
        Labels: {[label.name for label in issue.labels]}
        """
        
        # Gerar resposta
        resposta = gerar_resposta_github(issue.body or issue.title, contexto)
        
        # Adicionar resposta como comentário
        issue.create_comment(f"🌊 **Resposta do Mestre Digital** 🌊\n\n{resposta}\n\n---\n*Resposta gerada automaticamente pelo Mestre Digital do Instituto Águas Primordiais*")
        
        print(f"✅ Resposta enviada para a issue #{ISSUE_NUMBER}")
        
    except Exception as e:
        print(f"❌ Erro ao responder issue: {e}")

def responder_comentario_github():
    """Responde automaticamente a um comentário no GitHub"""
    
    if not all([REPOSITORY, GITHUB_TOKEN]):
        print("Variáveis de ambiente não configuradas corretamente")
        return
    
    try:
        # Obter repositório e último comentário
        repo = g.get_repo(REPOSITORY)
        
        # Para simplificar, vamos responder à última issue aberta
        issues = repo.get_issues(state='open')
        if issues.totalCount > 0:
            issue = issues[0]
            
            # Obter último comentário
            comments = list(issue.get_comments())
            if comments:
                ultimo_comentario = comments[-1]
                
                # Gerar resposta
                resposta = gerar_resposta_github(ultimo_comentario.body, f"Comentário de {ultimo_comentario.user.login}")
                
                # Adicionar resposta
                issue.create_comment(f"🌊 **Resposta do Mestre Digital** 🌊\n\n{resposta}\n\n---\n*Resposta gerada automaticamente*")
                
                print(f"✅ Resposta enviada para o comentário na issue #{issue.number}")
        
    except Exception as e:
        print(f"❌ Erro ao responder comentário: {e}")

def testar_resposta(pergunta):
    """Testa a resposta do mestre localmente"""
    resposta = gerar_resposta_github(pergunta)
    print(f"\n🌊 PERGUNTA: {pergunta}")
    print(f"\n🌊 RESPOSTA:\n{resposta}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Modo teste
        testar_resposta("Qual é a importância das Águas Primordiais na Kabbalah?")
    elif ISSUE_NUMBER > 0:
        # Modo produção - responder issue
        responder_issue_github()
    else:
        print("Use: python bot.py test  # para testar localmente")
        print("Ou configure as variáveis de ambiente para responder issues do GitHub")
