import os
import openai

# Configuração da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta(prompt):
    """Gera uma resposta usando o modelo da OpenAI."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

if __name__ == "__main__":
    # Simula a leitura de uma issue do GitHub
    issue_title = "Dúvida sobre a Aula 1"
    issue_body = "Não entendi a relação entre os conceitos da primeira aula."
    
    prompt = f"Título da Dúvida: {issue_title}\n\nDescrição: {issue_body}\n\nBaseado no conhecimento do Instituto, qual seria a resposta?"
    
    resposta = gerar_resposta(prompt)
    
    print(f"Resposta do Mestre Digital:\n{resposta}")