from unittest.mock import patch

import pytest

from app.schemas.skill_schema import SkillGenerateRequest
from app.services import skill_service


@pytest.fixture
def valid_request():
    """正常なSkillGenerateRequestを作成する"""

    return SkillGenerateRequest(
        name="web-research",
        description="Web検索を使って情報を調査するSkill。",
        instructions=[
            "ユーザーの質問を確認する",
            "必要な情報をWeb検索する",
        ],
        ai_provider="ollama",
        ai_model="llama3.2",
    )


@pytest.mark.parametrize(
    ("ai_provider", "ai_model", "service_path"),
    [
        (
            "openai",
            "gpt-5",
            "app.services.skill_service.openai_service.generate_with_openai",
        ),
        (
            "gemini",
            "gemini-2.5-flash",
            "app.services.skill_service.gemini_service.generate_with_gemini",
        ),
        (
            "ollama",
            "llama3.2",
            "app.services.skill_service.ollama_service.generate_with_ollama",
        ),
    ],
)
def test_generate_skill_success(
    valid_request,
    ai_provider,
    ai_model,
    service_path,
):
    """指定したAI Providerのサービスが呼び出されること"""

    valid_request.ai_provider = ai_provider
    valid_request.ai_model = ai_model

    mock_prompt = "生成用プロンプト"
    mock_response = "# Skill\n\n生成されたSkill.md"

    with (
        patch(
            "app.services.skill_service.create_skill_prompt",
            return_value=mock_prompt,
        ) as mock_create_prompt,
        patch(
            service_path,
            return_value=mock_response,
        ) as mock_generate,
    ):
        response = skill_service.generate_skill(valid_request)

    mock_create_prompt.assert_called_once_with(valid_request)
    mock_generate.assert_called_once_with(
        mock_prompt,
        valid_request.ai_model,
    )

    assert response == mock_response


def test_generate_skill_error(valid_request):
    """Skill.md生成中にエラーが発生した場合、例外が再送出されること"""

    valid_request.ai_provider = "openai"
    valid_request.ai_model = "gpt-5"

    error = Exception("OpenAI API error")

    with (
        patch(
            "app.services.skill_service.create_skill_prompt",
            return_value="生成用プロンプト",
        ),
        patch(
            "app.services.skill_service.openai_service.generate_with_openai",
            side_effect=error,
        ),
    ):
        with pytest.raises(Exception, match="OpenAI API error"):
            skill_service.generate_skill(valid_request)