"""
Board module for Tic-Tac-Toe game.
Manages the game board state and enforces game rules.
"""

import copy
from config import EMPTY_CELL


class Board:
    """Manages the game board state and enforces game rules."""
    
    def __init__(self, size: int = 3):
        """
        Initialize board with specified size.
        
        Args:
            size: The dimension of the square board (default: 3 for 3×3)
        """
        self.size = size
        self.grid = [[EMPTY_CELL for _ in range(size)] for _ in range(size)]
    
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
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """
        Check if a move is legal (within bounds and cell is empty).
        
        Args:
            row: Row index
            col: Column index
            
        Returns:
            bool: True if move is valid, False otherwise
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col] == EMPTY_CELL
        return False
    
    def check_winner(self) -> str | None:
        """
        Check if there is a winner.
        
        Returns:
            str | None: "X", "O", or None if no winner yet
        """
        # Check rows
        for row in range(self.size):
            if self.grid[row][0] != EMPTY_CELL:
                if all(self.grid[row][col] == self.grid[row][0] for col in range(self.size)):
                    return self.grid[row][0]
        
        # Check columns
        for col in range(self.size):
            if self.grid[0][col] != EMPTY_CELL:
                if all(self.grid[row][col] == self.grid[0][col] for row in range(self.size)):
                    return self.grid[0][col]
        
        # Check main diagonal (top-left to bottom-right)
        if self.grid[0][0] != EMPTY_CELL:
            if all(self.grid[i][i] == self.grid[0][0] for i in range(self.size)):
                return self.grid[0][0]
        
        # Check anti-diagonal (top-right to bottom-left)
        if self.grid[0][self.size - 1] != EMPTY_CELL:
            if all(self.grid[i][self.size - 1 - i] == self.grid[0][self.size - 1] for i in range(self.size)):
                return self.grid[0][self.size - 1]
        
        return None
    
    def is_full(self) -> bool:
        """
        Check if all cells are occupied.
        
        Returns:
            bool: True if board is full, False otherwise
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == EMPTY_CELL:
                    return False
        return True
    
    def to_flat_list(self) -> list[str]:
        """
        Convert the 2D grid to a 1D list for BST storage.
        
        Returns:
            list[str]: Flat list representation of the board
        """
        flat = []
        for row in self.grid:
            flat.extend(row)
        return flat
    
    def get_empty_cells(self) -> list[tuple[int, int]]:
        """
        Get list of all empty cell coordinates.
        
        Returns:
            list[tuple[int, int]]: List of (row, col) tuples for empty cells
        """
        empty_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == EMPTY_CELL:
                    empty_cells.append((row, col))
        return empty_cells
    
    def clone(self):
        """
        Create a deep copy of the board for move simulation.
        
        Returns:
            Board: A new Board instance with the same state
        """
        new_board = Board(self.size)
        new_board.grid = copy.deepcopy(self.grid)
        return new_board
    
    def reset(self):
        """Clear the board for a new game."""
        self.grid = [[EMPTY_CELL for _ in range(self.size)] for _ in range(self.size)]
    
    def __str__(self) -> str:
        """
        String representation of the board for display.
        
        Returns:
            str: Formatted board display
        """
        lines = []
        
        # Create column headers
        col_headers = "   " + "   ".join(str(i) for i in range(self.size))
        lines.append(col_headers)
        lines.append("  " + "----" * self.size)
        
        # Create rows with row numbers
        for row_idx in range(self.size):
            row_str = f"{row_idx} | " + " | ".join(self.grid[row_idx][col] for col in range(self.size)) + " |"
            lines.append(row_str)
            if row_idx < self.size - 1:
                lines.append("  " + "----" * self.size)
        
        return "\n".join(lines)
