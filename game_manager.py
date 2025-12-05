"""
Game Manager module for Tic-Tac-Toe game.
Orchestrates the game flow and manages game state.
"""

from board import Board
from player import Player, HumanPlayer
from ai_player import AIPlayer
from losing_tree import LosingStateTree


class GameManager:
    """Orchestrates the game flow and manages game state."""
    
    def __init__(self, board_size: int = 3):
        """
        Initialize the game manager.
        
        Args:
            board_size: Size of the game board (default: 3 for 3×3)
        """
        pass
    
    def setup_players(self):
        """Initialize human and AI players."""
        pass
    
    def play_game(self):
        """Main game loop for a single game."""
        pass
    
    def switch_player(self):
        """Alternate between players."""
        pass
    
    def handle_game_end(self, winner: str | None):
        """
        Process win/loss/draw and trigger AI learning.
        
        Args:
            winner: Symbol of winning player or None for draw
        """
        pass
    
    def play_multiple_games(self):
        """Allow playing multiple games in sequence."""
        pass
    
    def display_board(self):
        """Output current board state."""
        pass
