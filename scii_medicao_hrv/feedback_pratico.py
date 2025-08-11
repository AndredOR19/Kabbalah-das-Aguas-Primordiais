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

def gerar_feedback_pratica(relatorio_analise, nome_pratica):
    """
    Gera um feedback prático com base no relatório de análise.

    Args:
        relatorio_analise (str): O texto do relatório gerado pelo Módulo 2.
        nome_pratica (str): O nome da prática para contextualizar o feedback.

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
        feedback = gerar_feedback_alinhado(arquétipo)
    else:
        feedback = gerar_feedback_nao_alinhado(arquétipo)

    # 3. Formata a saída para o usuário
    output = f"""
    **************************************************
    FEEDBACK PARA A PRÓXIMA CALIBRAÇÃO - {arquétipo.upper()}
    **************************************************

    {feedback}

    **************************************************
    """

    return output

def gerar_feedback_alinhado(arquétipo):
    """
    Gera uma mensagem de validação e foco para um relatório "Alinhado".

    Args:
        arquétipo (str): O nome do arquétipo da prática (ex: "Aleph").

    Returns:
        str: A mensagem de feedback positivo.
    """
    # Mensagens personalizadas por arquétipo
    feedbacks = {
        "Aleph": "O sistema confirma um forte alinhamento com a energia do Aleph. Para a próxima prática, mantenha o foco na intenção de Unidade e Conexão, visualizando o Vav como a ponte entre o céu e a terra.",
        "Tiferet": "Ressonância com Tiferet estabelecida. O equilíbrio foi alcançado. Para a próxima sessão, concentre-se em irradiar essa harmonia do coração para o resto do corpo.",
        "Default": "O alinhamento foi bem-sucedido. Continue com a mesma intenção e foco na próxima prática para aprofundar a conexão."
    }
    return feedbacks.get(arquétipo, feedbacks["Default"])

def gerar_feedback_nao_alinhado(arquétipo):
    """
    Gera uma mensagem de ajuste e direcionamento para um relatório "Não Alinhado".

    Args:
        arquétipo (str): O nome do arquétipo da prática (ex: "Aleph").

    Returns:
        str: A mensagem de feedback corretivo.
    """
    # Mensagens personalizadas por arquétipo
    feedbacks = {
        "Aleph": "O sistema detectou um desvio no alinhamento com o Aleph. Para a próxima prática, direcione sua atenção para a respiração, visualizando o ar como a fonte da vida e a energia que preenche o seu corpo. Foque menos na forma da letra e mais na sua essência de 'ar primordial'.",
        "Tiferet": "Desvio detectado. A energia de Tiferet requer um relaxamento mais profundo. Na próxima vez, solte a tensão dos ombros e do maxilar antes de começar. A harmonia nasce da entrega, não do esforço.",
        "Default": "Desvio detectado. Reavalie seu ambiente e estado interno. Certifique-se de que não há distrações e que sua intenção está clara antes de iniciar a próxima medição."
    }
    return feedbacks.get(arquétipo, feedbacks["Default"])

# Exemplo de uso do módulo
if __name__ == "__main__":
    # Importa os módulos anteriores para simular o fluxo completo
    from medicao_hrv import iniciar_medicao_hrv
    from analise_hrv import analisar_assinatura_vibracional

    print("--- Simulando o Ciclo Completo de Calibração Automática ---")

    # --- MÓDULO 1: MEDIÇÃO ---
    pratica_atual = "Ativacao_Aleph"
    caminho_do_arquivo = iniciar_medicao_hrv(10, pratica_atual)

    # --- MÓDULO 2: ANÁLISE ---
    assinatura_aleph = {
        "hrv_media_ideal": 60,       # Foco e calma
        "desvio_padrao_ideal": 15    # Alta variabilidade, prontidão
    }
    relatorio_da_analise = analisar_assinatura_vibracional(caminho_do_arquivo, assinatura_aleph)
    print(relatorio_da_analise)

    # --- MÓDULO 3: FEEDBACK ---
    feedback_final = gerar_feedback_pratica(relatorio_da_analise, pratica_atual)
    print(feedback_final)
