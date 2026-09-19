from typing import Annotated, Any

from pydantic import BaseModel, Field, field_validator, model_validator

from app.schemas.ai_schema import (
    GeminiModel,
    OllamaModel,
    OpenAIModel,
    ProviderType,
)


class SkillGenerateRequest(BaseModel):
    """Skill.md生成APIのリクエスト"""

    name: str = Field(
        min_length=1,
        max_length=64,
        pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
        examples=["web-research"],
    )

    description: str = Field(
        min_length=1,
        max_length=1024,
        examples=["Web検索を使って情報を調査し、根拠付きで整理するSkill。"],
    )

    instructions: list[Annotated[str, Field(min_length=1)]] = Field(
        min_length=1,
        examples=[
            [
                "ユーザーの質問を確認する",
                "必要な情報をWeb検索する",
                "複数の情報源を比較する",
                "根拠を示して回答する",
            ]
        ],
    )

    ai_provider: ProviderType
    ai_model: str

    @field_validator("name", "description", mode="before")
    @classmethod
    def strip_string(cls, value: Any) -> Any:
        if isinstance(value, str):
            return value.strip()

        return value

    @field_validator("instructions", mode="before")
    @classmethod
    def strip_instructions(cls, value: Any) -> Any:
        if isinstance(value, list):
            return [instruction.strip() if isinstance(instruction, str) else instruction for instruction in value]

        return value

    @model_validator(mode="after")
    def validate_ai_model(self):
        valid_models = {
            ProviderType.OPENAI: OpenAIModel,
            ProviderType.GEMINI: GeminiModel,
            ProviderType.OLLAMA: OllamaModel,
        }

        model_type = valid_models[self.ai_provider]

        if self.ai_model not in [model.value for model in model_type]:
            raise ValueError(f"{self.ai_provider.value}では利用できないモデルです: " f"{self.ai_model}")

        return self


class SkillGenerateResponse(BaseModel):
    """Skill.md生成APIのレスポンス"""

    content: str
