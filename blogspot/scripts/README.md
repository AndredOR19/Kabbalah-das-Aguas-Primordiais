# Scripts de Arquivamento do Blog

Este diretório contém scripts e ferramentas para automatizar o arquivamento do blog Kabbalah das Águas Primordiais.

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure o arquivo `config.json` com suas preferências:
- URLs do blog
- Configurações de imagem
- Categorias e tags padrão
- Opções de backup

## Uso

### Arquivar Novo Post
```bash
python blog_archiver.py --post <URL_DO_POST>
```

### Arquivar Todo o Blog
```bash
python blog_archiver.py --archive-all
```

### Atualizar Índice
```bash
python blog_archiver.py --update-index
```

## Funcionalidades

- Download automático de posts
- Conversão para markdown
- Download e otimização de imagens
- Geração de índice
- Sistema de tags e categorias
- Backup automático
- Múltiplos formatos de exportação

## Estrutura de Arquivos

```
scripts/
├── blog_archiver.py     # Script principal
├── requirements.txt     # Dependências Python
├── config.json         # Configurações
└── README.md          # Esta documentação
```

## Metadados

Os posts são salvos com metadados YAML:
```yaml
---
title: Título do Post
date: 2025-08-01
tags: [tag1, tag2]
categories: [cat1, cat2]
author: Nome do Autor
original_url: URL_ORIGINAL
---
```

## Backup

O script mantém backups automáticos:
- Frequência configurável
- Rotação de versões
- Compressão automática

## Contribuindo

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Envie um pull request
