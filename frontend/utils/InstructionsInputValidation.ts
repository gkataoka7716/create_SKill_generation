export function getInstructionsError(
  instructions: string[],
): string | null {
  // 1行だけの場合は、未入力でもエラーにしない
  if (instructions.length <= 1) {
    return null;
  }

  // 2行以上ある場合、未入力の行があればエラー
  if (
    instructions.some(
      (instruction) => instruction.trim().length === 0,
    )
  ) {
    return "入力されていないInstructionsがあります";
  }

  return null;
}