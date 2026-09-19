"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { RotateCcw } from "lucide-react";

import NameInput from "@/components/nameInput";
import DescriptionInput from "@/components/descriptionInput";
import InstructionsInput from "@/components/InstructionsInput";
import AIModelSelect from "@/components/aiModelSelect";

import { getNameError } from "@/utils/NameInputValidation";
import { getDescriptionError } from "@/utils/DescriptionInputValidation";
import { getInstructionsError } from "@/utils/InstructionsInputValidation";
import { createSkill } from "@/api/skill";

type Instruction = {
  id: number;
  value: string;
};

type AIModel = {
  provider: string;
  model: string;
  label: string;
};

export default function PromptCreatePage() {
  const router = useRouter();
  const [selectedModel, setSelectedModel] = useState<AIModel>({
    provider: "ollama",
    model: "llama3.2",
    label: "Llama 3.2",
  });

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const [instructions, setInstructions] = useState<Instruction[]>([
    {
      id: 1,
      value: "",
    },
  ]);

  // Instructionsを初期状態に戻すためのキー
  const [instructionsResetKey, setInstructionsResetKey] = useState(0);
  const [isHydrated, setIsHydrated] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

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
  
  useEffect(() => {
    const data = sessionStorage.getItem("skillInput");

    const hydrationTimer = window.setTimeout(() => {
      if (!data) {
        setIsHydrated(true);
        return;
      }

      try {
        const saved = JSON.parse(data);

        setName(saved.name ?? "");
        setDescription(saved.description ?? "");
        setInstructions(
          saved.instructions ?? [{ id: Date.now(), value: "" }],
        );
        setSelectedModel(
          saved.selectedModel ?? {
            provider: "ollama",
            model: "llama3.2",
            label: "Llama 3.2",
          },
        );
      } catch (error) {
        console.error("入力内容の復元に失敗しました:", error);
      } finally {
        setIsHydrated(true);
      }
    }, 0);

    return () => window.clearTimeout(hydrationTimer);
  }, []);

  // すべてリセット
  const resetAll = () => {
    setName("");
    setDescription("");

    setInstructions([
      {
        id: Date.now(),
        value: "",
      },
    ]);

    // InstructionsInputを再生成して初期状態に戻す
    setInstructionsResetKey((prev) => prev + 1);

    // AIモデルは初期値のOllama / Llama 3.2のまま
    setSelectedModel({
      provider: "ollama",
      model: "llama3.2",
      label: "Llama 3.2",
    });
  };

  const handleCreate = async () => {
    if (!isFormValid || isSubmitting) {
      return;
    }

    const inputSnapshot = {
      name,
      description,
      instructions: instructions.map((instruction) => ({ ...instruction })),
      selectedModel: { ...selectedModel },
    };

    const data = {
      name: inputSnapshot.name.trim(),
      description: inputSnapshot.description.trim(),
      instructions: inputSnapshot.instructions.map(
        (instruction) => instruction.value.trim(),
      ),
      ai_provider: inputSnapshot.selectedModel.provider,
      ai_model: inputSnapshot.selectedModel.model,
    };

    // 再修正用に入力内容を保存
    sessionStorage.setItem("skillInput", JSON.stringify(inputSnapshot));
    setIsSubmitting(true);

    try {
      const result = await createSkill(data);

      sessionStorage.setItem(
        "skillResult",
        JSON.stringify(result),
      );

      router.push("/result");
    } catch (error) {
      console.error(error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 px-4 py-10">
      <div className="mx-auto w-full max-w-3xl">
        <div className="rounded-xl bg-white shadow-sm">
          {/* ヘッダー */}
          <div className="flex items-center justify-between border-b border-gray-200 px-8 py-6">
            <h1 className="text-2xl font-bold text-gray-800">
              プロンプト作成
            </h1>

            <AIModelSelect
              value={selectedModel.model}
              onChange={setSelectedModel}
            />
          </div>

          <div className="space-y-8 p-8">
            {/* 名前 */}
            <NameInput value={name} onChange={setName} />

            {/* 説明 */}
            <DescriptionInput
              value={description}
              onChange={setDescription}
            />

            {/* Instructions */}
            <InstructionsInput
              key={instructionsResetKey}
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
                disabled={!isHydrated || !isFormValid || isSubmitting}
                className="rounded-md bg-blue-600 px-8 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-gray-300"
              >
                {isSubmitting ? "作成中..." : "作成"}
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}