export function getDescriptionError(value: string): string | null {
  // 未入力の場合はエラーを表示しない
  if (value.length === 0) {
    return null;
  }

  // 半角・全角スペースのみの場合
  if (/^[ 　]+$/.test(value)) {
    return "説明を入力してください";
  }

  // 先頭に半角・全角スペースがある
  if (/^[ 　]/.test(value)) {
    return "先頭に空白を入力することはできません";
  }

  // 末尾に半角・全角スペースがある
  if (/[ 　]$/.test(value)) {
    return "末尾に空白を入力することはできません";
  }

  // 1024文字を超えている
  if (value.length > 1024) {
    return "1024文字以内で入力してください";
  }

  return null;
}
