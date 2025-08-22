def gerar_ritual_personalizado(diagnostico):
    """
    Gera ritual personalizado baseado no diagnóstico
    """
    template = f"""
# RITUAL PERSONALIZADO PARA {diagnostico['nome']}

## Análise do Seu Perfil:
- Desequilíbrio principal: Camada {diagnostico['desequilíbrio_principal']}
- Pontuação: Mente {diagnostico['pontuacao'][12]}, Matéria {diagnostico['pontuacao'][7]}, Força {diagnostico['pontuacao'][3]}

## Ritual Recomendado:
{escolher_ritual(diagnostico)}

## Materiais Necessários:
{gerar_materiais(diagnostico)}

## Passo a Passo:
1. {gerar_passos(diagnostico)}
2. ...
3. ...

## Duração Esperada: {random.randint(15, 45)} minutos
"""
    return template