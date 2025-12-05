"""
Test script for Phase 1 implementation.
Tests Board, Player, and basic game functionality.
"""

from board import Board
from player import HumanPlayer
from config import SYMBOL_X, SYMBOL_O, EMPTY_CELL


def test_board():
    """Test Board class functionality."""
    print("Testing Board class...")
    
    # Test initialization
    board = Board(3)
    assert board.size == 3
    assert len(board.grid) == 3
    print("✓ Board initialization works")
    
    # Test valid move
    assert board.is_valid_move(0, 0) == True
    assert board.apply_move(0, 0, SYMBOL_X) == True
    assert board.grid[0][0] == SYMBOL_X
    print("✓ Valid move works")
    
    # Test invalid move (occupied cell)
    assert board.is_valid_move(0, 0) == False
    assert board.apply_move(0, 0, SYMBOL_O) == False
    print("✓ Invalid move (occupied) detected")
    
    # Test invalid move (out of bounds)
    assert board.is_valid_move(5, 5) == False
    assert board.is_valid_move(-1, 0) == False
    print("✓ Invalid move (out of bounds) detected")
    
    # Test empty cells
    empty = board.get_empty_cells()
    assert len(empty) == 8  # 9 total - 1 occupied
    print("✓ Get empty cells works")
    
    # Test flat list conversion
    flat = board.to_flat_list()
    assert len(flat) == 9
    assert flat[0] == SYMBOL_X
    print("✓ Flat list conversion works")
    
    # Test clone
    cloned = board.clone()
    assert cloned.grid[0][0] == SYMBOL_X
    cloned.apply_move(1, 1, SYMBOL_O)
    assert board.grid[1][1] == EMPTY_CELL  # Original unchanged
    print("✓ Board cloning works")
    
    # Test is_full
    assert board.is_full() == False
    for i in range(3):
        for j in range(3):
            board.apply_move(i, j, SYMBOL_X)
    assert board.is_full() == True
    print("✓ is_full() works")
    
    # Test reset
    board.reset()
    assert board.grid[0][0] == EMPTY_CELL
    print("✓ Board reset works")


def test_winner_detection():
    """Test winner detection logic."""
    print("\nTesting winner detection...")
    
    board = Board(3)
    
    # Test row win
    board.apply_move(0, 0, SYMBOL_X)
    board.apply_move(0, 1, SYMBOL_X)
    board.apply_move(0, 2, SYMBOL_X)
    assert board.check_winner() == SYMBOL_X
    print("✓ Row win detected")
    
    # Test column win
    board.reset()
    board.apply_move(0, 0, SYMBOL_O)
    board.apply_move(1, 0, SYMBOL_O)
    board.apply_move(2, 0, SYMBOL_O)
    assert board.check_winner() == SYMBOL_O
    print("✓ Column win detected")
    
    # Test main diagonal win
    board.reset()
    board.apply_move(0, 0, SYMBOL_X)
    board.apply_move(1, 1, SYMBOL_X)
    board.apply_move(2, 2, SYMBOL_X)
    assert board.check_winner() == SYMBOL_X
    print("✓ Main diagonal win detected")
    
    # Test anti-diagonal win
    board.reset()
    board.apply_move(0, 2, SYMBOL_O)
    board.apply_move(1, 1, SYMBOL_O)
    board.apply_move(2, 0, SYMBOL_O)
    assert board.check_winner() == SYMBOL_O
    print("✓ Anti-diagonal win detected")
    
    # Test no winner
    board.reset()
    board.apply_move(0, 0, SYMBOL_X)
    board.apply_move(0, 1, SYMBOL_O)
    assert board.check_winner() == None
    print("✓ No winner detected correctly")


def test_board_display():
    """Test board string representation."""
    print("\nTesting board display...")
    
    board = Board(3)
    board.apply_move(0, 0, SYMBOL_X)
    board.apply_move(1, 1, SYMBOL_O)
    board.apply_move(2, 2, SYMBOL_X)
    
    display = str(board)
    assert SYMBOL_X in display
    assert SYMBOL_O in display
    print("✓ Board display works")
    print("\nSample board display:")
    print(display)


def test_different_board_sizes():
    """Test different board sizes."""
    print("\nTesting different board sizes...")
    
    # Test 4x4 board
    board4 = Board(4)
    assert board4.size == 4
    assert len(board4.grid) == 4
    assert len(board4.to_flat_list()) == 16
    print("✓ 4x4 board works")
    
    # Test 5x5 board
    board5 = Board(5)
    assert board5.size == 5
    assert len(board5.get_empty_cells()) == 25
    print("✓ 5x5 board works")


def test_player_classes():
    """Test Player class structure."""
    print("\nTesting Player classes...")
    
    player = HumanPlayer(SYMBOL_X)
    assert player.symbol == SYMBOL_X
    print("✓ HumanPlayer initialization works")


def run_all_tests():
    """Run all Phase 1 tests."""
    print("="*50)
    print("   Phase 1 Testing Suite")
    print("="*50)
    
    try:
        test_board()
        test_winner_detection()
        test_board_display()
        test_different_board_sizes()
        test_player_classes()
        
        print("\n" + "="*50)
        print("   ✅ All Phase 1 tests PASSED!")
        print("="*50)
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
