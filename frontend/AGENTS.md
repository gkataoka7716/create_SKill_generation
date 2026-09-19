# AGENTS.md

このリポジトリのフロントエンドは、Next.js 16 + React 19 の構成で動作します。  
このプロジェクトは単一のアプリではなく、バックエンド API と分離した構成です。

## 重要な前提

- バックエンドは FastAPI で、Docker Compose で起動する
- フロントエンドは Next.js で、`npm run dev` で起動する
- API のベース URL は `NEXT_PUBLIC_API_URL` で管理する
- ルート URL は `/create` にリダイレクトされる

## 実際の構成

- API: `http://localhost:8000`
- Frontend: `http://localhost:3000`
- API のベース URL 変数: `NEXT_PUBLIC_API_URL=http://localhost:8000/v1`

## 必須の環境変数

`frontend/.env` で次を設定してください。

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/v1
```

バックエンドの環境変数はリポジトリ直下の `.env` に置き、以下を設定してください。

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_model
```

## API 契約

フロントエンドが呼び出す主要 API は次の通りです。

- `POST /v1/skills/generate`

リクエスト例:

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

レスポンス例:

```json
{
  "content": "---\nname: web-research\n..."
}
```

## フロントエンドの作業ルール

- 画面は `frontend/app/` 配下に配置する
- API 呼び出しは `frontend/api/skill.ts` に集約する
- バリデーションは `frontend/utils/` 配下の関数を使う
- `frontend/app/page.tsx` はルートページのリダイレクト専用である
- 画面固有のロジックは `components/` に分離する

## 代表ファイル

- `frontend/app/page.tsx` — ルート遷移
- `frontend/app/create/page.tsx` — Skill 作成画面
- `frontend/api/skill.ts` — API 呼び出し
- `frontend/utils/NameInputValidation.ts` — name の validation
- `frontend/utils/DescriptionInputValidation.ts` — description の validation
- `frontend/utils/InstructionsInputValidation.ts` — instructions の validation

## 開発コマンド

```bash
cd frontend
npm install
npm run dev
npm run lint
npm run build
```

## 注意事項

- Docker Compose はバックエンド用であり、フロントエンドを同時に起動する設定ではない
- API 仕様を変える場合は、バックエンドの schema とフロントエンドの API 呼び出しを同時に更新する
- `NEXT_PUBLIC_API_URL` はフロントエンド用の環境変数であり、OpenAI API Key ではない

