"""
Tic Tac Toe AI with BST Project
Fal25 CS034 | CRN: 78704
Group 2:
    Jenny Morris
    Chih-Hsiang Chang
    Nathaniel John Hernandez
    

File:
    Player class - player.py

    Player module for Tic-Tac-Toe game.
    Defines base Player class and HumanPlayer implementation.

To Do:
    ???

"""

from board import Board


class Player:
    """Abstract base class defining the player interface."""
    
    def __init__(self, symbol: str):
        """
        Initialize a player.
        
        Args:
            symbol: The player's symbol ("X" or "O")
        """
        self.symbol = symbol
    
    def choose_move(self, board: Board) -> tuple[int, int]:
        """
        Choose a move for the current board state.
        Abstract method to be implemented by subclasses.
        
        Args:
            board: Current game board
            
        Returns:
            tuple[int, int]: (row, col) coordinates of chosen move
        """
        raise NotImplementedError("Subclasses must implement choose_move()")


class HumanPlayer(Player):
    """Handles human player input."""
    
    def __init__(self, symbol: str):
        """
        Initialize a human player.
        
        Args:
            symbol: The player's symbol ("X" or "O")
        """
        super().__init__(symbol)
    
    def choose_move(self, board: Board) -> tuple[int, int]:
        """
        Prompt user for row and column input.
        
        Args:
            board: Current game board
            
        Returns:
            tuple[int, int]: (row, col) coordinates of chosen move
        """
        while True:
            try:
                print(f"\nPlayer {self.symbol}'s turn")
                row = int(input(f"Enter row (0-{board.size - 1}): "))
                col = int(input(f"Enter column (0-{board.size - 1}): "))
                
                if board.is_valid_move(row, col):
                    return (row, col)
                else:
                    print("Invalid move! Cell is either occupied or out of bounds. Try again.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
            except KeyboardInterrupt:
                print("\nGame interrupted by user.")
                raise
