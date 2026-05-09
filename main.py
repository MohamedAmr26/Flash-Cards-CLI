#!/usr/bin/env python3

import sys
import os

# Make sure sibling packages resolve correctly regardless of cwd
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "Modules"))

from Modules.menu        import ConsoleMenu
from Modules.deck_manager import DeckManager
from Modules.quiz_engine  import QuizEngine
from Modules.stats        import Stats


def main():
    menu    = ConsoleMenu()
    decks   = DeckManager()
    engine  = QuizEngine()
    stats   = Stats()

    while True:
        choice = menu.show_menu()

        # 1 ── Choose & play a deck
        if choice == 1:
            deck_names = decks.list_decks()
            idx = menu.choose_deck(deck_names)

            if idx == 0 or not deck_names:
                continue

            if idx < 1 or idx > len(deck_names):
                print("⚠️  Invalid selection.")
                continue

            deck_name  = deck_names[idx - 1]
            deck_cards = decks.get_deck(deck_name)

            if not deck_cards:
                print(f"⚠️  '{deck_name}' is empty. Add some cards first.")
                continue

            result = engine.start_session(deck_name, deck_cards)
            stats.log_result(
                result["deck"],
                result["score"],
                result["total"],
                result["time_taken"],
            )

        # 2 ── Create a deck
        elif choice == 2:
            deck_name = menu.create_deck_menu()
            if deck_name:
                decks.create_deck(deck_name)

        # 3 ── Add a flashcard
        elif choice == 3:
            deck_name, question, answer = menu.add_flashcard_menu()
            if deck_name and question and answer:
                decks.add_to_deck(deck_name, question, answer)

        # 4 ── Remove a flashcard
        elif choice == 4:
            deck_name, card_index = menu.remove_flashcard_menu()
            if deck_name and card_index != -1:
                decks.remove_from_deck(deck_name, card_index)

        # 5 ── Delete a deck
        elif choice == 5:
            deck_name = menu.delete_deck_menu()
            if deck_name:
                decks.remove_deck(deck_name)

        # 6 ── Show stats
        elif choice == 6:
            all_stats = stats.get_all_stats()
            menu.show_stats(all_stats)

        # 0 ── Exit
        elif choice == 0:
            print("👋 Goodbye!")
            break

        else:
            print("⚠️  Invalid option, please try again.")


if __name__ == "__main__":
    main()