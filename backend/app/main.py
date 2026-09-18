from contextlib import asynccontextmanager

from fastapi import FastAPI

# Router
# from routers import skill_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPIの起動時・終了時に実行する処理。

    起動時：
    - DBの初期化
    - 必要なファイル・ディレクトリの作成
    - 初期データの登録

    終了時：
    - DB接続の終了
    - リソースの解放
    """

    # ===== 起動時処理 =====
    print("Skill.md Generator APIを起動しました")

    yield

    # ===== 終了時処理 =====
    print("Skill.md Generator APIを終了します")


app = FastAPI(
    title="Skill.md Generator API",
    description="Skill.mdを作成・生成するためのAPI",
    version="1.0.0",
    lifespan=lifespan,
)


# Routerを登録
# app.include_router(skill_router.router)


@app.get("/")
def root():
    """APIの動作確認用エンドポイント"""
    return {"message": "Skill.md Generator API"}