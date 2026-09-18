最初は以下のような構成でもよい。

```md
---
name: skill-name
description: このSkillが何をするものなのか、いつ使うものなのか
---

# Skillの名前

## 手順

1. ○○を確認する。
2. ○○を実行する。
3. 結果を確認する。
```

最終的には以下の構成まで発展させたい
```md
---
name: {{skill_name}}
description: {{skill_description}}
---

# {{skill_title}}

## 概要

{{overview}}

## 使用する場面

{{when_to_use}}

## 手順

### Step 1: {{step1_title}}

{{step1_description}}

### Step 2: {{step2_title}}

{{step2_description}}

### Step 3: {{step3_title}}

{{step3_description}}

## ルール

{{rules}}

## 例

### 入力例

{{input_example}}

### 出力例

{{output_example}}

## 例外・注意事項

{{edge_cases}}
```