"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";

import NameInput from "@/components/nameInput";
import DescriptionInput from "@/components/descriptionInput";
import InstructionsInput from "@/components/InstructionsInput";
import { getNameError } from "@/utils/NameInputValidation";
import { getDescriptionError } from "@/utils/DescriptionInputValidation";
import { getInstructionsError } from "@/utils/InstructionsInputValidation";
import { createSkill } from "@/api/skill";

type Instruction = {
  id: number;
  value: string;
};

export default function PromptCreatePage() {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const [instructions, setInstructions] = useState<Instruction[]>([
    {
      id: 1,
      value: "",
    },
  ]);

  // バリデーションエラー
  const nameError = getNameError(name);
  const descriptionError = getDescriptionError(description);

  const instructionsError = getInstructionsError(
    instructions.map((instruction) => instruction.value),
  );

  // Instructionsが1件以上入力されているか
  const hasInstructions = instructions.some(
    (instruction) => instruction.value.trim() !== "",
  );

  // 空のInstructionsが存在するか
  const hasEmptyInstruction = instructions.some(
    (instruction) => instruction.value.trim() === "",
  );

  // 作成可能か
  const isFormValid =
    name.trim() !== "" &&
    description.trim() !== "" &&
    nameError === null &&
    descriptionError === null &&
    hasInstructions &&
    !hasEmptyInstruction &&
    instructionsError === null;

  const resetAll = () => {
    setName("");
    setDescription("");
    setInstructions([
      {
        id: Date.now(),
        value: "",
      },
    ]);
  };

  const handleCreate = async () => {
    if (!isFormValid) {
      return;
    }

    const data = {
      name: name.trim(),
      description: description.trim(),
      instructions: instructions.map((instruction) => instruction.value.trim()),
    };

    try {
      const result = await createSkill(data);

      console.log("作成成功:", result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 px-4 py-10">
      <div className="mx-auto w-full max-w-3xl">
        <div className="rounded-xl bg-white shadow-sm">
          {/* ヘッダー */}
          <div className="border-b border-gray-200 px-8 py-6">
            <h1 className="text-2xl font-bold text-gray-800">プロンプト作成</h1>
          </div>

          <div className="space-y-8 p-8">
            {/* 名前 */}
            <NameInput value={name} onChange={setName} />

            {/* 説明 */}
            <DescriptionInput value={description} onChange={setDescription} />

            {/* Instructions */}
            <InstructionsInput
              value={instructions}
              onChange={setInstructions}
            />

            {/* フッター */}
            <div className="flex items-center justify-between border-t border-gray-200 pt-6">
              {/* すべてリセット */}
              <button
                type="button"
                onClick={resetAll}
                className="flex items-center gap-1.5 rounded-md px-3 py-2 text-sm text-gray-500 transition hover:bg-gray-100 hover:text-gray-700"
              >
                <RotateCcw size={16} />
                すべてリセット
              </button>

              {/* 作成 */}
              <button
                type="button"
                onClick={handleCreate}
                disabled={!isFormValid}
                className="rounded-md bg-blue-600 px-8 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-gray-300"
              >
                作成
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
