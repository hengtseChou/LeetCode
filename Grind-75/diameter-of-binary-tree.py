# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.diameter = 0

    def recursive(self, node):
        if node is None:
            return 0
        left = self.recursive(node.left)
        right = self.recursive(node.right)
        # At any node, the longest path that goes through that node
        # is equal to the height of the left subtree plus the height of the right subtree.
        # This is because such a path would start at one leaf node in the left subtree,
        # travel up to the current node, and then down to another leaf node in the right subtree.
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursive(root)
        return self.diameter
