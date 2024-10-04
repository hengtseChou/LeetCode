# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # ref: https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

        def dfs(node, min_val, max_val):
            if node is None:
                return True
            if node.val < min_val or node.val > max_val:
                return False
            return dfs(node.left, min_val, node.val - 1) and dfs(node.right, node.val + 1, max_val)

        return dfs(root, float("-inf"), float("inf"))
