from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from ..config import settings
from ..models import InboundMessage, OutboundMessage, AgentResponse
from ..services.router import AgentRouter

app = FastAPI(title="Enhanced WhatsApp Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

router = AgentRouter()


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.post("/webhook", response_model=OutboundMessage)
async def whatsapp_webhook(msg: InboundMessage):
    """Generic webhook endpoint.

    In a real deployment you would map the provider's payload to InboundMessage,
    verify signatures, and then call this logic.
    """
    agent_response: AgentResponse = router.route(msg)
    return OutboundMessage(to_number=msg.from_number, text=agent_response.text)


@app.post("/simulate", response_model=OutboundMessage)
async def simulate(msg: InboundMessage):
    """Local testing endpoint.

    Send a JSON body like:
    {
      "from_number": "whatsapp:+10000000000",
      "to_number": "whatsapp:+19999999999",
      "text": "Hi, what are your opening hours?"
    }
    """
    agent_response: AgentResponse = router.route(msg)
    return OutboundMessage(to_number=msg.from_number, text=agent_response.text)
