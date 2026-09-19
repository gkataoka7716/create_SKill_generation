from google import genai


client = genai.Client()


def generate_with_gemini(prompt: str, model: str) -> str:
    """Geminiを使用してプロンプトを実行する"""

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return response.text