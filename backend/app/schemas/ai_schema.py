from enum import Enum


class ProviderType(str, Enum):
    OPENAI = "openai"
    GEMINI = "gemini"
    OLLAMA = "ollama"


class OpenAIModel(str, Enum):
    GPT_5_6 = "gpt-5.6"
    GPT_5_6_MINI = "gpt-5.6-mini"


class GeminiModel(str, Enum):
    GEMINI_3_8_FLASH = "gemini-3.8-flash"
    GEMINI_3_7_FLASH = "gemini-3.7-flash"


class OllamaModel(str, Enum):
    LLAMA_3_2 = "llama3.2"
    QWEN_3_VL = "qwen3-vl"
