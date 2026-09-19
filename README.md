# Skill.md Generator

## 概要

Skill.md Generator は、Skill の名前・説明・手順と利用する AI Provider / Model を入力すると、Skill.md を生成する Web アプリです。
ユーザーはフロントエンドのフォームに必要事項を入力し、バックエンド API が OpenAI、Gemini、または Ollama を使って Skill.md を生成します。

## 構成

- `backend`
  - FastAPI API
  - AI Provider の選択と Skill.md 生成
- `frontend`
  - Next.js フロントエンド
  - 入力フォーム、バリデーション、生成結果表示
- `ollama`
  - Docker Compose で起動するローカル AI 実行環境
- `docker-compose.dev.yaml`
  - Backend と Ollama を起動する開発用設定

## 主な機能

- Skill 名、説明、手順の入力
- AI Provider / Model の選択
- フォームのバリデーション
- OpenAI、Gemini、Ollama による Skill.md 生成
- 生成された Skill.md の表示

## 対応 AI Provider / Model

| Provider | Model |
| --- | --- |
| OpenAI | `gpt-5.6`, `gpt-5.6-mini` |
| Gemini | `gemini-3.8-flash`, `gemini-3.7-flash` |
| Ollama | `llama3.2`, `qwen3-vl` |

`ai_provider` と `ai_model` の組み合わせはバックエンドで検証されます。

## 必要な環境

- Docker / Docker Compose
- Node.js / npm
- 利用する AI Provider の API キーまたは Ollama のモデル

## 環境変数

### Backend 用

プロジェクト直下の `.env` に、利用する外部 Provider の API キーを設定します。

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

- `.env` は Git にコミットしないでください。
- OpenAI または Gemini を利用する場合は、対応する API キーが必要です。
- Ollama は Compose 内の `http://ollama:11434` に接続します。

### Frontend 用

`frontend/.env.local` にバックエンド API のベース URLを設定します。

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/v1
```

## 起動方法

### 1. Backend と Ollama の起動

プロジェクトルートで実行します。

```bash
docker compose -f docker-compose.dev.yaml up -d --build
```

Backend は `http://localhost:8000`、Ollama は `http://localhost:11434` で起動します。

### 2. Ollama モデルの準備

利用するモデルを Ollama コンテナへ取得します。

```bash
docker compose -f docker-compose.dev.yaml exec ollama ollama pull llama3.2
```

`qwen3-vl` を利用する場合は、モデル名を `qwen3-vl` に変更してください。

### 3. Frontend の起動

別のターミナルで実行します。

```bash
cd frontend
npm install
npm run dev
```

Frontend は通常 `http://localhost:3000` で起動します。ルートページは `/create` へリダイレクトされます。

Backend をホスト上で単体起動する場合は、Ollama 接続先が Docker 内のホスト名 `ollama` に固定されているため、Ollama の接続設定に注意してください。

## 動作確認

- Frontend: http://localhost:3000
- Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## API 仕様

### `POST /v1/skills/generate`

指定した Provider と Model で Skill.md を生成します。

#### リクエスト例

```json
{
  "name": "web-research",
  "description": "Web検索を使って情報を調査し、根拠付きで整理するSkill。",
  "instructions": [
    "ユーザーの質問を確認する",
    "必要な情報をWeb検索する",
    "複数の情報源を比較する",
    "根拠を示して回答する"
  ],
  "ai_provider": "ollama",
  "ai_model": "llama3.2"
}
```

#### レスポンス例

```json
{
  "content": "---\nname: web-research\n..."
}
```

### `GET /health`

API のヘルスチェックを実行します。

### `POST /test/ollama`

Ollama の疎通を確認します。`llama3.2` を使用します。

## バリデーションとエラー

- `name`
  - 1〜64文字
  - 小文字英字・数字・ハイフンのみ
  - 先頭・末尾・連続したハイフンは不可
- `description`
  - 1〜1024文字
- `instructions`
  - 1件以上必須
  - 各項目は1文字以上
- `ai_provider` と `ai_model`
  - 対応している組み合わせであることが必須

入力バリデーションエラーは `422`、AI生成処理のエラーは `500` を返します。
Frontend からの接続は `http://localhost:3000` のみ CORS で許可されています。

## 開発用コマンド

### Backend

Docker Compose を利用する場合:

```bash
docker compose -f docker-compose.dev.yaml exec backend black .
docker compose -f docker-compose.dev.yaml exec backend python -m pytest -v
```

Backend を直接起動する場合:

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm run lint
npm run build
npm run start
npm run format
```

Frontend には現在、テスト用の npm script はありません。

## 停止

```bash
docker compose -f docker-compose.dev.yaml down
```

## 補足

Backend と Frontend は分離しており、Docker Compose は Backend と Ollama のみを起動します。Frontend は別途起動してください。

