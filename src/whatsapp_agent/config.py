import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    whatsapp_verify_token: str = os.getenv("WHATSAPP_VERIFY_TOKEN", "change-me")
    whatsapp_business_number: str = os.getenv("WHATSAPP_BUSINESS_NUMBER", "whatsapp:+1234567890")

    model_name: str = os.getenv("WHATSAPP_AGENT_MODEL", "gpt-4o-mini")


settings = Settings()
