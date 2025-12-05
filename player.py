"""
Player module for Tic-Tac-Toe game.
Defines base Player class and HumanPlayer implementation.
"""

from board import Board


class Player:
    """Abstract base class defining the player interface."""
    
    def __init__(self, symbol: str, name: str):
        """
        Initialize a player.
        
        Args:
            symbol: The player's symbol ("X" or "O")
            name: Player's name for display
        """
        pass
    
    def choose_move(self, board: Board) -> tuple[int, int]:
        """
        Choose a move for the current board state.
        Abstract method to be implemented by subclasses.
        
        Args:
            board: Current game board
            
        Returns:
            tuple[int, int]: (row, col) coordinates of chosen move
        """
        pass


class HumanPlayer(Player):
    """Handles human player input."""
    
    def __init__(self, symbol: str, name: str = "Human"):
        """
        Initialize a human player.
        
        Args:
            symbol: The player's symbol ("X" or "O")
            name: Player's name (default: "Human")
        """
        pass
    
    def choose_move(self, board: Board) -> tuple[int, int]:
        """
        Prompt user for row and column input.
        
        Args:
            board: Current game board
            
        Returns:
            tuple[int, int]: (row, col) coordinates of chosen move
        """
        pass
