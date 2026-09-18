from fastapi import APIRouter

from app.schemas.skill_schema import (
    SkillGenerateRequest,
    SkillGenerateResponse,
)
from app.services import skill_service
import logging

logger = logging.getLogger()
router = APIRouter(prefix="/skills", tags=["skills"],)

@router.post("/generate", response_model=SkillGenerateResponse,)
def generate_skill(request: SkillGenerateRequest):
    """
    Skill.mdを生成するAPI。
    """
    try:
        response = skill_service.generate_skill(request)

        return SkillGenerateResponse(
            content="生成されたSkill.mdの内容"
        )

    except Exception as e:
        return e
