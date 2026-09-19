## テスト

### Schemaの単体テスト

`SkillGenerateRequest`、`SkillGenerateResponse` のバリデーションテストを実行します。

```bash
docker compose -f docker-compose.dev.yaml exec backend pytest test/schemas/test_skill_schema.py -v
```

### 全テスト

プロジェクト内のすべてのpytestを実行します。

```bash
docker compose -f docker-compose.dev.yaml exec backend pytest -v
```

## コード整形

Blackを使用してPythonコードを整形します。

```bash
docker compose -f docker-compose.dev.yaml exec backend black .
```