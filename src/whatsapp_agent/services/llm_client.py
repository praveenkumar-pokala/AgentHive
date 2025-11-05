from typing import List

from openai import OpenAI

from ..config import settings


def get_client() -> OpenAI:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY not set; cannot call LLM.")
    return OpenAI(api_key=settings.openai_api_key)


def chat_completion(messages: List[dict], model: str | None = None) -> str:
    client = get_client()
    model_name = model or settings.model_name
    resp = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.2,
    )
    return resp.choices[0].message.content or ""
