from openai import OpenAI
import logging

logger = logging.getLogger()
client = OpenAI()


def generate_with_openai(prompt: str) -> str:
    response = client.responses.create(
        model="使用するモデル",
        input=prompt,
    )

    return response.output_text