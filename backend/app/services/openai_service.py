import logging
import os

import openai
from openai import OpenAI

logger = logging.getLogger()

client = OpenAI()


def generate_with_openai(prompt: str, model: str) -> str:
    try:
        response = client.responses.create(
            model=model,
            input=prompt,
        )

        logger.info("OpenAIによるSkill.md生成に成功しました")
        return response.output_text

    except openai.AuthenticationError as e:
        logger.error(f"OpenAIの認証に失敗しました: {e}")
        raise

    except openai.PermissionDeniedError as e:
        logger.error(f"OpenAIへのアクセスが拒否されました: {e}")
        raise

    except openai.BadRequestError as e:
        logger.error(f"OpenAIへのリクエストが不正です: {e}")
        raise

    except openai.RateLimitError as e:
        logger.error(f"OpenAIのレート制限に達しました: {e}")
        raise

    except openai.APITimeoutError as e:
        logger.error(f"OpenAIへのリクエストがタイムアウトしました: {e}")
        raise

    except openai.APIConnectionError as e:
        logger.error(f"OpenAIへの接続に失敗しました: {e}")
        raise

    except openai.InternalServerError as e:
        logger.error(f"OpenAI側でサーバーエラーが発生しました: {e}")
        raise

    except openai.APIStatusError as e:
        logger.error(f"OpenAI APIでエラーが発生しました: " f"status_code={e.status_code}, error={e}")
        raise

    except openai.APIError as e:
        logger.error(f"OpenAI APIで予期しないエラーが発生しました: {e}")
        raise
