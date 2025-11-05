from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class InboundMessage(BaseModel):
    """Canonical inbound WhatsApp message.

    In production you would adapt this to Twilio's or Meta's exact payload.
    For this demo, we keep it clean and simple.
    """

    from_number: str
    to_number: str
    text: str
    timestamp: datetime | None = None


class OutboundMessage(BaseModel):
    to_number: str
    text: str
    media_url: Optional[str] = None


class AgentResponse(BaseModel):
    """Response from an internal agent before we adapt to WhatsApp format."""

    text: str
    agent_name: str
    confidence: float = 1.0
