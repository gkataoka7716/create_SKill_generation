from ollama import generate


def generate_with_ollama(prompt: str, model: str) -> str:
    """Ollamaを使用してプロンプトを実行する"""

    response = generate(
        model=model,
        prompt=prompt,
    )

    return response["response"]