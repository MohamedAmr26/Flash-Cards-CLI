from abc import ABC, abstractmethod
from typing import List, Dict

"""

deck structure
{
    "deck name": [{"card question": "card answer"}]
}

"""

class DeckManagerAbstract(ABC):

    @abstractmethod
    def create_deck(self, deck_name: str) -> bool:
        """Creates a new deck. Returns True if successful."""
        pass

    @abstractmethod
    def add_to_deck(self, deck_name: str, question: str, answer: str) -> bool:
        """Adds a flashcard to a specific deck."""
        pass

    @abstractmethod
    def remove_from_deck(self, deck_name: str, card_index: int) -> bool:
        """Removes a specific flashcard from a deck."""
        pass

    @abstractmethod
    def get_deck(self, deck_name: str) -> List[Dict]:
        """Returns all flashcards inside a specific deck."""
        pass

    @abstractmethod
    def remove_deck(self, deck_name: str) -> bool:
        """Deletes an entire deck."""
        pass