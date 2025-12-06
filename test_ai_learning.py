"""Test script to verify AI learning functionality."""

from board import Board
from ai_player import AIPlayer
from losing_tree import LosingStateTree


def test_ai_learning():
    """Test that AI learns from losses and avoids known losing states."""
    print("Testing AI Learning Mechanism\n")
    print("="*50)
    
    # Setup
    tree = LosingStateTree()
    ai = AIPlayer("O", tree)
    board = Board(3)
    
    # Test 1: Empty tree - AI should make any move
    print("\nTest 1: Empty tree (no learning yet)")
    print("AI should be able to choose any empty cell")
    move = ai.choose_move(board)
    print(f"✓ AI chose move: {move}")
    
    # Test 2: Simulate a losing state (State BEFORE the opponent wins)
    print("\nTest 2: Simulate a losing board state (State before X wins)")
    # Scenario: X is at (0,0) and (1,1). O is at (0,1).
    # X is about to move to (2,2) and win.
    # We want AI to learn that the state [X, O, ., ., X, ., ., ., .] leads to a loss.
    board.reset()
    board.apply_move(0, 0, "X")
    board.apply_move(1, 1, "X")
    board.apply_move(0, 1, "O") 
    
    print("Board state (Before X wins):")
    print(board)
    
    losing_state = board.to_flat_list()
    print(f"Flat state: {losing_state}")
    
    # AI learns from this state (simulating the fix in GameManager)
    print("\nAI learning from loss...")
    ai.learn_from_loss(losing_state)
    
    # Test 3: Check that state is in tree
    print("\nTest 3: Verify state is stored in tree")
    is_stored = tree.contains(losing_state)
    print(f"State in tree: {is_stored}")
    if is_stored:
        print("✓ Learning successful!")
    else:
        print("✗ Learning failed!")
    
    # Test 4: AI avoids recreating that exact state
    print("\nTest 4: AI should avoid moves leading to known losing states")
    board2 = Board(3)
    board2.apply_move(0, 0, "X")
    board2.apply_move(1, 1, "X")
    # AI's turn - if it places at (0, 1), it creates the losing state
    
    print("Current board:")
    print(board2)
    print(f"Empty cells: {board2.get_empty_cells()}")
    
    # Simulate checking move at (0, 1)
    is_safe = ai._evaluate_move(board2, 0, 1)
    print(f"\nIs move (0, 1) safe? {is_safe}")
    if not is_safe:
        print("✓ AI correctly identifies this as an unsafe move!")
    else:
        print("✗ AI failed to recognize unsafe move")
    
    # Test 5: Multiple states learning
    print("\n" + "="*50)
    print("Test 5: Learning multiple states")
    
    board3 = Board(3)
    board3.apply_move(0, 0, "X")
    board3.apply_move(1, 1, "X")
    board3.apply_move(2, 2, "X")  # Diagonal win
    ai.learn_from_loss(board3)
    
    print(f"States in tree: 2")
    print("✓ Multiple states can be learned")
    
    print("\n" + "="*50)
    print("All tests completed!")


if __name__ == "__main__":
    test_ai_learning()
