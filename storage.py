import json
import os

DATA_DIR = "data"
DECKS_FILE = os.path.join(DATA_DIR, "decks.json")
SCORES_FILE = os.path.join(DATA_DIR, "scores.json")


def _read_json(path, fallback):
    if not os.path.exists(path):
        return fallback
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return fallback


def _write_json(path, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_decks():
    return _read_json(DECKS_FILE, {})

def save_decks(data):
    _write_json(DECKS_FILE, data)

def load_scores():
    return _read_json(SCORES_FILE, [])

def save_scores(data):
    _write_json(SCORES_FILE, data)