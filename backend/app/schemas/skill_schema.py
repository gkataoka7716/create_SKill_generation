from pydantic import BaseModel


class SkillGenerateRequest(BaseModel):
    """Skill.md生成APIのリクエスト"""

    name: str
    description: str
    instructions: str


class SkillGenerateResponse(BaseModel):
    """Skill.md生成APIのレスポンス"""

    content: str