from typing import List, Dict

from Abstract_Modules.deck_managerABC import DeckManagerAbstract
from Modules.storage import load_decks, save_decks

class DeckManager(DeckManagerAbstract):
    def __init__(self):
        self.decks = load_decks()

    def create_deck(self, deck_name: str) -> bool:
        """Creates a new deck. Returns True if successful."""

        deck_name = deck_name.strip()

        if not deck_name:
            print("⚠️ Deck name cannot be empty.")
            return False

        if deck_name in self.decks:
            print(f"⚠️ Deck '{deck_name}' already exists.")
            return False

        self.decks[deck_name] = []
        save_decks(self.decks)

        print(f"✅ Deck '{deck_name}' created successfully.")
        return True

    def add_to_deck(self, deck_name: str, question: str, answer: str) -> bool:
        """Adds a flashcard to a specific deck."""

        if deck_name not in self.decks:
            print(f"⚠️ Deck '{deck_name}' does not exist.")
            return False

        question = question.strip()
        answer = answer.strip()

        if not question or not answer:
            print("⚠️ Question and answer cannot be empty.")
            return False

        card = {question: answer}
        self.decks[deck_name].append(card)

        save_decks(self.decks)

        print(f"✅ Flashcard added to '{deck_name}'.")
        return True

    def remove_from_deck(self, deck_name: str, card_index: int) -> bool:
        """Removes a specific flashcard from a deck."""

        if deck_name not in self.decks:
            print(f"⚠️ Deck '{deck_name}' does not exist.")
            return False

        deck = self.decks[deck_name]

        if not deck:
            print(f"⚠️ Deck '{deck_name}' is empty.")
            return False

        if card_index < 0 or card_index >= len(deck):
            print("⚠️ Invalid flashcard index.")
            return False

        removed_card = deck.pop(card_index)

        save_decks(self.decks)

        removed_question = list(removed_card.keys())[0]
        print(f"✅ Removed flashcard: '{removed_question}'.")

        return True

    def get_deck(self, deck_name: str) -> List[Dict]:
        """Returns all flashcards inside a specific deck."""

        if deck_name not in self.decks:
            print(f"⚠️ Deck '{deck_name}' does not exist.")
            return []

        return self.decks[deck_name]

    def remove_deck(self, deck_name: str) -> bool:
        """Deletes an entire deck."""

        if deck_name not in self.decks:
            print(f"⚠️ Deck '{deck_name}' does not exist.")
            return False

        del self.decks[deck_name]

        save_decks(self.decks)

        print(f"✅ Deck '{deck_name}' deleted successfully.")
        return True

    def list_decks(self) -> List[str]:
        """Returns a list of all deck names."""

        return list(self.decks.keys())
