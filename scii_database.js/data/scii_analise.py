# scii_analise.py
# Sistema de Correspondência Integrada e Inteligente (SCII) - Versão Python Offline

import json
import re
import random
from datetime import datetime

# === Carregar o banco de dados SCII ===
# Substitua este dicionário pelo seu JSON completo (ou carregue de um arquivo)
scii_data = {
  "metadata": {
    "version": "1.0.0",
    "last_updated": "2025-07-28",
    "description": "Base de Dados Estruturada para o Sistema de Correspondência Integrada e Inteligente (SCII). Mapeia as relações entre Letras Hebraicas, Planetas, Sephirot e Chakras."
  },
  "letras": {
    "Aleph": {
      "valor_gemátrico": 1,
      "pictograma": "Touro / Cabeça de Boi",
      "som": "Silenciosa (portadora de vogal)",
      "elemento_primordial": "Ar",
      "planeta": "Urano",
      "astro_secundario": "O Louco (Tarot)",
      "funcao_corpo_somatico": "Respiração, Prana, Diafragma, sistema nervoso autônomo",
      "acao_espiritual": "Potencial puro, o 'ainda não', Vontade Primordial, Unidade, o sopro que inicia",
      "caminho_arvore_vida": "1-2 (Kether-Chokmah)",
      "diagnostico_bloqueio": "Paralisia por excesso de potencial, falta de iniciativa, desconexão com o propósito, ansiedade generalizada, incapacidade de começar.",
      "comando_ritualistico": "Inalar o potencial do todo, expirar a ação no particular."
    },
    "Beth": {
      "valor_gemátrico": 2,
      "pictograma": "Casa / Tenda / Recipiente",
      "som": "B / V",
      "elemento_primordial": "Matéria (como recipiente)",
      "planeta": "Mercúrio",
      "astro_secundario": "O Mago (Tarot)",
      "funcao_corpo_somatico": "Boca, o recipiente do Verbo, sistema digestivo, o corpo como casa da alma",
      "acao_espiritual": "Interiorização, criação de um espaço interno, delimitação, foco, a primeira contração",
      "caminho_arvore_vida": "1-3 (Kether-Binah)",
      "diagnostico_bloqueio": "Dispersão, falta de foco, incapacidade de materializar ideias, falar sem agir, sentir-se 'sem casa' ou desprotegido.",
      "comando_ritualistico": "Construir o Templo interior, dar um corpo à Palavra."
    },
    # ... (todas as outras letras, planetas, sephirot e chakras)
    # [Inclua aqui todo o JSON que você já tem]
  },
  "planetas": {
    "Saturno": {
      "principio": "Estrutura, Limite, Karma, Tempo, Disciplina, Construção, Morte, Maturidade",
      "letras_associadas": ["Tav"],
      "sephira": "Binah",
      "palavra_chave": "Responsabilidade",
      "arquetipo": "O Velho Sábio / O Construtor / O Ceifador",
      "diagnostico": "Restrição, cobrança kármica, necessidade de maturidade, fim de ciclo, lições duras mas necessárias, construção de bases sólidas."
    },
    # ... (todos os outros planetas)
  },
  "sephirot": {
    "Kether": {
      "numero": 1,
      "nome": "Coroa",
      "imagem_magica": "Um rei antigo visto de perfil",
      "planeta_associado": "Urano/Netuno (começo de tudo)",
      "virtude": "Realização, perfeição da Unidade",
      "vicio": "N/A",
      "ponto_corpo_somatico": "Coroa, acima do topo da cabeça",
      "experiencia_espiritual": "União com Deus, o Ponto Primordial"
    },
    # ... (todas as outras sephirot)
  },
  "chakras": {
    "Muladhara": {
      "nome": "Chakra Básico",
      "localizacao": "Base da coluna, períneo",
      "cor": "Vermelho",
      "elemento_associado": "Terra",
      "funcao_psicologica": "Sobrevivência, estabilidade, segurança material, instintos primários",
      "letras_hebraicas_relacionadas": ["Tav"],
      "planeta_regente": "Saturno",
      "diagnostico_bloqueio": "Insegurança financeira, medo, falta de 'chão', desconexão com o corpo, ganância, fadiga crônica."
    },
    # ... (todos os outros chakras)
  }
}

# === Função: Normalizar texto (remover acentos e converter para minúsculas) ===
def normalizar(texto):
    if isinstance(texto, str):
        return re.sub(r'[\u0300-\u036f]', '', texto.lower().normalize('NFD'))
    return str(texto).lower()

# === Função: Busca Reversa Universal ===
def busca_reversa(termo):
    resultados = []
    termo_norm = normalizar(termo)

    def buscar_em_obj(obj, origem, caminho=""):
        for chave, valor in obj.items():
            caminho_atual = f"{caminho}.{chave}" if caminho else chave

            if isinstance(valor, dict):
                buscar_em_obj(valor, origem, caminho_atual)
            elif isinstance(valor, list):
                valor_str = ", ".join(map(str, valor))
                if termo_norm in normalizar(valor_str):
                    resultados.append({
                        "origem": origem,
                        "campo": caminho_atual,
                        "valor": valor_str,
                        "objeto": obj
                    })
            else:
                valor_str = str(valor)
                if termo_norm in normalizar(valor_str):
                    resultados.append({
                        "origem": origem,
                        "campo": caminho_atual,
                        "valor": valor_str,
                        "objeto": obj
                    })

    # Buscar em todas as seções
    for secao in ["letras", "planetas", "sephirot", "chakras"]:
        if secao in scii_data:
            buscar_em_obj(scii_data[secao], secao)

    return resultados

# === Função: Mostrar detalhes de uma Sefirah ===
def mostrar_sephira(nome):
    sephira = scii_data["sephirot"].get(nome)
    if not sephira:
        print(f"Sefirah '{nome}' não encontrada.")
        return

    print(f"\n=== {nome} ===")
    for k, v in sephira.items():
        print(f"{k.replace('_', ' ').title()}: {v}")

# === Função: Modo Meditação ===
def modo_meditacao():
    letras = list(scii_data["letras"].values())
    comando = random.choice(letras)["comando_ritualistico"]
    print(f"\n✨ MODO MEDITAÇÃO\n")
    print(f"🔁 Respire fundo e repita:\n")
    print(f"  \"{comando}\"")
    print(f"\n(Repita por 5-10 minutos. Pressione Enter para outro comando ou 'sair' para parar.)")
    
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "sair":
            break
        comando = random.choice(letras)["comando_ritualistico"]
        print(f"\n🔁 \"{comando}\"")

# === Função: Exportar Relatório ===
def exportar_relatorio(resultados, nome_arquivo=None):
    if not nome_arquivo:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"relatorio_scii_{timestamp}.txt"
    
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=== RELATÓRIO SCII ===\n")
        f.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        for r in resultados:
            f.write(f"Origem: {r['origem']}\n")
            f.write(f"Campo: {r['campo']}\n")
            f.write(f"Valor: {r['valor']}\n")
            f.write(f"{'-'*50}\n")
    print(f"✅ Relatório salvo como '{nome_arquivo}'")

# === Menu Interativo ===
def menu():
    print("\n" + "="*60)
    print("SCII - Sistema de Correspondência Integrada e Inteligente")
    print("="*60)
    print("1. Busca Reversa por termo (ex: 'Fogo', 'Sol', 'Tav')")
    print("2. Mostrar detalhes de uma Sefirah")
    print("3. Modo Meditação (comandos ritualísticos)")
    print("4. Exportar relatório de busca")
    print("5. Sair")
    print("="*60)

def main():
    resultados_busca = []
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            termo = input("Digite o termo para busca (ex: Fogo, Vênus, Respiração): ").strip()
            if termo:
                resultados_busca = busca_reversa(termo)
                print(f"\n🔎 Encontrados {len(resultados_busca)} resultados para '{termo}':\n")
                for i, r in enumerate(resultados_busca, 1):
                    print(f"{i}. [{r['origem']}] {r['campo']} = {r['valor']}")
            else:
                print("Termo vazio.")
        
        elif opcao == "2":
            nome = input("Nome da Sefirah (ex: Kether, Tiphareth): ").strip().title()
            mostrar_sephira(nome)
        
        elif opcao == "3":
            modo_meditacao()
        
        elif opcao == "4":
            if resultados_busca:
                nome_arq = input("Nome do arquivo (Enter para automático): ").strip()
                exportar_relatorio(resultados_busca, nome_arq or None)
            else:
                print("Nenhum resultado para exportar. Faça uma busca primeiro.")
        
        elif opcao == "5":
            print("Encerrando o sistema SCII. Paz e Luz.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    # Para carregar de um arquivo JSON externo, use:
    # with open('scii_database.json', 'r', encoding='utf-8') as f:
    #     scii_data = json.load(f)
    
    main()
