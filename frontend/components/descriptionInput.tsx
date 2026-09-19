"use client";

import HelpPopover from "@/components/HelpPopover";
import { getDescriptionError } from "@/utils/DescriptionInputValidation";

type DescriptionInputProps = {
  value: string;
  onChange: (value: string) => void;
};

export default function DescriptionInput({
  value,
  onChange,
}: DescriptionInputProps) {
  const error = getDescriptionError(value);

  return (
    <div className="space-y-2">
      {/* ラベル */}
      <div className="flex items-center">
        <label
          htmlFor="description"
          className="text-sm font-semibold text-gray-700"
        >
          Description
        </label>

        <span className="text-xs font-medium text-red-500">
          *
        </span>

        <span className="ml-2">
          <HelpPopover
            title="Descriptionについて"
            description="このSkillが何をするものなのかを、初めて見る人にも分かるように説明してください。空欄にはできません。具体的な役割や目的を書くと分かりやすくなります。"
          />
        </span>
      </div>

      {/* 説明入力欄 */}
      <textarea
        id="description"
        name="description"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="このプロンプトについての説明を入力"
        rows={3}
        className={`w-full resize-none rounded-md border px-4 py-3 text-sm text-gray-800 outline-none transition placeholder:text-gray-400 focus:ring-2 ${
          error
            ? "border-red-500 focus:border-red-500 focus:ring-red-100"
            : "border-gray-300 focus:border-blue-500 focus:ring-blue-100"
        }`}
      />

      {/* エラーメッセージ */}
      {error && (
        <p className="text-xs text-red-500">
          {error}
        </p>
      )}
    </div>
  );
}