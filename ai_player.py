"""
Tic Tac Toe AI with BST Project
Fal25 CS034 | CRN: 78704
Group 2:
    Jenny Morris
    Chih-Hsiang Chang
    Nathaniel John Hernandez
    

File:
    AI Player class - ai_player.py

    AI Player module for Tic-Tac-Toe game.
    Implements the learning AI opponent.

To Do:
    Write functions

"""

from player import Player
from board import Board
from losing_tree import LosingStateTree


class AIPlayer(Player):
    """Implements the learning AI opponent."""
    
    def __init__(self, symbol: str, losing_tree: LosingStateTree):
        """
        Initialize an AI player.
        
        Args:
            symbol: The player's symbol ("X" or "O")
            losing_tree: Reference to the BST of losing board states
        """
        pass
    
    def choose_move(self, board: Board) -> tuple[int, int]:
        """
        Select best move by avoiding known losing states.
        
        Args:
            board: Current game board
            
        Returns:
            tuple[int, int]: (row, col) coordinates of chosen move
        """
        pass
    
    def learn_from_loss(self, board: Board):
        """
        Store the final losing board state in the BST.
        
        Args:
            board: The final board state when AI lost
        """
        pass
    
    def _evaluate_move(self, board: Board, row: int, col: int) -> bool:
        """
        Check if a move leads to a losing state.
        
        Args:
            board: Current game board
            row: Row index of potential move
            col: Column index of potential move
            
        Returns:
            bool: True if move is safe (not in losing states), False if unsafe
        """
        pass
