from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ollama import AsyncClient

from app.routers import skill_router


logger = logging.getLogger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI起動時・終了時に実行する処理。
    """

    # ===== 起動時処理 =====
    logger.info("[info] Skill.md Generator APIを起動しました")

    yield

    # ===== 終了時処理 =====
    logger.info("[info] Skill.md Generator APIを終了します")


app = FastAPI(
    title="Skill.md Generator API",
    description="Skill.mdを作成・生成するためのAPI",
    version="1.0.0",
    lifespan=lifespan,
)


# ===== CORS設定 =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===== API Version 1 =====
app.include_router(
    skill_router.router,
    prefix="/v1",
)


@app.get("/health")
def root():
    """APIの動作確認用エンドポイント"""
    return {"message": "Skill.md Generator API"}


@app.post("/test/ollama")
async def test_ollama():
    client = AsyncClient(host="http://ollama:11434")

    response = await client.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": "こんにちは。1+1はいくつですか？",
            }
        ],
    )

    return {
        "response": response["message"]["content"],
    }