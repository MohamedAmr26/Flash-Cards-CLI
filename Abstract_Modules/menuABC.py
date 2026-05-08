from abc import ABC, abstractmethod
from typing import List, Dict

class MenuAbstract(ABC):
    
    @abstractmethod
    def show_menu(self) -> int:
        """Returns: 1: Choose deck, 2: Show stats, 0: exit"""
        pass

    @abstractmethod
    def choose_deck(self, decks_list: List[Dict]) -> int:
        """Returns deck_idx or 0 to go back"""
        pass

    @abstractmethod
    def show_flashcard(self, flash_card: str, flash_card_number: int) -> str:
        """Displays the card and Returns the user's answer"""
        pass

    @abstractmethod
    def show_score(self, deck_name: str, score: int, total: int) -> int:
        """Returns 0 to return to main_menu"""
        pass

    @abstractmethod
    def show_stats(self, stats: List[Dict]) -> int:
        """Returns 0 to return to main_menu"""
        pass

    @abstractmethod
    def create_deck_menu(self) -> str:
        pass

    @abstractmethod
    def add_flashcard_menu(self):
        pass

    @abstractmethod
    def remove_flashcard_menu(self):
        pass

    @abstractmethod
    def delete_deck_menu(self):
        pass
