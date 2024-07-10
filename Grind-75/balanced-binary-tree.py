# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # The depth of a node is the number of edges present in path from the root node 
    # of a tree to that node.
    # The height of a node is the number of edges present in the longest path 
    # connecting that node to a leaf node.
    # https://stackoverflow.com/questions/2603692/what-is-the-difference-between-depth-and-height-in-a-tree
    # sol ref: https://leetcode.com/problems/balanced-binary-tree/solutions/5180394/easy-solution-with-explanation
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.is_bal = True

        def max_depth(node):

            if node is None:
                return 0
            l = max_depth(node.left)
            r = max_depth(node.right)

            if (abs(l-r) > 1):
                self.is_bal = False
            return max(l, r) + 1
        
        max_depth(root)
        return self.is_bal
