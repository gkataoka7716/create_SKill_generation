"use client";

import aiModelData from "@/data/aiModel.json";

type AIModel = {
  provider: string;
  model: string;
  label: string;
};

type AIModelSelectProps = {
  value: string;
  onChange: (value: AIModel) => void;
};

export default function AIModelSelect({
  value,
  onChange,
}: AIModelSelectProps) {
  const models: AIModel[] = aiModelData.models;

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedModel = models.find(
      (item) => item.model === event.target.value,
    );

    if (selectedModel) {
      onChange(selectedModel);
    }
  };

  return (
    <div className="w-64">
      <label
        htmlFor="ai-model"
        className="mb-1 block text-sm font-medium text-gray-700"
      >
        AIモデル
      </label>

      <select
        id="ai-model"
        value={value}
        onChange={handleChange}
        className="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm text-gray-700 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
      >
        <option value="" disabled>
          AIモデルを選択してください
        </option>

        {models.map((item) => (
          <option key={`${item.provider}-${item.model}`} value={item.model}>
            {item.provider}  {item.label}
          </option>
        ))}
      </select>
    </div>
  );
}