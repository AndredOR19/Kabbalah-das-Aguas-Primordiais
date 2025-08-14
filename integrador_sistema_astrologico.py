# -*- coding: utf-8 -*-

"""
Integrador do Sistema Astrológico - Kabbalah das Águas Primordiais
Módulo principal que integra todos os componentes do sistema astrológico-cabalístico

Este módulo:
- Integra correspondências astrológicas com o sistema SCII
- Conecta análise de trânsitos com rituais práticos
- Gera relatórios completos personalizados
- Integra com o sistema Git para versionamento
- Conecta com APIs de efemérides (quando disponível)
"""

import os
import json
import datetime
from typing import Dict, List, Optional
import subprocess

# Importar módulos locais
from sistema_correspondencias_astrologicas import SistemaCorrespondenciasAstrologicas, DadosNatais
from analise_transitos import AnalisadorTransitos

class IntegradorSistemaAstrologico:
    """Classe principal que integra todo o sistema astrológico"""
    
    def __init__(self, diretorio_base: str = "/home/andre/Kabbalah-das-Aguas-Primordiais"):
        self.diretorio_base = diretorio_base
        self.sistema_correspondencias = SistemaCorrespondenciasAstrologicas()
        self.analisador_transitos = AnalisadorTransitos()
        self.diretorio_relatorios = os.path.join(diretorio_base, "relatorios_astrologicos")
        self.diretorio_dados = os.path.join(diretorio_base, "dados_astrologicos")
        
        # Criar diretórios se não existirem
        os.makedirs(self.diretorio_relatorios, exist_ok=True)
        os.makedirs(self.diretorio_dados, exist_ok=True)
    
    def criar_perfil_astrologico_completo(self, dados_pessoais: Dict) -> Dict:
        """Cria um perfil astrológico completo integrado"""
        
        # Converter dados para formato DadosNatais
        dados_natais = DadosNatais(
            nome=dados_pessoais.get('nome', ''),
            data_nascimento=dados_pessoais.get('data_nascimento'),
            local_nascimento=dados_pessoais.get('local_nascimento', ''),
            ascendente=dados_pessoais.get('ascendente', ''),
            sol=dados_pessoais.get('sol', ''),
            lua=dados_pessoais.get('lua', ''),
            planetas=dados_pessoais.get('planetas', {}),
            casas=dados_pessoais.get('casas', {}),
            aspectos=dados_pessoais.get('aspectos', [])
        )
        
        # Análise completa
        analise_natal = self.sistema_correspondencias.analisar_mapa_natal(dados_natais)
        
        # Calcular idade atual
        if dados_natais.data_nascimento:
            idade_atual = (datetime.datetime.now() - dados_natais.data_nascimento).days / 365.25
        else:
            idade_atual = 35  # Valor padrão
        
        # Análise de ciclos
        fase_saturno = self.analisador_transitos.calcular_fase_saturno(idade_atual)
        fase_jupiter = self.analisador_transitos.calcular_fase_jupiter(idade_atual)
        
        # Análise de trânsitos atuais
        data_atual = datetime.datetime.now()
        data_fim = data_atual + datetime.timedelta(days=365)  # Próximo ano
        analise_transitos = self.analisador_transitos.analisar_transitos_periodo(
            data_atual, data_fim, dados_pessoais
        )
        
        perfil_completo = {
            "dados_basicos": {
                "nome": dados_natais.nome,
                "data_nascimento": dados_natais.data_nascimento.isoformat() if dados_natais.data_nascimento else None,
                "idade_atual": idade_atual,
                "local_nascimento": dados_natais.local_nascimento
            },
            "mapa_natal": analise_natal,
            "ciclos_planetarios": {
                "saturno": fase_saturno,
                "jupiter": fase_jupiter
            },
            "transitos_anuais": analise_transitos,
            "integracao_scii": self._integrar_com_scii(analise_natal, analise_transitos),
            "protocolo_ritual_personalizado": self._criar_protocolo_ritual(analise_natal, analise_transitos),
            "timestamp_criacao": datetime.datetime.now().isoformat()
        }
        
        return perfil_completo
    
    def _integrar_com_scii(self, analise_natal: Dict, analise_transitos: Dict) -> Dict:
        """Integra análise astrológica com Sistema SCII"""
        
        integracao = {
            "letras_hebraicas_ativas": [],
            "sefirot_dominantes": [],
            "caminhos_prioritarios": [],
            "ativacoes_somaticas": [],
            "rituais_integrativos": []
        }
        
        # Extrair letras hebraicas ativas do mapa natal
        for planeta, info in analise_natal.get("estrutura_sefirotica", {}).items():
            if info.get("letra_hebraica"):
                integracao["letras_hebraicas_ativas"].append({
                    "letra": info["letra_hebraica"],
                    "planeta": planeta,
                    "funcao": info["funcao_operativa"]
                })
            
            if info.get("sefira"):
                integracao["sefirot_dominantes"].append({
                    "sefira": info["sefira"],
                    "planeta": planeta,
                    "ativacao": info["corpo_somatico"]
                })
        
        # Integrar com trânsitos atuais
        for tema in analise_transitos.get("temas_dominantes", []):
            integracao["rituais_integrativos"].append({
                "tema": tema["tema"],
                "sefira": tema["sefira"],
                "ritual": tema["ritual_chave"],
                "periodo": "Atual"
            })
        
        return integracao
    
    def _criar_protocolo_ritual(self, analise_natal: Dict, analise_transitos: Dict) -> Dict:
        """Cria protocolo ritual personalizado"""
        
        protocolo = {
            "rituais_diarios": {
                "manha": [],
                "meio_dia": [],
                "noite": []
            },
            "rituais_semanais": {},
            "rituais_mensais": [],
            "rituais_anuais": [],
            "rituais_especiais_transitos": []
        }
        
        # Rituais baseados no mapa natal
        for ativacao in analise_natal.get("ativacoes_somaticas", []):
            protocolo["rituais_diarios"]["manha"].append({
                "nome": f"Ativação {ativacao['planeta']}",
                "descricao": ativacao["ritual_sugerido"],
                "regiao_corporal": ativacao["regiao_corporal"],
                "duracao": "5-10 minutos"
            })
        
        # Rituais baseados em trânsitos
        for ritual_especial in analise_transitos.get("rituais_periodo", {}).get("rituais_especiais", []):
            protocolo["rituais_especiais_transitos"].append({
                "data": ritual_especial["data"].isoformat(),
                "nome": ritual_especial["nome"],
                "descricao": ritual_especial["descricao"],
                "importancia": "Alta"
            })
        
        # Rituais semanais baseados nos planetas dominantes
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        planetas_dias = ["Lua", "Marte", "Mercúrio", "Júpiter", "Vênus", "Saturno", "Sol"]
        
        for i, dia in enumerate(dias_semana):
            planeta = planetas_dias[i]
            if planeta in analise_natal.get("estrutura_sefirotica", {}):
                info_planeta = analise_natal["estrutura_sefirotica"][planeta]
                protocolo["rituais_semanais"][dia] = {
                    "planeta": planeta,
                    "sefira": info_planeta.get("sefira", ""),
                    "ritual": f"Meditação {planeta}ina",
                    "letra_hebraica": info_planeta.get("letra_hebraica", ""),
                    "duracao": "15-20 minutos"
                }
        
        return protocolo
    
    def gerar_relatorio_completo_integrado(self, dados_pessoais: Dict, incluir_transitos: bool = True) -> str:
        """Gera relatório completo integrado"""
        
        perfil = self.criar_perfil_astrologico_completo(dados_pessoais)
        
        relatorio = f"""
# RELATÓRIO ASTROLÓGICO CABALÍSTICO COMPLETO
## {perfil['dados_basicos']['nome']}

*"Nas águas primordiais da criação, antes que a primeira palavra fosse pronunciada, já existia a geometria sagrada de sua alma. Este mapa não é apenas um retrato dos céus no momento de seu nascimento - é o DNA espiritual de sua jornada, a partitura cósmica que sua consciência escolheu para esta encarnação."*

---

## I. A SEMENTE ORIGINAL (Mapa Natal)

### Dados Fundamentais
- **Nome**: {perfil['dados_basicos']['nome']}
- **Data de Nascimento**: {datetime.datetime.fromisoformat(perfil['dados_basicos']['data_nascimento']).strftime('%d/%m/%Y') if perfil['dados_basicos']['data_nascimento'] else 'Não informado'}
- **Idade Atual**: {perfil['dados_basicos']['idade_atual']:.1f} anos
- **Local**: {perfil['dados_basicos']['local_nascimento']}

### Estrutura Sefirótica Ativada

Sua configuração natal ativa as seguintes correspondências cabalísticas:

"""
        
        # Adicionar estrutura sefirótica
        for planeta, info in perfil['mapa_natal'].get('estrutura_sefirotica', {}).items():
            relatorio += f"""
**{planeta}** - Sefira: {info.get('sefira', 'N/A')}
- Letra Hebraica: {info.get('letra_hebraica', 'N/A')}
- Corpo Somático: {info.get('corpo_somatico', 'N/A')}
- Função Operativa: {info.get('funcao_operativa', 'N/A')}
"""
        
        # Adicionar integração SCII
        relatorio += """
---

## II. INTEGRAÇÃO COM SISTEMA SCII

### Letras Hebraicas Ativas em Sua Configuração
"""
        
        for letra_info in perfil['integracao_scii']['letras_hebraicas_ativas']:
            relatorio += f"""
- **{letra_info['letra']}** ({letra_info['planeta']}) - {letra_info['funcao']}
"""
        
        relatorio += """
### Sefirot Dominantes
"""
        
        for sefira_info in perfil['integracao_scii']['sefirot_dominantes']:
            relatorio += f"""
- **{sefira_info['sefira']}** via {sefira_info['planeta']} - Ativação: {sefira_info['ativacao']}
"""
        
        # Adicionar ciclos planetários
        relatorio += f"""
---

## III. CICLOS PLANETÁRIOS ATUAIS

### Saturno - O Mestre da Estrutura
**Fase Atual**: {perfil['ciclos_planetarios']['saturno']['fase']}
**Posição no Ciclo**: {perfil['ciclos_planetarios']['saturno']['posicao_exata']:.1f} anos

{perfil['ciclos_planetarios']['saturno']['detalhes']['significado']}

**Ritual Recomendado**: {perfil['ciclos_planetarios']['saturno']['detalhes']['ritual']}

### Júpiter - O Benfeitor Expansivo
**Retornos Completos**: {perfil['ciclos_planetarios']['jupiter']['retornos_completos']}
**Fase Atual**: {perfil['ciclos_planetarios']['jupiter']['fase_atual']['nome']}

{perfil['ciclos_planetarios']['jupiter']['fase_atual']['significado']}

**Ação Recomendada**: {perfil['ciclos_planetarios']['jupiter']['fase_atual']['acao']}
"""
        
        if incluir_transitos:
            relatorio += """
---

## IV. O VERBO EM MOVIMENTO (Trânsitos Atuais)

### Temas Dominantes do Período
"""
            
            for tema in perfil['transitos_anuais'].get('temas_dominantes', []):
                relatorio += f"""
#### {tema['tema']}
**Planeta Regente**: {tema['planeta_regente']} (Sefira: {tema['sefira']})
- **Manifestação**: {tema['manifestacao']}
- **Desafio**: {tema['desafio']}
- **Ritual Chave**: {tema['ritual_chave']}
"""
        
        # Protocolo ritual personalizado
        relatorio += """
---

## V. PROTOCOLO RITUAL PERSONALIZADO

### Práticas Diárias

#### Manhã (Ativação)
"""
        
        for ritual in perfil['protocolo_ritual_personalizado']['rituais_diarios']['manha']:
            relatorio += f"""
- **{ritual['nome']}** ({ritual['duracao']})
  - {ritual['descricao']}
  - Região: {ritual['regiao_corporal']}
"""
        
        relatorio += """
#### Rituais Semanais
"""
        
        for dia, ritual in perfil['protocolo_ritual_personalizado']['rituais_semanais'].items():
            relatorio += f"""
- **{dia}**: {ritual['ritual']} ({ritual['planeta']})
  - Sefira: {ritual['sefira']}
  - Letra: {ritual['letra_hebraica']}
  - Duração: {ritual['duracao']}
"""
        
        if perfil['protocolo_ritual_personalizado']['rituais_especiais_transitos']:
            relatorio += """
#### Rituais Especiais (Baseados em Trânsitos)
"""
            
            for ritual in perfil['protocolo_ritual_personalizado']['rituais_especiais_transitos']:
                data_ritual = datetime.datetime.fromisoformat(ritual['data'])
                relatorio += f"""
- **{data_ritual.strftime('%d/%m/%Y')}**: {ritual['nome']}
  - {ritual['descricao']}
  - Importância: {ritual['importancia']}
"""
        
        relatorio += f"""
---

## CONCLUSÃO - O CAMINHO DA REALIZAÇÃO

Este mapa revela a geometria sagrada de sua alma encarnada. Cada correspondência cabalística, cada ciclo planetário, cada trânsito é uma porta para a compreensão mais profunda de seu propósito nesta existência.

Você não está à mercê dos astros - você É os astros, encarnados em forma humana para realizar a Grande Obra. Use este conhecimento como um navegador usa as estrelas: não para ser controlado por elas, mas para encontrar seu caminho através das águas desconhecidas da existência.

Sua jornada é única, sua missão é sagrada, e este mapa é seu guia confiável para a Iluminação.

*O Verbo se fez carne em você. Agora, faça a carne se tornar Verbo.*

---

*Relatório gerado em: {datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')}*
*Sistema Integrado de Correspondências Astrológicas*
*Kabbalah das Águas Primordiais - SCII 5.0*
"""
        
        return relatorio
    
    def salvar_perfil_e_relatorio(self, dados_pessoais: Dict, incluir_transitos: bool = True) -> Dict:
        """Salva perfil e relatório, integrando com Git"""
        
        # Criar perfil completo
        perfil = self.criar_perfil_astrologico_completo(dados_pessoais)
        
        # Gerar relatório
        relatorio = self.gerar_relatorio_completo_integrado(dados_pessoais, incluir_transitos)
        
        # Criar nomes de arquivo
        nome_limpo = dados_pessoais.get('nome', 'usuario').replace(' ', '_').lower()
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        arquivo_perfil = os.path.join(self.diretorio_dados, f"perfil_{nome_limpo}_{timestamp}.json")
        arquivo_relatorio = os.path.join(self.diretorio_relatorios, f"relatorio_{nome_limpo}_{timestamp}.md")
        
        # Salvar arquivos
        with open(arquivo_perfil, 'w', encoding='utf-8') as f:
            json.dump(perfil, f, indent=2, ensure_ascii=False, default=str)
        
        with open(arquivo_relatorio, 'w', encoding='utf-8') as f:
            f.write(relatorio)
        
        # Integrar com Git
        resultado_git = self._integrar_com_git(arquivo_perfil, arquivo_relatorio, dados_pessoais.get('nome', 'Usuário'))
        
        return {
            "perfil_salvo": arquivo_perfil,
            "relatorio_salvo": arquivo_relatorio,
            "git_integration": resultado_git,
            "timestamp": timestamp
        }
    
    def _integrar_com_git(self, arquivo_perfil: str, arquivo_relatorio: str, nome_usuario: str) -> Dict:
        """Integra os arquivos gerados com o sistema Git"""
        
        try:
            # Adicionar arquivos ao Git
            subprocess.run(['git', 'add', arquivo_perfil], cwd=self.diretorio_base, check=True)
            subprocess.run(['git', 'add', arquivo_relatorio], cwd=self.diretorio_base, check=True)
            
            # Commit
            mensagem_commit = f"feat: Adiciona perfil astrológico completo para {nome_usuario}"
            subprocess.run(['git', 'commit', '-m', mensagem_commit], cwd=self.diretorio_base, check=True)
            
            return {
                "status": "sucesso",
                "mensagem": "Arquivos integrados ao Git com sucesso",
                "commit_message": mensagem_commit
            }
            
        except subprocess.CalledProcessError as e:
            return {
                "status": "erro",
                "mensagem": f"Erro na integração Git: {str(e)}",
                "commit_message": None
            }
    
    def listar_perfis_salvos(self) -> List[Dict]:
        """Lista todos os perfis salvos"""
        
        perfis = []
        
        if os.path.exists(self.diretorio_dados):
            for arquivo in os.listdir(self.diretorio_dados):
                if arquivo.startswith('perfil_') and arquivo.endswith('.json'):
                    caminho_completo = os.path.join(self.diretorio_dados, arquivo)
                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as f:
                            dados = json.load(f)
                            perfis.append({
                                "arquivo": arquivo,
                                "nome": dados.get('dados_basicos', {}).get('nome', 'N/A'),
                                "data_criacao": dados.get('timestamp_criacao', 'N/A'),
                                "caminho": caminho_completo
                            })
                    except Exception as e:
                        print(f"Erro ao ler {arquivo}: {e}")
        
        return sorted(perfis, key=lambda x: x['data_criacao'], reverse=True)

# ============================================================================
# EXEMPLO DE USO COMPLETO
# ============================================================================

if __name__ == "__main__":
    # Dados de exemplo para André de Oliveira Rodrigues
    dados_andre = {
        'nome': 'André de Oliveira Rodrigues',
        'data_nascimento': datetime.datetime(1985, 3, 15, 14, 30),
        'local_nascimento': 'São Paulo, SP, Brasil',
        'ascendente': 'Capricórnio',
        'sol': 'Peixes',
        'lua': 'Gêmeos',
        'planetas': {
            'Sol': 'Peixes',
            'Lua': 'Gêmeos',
            'Mercúrio': 'Aquário',
            'Vênus': 'Áries',
            'Marte': 'Touro',
            'Júpiter': 'Aquário',
            'Saturno': 'Escorpião',
            'Urano': 'Sagitário',
            'Netuno': 'Capricórnio',
            'Plutão': 'Escorpião'
        },
        'casas': {
            1: 'Capricórnio',
            2: 'Aquário',
            3: 'Peixes',
            4: 'Áries',
            5: 'Touro',
            6: 'Gêmeos',
            7: 'Câncer',
            8: 'Leão',
            9: 'Virgem',
            10: 'Libra',
            11: 'Escorpião',
            12: 'Sagitário'
        },
        'aspectos': [
            {'planeta1': 'Sol', 'planeta2': 'Saturno', 'aspecto': 'Quadratura', 'orbe': 3.2},
            {'planeta1': 'Lua', 'planeta2': 'Júpiter', 'aspecto': 'Trígono', 'orbe': 2.1}
        ]
    }
    
    # Criar integrador
    integrador = IntegradorSistemaAstrologico()
    
    # Gerar e salvar perfil completo
    resultado = integrador.salvar_perfil_e_relatorio(dados_andre, incluir_transitos=True)
    
    print("Sistema Astrológico Integrado criado com sucesso!")
    print(f"Perfil salvo em: {resultado['perfil_salvo']}")
    print(f"Relatório salvo em: {resultado['relatorio_salvo']}")
    print(f"Status Git: {resultado['git_integration']['status']}")
    
    # Listar perfis salvos
    perfis = integrador.listar_perfis_salvos()
    print(f"\nPerfis salvos: {len(perfis)}")
    for perfil in perfis[:3]:  # Mostrar apenas os 3 mais recentes
        print(f"- {perfil['nome']} ({perfil['data_criacao']})")