from abc import ABC, abstractmethod
from typing import List, Dict

class StatsAbstract(ABC):
    @abstractmethod
    def log_result(self, deck_name: str, score: int, total_questions: int, time_taken: float) -> None: pass
    @abstractmethod
    def get_all_stats(self) -> List[Dict]: pass