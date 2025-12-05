"""Unit tests for LosingStateTree binary search tree."""

import os
import tempfile
import unittest

from losing_tree import LosingStateTree


class LosingStateTreeTests(unittest.TestCase):
    """Verify insert and contains behavior for the BST of board states."""

    def setUp(self):
        self.tree = LosingStateTree()

    def test_empty_tree_contains_returns_false(self):
        self.assertFalse(self.tree.contains([" ", "X", "O"]))

    def test_insert_and_contains_single_state(self):
        state = ["X", "O", " "]
        self.tree.insert(state)
        self.assertTrue(self.tree.contains(state))

    def test_insert_respects_bst_order(self):
        left_state = [" ", "O", "X"]
        root_state = ["O", " ", "X"]
        right_state = ["X", "X", "O"]

        self.tree.insert(root_state)
        self.tree.insert(left_state)
        self.tree.insert(right_state)

        self.assertTrue(self.tree.contains(left_state))
        self.assertTrue(self.tree.contains(root_state))
        self.assertTrue(self.tree.contains(right_state))

    def test_duplicate_inserts_do_not_break_tree(self):
        state = ["X", "O", " "]
        self.tree.insert(state)
        self.tree.insert(state)  # should be ignored gracefully
        self.assertTrue(self.tree.contains(state))

    def test_save_and_load_round_trip(self):
        states = [
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", "X", "O"],
        ]
        for state in states:
            self.tree.insert(state)

        with tempfile.TemporaryDirectory() as tmpdir:
            filename = os.path.join(tmpdir, "states.json")
            self.tree.save_to_file(filename)

            new_tree = LosingStateTree()
            new_tree.load_from_file(filename)

            for state in states:
                self.assertTrue(new_tree.contains(state))


if __name__ == "__main__":
    unittest.main()
