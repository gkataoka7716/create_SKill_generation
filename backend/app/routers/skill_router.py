import logging

from fastapi import APIRouter, HTTPException

from app.schemas.skill_schema import (
    SkillGenerateRequest,
    SkillGenerateResponse,
)
from app.services import skill_service

logger = logging.getLogger()

router = APIRouter(
    prefix="/skills",
    tags=["skills"],
)


@router.post(
    "/generate",
    response_model=SkillGenerateResponse,
)
def generate_skill(request: SkillGenerateRequest):
    """
    Skill.mdを生成するAPI。
    """
    try:
        logger.info("[Info] Skill.mdの生成を開始します。")

        response = skill_service.generate_skill(request)

        logger.info("[Info] Skill.mdの生成が完了しました。")

        return SkillGenerateResponse(
            content=response,
        )

    except Exception:
        logger.exception("[Error] Skill.mdの生成中にエラーが発生しました。")

        raise HTTPException(
            status_code=500,
            detail="Skill.mdの生成に失敗しました。",
        )
