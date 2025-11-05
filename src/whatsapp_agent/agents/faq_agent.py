from ..models import InboundMessage, AgentResponse
from ..services.llm_client import chat_completion
from ..services.state_store import memory
from .base import BaseAgent


FAQ_CONTEXT = """You are a helpful FAQ assistant for a small business using WhatsApp.
You answer questions about opening hours, address, phone number, services,
and simple policies. If the user asks for something outside that scope,
answer briefly and suggest they talk to a human agent.
"""


class FaqAgent(BaseAgent):
    name = "faq-agent"

    def handle(self, msg: InboundMessage) -> AgentResponse:
        user_id = msg.from_number
        history = memory.get(user_id)
        history = history[-4:]  # keep context short

        messages = [
            {"role": "system", "content": FAQ_CONTEXT},
        ] + history + [
            {"role": "user", "content": msg.text},
        ]

        try:
            reply = chat_completion(messages)
        except Exception as e:  # fallback
            reply = (
                "Our opening hours are 9:00–17:00 Monday to Friday, and we are located at "
                "123 Example Street. For anything else, please contact support."
            )

        memory.add(user_id, "user", msg.text)
        memory.add(user_id, "assistant", reply)
        return AgentResponse(text=reply, agent_name=self.name)
