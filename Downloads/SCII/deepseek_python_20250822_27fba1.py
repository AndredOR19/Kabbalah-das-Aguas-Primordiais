def tutorial_interativo():
    """
    Tutorial em linha de comando para novos usuários
    """
    print("Bem-vindo ao Sistema Kabbalah das Águas Primordiais!")
    print("Vamos configurar seu perfil inicial...")
    
    nome = input("Seu nome: ")
    experiencia = input("Nível de experiência (iniciante/intermediário/avançado): ")
    
    print(f"\nPerfeito, {nome}! Criando perfil {experiencia}...")
    
    # Configuração automática baseada no nível
    config = {
        'iniciante': {'rituais_simples': True, 'alertas_frequentes': True},
        'intermediário': {'rituais_complexos': True, 'analise_avancada': False},
        'avançado': {'acesso_total': True, 'personalizacao_avancada': True}
    }
    
    return config[experiencia.lower()]