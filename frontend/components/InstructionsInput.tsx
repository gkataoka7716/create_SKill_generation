"use client";

import { useState } from "react";
import { Plus, RotateCcw, Trash2 } from "lucide-react";

import HelpPopover from "@/components/HelpPopover";
import { getInstructionsError } from "@/utils/InstructionsInputValidation";

type Instruction = {
  id: number;
  value: string;
};

type InstructionsInputProps = {
  value: Instruction[];
  onChange: (value: Instruction[]) => void;
};

type DeletedInstruction = {
  instruction: Instruction;
  index: number;
};

export default function InstructionsInput({
  value,
  onChange,
}: InstructionsInputProps) {
  // 直前に削除した1件だけ保持
  const [deletedInstruction, setDeletedInstruction] =
    useState<DeletedInstruction | null>(null);

  const addInstruction = () => {
    onChange([
      ...value,
      {
        id: Date.now(),
        value: "",
      },
    ]);
  };

  const updateInstruction = (id: number, text: string) => {
    onChange(
      value.map((instruction) =>
        instruction.id === id
          ? { ...instruction, value: text }
          : instruction,
      ),
    );
  };

  const deleteInstruction = (id: number) => {
    const index = value.findIndex(
      (instruction) => instruction.id === id,
    );

    if (index === -1) {
      return;
    }

    // 削除した行を保存
    setDeletedInstruction({
      instruction: value[index],
      index,
    });

    // 最低1行は残す
    if (value.length === 1) {
      onChange([
        {
          ...value[0],
          value: "",
        },
      ]);
      return;
    }

    onChange(value.filter((instruction) => instruction.id !== id));
  };

  const restoreInstruction = () => {
    if (!deletedInstruction) {
      return;
    }

    const { instruction, index } = deletedInstruction;

    const restoredInstructions = [...value];

    restoredInstructions.splice(index, 0, instruction);

    onChange(restoredInstructions);

    // 元に戻したらUndoは1回で終了
    setDeletedInstruction(null);
  };

  const instructionsError = getInstructionsError(
    value.map((instruction) => instruction.value),
  );

  return (
    <div>
      {/* ラベル */}
      <div className="mb-3 flex items-center">
        <h2 className="text-sm font-semibold text-gray-700">
          Instructions
        </h2>

        <span className="text-xs font-medium text-red-500">
          *
        </span>

        <span className="ml-2">
          <HelpPopover
            title="Instructionsについて"
            description="AIに実行してほしい手順を、1行ずつ入力してください。最低1つ必要で、空欄の手順は登録できません。上から順番に実行してほしい内容を入力してください。"
          />
        </span>
      </div>

      {/* 入力行 */}
      <div className="space-y-3">
        {value.map((instruction, index) => {
          const hasError =
            value.length > 1 &&
            instruction.value.trim().length === 0;

          return (
            <div
              key={instruction.id}
              className="flex items-center gap-2"
            >
              {/* 行番号 */}
              <div className="flex h-11 w-10 shrink-0 items-center justify-center rounded-md border border-gray-300 bg-gray-50 text-sm font-medium text-gray-500">
                {index + 1}
              </div>

              {/* 入力欄 */}
              <input
                type="text"
                value={instruction.value}
                onChange={(e) =>
                  updateInstruction(
                    instruction.id,
                    e.target.value,
                  )
                }
                placeholder="指示内容を入力"
                className={`h-11 w-full rounded-md border px-4 text-sm text-gray-800 outline-none transition placeholder:text-gray-400 ${
                  hasError
                    ? "border-red-400 focus:border-red-500 focus:ring-2 focus:ring-red-100"
                    : "border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-100"
                }`}
              />

              {/* 削除ボタン */}
              <button
                type="button"
                onClick={() =>
                  deleteInstruction(instruction.id)
                }
                className="flex h-11 w-11 shrink-0 items-center justify-center rounded-md text-gray-400 transition hover:bg-red-50 hover:text-red-500"
                aria-label={`${index + 1}行目を削除`}
              >
                <Trash2 size={18} />
              </button>
            </div>
          );
        })}
      </div>

      {/* エラーメッセージ */}
      {instructionsError && (
        <p className="mt-2 text-sm text-red-500">
          {instructionsError}
        </p>
      )}

      {/* 操作ボタン */}
      <div className="mt-4 flex items-center justify-center gap-3">
        {/* 行を追加 */}
        <button
          type="button"
          onClick={addInstruction}
          className="flex items-center gap-1 rounded-md px-4 py-2 text-sm font-medium text-blue-600 transition hover:bg-blue-50"
        >
          <Plus size={18} />
          行を追加
        </button>

        {/* 元に戻す */}
        {deletedInstruction && (
          <button
            type="button"
            onClick={restoreInstruction}
            className="flex items-center gap-1 rounded-md px-4 py-2 text-sm font-medium text-gray-600 transition hover:bg-gray-100"
          >
            <RotateCcw size={16} />
            元に戻す
          </button>
        )}
      </div>
    </div>
  );
}