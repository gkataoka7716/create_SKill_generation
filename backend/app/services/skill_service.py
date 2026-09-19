from app.prompts.skill_prompt import create_skill_prompt
from app.services import openai_service, gemini_service, ollama_service
from app.schemas.skill_schema import SkillGenerateRequest
from app.schemas.ai_schema import (
    GeminiModel,
    OllamaModel,
    OpenAIModel,
    ProviderType,
)
import logging

logger = logging.getLogger()


def generate_skill(request: SkillGenerateRequest):
    try:
        prompt = create_skill_prompt(request)

        logger.info("[Info] Skill.mdの生成を開始します")

        if request.ai_provider == ProviderType.OPENAI:
            response = openai_service.generate_with_openai(
                prompt,
                request.ai_model,
            )

        elif request.ai_provider == ProviderType.GEMINI:
            response = gemini_service.generate_with_gemini(
                prompt,
                request.ai_model,
            )

        elif request.ai_provider == ProviderType.OLLAMA:
            response = ollama_service.generate_with_ollama(
                prompt,
                request.ai_model,
            )

        return response

    except Exception as e:
        logger.exception("Skill.md生成中に予期しないエラーが発生しました")
        raise
