import pytest
from pydantic import ValidationError

from app.schemas.skill_schema import (
    SkillGenerateRequest,
    SkillGenerateResponse,
)

# ----------
#   共通化
# ----------


def create_valid_request(**overrides):
    data = {
        "name": "web-research",
        "description": "Web検索を行うSkill。",
        "instructions": ["Web検索する"],
        "ai_provider": "ollama",
        "ai_model": "llama3.2"
    }

    data.update(overrides)

    return SkillGenerateRequest(**data)


# --------------------
#   nameのバリデーション
# --------------------


@pytest.mark.parametrize(
    "name, is_valid",
    [
        # 正常系
        ("web-research", True),
        ("web123", True),
        ("123", True),
        ("web-123-research", True),
        ("a" * 64, True),
        # 異常系
        ("", False),
        (" ", False),
        ("　", False),
        ("a" * 65, False),
        ("Web-Research", False),
        ("web_research", False),
        ("web research", False),
        ("web--research", False),
        ("-web-research", False),
        ("web-research-", False),
    ],
)
def test_name_validation(name, is_valid):
    """nameの正常値と異常値をテストする"""

    if is_valid:
        request = create_valid_request(name=name)
        assert request.name == name
    else:
        with pytest.raises(ValidationError):
            create_valid_request(name=name)


# ---------------------------
#   descriptionのバリデーション
# ---------------------------


@pytest.mark.parametrize(
    "description, is_valid",
    [
        # 正常系
        ("a", True),
        ("Web検索を使って情報を調査するSkill。", True),
        ("a" * 1024, True),
        # 異常系
        ("", False),
        (" ", False),
        ("　", False),
        ("a" * 1025, False),
    ],
)
def test_description_validation(description, is_valid):
    """descriptionの正常値と異常値をテストする"""

    if is_valid:
        request = create_valid_request(description=description)
        assert request.description == description
    else:
        with pytest.raises(ValidationError):
            create_valid_request(description=description)


# ---------------------------
#   descriptionのバリデーション
# ---------------------------
@pytest.mark.parametrize(
    "instructions, is_valid",
    [
        # 正常系
        (["a"], True),
        (["a", "b"], True),
        (["a", "b", "c"], True),
        # 異常系
        ([], False),
        ([""], False),
        ([" "], False),
        (["　"], False),
        (["a", ""], False),
        (["a", " "], False),
        (["a", "　"], False),
        (["", "b", "c"], False),
        ([" ", "b", "c"], False),
        (["　", "b", "c"], False),
        (["a", "", "c"], False),
        (["a", " ", "c"], False),
        (["a", "　", "c"], False),
        (["a", "b", ""], False),
        (["a", "b", " "], False),
        (["a", "b", "　"], False),
    ],
)
def test_instructions_validation(instructions, is_valid):
    """instructionsの正常値と異常値をテストする"""

    if is_valid:
        request = create_valid_request(instructions=instructions)
        assert request.instructions == instructions
    else:
        with pytest.raises(ValidationError):
            create_valid_request(instructions=instructions)

# ------------------------
#   ai_providerのバリデーション
# ------------------------

@pytest.mark.parametrize(
    "ai_provider, is_valid",
    [
        # 正常系
        ("openai", True),
        ("gemini", True),
        ("ollama", True),
        # 異常系
        ("", False),
        ("invalid", False),
        ("OpenAI", False),
        ("open_ai", False),
    ],
)
def test_ai_provider_validation(ai_provider, is_valid):
    """ai_providerの正常値と異常値をテストする"""

    if is_valid:
        if ai_provider == "openai":
            ai_model = "gpt-5.6"
        elif ai_provider == "gemini":
            ai_model = "gemini-3.8-flash"
        else:
            ai_model = "llama3.2"

        request = create_valid_request(
            ai_provider=ai_provider,
            ai_model=ai_model,
        )

        assert request.ai_provider.value == ai_provider

    else:
        with pytest.raises(ValidationError):
            create_valid_request(
                ai_provider=ai_provider,
                ai_model="llama3.2",
            )


# ---------------------
#   ai_modelのバリデーション
# ---------------------

@pytest.mark.parametrize(
    "ai_provider, ai_model, is_valid",
    [
        # OpenAI
        ("openai", "gpt-5.6", True),
        ("openai", "invalid-model", False),

        # Gemini
        ("gemini", "gemini-3.8-flash", True),
        ("gemini", "invalid-model", False),

        # Ollama
        ("ollama", "llama3.2", True),
        ("ollama", "invalid-model", False),
    ],
)
def test_ai_model_validation(ai_provider, ai_model, is_valid):
    """ai_providerに対応したai_modelの正常値と異常値をテストする"""

    if is_valid:
        request = create_valid_request(
            ai_provider=ai_provider,
            ai_model=ai_model,
        )

        assert request.ai_provider.value == ai_provider
        assert request.ai_model == ai_model

    else:
        with pytest.raises(ValidationError):
            create_valid_request(
                ai_provider=ai_provider,
                ai_model=ai_model,
            )