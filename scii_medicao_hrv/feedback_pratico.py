# -*- coding: utf-8 -*-
"""
SCII - Módulo de Feedback Prático

Este script analisa o relatório gerado pelo módulo de análise e fornece
um feedback prático e direcionado ao usuário para a próxima prática, fechando
o ciclo de calibração automática.

Autor: Karuv Beni EL (André de Oliveira Rodrigues)
Data: 11 de Agosto de 2025
"""

import re
import sys
import argparse

def gerar_feedback_pratica(relatorio_analise, nome_pratica, tema_consulta):
    """
    Gera um feedback prático com base no relatório de análise.

    Args:
        relatorio_analise (str): O texto do relatório gerado pelo Módulo 2.
        nome_pratica (str): O nome da prática para contextualizar o feedback.
        tema_consulta (str): O tema da consulta do usuário (ex: "Amor", "Carreira").

    Returns:
        str: Uma instrução clara e construtiva para a próxima prática.
    """
    print("\n--- Gerando Feedback Prático para o Usuário ---")

    # 1. Analisa o relatório para encontrar o status de alinhamento
    # Usamos uma expressão regular para encontrar a linha "Status: ..."
    match = re.search(r"Status: (Alinhado|Não Alinhado)", relatorio_analise)

    if not match:
        return "Erro: Não foi possível determinar o status de alinhamento a partir do relatório."

    status_alinhamento = match.group(1)

    # Extrai o arquétipo do nome da prática (ex: "Ativacao_Aleph" -> "Aleph")
    arquétipo = nome_pratica.split('_')[-1]

    # 2. Gera o feedback com base no status
    if status_alinhamento == "Alinhado":
        feedback = gerar_feedback_alinhado(arquétipo, tema_consulta)
    else:
        feedback = gerar_feedback_nao_alinhado(arquétipo, tema_consulta)

    # 3. Formata a saída para o usuário
    output = f"""
    **************************************************
    FEEDBACK PARA A PRÓXIMA CALIBRAÇÃO - {arquétipo.upper()}
    **************************************************

    {feedback}

    **************************************************
    """

    return output

def gerar_feedback_alinhado(arquétipo, tema):
    """
    Gera uma mensagem de validação e foco para um relatório "Alinhado".

    Args:
        arquétipo (str): O nome do arquétipo da prática (ex: "Aleph").
        tema (str): O tema da consulta do usuário.

    Returns:
        str: A mensagem de feedback positivo.
    """
    # Lógica para cruzar arquétipo e tema
    base_feedback = f"O sistema confirma um forte alinhamento com a energia de {arquétipo}. "
    
    if tema == "Amor":
        contexto = f"Isso indica uma base sólida e coerente para manifestar harmonia em seus relacionamentos. Mantenha essa vibração de equilíbrio."
    elif tema == "Carreira":
        contexto = f"Sua vibração está propícia para novos começos e para tomar decisões com clareza e força. Confie na sua prontidão."
    elif tema == "Autoconhecimento":
        contexto = f"A ressonância indica que você está em um estado receptivo para insights profundos. Continue a explorar seu mundo interior com essa mesma estabilidade."
    else:
        contexto = "Continue com a mesma intenção e foco na próxima prática para aprofundar a conexão."

    return base_feedback + contexto

def gerar_feedback_nao_alinhado(arquétipo, tema):
    """
    Gera uma mensagem de ajuste e direcionamento para um relatório "Não Alinhado".

    Args:
        arquétipo (str): O nome do arquétipo da prática (ex: "Aleph").
        tema (str): O tema da consulta do usuário.

    Returns:
        str: A mensagem de feedback corretivo.
    """
    base_feedback = f"O sistema detectou um desvio no alinhamento com {arquétipo} em sua consulta sobre {tema}. "

    if tema == "Amor":
        contexto = f"A instabilidade vibracional sugere que questões emocionais não resolvidas podem estar interferindo em seus relacionamentos. Antes da próxima prática, medite sobre o que significa 'segurança emocional' para você."
    elif tema == "Carreira":
        contexto = f"A vibração dispersa indica uma falta de foco ou clareza em seus objetivos profissionais. Para a próxima prática, escreva em um papel uma única meta profissional e medite sobre ela antes de iniciar."
    elif tema == "Autoconhecimento":
        contexto = f"O desvio sugere que a mente está muito agitada para permitir uma introspecção verdadeira. Foque na respiração para acalmar o fluxo de pensamentos antes de mergulhar em questões profundas."
    else:
        contexto = "Reavalie seu ambiente e estado interno. Certifique-se de que não há distrações e que sua intenção está clara."

    return base_feedback + contexto

# Exemplo de uso do módulo
if __name__ == "__main__":
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="SCII - Módulo de Feedback Prático.")
    parser.add_argument("relatorio_arquivo", type=str, nargs='?', default=sys.stdin, help="Caminho para o arquivo de relatório de análise. Se não for fornecido, lê da entrada padrão (pipe).")
    parser.add_argument("--pratica", type=str, default="Default", help="Nome da prática para contextualizar o feedback.")
    parser.add_argument("--tema", type=str, default="Autoconhecimento", help="O tema da consulta do usuário.")

    args = parser.parse_args()

    relatorio_texto = ""
    # Verifica se a entrada é da stdin (pipe)
    if args.relatorio_arquivo is sys.stdin:
        if not sys.stdin.isatty():
            relatorio_texto = sys.stdin.read()
        else:
            print("Erro: Forneça o caminho de um arquivo de relatório ou use um pipe.")
            sys.exit(1)
    else:
        try:
            with open(args.relatorio_arquivo, 'r', encoding='utf-8') as f:
                relatorio_texto = f.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo de relatório não encontrado em: {args.relatorio_arquivo}")
            sys.exit(1)

    # Gera o feedback com base no texto do relatório
    feedback_final = gerar_feedback_pratica(relatorio_texto, args.pratica, args.tema)
    print(feedback_final)
