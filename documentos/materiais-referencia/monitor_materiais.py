# -*- coding: utf-8 -*-

"""
Monitor de Materiais de Referência
Sistema para acompanhar e processar materiais adicionados pelo usuário

Este script monitora as pastas de materiais e gera relatórios sobre o que foi adicionado,
facilitando o processo de criação da apostila integrada.
"""

import os
import datetime
from typing import Dict, List
import json

class MonitorMateriais:
    """Classe para monitorar e catalogar materiais de referência"""
    
    def __init__(self, diretorio_base: str = "/home/andre/Kabbalah-das-Aguas-Primordiais/documentos/materiais-referencia"):
        self.diretorio_base = diretorio_base
        self.pastas_monitoradas = [
            "apostilas-astrologia",
            "textos-correspondencias", 
            "rituais-astrologicos",
            "ciclos-planetarios",
            "cabala-astrologica",
            "referencias-historicas"
        ]
        self.arquivo_catalogo = os.path.join(diretorio_base, "catalogo_materiais.json")
    
    def escanear_materiais(self) -> Dict:
        """Escaneia todas as pastas e cataloga os materiais encontrados"""
        
        catalogo = {
            "data_escaneamento": datetime.datetime.now().isoformat(),
            "total_arquivos": 0,
            "materiais_por_categoria": {},
            "arquivos_novos": [],
            "resumo_conteudo": {}
        }
        
        # Carregar catálogo anterior se existir
        catalogo_anterior = self._carregar_catalogo_anterior()
        arquivos_anteriores = set()
        if catalogo_anterior:
            for categoria, arquivos in catalogo_anterior.get("materiais_por_categoria", {}).items():
                arquivos_anteriores.update([arq["caminho"] for arq in arquivos])
        
        for pasta in self.pastas_monitoradas:
            caminho_pasta = os.path.join(self.diretorio_base, pasta)
            
            if os.path.exists(caminho_pasta):
                arquivos = self._escanear_pasta(caminho_pasta)
                catalogo["materiais_por_categoria"][pasta] = arquivos
                catalogo["total_arquivos"] += len(arquivos)
                
                # Identificar arquivos novos
                for arquivo in arquivos:
                    if arquivo["caminho"] not in arquivos_anteriores:
                        catalogo["arquivos_novos"].append({
                            "categoria": pasta,
                            "arquivo": arquivo["nome"],
                            "caminho": arquivo["caminho"],
                            "tamanho": arquivo["tamanho"],
                            "data_adicao": arquivo["data_modificacao"]
                        })
                
                # Gerar resumo da categoria
                catalogo["resumo_conteudo"][pasta] = {
                    "total_arquivos": len(arquivos),
                    "tipos_arquivo": list(set([arq["extensao"] for arq in arquivos])),
                    "tamanho_total": sum([arq["tamanho"] for arq in arquivos])
                }
        
        # Salvar catálogo atualizado
        self._salvar_catalogo(catalogo)
        
        return catalogo
    
    def _escanear_pasta(self, caminho_pasta: str) -> List[Dict]:
        """Escaneia uma pasta específica e retorna informações dos arquivos"""
        
        arquivos = []
        
        for item in os.listdir(caminho_pasta):
            caminho_item = os.path.join(caminho_pasta, item)
            
            # Pular README.md das pastas
            if item == "README.md":
                continue
                
            if os.path.isfile(caminho_item):
                stat = os.stat(caminho_item)
                
                arquivo_info = {
                    "nome": item,
                    "caminho": caminho_item,
                    "extensao": os.path.splitext(item)[1].lower(),
                    "tamanho": stat.st_size,
                    "data_modificacao": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "data_criacao": datetime.datetime.fromtimestamp(stat.st_ctime).isoformat()
                }
                
                arquivos.append(arquivo_info)
        
        return sorted(arquivos, key=lambda x: x["data_modificacao"], reverse=True)
    
    def _carregar_catalogo_anterior(self) -> Dict:
        """Carrega o catálogo anterior se existir"""
        
        if os.path.exists(self.arquivo_catalogo):
            try:
                with open(self.arquivo_catalogo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Erro ao carregar catálogo anterior: {e}")
        
        return {}
    
    def _salvar_catalogo(self, catalogo: Dict):
        """Salva o catálogo atualizado"""
        
        try:
            with open(self.arquivo_catalogo, 'w', encoding='utf-8') as f:
                json.dump(catalogo, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar catálogo: {e}")
    
    def gerar_relatorio_materiais(self) -> str:
        """Gera relatório em markdown sobre os materiais disponíveis"""
        
        catalogo = self.escanear_materiais()
        
        relatorio = f"""
# RELATÓRIO DE MATERIAIS DE REFERÊNCIA
## Kabbalah das Águas Primordiais - Apostila Astrológica

**Data do Escaneamento**: {datetime.datetime.fromisoformat(catalogo['data_escaneamento']).strftime('%d/%m/%Y às %H:%M')}
**Total de Arquivos**: {catalogo['total_arquivos']}

---

## 📊 RESUMO POR CATEGORIA

"""
        
        for categoria, resumo in catalogo["resumo_conteudo"].items():
            nome_categoria = categoria.replace('-', ' ').title()
            relatorio += f"""
### {nome_categoria}
- **Arquivos**: {resumo['total_arquivos']}
- **Tipos**: {', '.join(resumo['tipos_arquivo']) if resumo['tipos_arquivo'] else 'Nenhum'}
- **Tamanho Total**: {self._formatar_tamanho(resumo['tamanho_total'])}
"""
        
        if catalogo["arquivos_novos"]:
            relatorio += """
---

## 🆕 ARQUIVOS ADICIONADOS RECENTEMENTE

"""
            for arquivo in catalogo["arquivos_novos"]:
                data_adicao = datetime.datetime.fromisoformat(arquivo['data_adicao']).strftime('%d/%m/%Y')
                relatorio += f"""
- **{arquivo['arquivo']}** ({arquivo['categoria']})
  - Adicionado em: {data_adicao}
  - Tamanho: {self._formatar_tamanho(arquivo['tamanho'])}
"""
        
        relatorio += """
---

## 📋 DETALHAMENTO POR CATEGORIA

"""
        
        for categoria, arquivos in catalogo["materiais_por_categoria"].items():
            if arquivos:  # Só mostrar categorias com arquivos
                nome_categoria = categoria.replace('-', ' ').title()
                relatorio += f"""
### {nome_categoria}

"""
                for arquivo in arquivos:
                    data_mod = datetime.datetime.fromisoformat(arquivo['data_modificacao']).strftime('%d/%m/%Y')
                    relatorio += f"""
- **{arquivo['nome']}**
  - Tipo: {arquivo['extensao'].upper()}
  - Tamanho: {self._formatar_tamanho(arquivo['tamanho'])}
  - Modificado: {data_mod}
"""
        
        relatorio += f"""
---

## 🎯 PRÓXIMOS PASSOS

Com base nos materiais disponíveis, posso agora:

1. **Analisar o conteúdo** dos arquivos adicionados
2. **Extrair informações relevantes** para nossa apostila
3. **Criar sínteses integradas** na pasta `materiais-processados`
4. **Desenvolver a estrutura** da apostila cabalística
5. **Gerar conteúdo original** baseado nas referências

---

## 📞 STATUS DO PROJETO

- **Materiais Coletados**: {catalogo['total_arquivos']} arquivos
- **Categorias Ativas**: {len([cat for cat, resumo in catalogo['resumo_conteudo'].items() if resumo['total_arquivos'] > 0])} de {len(self.pastas_monitoradas)}
- **Pronto para Processamento**: {'Sim' if catalogo['total_arquivos'] > 0 else 'Aguardando materiais'}

---

*Relatório gerado automaticamente pelo Monitor de Materiais*
*Kabbalah das Águas Primordiais - SCII 5.0*
"""
        
        return relatorio
    
    def _formatar_tamanho(self, tamanho_bytes: int) -> str:
        """Formata tamanho em bytes para formato legível"""
        
        if tamanho_bytes < 1024:
            return f"{tamanho_bytes} B"
        elif tamanho_bytes < 1024 * 1024:
            return f"{tamanho_bytes / 1024:.1f} KB"
        elif tamanho_bytes < 1024 * 1024 * 1024:
            return f"{tamanho_bytes / (1024 * 1024):.1f} MB"
        else:
            return f"{tamanho_bytes / (1024 * 1024 * 1024):.1f} GB"
    
    def salvar_relatorio(self) -> str:
        """Gera e salva relatório de materiais"""
        
        relatorio = self.gerar_relatorio_materiais()
        arquivo_relatorio = os.path.join(self.diretorio_base, "relatorio_materiais.md")
        
        with open(arquivo_relatorio, 'w', encoding='utf-8') as f:
            f.write(relatorio)
        
        return arquivo_relatorio

# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    monitor = MonitorMateriais()
    arquivo_relatorio = monitor.salvar_relatorio()
    
    print("Monitor de Materiais executado com sucesso!")
    print(f"Relatório salvo em: {arquivo_relatorio}")
    
    # Mostrar resumo rápido
    catalogo = monitor.escanear_materiais()
    print(f"\nResumo:")
    print(f"- Total de arquivos: {catalogo['total_arquivos']}")
    print(f"- Arquivos novos: {len(catalogo['arquivos_novos'])}")
    print(f"- Categorias com conteúdo: {len([cat for cat, resumo in catalogo['resumo_conteudo'].items() if resumo['total_arquivos'] > 0])}")