# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # ref: https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0102.Binary%20Tree%20Level%20Order%20Traversal/README_EN.md
        # ref: http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html
        # ref: https://www.geeksforgeeks.org/level-order-tree-traversal/

        # via bfs

        ans = []
        if root is None:
            return ans

        queue = deque([root])
        while queue:
            current_lvl = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current_lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(current_lvl)
        return ans
