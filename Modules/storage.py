import json
import os

DATA_DIR = "data"
DECKS_FILE = os.path.join(DATA_DIR, "decks.json")
SCORES_FILE = os.path.join(DATA_DIR, "scores.json")

_FILE_MAP = {
    "decks.json":  DECKS_FILE,
    "scores.json": SCORES_FILE,
}


def _read_json(path, fallback):
    if not os.path.exists(path):
        return fallback
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return fallback


def _write_json(path, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# ── named helpers ──────────────────────────────────────────────
def load_decks() -> dict:
    return _read_json(DECKS_FILE, {})

def save_decks(data: dict) -> None:
    _write_json(DECKS_FILE, data)

def load_scores() -> dict:
    return _read_json(SCORES_FILE, {})

def save_scores(data: dict) -> None:
    _write_json(SCORES_FILE, data)

# ── generic helpers used by stats.py ──────────────────────────
def load(filename: str):
    """Load JSON by short filename ('scores.json') or full path."""
    path = _FILE_MAP.get(filename, filename)
    return _read_json(path, {})

def save(filename: str, data) -> None:
    """Save JSON by short filename ('scores.json') or full path."""
    path = _FILE_MAP.get(filename, filename)
    _write_json(path, data)