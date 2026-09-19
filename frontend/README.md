# 概要

ユーザー情報の登録・編集を行うWebアプリケーションのフロントエンドです。

## 画面

| URL | 画面 |
|---|---|
| `/create` | Skill.mdの作成 |
| `/xxxxx` | xxxxx |

## バリデーション

### name

- 1〜64文字
- 使用可能な文字：小文字、数字、`_`

### 説明

- 1〜1024文字

### Instructions

- 1件以上必要
- 複数件ある場合、空欄のInstructionsは登録不可

## 実行コマンド

### パッケージインストール

```bash
npm install
```

### 開発サーバー起動

```bash
npm run dev
```

### 本番用ビルド

```bash
npm run build
```

### 本番サーバー起動

```bash
npm run start
```

### Lint

```bash
npm run lint
```

### Prettier

```bash
npm run format
```