# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

	# dfs
	# from collections import defaultdict
        # level_sum = defaultdict(int)
        # def dfs(node, level):
        #     if node is None:
        #         return
        #     level_sum[level] += node.val
        #     dfs(node.left, level + 1)
        #     dfs(node.right, level + 1)

        # dfs(root, 1)
        # if k > len(level_sum):
        #     return -1
        # values = list(level_sum.values())
        # values = sorted(values, reverse=True)
        # return values[k - 1]

	# bfs
	import heapq
        queue = deque([root])
        k_max = []

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            heapq.heappush(k_max, level_sum)
            if len(k_max) > k:
                heapq.heappop(k_max)

        if len(k_max) < k:
            return -1
        return k_max[0]
