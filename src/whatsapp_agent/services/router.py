from typing import List

from ..models import InboundMessage, AgentResponse
from ..config import settings
from ..agents.faq_agent import FaqAgent
from ..agents.smalltalk_agent import SmallTalkAgent
from ..agents.task_agent import TaskAgent


class AgentRouter:
    """Simple multi-agent router.

    In a more complex system, this could itself be an LLM-based router.
    Here we use a rule + keyword approach for clarity.
    """

    def __init__(self) -> None:
        self.faq_agent = FaqAgent()
        self.smalltalk_agent = SmallTalkAgent()
        self.task_agent = TaskAgent()

    def route(self, msg: InboundMessage) -> AgentResponse:
        text = msg.text.strip().lower()

        # Very basic routing rules
        if any(k in text for k in ["hours", "time", "open", "close", "location", "address"]):
            return self.faq_agent.handle(msg)
        if any(k in text for k in ["book", "order", "schedule", "appointment"]):
            return self.task_agent.handle(msg)
        # fallback: smalltalk / general Q&A
        return self.smalltalk_agent.handle(msg)
