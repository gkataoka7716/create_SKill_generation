from pydantic import BaseModel, Field, field_validator
from typing import Annotated


class SkillGenerateRequest(BaseModel):
    """Skill.md生成APIのリクエスト"""

    name: str = Field(
        min_length=1,
        max_length=64,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
    )
    description: str = Field(min_length=1, max_length=1024)
    instructions: list[Annotated[str, Field(min_length=1)]] = Field(min_length=1)

    @field_validator("name", "description", mode="before")
    @classmethod
    def strip_string(cls, value: str) -> str:
        return value.strip()

    @field_validator("instructions", mode="before")
    @classmethod
    def strip_instructions(cls, value: list[str]) -> list[str]:
        return [instruction.strip() for instruction in value]


class SkillGenerateResponse(BaseModel):
    """Skill.md生成APIのレスポンス"""

    content: str
