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
import random
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
        super().__init__(symbol)
        self.losing_tree = losing_tree
    
    def choose_move(self, board: Board) -> tuple[int, int]:
        """
        Select best move by avoiding known losing states.
        
        Args:
            board: Current game board
            
        Returns:
            tuple[int, int]: (row, col) coordinates of chosen move
        """
        empty_cells = board.get_empty_cells()
        safe_moves = []
        unsafe_moves = []
        
        # Evaluate each possible move
        for row, col in empty_cells:
            if self._evaluate_move(board, row, col):
                safe_moves.append((row, col))
            else:
                unsafe_moves.append((row, col))
        
        # Prefer safe moves, fall back to unsafe if needed
        if safe_moves:
            return random.choice(safe_moves)
        else:
            return random.choice(unsafe_moves)
    
    def learn_from_loss(self, board: Board | list[str]):
        """
        Store the final losing board state in the BST.
        
        Args:
            board: The final board state when AI lost, or the flat list state
        """
        if isinstance(board, list):
            losing_state = board
        else:
            losing_state = board.to_flat_list()
            
        self.losing_tree.insert(losing_state)
        print(f"AI learned to avoid state: {losing_state}")
    
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
        # Clone board and simulate the move
        temp_board = board.clone()
        temp_board.apply_move(row, col, self.symbol)
        
        # Convert to flat list for BST lookup
        state = temp_board.to_flat_list()
        
        # Return True if safe (not in losing tree), False if unsafe
        return not self.losing_tree.contains(state)
