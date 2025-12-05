"""
Binary Search Tree module for storing losing board states.
Implements LosingStateNode and LosingStateTree classes.
"""


class LosingStateNode:
    """Represents a single node in the binary search tree."""
    
    def __init__(self, state: list[str]):
        """
        Initialize a node with a board state.
        
        Args:
            state: Flat list representation of a losing board state
        """
        self.state = state
        self.left: "LosingStateNode | None" = None
        self.right: "LosingStateNode | None" = None


class LosingStateTree:
    """Binary search tree for storing and querying losing board states."""
    
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root: LosingStateNode | None = None
    
    def insert(self, state: list[str]):
        """
        Add a new losing state to the tree.
        
        Args:
            state: Flat list representation of a board state
        """
        if self.root is None:
            self.root = LosingStateNode(state)
        else:
            self.root = self._insert_recursive(self.root, state)
    
    def contains(self, state: list[str]) -> bool:
        """
        Check if a state exists in the tree.
        
        Args:
            state: Flat list representation of a board state
            
        Returns:
            bool: True if state exists in tree, False otherwise
        """
        return self._contains_recursive(self.root, state)
    
    def _insert_recursive(self, node: LosingStateNode, state: list[str]) -> LosingStateNode:
        """
        Helper method for recursive insertion.
        
        Args:
            node: Current node in traversal
            state: State to insert
            
        Returns:
            LosingStateNode: Updated node
        """
        if state == node.state:
            return node
        if state < node.state:
            if node.left is None:
                node.left = LosingStateNode(state)
            else:
                node.left = self._insert_recursive(node.left, state)
        else:
            if node.right is None:
                node.right = LosingStateNode(state)
            else:
                node.right = self._insert_recursive(node.right, state)
        return node
    
    def _contains_recursive(self, node: LosingStateNode | None, state: list[str]) -> bool:
        """
        Helper method for recursive searching.
        
        Args:
            node: Current node in traversal
            state: State to search for
            
        Returns:
            bool: True if state found, False otherwise
        """
        if node is None:
            return False
        if state == node.state:
            return True
        if state < node.state:
            return self._contains_recursive(node.left, state)
        return self._contains_recursive(node.right, state)
    
    def save_to_file(self, filename: str):
        """
        (Optional) Serialize tree to file.
        
        Args:
            filename: Path to save file
        """
        import json

        def _inorder(node: LosingStateNode | None, states: list[list[str]]):
            if node is None:
                return
            _inorder(node.left, states)
            states.append(node.state)
            _inorder(node.right, states)

        states: list[list[str]] = []
        _inorder(self.root, states)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(states, file)
    
    def load_from_file(self, filename: str):
        """
        (Optional) Load tree from file.
        
        Args:
            filename: Path to load file
        """
        import json

        with open(filename, "r", encoding="utf-8") as file:
            states = json.load(file)

        # Rebuild tree from saved states
        for state in states:
            self.insert(state)
