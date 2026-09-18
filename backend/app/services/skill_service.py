from prompts.skill_prompt import create_skill_prompt
from services.openai_service import generate_with_openai
from app.schemas.skill_schema import SkillGenerateRequest
import logging

logger = logging.getLogger()

def generate_skill(request: SkillGenerateRequest):
    try:
        prompt = create_skill_prompt(request)

        response = generate_with_openai(prompt)

        return response

    except Exception as e:
        raise 