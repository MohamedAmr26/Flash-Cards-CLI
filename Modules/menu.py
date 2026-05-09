from Abstract_Modules.menuABC import MenuAbstract
from typing import List, Dict

class ConsoleMenu(MenuAbstract):

    def show_menu(self) -> int:
        print("\n========== FLASHCARD APP ==========")
        print("1. Choose Deck")
        print("2. Create Deck")
        print("3. Add Flashcard")
        print("4. Remove Flashcard")
        print("5. Delete Deck")
        print("6. Show Stats")
        print("0. Exit")
        
        try:
            return int(input("Choose option: "))
        except ValueError:
            return -1

    def choose_deck(self, decks_list: List[str]) -> int:        
        print("\n========== DECKS ==========")
        if not decks_list:
            print("No decks available.")
            return 0
        for i, deck in enumerate(decks_list, start=1):
            print(f"{i}. {deck}")
        print("0. Back")
        try:
            return int(input("Choose deck: "))
        except ValueError:
            return -1

    def show_flashcard(self, flash_card: str, flash_card_number: int) -> str:
        print(f"\n========== CARD #{flash_card_number} ==========")
        print(f"Question: {flash_card}")
        return input("Answer: ")

    def show_score(self, deck_name: str, score: int, total: int) -> int:
        print("\n========== SCORE ==========")
        print(f"Deck: {deck_name}")
        print(f"Result: {score}/{total}")
        input("Press Enter to continue...")
        return 0

    def show_stats(self, stats: List[Dict]) -> int:
        print("\n========== STATS ==========")
        if not stats:
            print("No stats available.")
        for stat in stats:
            print(f"Deck: {stat['deck']} | Score: {stat['score']}/{stat['total']}")
        input("Press Enter to continue...")
        return 0

    def create_deck_menu(self) -> str:
        print("\n========== CREATE DECK ==========")
        return input("Enter deck name: ")

    def add_flashcard_menu(self) -> tuple[str, str, str]:
        print("\n========== ADD FLASHCARD ==========")
        deck_name = input("Deck name: ")
        question  = input("Question: ")
        answer    = input("Answer: ")
        return deck_name, question, answer

    def remove_flashcard_menu(self):
        print("\n========== REMOVE FLASHCARD ==========")
        deck_name = input("Deck name: ")
        try:
            card_index = int(input("Card index: "))
        except ValueError:
            return deck_name, -1
        return deck_name, card_index

    def delete_deck_menu(self) -> str:
        print("\n========== DELETE DECK ==========")
        return input("Deck name: ")