# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, node):
        if node is None:
            return 0
        left = self.recursive(node.left)
        right = self.recursive(node.right)
        return max(left, right) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maximum depth is the number of nodes along the longest path
        # from the root node down to the farthest leaf node.
        return self.recursive(root)
