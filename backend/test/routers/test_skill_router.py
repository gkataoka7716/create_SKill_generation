from unittest.mock import patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routers.skill_router import router


@pytest.fixture
def client():
    """テスト用FastAPIアプリを作成する"""

    app = FastAPI()
    app.include_router(router)

    return TestClient(app)


def test_generate_skill(client):
    """Skill.mdを正常に生成できること"""

    request_data = {
        "name": "web-research",
        "description": "Web検索を使って情報を調査するSkill。",
        "instructions": [
            "ユーザーの質問を確認する",
            "必要な情報をWeb検索する",
        ],
        "ai_provider": "ollama",
        "ai_model": "llama3.2",
    }

    mock_response = "# Skill\n\n生成されたSkill.md"

    with patch(
        "app.routers.skill_router.skill_service.generate_skill",
        return_value=mock_response,
    ) as mock_generate_skill:
        response = client.post(
            "/skills/generate",
            json=request_data,
        )

    assert response.status_code == 200
    assert response.json() == {
        "content": mock_response,
    }

    mock_generate_skill.assert_called_once()


def test_generate_skill_passes_request(client):
    """Serviceに正しいリクエストが渡されること"""

    request_data = {
        "name": "web-research",
        "description": "Web検索を使って情報を調査するSkill。",
        "instructions": [
            "ユーザーの質問を確認する",
        ],
        "ai_provider": "ollama",
        "ai_model": "llama3.2",
    }

    with patch(
        "app.routers.skill_router.skill_service.generate_skill",
        return_value="# Skill",
    ) as mock_generate_skill:
        response = client.post(
            "/skills/generate",
            json=request_data,
        )

    assert response.status_code == 200

    request = mock_generate_skill.call_args.args[0]

    assert request.name == request_data["name"]
    assert request.description == request_data["description"]
    assert request.instructions == request_data["instructions"]


def test_generate_skill_error(client):
    """Serviceでエラーが発生した場合に500を返すこと"""

    request_data = {
        "name": "web-research",
        "description": "Web検索を使って情報を調査するSkill。",
        "instructions": [
            "ユーザーの質問を確認する",
        ],
        "ai_provider": "ollama",
        "ai_model": "llama3.2",
    }

    with patch(
        "app.routers.skill_router.skill_service.generate_skill",
        side_effect=Exception("Service error"),
    ):
        response = client.post(
            "/skills/generate",
            json=request_data,
        )

    assert response.status_code == 500
    assert response.json() == {
        "detail": "Skill.mdの生成に失敗しました。",
    }
