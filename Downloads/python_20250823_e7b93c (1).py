#!/usr/bin/env python3
"""
Script para migrar conteúdo do Blogger para Markdown
Uso: python migracao-blog.py [URL do blog]
"""

import requests
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime

def migrar_blog(url_blog):
    """Função principal para migrar conteúdo do blog"""
    print(f"Iniciando migração do blog: {url_blog}")
    
    # Criar diretório para posts
    if not os.path.exists('posts'):
        os.makedirs('posts')
    
    # Aqui viria o código para extrair posts do Blogger
    # Esta é uma implementação simplificada
    
    posts_exemplo = [
        {
            'titulo': 'Introdução às Águas Primordiais',
            'conteudo': '<p>Este é um post sobre as águas primordiais...</p>',
            'data': '2023-05-15',
            'tags': ['kabbalah', 'águas primordiais', 'misticismo']
        }
    ]
    
    for post in posts_exemplo:
        # Converter HTML para Markdown (simplificado)
        conteudo_md = html_para_markdown(post['conteudo'])
        
        # Criar arquivo Markdown
        nome_arquivo = criar_nome_arquivo(post['titulo'])
        caminho_arquivo = os.path.join('posts', nome_arquivo)
        
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(f"# {post['titulo']}\n\n")
            f.write(f"Data: {post['data']}\n\n")
            f.write(f"Tags: {', '.join(post['tags'])}\n\n")
            f.write(conteudo_md)
        
        print(f"Post migrado: {nome_arquivo}")

def html_para_markdown(html):
    """Conversor simples de HTML para Markdown"""
    # Esta é uma implementação básica - na prática, use uma biblioteca
    markdown = html.replace('<p>', '').replace('</p>', '\n\n')
    markdown = markdown.replace('<strong>', '**').replace('</strong>', '**')
    markdown = markdown.replace('<em>', '*').replace('</em>', '*')
    return markdown

def criar_nome_arquivo(titulo):
    """Cria um nome de arquivo válido a partir do título"""
    nome = titulo.lower()
    nome = nome.replace(' ', '-')
    nome = ''.join(c for c in nome if c.isalnum() or c == '-')
    return nome + '.md'

if __name__ == '__main__':
    # URL do blog do Kabbalah das Águas Primordiais
    url_blog = 'https://kabbalahdasaguasprimordiais.blogspot.com'
    migrar_blog(url_blog)