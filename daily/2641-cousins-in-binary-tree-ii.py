# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        from collections import defaultdict

        level_sum = defaultdict(int)

        def dfs_sum(node, level):
            if node is None:
                return
            level_sum[level] += node.val
            dfs_sum(node.left, level + 1)
            dfs_sum(node.right, level + 1)
            left_val = node.left.val if node.left is not None else 0
            right_val = node.right.val if node.right is not None else 0
            node.children_sum = left_val + right_val

        def dfs_update(node, parent, level):
            if node is None:
                return
            if parent is None:
                sum_of_siblings = node.val
            else:
                sum_of_siblings = parent.children_sum
            node.val = level_sum[level] - sum_of_siblings
            dfs_update(node.left, node, level + 1)
            dfs_update(node.right, node, level + 1)

        dfs_sum(root, 0)
        dfs_update(root, None, 0)
        return root
