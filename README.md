# Skill.md Generator

## 概要

Skill.mdを簡単に作成できるWebアプリケーションです。

ユーザーはWeb画面上のフォームに必要な情報を入力することで、Skill.mdの内容を作成できます。作成した内容はMarkdown形式でプレビューでき、完成したSkill.mdをファイルとしてダウンロードできます。

ログインや会員登録は不要で、誰でも利用できるシンプルな構成を想定しています。

## 主な機能

- Skill.mdの作成
- Skill.mdの編集
- Markdownプレビュー
- 入力内容のバリデーション
- Skill.mdファイルのダウンロード

## 開発目的

本プロジェクトでは、実際のWebサービス開発を想定し、クライアントからの要望をもとにした要件定義・画面設計・機能設計・実装・テストまでの開発工程を経験することを目的としています。

## 環境変数の設定

プロジェクト直下に `.env` を作成し、以下を設定します。

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_model
```

`.env` はGitにコミットしないでください。

## コンテナの起動

プロジェクトルートで以下を実行します。

```bash
docker compose -f docker-compose.dev.yaml up -d --build
```

## 起動確認

FastAPIのSwagger UIにアクセスします。

[http://localhost:8000/docs](http://localhost:8000/docs)

## Blackの実行

```bash
docker compose -f docker-compose.dev.yaml exec backend black .
```

## pytestの実行

```bash
docker compose -f docker-compose.dev.yaml exec backend pytest
```

## コンテナの停止

```bash
docker compose -f docker-compose.dev.yaml down
```

## コンテナの再起動

```bash
docker compose -f docker-compose.dev.yaml restart backend
```