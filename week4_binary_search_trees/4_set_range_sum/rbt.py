"""
Implementation of Red-Black Tree
"""
from bst import Node, BST, Color, ColorNode


class RBT(BST):
    """
    Implementation of red-black tree. The tree obeys the following restrictions:
        1. the red edge is always leaning towards the left.
        2. a parent node can at most have one red child edge.
    """

    def __init__(self, root: ColorNode):
        super().__init__(root)

    def _rotate_left(self, node: ColorNode) -> ColorNode:
        """
        The node's right child is red. Perform left-rotation to comply red-left-leaning rule.
        """
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _rotate_right(self, node: ColorNode) -> ColorNode:
        """
        The node's left child is red. Perform right-rotation to make the node's right child red.
        """
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _flip_color(self, node: ColorNode) -> None:
        """
        When both of both of the node's children is red. Make both of the back and the parent red.
        """
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK
        node.color = Color.RED

    def _is_red(self, node: ColorNode) -> bool:
        """
        Check is a node is red. If it's None, return False
        """
        if node == None:
            return False
        return node.color == Color.RED

    def add(self, val: int) -> None:
        """
        Add a new key to RBT.
        """
        self._root = self._add(self._root, val)
        self._root.color = Color.BLACK

    def _add(self, node: ColorNode, val: int) -> ColorNode:
        """
        Overwrite BST's _add method with ColorNode.
        """
        if node == None:
            # Always set the newly added color to RED, then use the
            # operations to maintain the restrictions. Think about how a
            # new node is added in a 2-3 tree helps.
            return ColorNode(val, color=Color.RED)
        if val < node.val:
            node.left = self._add(node._left, val)
        elif val > node.val:
            node.right = self._add(node._right, val)

        # maintain red-black rules. See Algorithms page 438 for details.
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_color(node)

        return node

