import random
import time
from typing import List, Dict

from Abstract_Modules.quiz_engineABC import QuizEngineAbstract 

class QuizEngine(QuizEngineAbstract):
    
    def shuffle_cards(self, deck_cards: List[Dict]) -> List[Dict]:

        shuffled = deck_cards.copy()
        random.shuffle(shuffled)
        return shuffled

    def evaluate_answer(self, user_answer: str, correct_answer: str) -> bool:

        return user_answer.strip().lower() == correct_answer.strip().lower()

    def start_session(self, deck_name: str, deck_cards: List[Dict]) -> Dict:

        score = 0
        start_time = time.time()
        shuffled_cards = self.shuffle_cards(deck_cards)

        print(f"\n--- Starting Quiz: {deck_name} ---")
        
        for card in shuffled_cards:
            question = list(card.keys())[0]
            answer = card[question]

            user_input = input(f"Question: {question}\nYour Answer: ")
            if self.evaluate_answer(user_input, answer):
                print("Correct! ✅")
                score += 1
            else:
                print(f"Wrong! ❌ The correct answer was: {answer}")

        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        return {
            "deck_name": deck_name,
            "score": score,
            "total_questions": len(deck_cards),
            "time_taken": total_time
        }
