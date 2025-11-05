from ..models import InboundMessage, AgentResponse
from ..services.llm_client import chat_completion
from ..services.state_store import memory
from .base import BaseAgent


SMALLTALK_SYSTEM = """You are a friendly WhatsApp assistant.
Keep replies short, warm, and on-topic. Avoid long paragraphs.
If asked for something you cannot do, say so politely.
"""


class SmallTalkAgent(BaseAgent):
    name = "smalltalk-agent"

    def handle(self, msg: InboundMessage) -> AgentResponse:
        user_id = msg.from_number
        history = memory.get(user_id)

        messages = [
            {"role": "system", "content": SMALLTALK_SYSTEM},
        ] + history + [
            {"role": "user", "content": msg.text},
        ]

        try:
            reply = chat_completion(messages)
        except Exception:
            reply = "Hi! 👋 How can I help you today?"

        memory.add(user_id, "user", msg.text)
        memory.add(user_id, "assistant", reply)
        return AgentResponse(text=reply, agent_name=self.name)
