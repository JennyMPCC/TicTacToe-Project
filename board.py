"""
Tic Tac Toe AI with BST Project
Fal25 CS034 | CRN: 78704
Group 2:
    Jenny Morris
    Chih-Hsiang Chang
    Nathaniel John Hernandez
    

File:
    Board class - board.py

    Board module for Tic-Tac-Toe game.
    Manages the game board state and enforces game rules.

To Do:
    Complete

"""

import copy
from config import EMPTY_CELL


class Board:
    """Manages the game board state and enforces game rules."""

    # PUBLIC METHODS   
    
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
        Returns the winning player's symbol if any, or None if there is no winner.

        Preconditions:
            The board state is valid, with only one winner at most.

        Returns:
            str of winner's symbol or None depending on state
        """
        # Check for wins in every row and column
        for i in range(self.size):
            # Check if all symbols in this row or column match one non-empty symbol
            if self.grid[i][i] != EMPTY_CELL:
                if (all(self.grid[i][col] == self.grid[i][i] for col in range(self.size))
                or  all(self.grid[row][i] == self.grid[i][i] for row in range(self.size))):
                    return self.grid[i][i]
            
        # Check main diagonal (top-left to bottom-right)
        if self.grid[0][0] != EMPTY_CELL:
            if all(self.grid[i][i] == self.grid[0][0] for i in range(self.size)):
                return self.grid[0][0]
        
        # Check anti-diagonal (top-right to bottom-left)
        if self.grid[0][self.size - 1] != EMPTY_CELL:
            if all(self.grid[i][self.size - 1 - i] == self.grid[0][self.size - 1] for i in range(self.size)):
                return self.grid[0][self.size - 1]

        # Once at this point: no wins found.
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
        return self.to_string()
    
    def to_string(self) -> str:
        """
        String representation of the board for display.
        
        Returns:
            str: Formatted board display
        """
        # Initialize board string with spacing for formatting
        board_str = "     "

        # Add column coordinates
        for i in range(self.size):
            board_str += "%2d  " % i
        board_str += "\n"
        board_str += "    " + "----" * self.size + "-\n"  # Add dividing line

        # Add each row of the grid plus row coordinates on the left side
        for i in range(self.size):
            board_str += "%2d " % i # Add row coordinate
            for j in range(self.size):
                board_str += " | %s" % self.grid[i][j] #Add symbol at coordinate and dividing lines
            board_str += " |\n"
            board_str += "    " + "----" * self.size + "-\n" # Add dividing line
        return board_str