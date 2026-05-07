from abc import ABC, abstractmethod
from typing import List, Dict

class QuizEngineAbstract(ABC):

    @abstractmethod
    def start_session(self, deck_name: str, deck_cards: List[Dict]) -> Dict:
        """
        Main loop for the quiz. 
        Returns a dictionary with session results (score, time_taken, etc.)
        """
        pass

    @abstractmethod
    def evaluate_answer(self, user_answer: str, correct_answer: str) -> bool:
        """Compares user input with the correct answer (case-insensitive)."""
        pass

    @abstractmethod
    def shuffle_cards(self, deck_cards: List[Dict]) -> List[Dict]:
        """Randomizes the order of the flashcards."""
        pass