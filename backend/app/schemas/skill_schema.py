from pydantic import BaseModel, Field
from typing import Annotated

class SkillGenerateRequest(BaseModel):
    """Skill.md生成APIのリクエスト"""

    name: str = Field(min_length=1, max_length=64, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",)
    description: str = Field(min_length=1, max_length=1024)
    instructions: list[Annotated[str, Field(min_length=1)]] = Field(min_length=1)


class SkillGenerateResponse(BaseModel):
    """Skill.md生成APIのレスポンス"""

    content: str