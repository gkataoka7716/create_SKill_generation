def create_skill_prompt(data):
    instructions = "\n".join(f"{index}. {instruction}" for index, instruction in enumerate(data.instructions, start=1))

    return f"""
あなたは、Agent Skills仕様に準拠したSKILL.mdを作成するアシスタントです。

以下の入力情報をもとに、実際に使用できるSKILL.mdを1つ作成してください。

【Skill名】
{data.name}

【説明】
{data.description}

【手順】
{instructions}

【作成ルール】
- SKILL.mdのFrontmatterを必ず先頭に記述してください。
- Frontmatterは以下の形式にしてください。

---
name: {data.name}
description: {data.description}
---

- `name` は入力された値をそのまま使用してください。変更・翻訳・言い換えをしないでください。
- `description` も入力された内容を基本的にそのまま使用してください。
- Markdown本文は日本語で作成してください。
- Frontmatterの後に、Skillの名前を見出しとして記述してください。
- 手順は `## 手順` の下に記述してください。
- 入力された手順を、意味を変えずにStep形式で整理してください。
- 手順の順番は入力された順番を維持してください。
- 入力されていない情報を勝手に追加しないでください。
- 現在のSKILL.mdでは「概要」「使用する場面」「ルール」「例」「例外・注意事項」などの項目は、入力情報に含まれていない限り追加しないでください。
- Skillの目的や動作内容について推測して、入力情報にない処理を追加しないでください。
- 手順の表現が多少簡潔になる程度の文章整理は構いませんが、意味を変更してはいけません。
- SKILL.mdとして正しく解釈できるMarkdownを出力してください。
- 出力はSKILL.mdの内容だけにしてください。
- 「以下がSKILL.mdです」などの説明文を付けないでください。
- ```md のようなコードフェンスで囲まないでください。

【出力形式】
以下のような形式で作成してください。

---
name: {data.name}
description: {data.description}
---

# {data.name}

## 手順

### Step 1

1つ目の手順

### Step 2

2つ目の手順

必要なStep数だけ続けてください。
"""
