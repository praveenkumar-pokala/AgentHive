from abc import ABC, abstractmethod

from ..models import InboundMessage, AgentResponse


class BaseAgent(ABC):
    name: str = "base-agent"

    @abstractmethod
    def handle(self, msg: InboundMessage) -> AgentResponse:
        ...
