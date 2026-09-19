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
    )


def test_generate_skill(valid_request):
    """Skill.mdを正常に生成して結果を返すこと"""

    mock_prompt = "生成用プロンプト"
    mock_response = "# Skill\n\n生成されたSkill.md"

    with (
        patch(
            "app.services.skill_service.create_skill_prompt",
            return_value=mock_prompt,
        ) as mock_create_prompt,
        patch(
            "app.services.skill_service.generate_with_openai",
            return_value=mock_response,
        ) as mock_generate,
    ):
        response = skill_service.generate_skill(valid_request)

    mock_create_prompt.assert_called_once_with(valid_request)
    mock_generate.assert_called_once_with(mock_prompt)

    assert response == mock_response


def test_generate_skill_error(valid_request):
    """Skill.md生成中にエラーが発生した場合、例外が再送出されること"""

    error = Exception("OpenAI API error")

    with patch(
        "app.services.skill_service.create_skill_prompt",
        return_value="生成用プロンプト",
    ), patch(
        "app.services.skill_service.generate_with_openai",
        side_effect=error,
    ):
        with pytest.raises(Exception, match="OpenAI API error"):
            skill_service.generate_skill(valid_request)