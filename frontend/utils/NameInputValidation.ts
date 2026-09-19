export function getNameError(value: string): string | null {
  // 未入力の場合はエラーを表示しない
  if (value.length === 0) {
    return null;
  }

  // 64文字を超えている
  if (value.length > 64) {
    return "64文字以内で入力してください";
  }

  // 使用できる文字をチェック
  if (!/^[a-z0-9-]+$/.test(value)) {
    return "小文字英字・数字・ハイフン（-）のみ使用できます";
  }

  // 先頭にハイフン
  if (value.startsWith("-")) {
    return "先頭にハイフン（-）は使用できません";
  }

  // 末尾にハイフン
  if (value.endsWith("-")) {
    return "末尾にハイフン（-）は使用できません";
  }

  // ハイフンが連続
  if (value.includes("--")) {
    return "ハイフン（-）を連続して使用することはできません";
  }

  return null;
}