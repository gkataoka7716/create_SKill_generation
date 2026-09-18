from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import skill_router
import logging

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


# API Version 1
app.include_router(
    skill_router.router,
    prefix="/v1",
)


@app.get("/health")
def root():
    """APIの動作確認用エンドポイント"""
    return {"message": "Skill.md Generator API"}
