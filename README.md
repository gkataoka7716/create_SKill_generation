# Skill.md Generator

## 概要

Skill.md Generator は、Skill の名前・説明・手順を入力すると、OpenAI を利用して Skill.md を生成する Web アプリです。

このリポジトリは、バックエンド API とフロントエンドの 2 つで構成されています。

- Backend: FastAPI による API サーバー
- Frontend: Next.js によるフォーム画面

ユーザーはフロントエンドのフォームに必要事項を入力し、バックエンド API が Skill.md を生成します。

## 構成

- backend
  - FastAPI API
  - OpenAI を使った Skill.md 生成
- frontend
  - Next.js フロントエンド
  - 入力フォーム
  - バリデーション
  - API 呼び出し
- docker-compose.dev.yaml
  - バックエンドのみを起動する開発用設定

## 主な機能

- Skill 名の入力
- Skill 説明の入力
- 手順（instructions）の入力
- フォームのバリデーション
- OpenAI による Skill.md 生成
- 生成された Skill.md の取得

## 必要な環境

- Docker / Docker Compose
- Node.js / npm
- OpenAI API Key

## 環境変数

### Backend 用

プロジェクト直下の `.env` に以下を設定します。

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_model
```

- `.env` は Git にコミットしないでください
- `OPENAI_API_KEY` はバックエンド側で使用されます
- `OPENAI_MODEL` はバックエンド側の OpenAI モデル名です

### Frontend 用

フロントエンドの `.env` に以下を設定します。

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/v1
```

この値は、フロントエンドがバックエンドの API ベース URL を呼び出すために必要です。

## 起動方法

### 1. Backend の起動

プロジェクトルートで実行します。

```bash
docker compose -f docker-compose.dev.yaml up -d --build
```

これにより FastAPI が `http://localhost:8000` で起動します。

### 2. Frontend の起動

別途、フロントエンド側を起動します。

```bash
cd frontend
npm install
npm run dev
```

デフォルトでは `http://localhost:3000` で起動します。

## 動作確認

### Backend API の確認

FastAPI の Swagger UI にアクセスします。

- http://localhost:8000/docs

また、ヘルスチェック用エンドポイント:

- http://localhost:8000/health

### Frontend の確認

- http://localhost:3000

ルートページは `/create` へリダイレクトされます。

## API 仕様

### POST /v1/skills/generate

Skill.md を生成します。

### リクエスト例

```json
{
  "name": "web-research",
  "description": "Web検索を使って情報を調査し、根拠付きで整理するSkill。",
  "instructions": [
    "ユーザーの質問を確認する",
    "必要な情報をWeb検索する",
    "複数の情報源を比較する",
    "根拠を示して回答する"
  ]
}
```

### バリデーション

- `name`
  - 1〜64文字
  - 小文字英字・数字・ハイフンのみ
  - 先頭・末尾・連続したハイフンは不可

- `description`
  - 1〜1024文字

- `instructions`
  - 1件以上必須
  - 各項目は1文字以上

### レスポンス例

```json
{
  "content": "---\nname: web-research\n..."
}
```

## 開発用コマンド

### Backend

```bash
docker compose -f docker-compose.dev.yaml exec backend black .
docker compose -f docker-compose.dev.yaml exec backend pytest
```

### Frontend

```bash
cd frontend
npm run lint
npm run build
```

## 停止

```bash
docker compose -f docker-compose.dev.yaml down
```

## 補足

このリポジトリでは、バックエンドとフロントエンドが分離した構成です。
Docker Compose はバックエンドだけを起動するため、開発時はフロントエンドも別途起動してください。
