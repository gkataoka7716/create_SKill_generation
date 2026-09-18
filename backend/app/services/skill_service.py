from app.prompts.skill_prompt import create_skill_prompt
from app.services.openai_service import generate_with_openai
from app.schemas.skill_schema import SkillGenerateRequest
import logging

logger = logging.getLogger()


def generate_skill(request: SkillGenerateRequest):
    try:
        prompt = create_skill_prompt(request)

        logger.info("[Info] Skill.mdの生成を開始します")
        response = generate_with_openai(prompt)

        return response

    except Exception as e:
        logger.exception("Skill.md生成中に予期しないエラーが発生しました")
        raise
