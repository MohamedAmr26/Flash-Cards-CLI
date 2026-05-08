from abc import ABC, abstractmethod
from typing import List, Dict

class MenuAbstract(ABC):
    @abstractmethod
    def show_menu(self) -> int:
        pass

    @abstractmethod
    def choose_deck(self, decks_list: List[Dict]) -> int:
        pass

    @abstractmethod
    def show_flashcard(self, flash_card: str, flash_card_number: int) -> str:
        pass
    
    @abstractmethod
    def show_score(self, deck_name: str, score: int, total: int) -> int:
        pass
    
    @abstractmethod
    def show_stats(self, stats: List[Dict]) -> int:
        pass
    
    @abstractmethod
    def create_deck_menu(self) -> str:
        pass
    
    @abstractmethod
    def add_flashcard_menu(self) -> tuple[str, str, str]:
        pass
    
    @abstractmethod
    def remove_flashcard_menu(self) -> tuple[str, int]:
        pass
    
    @abstractmethod
    def delete_deck_menu(self) -> str:
        pass