"""
Board module for Tic-Tac-Toe game.
Manages the game board state and enforces game rules.
"""


class Board:
    """Manages the game board state and enforces game rules."""
    
    def __init__(self, size: int = 3):
        """
        Initialize board with specified size.
        
        Args:
            size: The dimension of the square board (default: 3 for 3×3)
        """
        pass
    
    def apply_move(self, row: int, col: int, symbol: str) -> bool:
        """
        Place a symbol at the given position.
        
        Args:
            row: Row index
            col: Column index
            symbol: Player symbol ("X" or "O")
            
        Returns:
            bool: True if move was successfully applied, False otherwise
        """
        pass
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is legal (within bounds and cell is empty).
        
        Args:
            row: Row index
            col: Column index
            
        Returns:
            bool: True if move is valid, False otherwise
        """
        pass
    
    def check_winner(self) -> str | None:
        """
        Check if there is a winner.
        
        Returns:
            str | None: "X", "O", or None if no winner yet
        """
        pass
    
    def is_full(self) -> bool:
        """
        Check if all cells are occupied.
        
        Returns:
            bool: True if board is full, False otherwise
        """
        pass
    
    def to_flat_list(self) -> list[str]:
        """
        Convert the 2D grid to a 1D list for BST storage.
        
        Returns:
            list[str]: Flat list representation of the board
        """
        pass
    
    def get_empty_cells(self) -> list[tuple[int, int]]:
        """
        Get list of all empty cell coordinates.
        
        Returns:
            list[tuple[int, int]]: List of (row, col) tuples for empty cells
        """
        pass
    
    def clone(self):
        """
        Create a deep copy of the board for move simulation.
        
        Returns:
            Board: A new Board instance with the same state
        """
        pass
    
    def reset(self):
        """Clear the board for a new game."""
        pass
    
    def __str__(self) -> str:
        """
        String representation of the board for display.
        
        Returns:
            str: Formatted board display
        """
        pass
