from storage import load, save
from datetime import datetime, timedelta

SCORES_FILE = "scores.json"


def get_all_scores():
    """Load all scores from scores.json."""
    return load(SCORES_FILE)


def save_session(deck_name, score, total):
    """Save a quiz session result for a given deck."""
    scores = get_all_scores()

    if deck_name not in scores:
        scores[deck_name] = []

    session = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "score": score,
        "total": total
    }

    scores[deck_name].append(session)
    save(SCORES_FILE, scores)
    print(f"\n✅ Session saved: {score}/{total} for '{deck_name}'")


def get_best_score(sessions):
    """Return the highest score percentage from a list of sessions."""
    if not sessions:
        return None
    return max(sessions, key=lambda s: s["score"] / s["total"] if s["total"] > 0 else 0)


def get_average_score(sessions):
    """Return the average score percentage across all sessions."""
    if not sessions:
        return 0.0
    percentages = [s["score"] / s["total"] * 100 for s in sessions if s["total"] > 0]
    return sum(percentages) / len(percentages) if percentages else 0.0


def get_streak(sessions, threshold=0.7):
    """
    Return the current streak of consecutive sessions where
    score >= threshold (default 70%).
    Counts backwards from the most recent session.
    """
    if not sessions:
        return 0

    streak = 0
    # Go through sessions from most recent to oldest
    for session in reversed(sessions):
        if session["total"] == 0:
            break
        percentage = session["score"] / session["total"]
        if percentage >= threshold:
            streak += 1
        else:
            break

    return streak


def show_deck_stats(deck_name):
    """Display stats summary for a specific deck."""
    scores = get_all_scores()

    if deck_name not in scores or not scores[deck_name]:
        print(f"\n⚠️  No sessions found for deck: '{deck_name}'")
        return

    sessions = scores[deck_name]

    best    = get_best_score(sessions)
    average = get_average_score(sessions)
    streak  = get_streak(sessions)

    print(f"\n{'='*40}")
    print(f"  📊 Stats for: {deck_name}")
    print(f"{'='*40}")
    print(f"  Sessions played : {len(sessions)}")
    print(f"  Best score      : {best['score']}/{best['total']} "
          f"({best['score']/best['total']*100:.0f}%)  [{best['date']}]")
    print(f"  Average score   : {average:.1f}%")
    print(f"  Current streak  : {streak} session(s) above 70%")
    print(f"{'='*40}\n")


def show_all_stats():
    """Display a summary of stats for every deck that has been played."""
    scores = get_all_scores()

    if not scores:
        print("\n⚠️  No quiz sessions recorded yet.")
        return

    print(f"\n{'='*50}")
    print(f"  📈 Overall Stats — All Decks")
    print(f"{'='*50}")

    for deck_name, sessions in scores.items():
        if not sessions:
            continue

        average = get_average_score(sessions)
        best    = get_best_score(sessions)
        streak  = get_streak(sessions)

        print(f"\n  🗂  {deck_name}")
        print(f"     Sessions : {len(sessions)}")
        print(f"     Best     : {best['score']}/{best['total']} ({best['score']/best['total']*100:.0f}%)")
        print(f"     Average  : {average:.1f}%")
        print(f"     Streak   : {streak} 🔥" if streak >= 3 else f"     Streak   : {streak}")

    print(f"\n{'='*50}\n")


def show_session_history(deck_name, limit=10):
    """Show the last N sessions for a specific deck."""
    scores = get_all_scores()

    if deck_name not in scores or not scores[deck_name]:
        print(f"\n⚠️  No history found for '{deck_name}'")
        return

    sessions = scores[deck_name][-limit:]  # last N sessions

    print(f"\n  📅 Last {len(sessions)} session(s) for '{deck_name}':")
    print(f"  {'-'*35}")

    for i, s in enumerate(reversed(sessions), 1):
        pct  = s["score"] / s["total"] * 100 if s["total"] > 0 else 0
        icon = "✅" if pct >= 70 else "❌"
        print(f"  {i:>2}. {s['date']}  —  {s['score']}/{s['total']}  ({pct:.0f}%)  {icon}")

    print()