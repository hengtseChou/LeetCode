"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        visited = {}

        # def dfs(node):
        #     if node in visited:
        #         return visited[node]
        #     clone = Node(val=node.val)
        #     visited[node] = clone
        #     for neighbor in node.neighbors:
        #         clone.neighbors.append(dfs(neighbor))
        #     return clone
        # return dfs(node)

        # DFS vs. BFS: DFS is often simpler in recursive problems,
        # but BFS is more iterative and avoids recursion depth limits.

        # Both DFS and BFS approaches are efficient, with a time complexity of O(N + E),
        # where N is the number of nodes and E is the number of edges in the graph.

        from collections import deque

        visited[node] = Node(val=node.val)
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(val=neighbor.val)
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]
