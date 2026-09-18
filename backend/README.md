# Backend API

## Skill.md生成

### エンドポイント

```text
POST /v1/skills/generate
```

### 概要

入力されたSkill名、説明、手順をもとにSkill.mdを生成します。

### リクエスト

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

### リクエスト項目

| 項目 | 型 | 必須 | 説明 |
| --- | --- | --- | --- |
| `name` | `string` | ✅ | Skill名 |
| `description` | `string` | ✅ | Skillの説明 |
| `instructions` | `string[]` | ✅ | Skillの手順 |

### バリデーション

#### `name`

- 1～64文字
- 小文字英字・数字・ハイフンのみ使用可能
- 先頭・末尾にハイフンを使用しない
- ハイフンを連続して使用しない

#### `description`

- 1～1024文字

#### `instructions`

- 1つ以上必要
- 各要素は1文字以上

### レスポンス

```json
{
  "content": "---\nname: web-research\n..."
}
```

| 項目 | 型 | 説明 |
| --- | --- | --- |
| `content` | `string` | 生成されたSkill.mdの内容 |

### エラー

#### 422 Unprocessable Entity

リクエストのバリデーションに失敗した場合に返します。

例：

```json
{
  "detail": [
    {
      "type": "too_short",
      "loc": [
        "body",
        "instructions"
      ],
      "msg": "List should have at least 1 item after validation, not 0"
    }
  ]
}
```

#### 500 Internal Server Error

Skill.mdの生成処理で予期しないエラーが発生した場合に返します。