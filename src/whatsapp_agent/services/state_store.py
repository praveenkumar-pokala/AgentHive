from collections import defaultdict
from typing import Dict, List


class ConversationMemory:
    """Very simple in-memory store of last N messages per user.

    In production, persist this in Redis or a database.
    """

    def __init__(self, max_history: int = 10) -> None:
        self.max_history = max_history
        self._store: Dict[str, List[dict]] = defaultdict(list)

    def add(self, user_id: str, role: str, content: str) -> None:
        history = self._store[user_id]
        history.append({"role": role, "content": content})
        if len(history) > self.max_history:
            del history[0]

    def get(self, user_id: str) -> List[dict]:
        return list(self._store[user_id])


memory = ConversationMemory()
