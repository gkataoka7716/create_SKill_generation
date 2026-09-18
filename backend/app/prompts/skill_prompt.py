def create_skill_prompt(data):
    return f"""
あなたはSkill.mdを作成するアシスタントです。

Skill名:
{data.name}

説明:
{data.description}

指示:
{data.instructions}

上記の情報をもとに、Skill.mdを作成してください。
"""