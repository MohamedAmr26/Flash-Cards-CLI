import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from storage import load, save
from Abstract_Modules.statsABC import StatsAbstract
from datetime import datetime
from typing import List, Dict

SCORES_FILE = "scores.json"


class Stats(StatsAbstract):
    """Concrete implementation of StatsAbstract."""

    # ── StatsAbstract interface ────────────────────────────────

    def log_result(self, deck_name: str, score: int, total_questions: int, time_taken: float) -> None:
        """Formats the quiz result and persists it via Storage."""
        scores = load(SCORES_FILE)

        if deck_name not in scores:
            scores[deck_name] = []

        session = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "score": score,
            "total": total_questions,
            "time_taken": round(time_taken, 2),
        }

        scores[deck_name].append(session)
        save(SCORES_FILE, scores)
        print(f"\n✅ Session saved: {score}/{total_questions} for '{deck_name}'")

    def get_all_stats(self) -> List[Dict]:
        """
        Fetches stats from Storage and returns a flat list of summary dicts
        shaped for ConsoleMenu.show_stats:
            [{"deck": str, "score": int, "total": int}, ...]
        Each entry represents the *most recent* session for that deck.
        """
        scores = load(SCORES_FILE)
        result = []

        for deck_name, sessions in scores.items():
            if not sessions:
                continue
            latest = sessions[-1]
            result.append({
                "deck":  deck_name,
                "score": latest["score"],
                "total": latest["total"],
            })

        return result

    # ── extra helper methods (not in ABC but useful) ───────────

    def get_best_score(self, sessions: List[Dict]) -> Dict:
        if not sessions:
            return {}
        return max(sessions, key=lambda s: s["score"] / s["total"] if s["total"] > 0 else 0)

    def get_average_score(self, sessions: List[Dict]) -> float:
        if not sessions:
            return 0.0
        percentages = [s["score"] / s["total"] * 100 for s in sessions if s["total"] > 0]
        return sum(percentages) / len(percentages) if percentages else 0.0

    def get_streak(self, sessions: List[Dict], threshold: float = 0.7) -> int:
        """Current streak of consecutive sessions at or above threshold."""
        streak = 0
        for session in reversed(sessions):
            if session["total"] == 0:
                break
            if session["score"] / session["total"] >= threshold:
                streak += 1
            else:
                break
        return streak

    def show_deck_stats(self, deck_name: str) -> None:
        scores = load(SCORES_FILE)

        if deck_name not in scores or not scores[deck_name]:
            print(f"\n⚠️  No sessions found for deck: '{deck_name}'")
            return

        sessions = scores[deck_name]
        best    = self.get_best_score(sessions)
        average = self.get_average_score(sessions)
        streak  = self.get_streak(sessions)

        print(f"\n{'='*40}")
        print(f"  📊 Stats for: {deck_name}")
        print(f"{'='*40}")
        print(f"  Sessions played : {len(sessions)}")
        print(f"  Best score      : {best['score']}/{best['total']} "
              f"({best['score']/best['total']*100:.0f}%)  [{best['date']}]")
        print(f"  Average score   : {average:.1f}%")
        print(f"  Current streak  : {streak} session(s) above 70%")
        print(f"{'='*40}\n")

    def show_all_stats(self) -> None:
        scores = load(SCORES_FILE)

        if not scores:
            print("\n⚠️  No quiz sessions recorded yet.")
            return

        print(f"\n{'='*50}")
        print(f"  📈 Overall Stats — All Decks")
        print(f"{'='*50}")

        for deck_name, sessions in scores.items():
            if not sessions:
                continue
            average = self.get_average_score(sessions)
            best    = self.get_best_score(sessions)
            streak  = self.get_streak(sessions)

            print(f"\n  🗂  {deck_name}")
            print(f"     Sessions : {len(sessions)}")
            print(f"     Best     : {best['score']}/{best['total']} "
                  f"({best['score']/best['total']*100:.0f}%)")
            print(f"     Average  : {average:.1f}%")
            print(f"     Streak   : {streak} 🔥" if streak >= 3 else f"     Streak   : {streak}")

        print(f"\n{'='*50}\n")

    def show_session_history(self, deck_name: str, limit: int = 10) -> None:
        scores = load(SCORES_FILE)

        if deck_name not in scores or not scores[deck_name]:
            print(f"\n⚠️  No history found for '{deck_name}'")
            return

        sessions = scores[deck_name][-limit:]
        print(f"\n  📅 Last {len(sessions)} session(s) for '{deck_name}':")
        print(f"  {'-'*35}")

        for i, s in enumerate(reversed(sessions), 1):
            pct  = s["score"] / s["total"] * 100 if s["total"] > 0 else 0
            icon = "✅" if pct >= 70 else "❌"
            print(f"  {i:>2}. {s['date']}  —  {s['score']}/{s['total']}  ({pct:.0f}%)  {icon}")

        print()