import os
from openai import OpenAI
import logging

logger = logging.getLogger()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = os.getenv("OPENAI_MODEL")

def generate_with_openai(prompt: str) -> str:
    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text