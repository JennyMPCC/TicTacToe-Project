# TicTacToe-Project
Learning Tic-Tac-Toe AI with Binary Trees (CS034, CRN 78704) — Group 2

## Overview
- Human vs. AI Tic-Tac-Toe on configurable square boards (≥3×3).
- AI stores losing board states in a binary search tree and avoids them in future games.
- Optional persistence: losing states saved to `losing_states.json` between runs.

## How It Works
- `Board` models the grid, validates moves, checks wins, and can flatten to a list for tree lookups.
- `LosingStateTree` is a BST keyed by flat board lists; `contains` guards the AI from repeating losing lines.
- `AIPlayer` simulates each legal move, rejects ones already in the losing-state BST, and learns via `learn_from_loss` when beaten.
- `GameManager` runs the loop, swaps turns, handles multi-game play, and triggers auto-save after AI losses.

## Run the Game
- Prereqs: Python 3.10+ (no external packages required).
- From the repo root run: `py main.py`
- When prompted, pick a board size (press Enter for default 3). X (you) goes first against AI O.
- After each game, choose whether to play again; learned losing states persist if `AUTO_SAVE` is enabled.

## Key Files
- `main.py` — entry point; asks for board size and launches `GameManager`.
- `config.py` — board size bounds, symbols, persistence settings (`SAVE_FILE`, `AUTO_SAVE`).
- `board.py` — board storage, display, cloning, win/draw detection, flat-list conversion.
- `player.py` — base `Player` plus `HumanPlayer` input handling.
- `ai_player.py` — move selection that consults `LosingStateTree`; learning hook.
- `losing_tree.py` — BST for losing states with save/load helpers.
- `game_manager.py` — orchestrates setup, turns, win/draw handling, learning, and replay prompt.

## Meeting the Requirements
- Classes: Board, Player/HumanPlayer, AIPlayer, LosingStateTree (+ GameManager wrapper).
- Board size configurable (defaults to 3, min 3; supports larger square boards via input/config).
- Win condition: n-in-a-row for the chosen n (rows/cols/diagonals).
- AI learning: records final losing states, checks BST before choosing moves, prefers safe options.
- Optional persistence: JSON save/load of losing states controlled in `config.py`.

## Testing
- Lightweight tests are provided (e.g., `test_phase1.py`, `test_ai_learning.py`).
- Run all tests from the repo root: `py -m pytest`

## Notes and Limitations
- Console-based interaction only; any GUI would be additive.
- Tree growth is unbounded; for very large play volumes you may want pruning or deduplication strategies.
