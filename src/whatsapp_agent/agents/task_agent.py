from ..models import InboundMessage, AgentResponse
from ..services.llm_client import chat_completion
from ..services.state_store import memory
from .base import BaseAgent


TASK_SYSTEM = """You are a WhatsApp assistant that helps users with 'tasks' such as booking,
ordering, or scheduling. You cannot actually complete external tasks in this demo,
but you can collect structured information and confirm next steps.

Always ask for any missing required information in a concise way.
"""


class TaskAgent(BaseAgent):
    name = "task-agent"

    def handle(self, msg: InboundMessage) -> AgentResponse:
        user_id = msg.from_number
        history = memory.get(user_id)

        messages = [
            {"role": "system", "content": TASK_SYSTEM},
        ] + history + [
            {"role": "user", "content": msg.text},
        ]

        try:
            reply = chat_completion(messages)
        except Exception:
            reply = (
                "I can help collect details for your request. "
                "Please tell me what you want to book or schedule, and your preferred time."
            )

        memory.add(user_id, "user", msg.text)
        memory.add(user_id, "assistant", reply)
        return AgentResponse(text=reply, agent_name=self.name)
