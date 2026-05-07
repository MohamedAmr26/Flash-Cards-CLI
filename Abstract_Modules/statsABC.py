from abc import ABC, abstractmethod
from typing import List, Dict

class StatsAbstract(ABC):

    @abstractmethod
    def log_result(self, deck_name: str, score: int, total_questions: int, time_taken: float) -> None:
        """Formats the quiz result and passes it to the Storage module."""
        pass

    @abstractmethod
    def get_all_stats(self) -> List[Dict]:
        """Fetches stats from Storage to be sent to the Menu."""
        pass