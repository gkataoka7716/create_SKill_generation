"use client";

import HelpPopover from "@/components/HelpPopover";
import { getNameError } from "@/utils/NameInputValidation";

type NameInputProps = {
  value: string;
  onChange: (value: string) => void;
};

export default function NameInput({ value, onChange }: NameInputProps) {
  const error = getNameError(value);

  return (
    <div className="space-y-2">
      {/* ラベル */}
      <div className="flex items-center">
        <label htmlFor="name" className="text-sm font-semibold text-gray-700">
          Name
        </label>

        <span className="text-xs font-medium text-red-500">*</span>

        <span className="ml-2">
          <HelpPopover
            title="Nameについて"
            description="Skillの名前を入力してください。3〜20文字で、英字・数字・アンダースコア（_）のみ使用できます。空欄やスペース、日本語、その他の記号は使用できません。"
          />
        </span>
      </div>

      {/* 入力欄 */}
      <input
        id="name"
        type="text"
        name="name"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="プロンプト名を入力"
        autoComplete="off"
        className={`w-full rounded-md border px-4 py-3 text-sm text-gray-800 outline-none transition placeholder:text-gray-400 focus:ring-2 ${
          error
            ? "border-red-500 focus:border-red-500 focus:ring-red-100"
            : "border-gray-300 focus:border-blue-500 focus:ring-blue-100"
        }`}
      />

      {/* エラーメッセージ */}
      {error && <p className="text-xs text-red-500">{error}</p>}
    </div>
  );
}
