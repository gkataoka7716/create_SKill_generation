"use client";

import { CircleHelp } from "lucide-react";

type HelpPopoverProps = {
  title: string;
  description: string;
};

export default function HelpPopover({ title, description }: HelpPopoverProps) {
  return (
    <div className="group relative inline-flex">
      {/* ? アイコン */}
      <span
        className="cursor-help text-gray-400 transition hover:text-blue-500"
        aria-label={`${title}の説明`}
      >
        <CircleHelp size={16} />
      </span>

      {/* ポップオーバー */}
      <div className="pointer-events-none absolute left-0 top-7 z-50 w-72 rounded-lg border border-gray-200 bg-white p-4 opacity-0 shadow-lg transition-opacity duration-150 group-hover:opacity-100">
        <p className="mb-1 text-sm font-semibold text-gray-800">{title}</p>

        <p className="text-xs leading-5 text-gray-600">{description}</p>
      </div>
    </div>
  );
}
