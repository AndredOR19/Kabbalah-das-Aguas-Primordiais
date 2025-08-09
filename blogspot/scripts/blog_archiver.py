#!/usr/bin/env python3
"""
Blog Archiver - Kabbalah das Águas Primordiais
Script para automatizar o download e arquivamento do conteúdo do blog
Versão 2.0 - Com suporte a imagens e extração melhorada de conteúdo
"""

import os
import re
import json
import time
import requests
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse

class BlogArchiver:
    def __init__(self, base_url: str, output_dir: str):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.metadata_file = self.output_dir / 'metadata.json'
        self.media_dir = self.output_dir / 'midia'
        self.media_dir.mkdir(parents=True, exist_ok=True)
        self.metadata = self._load_metadata()

    def _load_metadata(self) -> Dict:
        """Carrega ou cria o arquivo de metadados"""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'last_update': datetime.now().isoformat(),
            'posts': [],
            'pages': [],
            'tags': {},
            'categories': {},
            'media': {}
        }

    def _save_metadata(self):
        """Salva o arquivo de metadados"""
        self.metadata['last_update'] = datetime.now().isoformat()
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)

    def _sanitize_filename(self, filename: str) -> str:
        """Remove caracteres inválidos do nome do arquivo"""
        return re.sub(r'[^\w\s-]', '', filename).strip().lower().replace(' ', '-')

    def _download_image(self, img_url: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Download uma imagem e salva no diretório de mídia
        Retorna: (caminho_relativo, caminho_absoluto) ou (None, None) se falhar
        """
        try:
            # Gera um nome único para a imagem
            img_hash = hashlib.md5(img_url.encode()).hexdigest()
            ext = os.path.splitext(urlparse(img_url).path)[1] or '.jpg'
            img_filename = f"{img_hash}{ext}"
            img_path = self.media_dir / img_filename
            
            # Se já existe, retorna o caminho
            if img_path.exists():
                return f"midia/{img_filename}", str(img_path)
            
            # Faz o download
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            
            # Salva a imagem
            with open(img_path, 'wb') as f:
                f.write(response.content)
            
            return f"midia/{img_filename}", str(img_path)
            
        except Exception as e:
            print(f"Erro ao baixar imagem {img_url}: {str(e)}")
            return None, None

    def _html_to_markdown(self, html_content: str, base_url: str) -> str:
        """Converte HTML para Markdown com suporte a imagens"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove scripts e estilos
        for tag in soup(['script', 'style']):
            tag.decompose()
        
        # Processa imagens
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src:
                # Converte URL relativa para absoluta
                img_url = urljoin(base_url, src)
                # Faz o download da imagem
                rel_path, _ = self._download_image(img_url)
                if rel_path:
                    # Atualiza o src da imagem para o caminho local
                    img['src'] = f"/{rel_path}"
        
        # Converte para texto mantendo alguns elementos HTML
        content = []
        for elem in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'a', 'ul', 'ol', 'li']):
            if elem.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                content.append(f"{'#' * int(elem.name[1])} {elem.get_text().strip()}\n")
            elif elem.name == 'p':
                content.append(f"{elem.get_text().strip()}\n")
            elif elem.name == 'img':
                src = elem.get('src', '')
                alt = elem.get('alt', 'imagem')
                if src:
                    content.append(f"![{alt}]({src})\n")
            elif elem.name == 'a':
                href = elem.get('href', '')
                text = elem.get_text().strip()
                if href:
                    content.append(f"[{text}]({href})")
            elif elem.name == 'ul':
                for li in elem.find_all('li', recursive=False):
                    content.append(f"- {li.get_text().strip()}\n")
            elif elem.name == 'ol':
                for i, li in enumerate(elem.find_all('li', recursive=False), 1):
                    content.append(f"{i}. {li.get_text().strip()}\n")
        
        return '\n'.join(content)

    def _extract_tags_from_content(self, content: str) -> List[str]:
        """Extrai tags do conteúdo baseado em palavras-chave"""
        keywords = [
            'Kabbalah', 'SCII', 'Corpo do Verbo', 'Oráculo',
            'Meditação', 'Práticas', 'Rituais', 'Águas Primordiais',
            'Consciência', 'Energia', 'Templo', 'Merkavah'
        ]
        
        tags = []
        content_lower = content.lower()
        for keyword in keywords:
            if keyword.lower() in content_lower:
                tags.append(keyword)
        
        return list(set(tags))

    def _get_post_metadata(self, url: str, soup: BeautifulSoup) -> Dict:
        """Extrai metadados de um post"""
        # Título
        title_elem = soup.find('h3', class_='post-title') or soup.find('h1')
        title = title_elem.get_text().strip() if title_elem else 'Sem título'
        
        # Data
        date_elem = soup.find(class_='date-header') or soup.find('time')
        date_str = datetime.now().strftime('%Y-%m-%d')
        if date_elem:
            date_text = date_elem.get_text().strip()
            try:
                # Tenta extrair a data do texto
                match = re.search(r'(\d{1,2}).*?(\d{4})', date_text)
                if match:
                    day, year = match.groups()
                    month = datetime.now().month  # Usa o mês atual como fallback
                    date_str = f"{year}-{month:02d}-{day.zfill(2)}"
            except:
                pass
        
        # Conteúdo
        content_elem = soup.find(class_='post-body') or soup.find('article')
        content = ''
        if content_elem:
            content = self._html_to_markdown(str(content_elem), url)
        
        # Tags e categorias
        tags = self._extract_tags_from_content(content)
        categories = ['Kabbalah', 'Estudos', 'Práticas'] if 'prática' in content.lower() else ['Kabbalah', 'Estudos']
        
        return {
            'title': title,
            'date': date_str,
            'url': url,
            'tags': tags,
            'categories': categories,
            'author': 'André de Oliveira Rodrigues',
            'content': content
        }

    def archive_post(self, url: str):
        """Arquiva um post específico"""
        try:
            print(f"\nArquivando post: {url}")
            
            # Faz o download da página
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extrai metadados e conteúdo
            post_data = self._get_post_metadata(url, soup)
            
            # Cria diretórios
            date = datetime.strptime(post_data['date'], '%Y-%m-%d')
            post_dir = self.output_dir / 'posts' / str(date.year) / f"{date.month:02d}"
            post_dir.mkdir(parents=True, exist_ok=True)
            
            # Salva o post
            filename = f"{self._sanitize_filename(post_data['title'])}.md"
            filepath = post_dir / filename
            
            print(f"Salvando em: {filepath}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self._create_post_markdown(post_data))
            
            # Atualiza metadados
            if url not in [p['url'] for p in self.metadata['posts']]:
                self.metadata['posts'].append({
                    'url': url,
                    'title': post_data['title'],
                    'date': post_data['date'],
                    'file': str(filepath),
                    'tags': post_data['tags'],
                    'categories': post_data['categories']
                })
                
                # Atualiza contagem de tags
                for tag in post_data['tags']:
                    self.metadata['tags'][tag] = self.metadata['tags'].get(tag, 0) + 1
            
            self._save_metadata()
            print(f"Post arquivado com sucesso: {post_data['title']}")
            
        except Exception as e:
            print(f"Erro ao arquivar {url}: {str(e)}")

    def _create_post_markdown(self, post: Dict) -> str:
        """Cria o conteúdo markdown para um post"""
        return f"""---
title: {post['title']}
date: {post['date']}
tags: {', '.join(post['tags'])}
categories: {', '.join(post['categories'])}
author: {post['author']}
original_url: {post['url']}
---

{post['content']}

---
*Este post foi arquivado automaticamente do [blog original]({post['url']})*
"""

    def update_index(self):
        """Atualiza o arquivo de índice"""
        index_content = """# Índice do Blog

## Posts Recentes
"""
        # Ordenar posts por data
        sorted_posts = sorted(
            self.metadata['posts'],
            key=lambda x: x['date'],
            reverse=True
        )
        
        # Adiciona posts recentes
        for post in sorted_posts[:10]:  # Últimos 10 posts
            tags = f" [*{', '.join(post['tags'])}*]" if post['tags'] else ""
            index_content += f"- [{post['title']}]({post['file']}){tags}\n"
        
        # Adiciona estatísticas
        index_content += "\n## Estatísticas\n"
        index_content += f"- Total de Posts: {len(self.metadata['posts'])}\n"
        index_content += f"- Última Atualização: {self.metadata['last_update']}\n"
        
        # Adiciona nuvem de tags
        if self.metadata['tags']:
            index_content += "\n## Tags\n"
            sorted_tags = sorted(
                self.metadata['tags'].items(),
                key=lambda x: x[1],
                reverse=True
            )
            for tag, count in sorted_tags:
                index_content += f"- {tag} ({count})\n"
        
        with open(self.output_dir / 'index.md', 'w', encoding='utf-8') as f:
            f.write(index_content)

def main():
    archiver = BlogArchiver(
        'https://kabbalahdasaguasprimordiais.blogspot.com',
        '/home/andre/O corpo do verbo/O-Corpo-do-Verbo--4/blogspot'
    )
    
    # Exemplo de uso
    archiver.archive_post('https://kabbalahdasaguasprimordiais.blogspot.com/2025/08/genese-da-engenharia-do-verbo.html')
    archiver.update_index()

if __name__ == '__main__':
    from blog_archiver import BlogArchiver

    archiver = BlogArchiver(
        'https://kabbalahdasaguasprimordiais.blogspot.com',
        'caminho/para/saida'
    )

    # Arquiva um post específico
    archiver.archive_post('https://kabbalahdasaguasprimordiais.blogspot.com/2025/08/genese-da-engenharia-do-verbo.html')

    # Atualiza o índice
    archiver.update_index()
