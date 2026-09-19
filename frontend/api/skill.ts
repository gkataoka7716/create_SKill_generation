type CreateSkillRequest = {
  name: string;
  description: string;
  instructions: string[];
};

type CreateSkillResponse = {
  content: string;
};

export async function createSkill(
  data: CreateSkillRequest,
): Promise<CreateSkillResponse> {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/skills/generate`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    },
  );

  if (!response.ok) {
    throw new Error("Skillの作成に失敗しました");
  }

  return response.json();
}
