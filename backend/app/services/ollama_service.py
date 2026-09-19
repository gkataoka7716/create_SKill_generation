from ollama import Client


client = Client(host="http://ollama:11434")


def generate_with_ollama(prompt: str, model: str):
    response = client.generate(
        model=model,
        prompt=prompt,
    )
    
    return response["response"]