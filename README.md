# Flash-Cards-CLI
# 🧠 Flashcards CLI App

## 📖 Overview
A lightweight, interactive Command-Line Interface (CLI) application built in Python for creating, managing, and taking flashcard quizzes. This project is developed as part of the **Software Product Management (SPM)** course to demonstrate modular architecture and clean code principles.

## ✨ Features
- **Deck Management:** Create, view, update, and delete flashcard decks effortlessly.
- **Interactive Quizzes:** Test your knowledge with randomized questions, case-insensitive evaluation, and immediate feedback.
- **Persistent Storage:** All decks and user scores are safely stored locally using JSON files.
- **Statistics Tracking:** Track your performance, view your score history, and monitor your learning progress.
- **Zero Dependencies:** Built entirely with standard Python libraries (`json`, `os`, `random`, `time`). No need for `pip install`.

## 🏗️ Project Architecture
The application is modularized based on the Single Responsibility Principle, making it scalable and easy to maintain:

*   `main.py`: The entry point of the application that ties everything together.
*   `menu.py`: The Presentation Layer; handles the CLI user interface and menu navigation.
*   `deck_manager.py`: Contains the business logic for deck and card CRUD operations.
*   `quiz_engine.py`: Manages the core quiz logic, card shuffling, and answer evaluation.
*   `stats.py`: Handles logging and formatting user quiz results.
*   `storage.py`: The Data Access Layer managing safe read/write operations to the `data/` JSON files.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/MohamedAmr26/Flash-Cards-CLI.git](https://github.com/MohamedAmr26/Flash-Cards-CLI.git)
