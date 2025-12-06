"""
Tic Tac Toe AI with BST Project
Fal25 CS034 | CRN: 78704
Group 2:
    Jenny Morris
    Chih-Hsiang Chang
    Nathaniel John Hernandez
    

File:
    Game Manager class - game_manager.py

    Game Manager module for Tic-Tac-Toe game.
    Orchestrates the game flow and manages game state.

To Do:
    ???

"""

from board import Board
from player import Player, HumanPlayer
from config import SYMBOL_X, SYMBOL_O
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
        self.board = Board(board_size)
        self.player_x = None
        self.player_o = None
        self.current_player = None
        self.games_played = 0
        self.losing_tree = LosingStateTree()  # Shared learning tree
        self.ai_player = None  # Track AI player for learning
        self.last_ai_state = None # Track state after AI's last move
    
    def setup_players(self):
        """Initialize human and AI players."""
        print("\n=== Tic-Tac-Toe Game Setup ===")
        
        # Phase 4: AI Player with shared losing tree
        self.player_x = HumanPlayer(SYMBOL_X)
        self.player_o = AIPlayer(SYMBOL_O, self.losing_tree)
        self.ai_player = self.player_o  # Track AI for learning
        
        # X always starts first
        self.current_player = self.player_x
        
        print(f"\nPlayer {SYMBOL_X} (Human) vs Player {SYMBOL_O} (AI)")
        print(f"Player {SYMBOL_X} goes first!\n")
    
    def play_game(self):
        """Main game loop for a single game."""
        print("\n" + "="*40)
        print(f"Starting Game #{self.games_played + 1}")
        print("="*40)
        
        self.board.reset()
        self.current_player = self.player_x
        self.last_ai_state = None
        
        while True:
            # Display current board
            self.display_board()
            
            # Get current player's move
            row, col = self.current_player.choose_move(self.board)
            
            # Apply the move
            self.board.apply_move(row, col, self.current_player.symbol)

            # Capture AI state
            if self.current_player == self.ai_player:
                self.last_ai_state = self.board.to_flat_list()
            
            # Check for winner
            winner = self.board.check_winner()
            if winner:
                self.display_board()
                self.handle_game_end(winner)
                break
            
            # Check for draw
            if self.board.is_full():
                self.display_board()
                self.handle_game_end(None)
                break
            
            # Switch to other player
            self.switch_player()
        
        self.games_played += 1
    
    def switch_player(self):
        """Alternate between players."""
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x
    
    def handle_game_end(self, winner: str | None):
        """
        Process win/loss/draw and trigger AI learning.
        
        Args:
            winner: Symbol of winning player or None for draw
        """
        print("\n" + "="*40)
        if winner:
            print(f"🎉 Player {winner} WINS! 🎉")
            
            # Trigger AI learning if human won (AI lost)
            if winner == SYMBOL_X and self.ai_player:
                print("AI is learning from this loss...")
                if self.last_ai_state:
                    self.ai_player.learn_from_loss(self.last_ai_state)
                else:
                    self.ai_player.learn_from_loss(self.board)
        else:
            print("🤝 It's a DRAW! 🤝")
        print("="*40)
    
    def play_multiple_games(self):
        """Allow playing multiple games in sequence."""
        self.setup_players()
        
        while True:
            self.play_game()
            
            # Ask if players want to play again
            play_again = input("\nPlay another game? (y/n): ").strip().lower()
            if play_again not in ['y', 'yes']:
                break
        
        print(f"\n=== Game Over ===")
        print(f"Total games played: {self.games_played}")
        print("Thanks for playing!")
    
    def display_board(self):
        """Output current board state."""
        print("\n" + str(self.board) + "\n")
