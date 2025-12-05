"""
Main entry point for Tic-Tac-Toe game.
"""

from game_manager import GameManager
from config import DEFAULT_BOARD_SIZE


def main():
    """
    Main function to start the game.
    """
    print("="*50)
    print("   Welcome to Learning Tic-Tac-Toe AI!")
    print("="*50)
    
    # Ask for board size
    while True:
        try:
            size_input = input(f"\nEnter board size (default {DEFAULT_BOARD_SIZE}): ").strip()
            if size_input == "":
                board_size = DEFAULT_BOARD_SIZE
                break
            board_size = int(size_input)
            if board_size >= 3:
                break
            else:
                print("Board size must be at least 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Create game manager and start playing
    game = GameManager(board_size)
    
    try:
        game.play_multiple_games()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
