"use client";

import { Copy, RefreshCw, RotateCcw } from "lucide-react";

type PromptResultPageProps = {
  contents: string;
};

export default function PromptResultPage({
  contents,
}: PromptResultPageProps) {
  // コピー
  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(contents);
      console.log("コピーしました");
    } catch (error) {
      console.error("コピーに失敗しました:", error);
    }
  };

  // 初めからやり直す
  const handleReset = () => {
    // TODO: 入力画面へ戻り、入力内容をリセットする
  };

  // 再生成する
  const handleRegenerate = () => {
    // TODO: 前回入力した値を使って再度実行する
  };

  return (
    <main className="min-h-screen bg-gray-100 px-4 py-10">
      <div className="mx-auto w-full max-w-3xl">
        <div className="rounded-xl bg-white shadow-sm">
          {/* ヘッダー */}
          <div className="border-b border-gray-200 px-8 py-6">
            <h1 className="text-2xl font-bold text-gray-800">
              プロンプト実行結果
            </h1>
          </div>

          <div className="space-y-8 p-8">
            {/* contents */}
            <div>
              <h2 className="mb-3 text-sm font-semibold text-gray-700">
                実行結果
              </h2>

              <div className="overflow-hidden rounded-md border border-gray-300 bg-gray-900">
                {/* contents本体 */}
                <pre className="min-h-48 overflow-x-auto whitespace-pre-wrap px-4 py-4 font-mono text-sm leading-7 text-gray-100">
                  {contents}
                </pre>

                {/* コピー */}
                <div className="flex justify-end border-t border-gray-700 px-3 py-2">
                  <button
                    type="button"
                    onClick={handleCopy}
                    className="flex items-center gap-1.5 rounded-md px-3 py-2 text-sm text-gray-300 transition hover:bg-gray-800 hover:text-white"
                  >
                    <Copy size={16} />
                    コピー
                  </button>
                </div>
              </div>
            </div>

            {/* フッター */}
            <div className="flex items-center justify-between border-t border-gray-200 pt-6">
              {/* 初めからやり直す */}
              <button
                type="button"
                onClick={handleReset}
                className="flex items-center gap-1.5 rounded-md px-3 py-2 text-sm text-gray-500 transition hover:bg-gray-100 hover:text-gray-700"
              >
                <RotateCcw size={16} />
                初めからやり直す
              </button>

              {/* 再生成する */}
              <button
                type="button"
                onClick={handleRegenerate}
                className="flex items-center gap-1.5 rounded-md bg-blue-600 px-6 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700"
              >
                <RefreshCw size={16} />
                再生成する
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}