# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        i = j = k = 0
        # use this dirs tuple to control the clockwise movement
        dirs = (0, 1, 0, -1, 0)
        while True:
            matrix[i][j] = head.val
            head = head.next
            if head is None:
                break
            while True:
                x, y = i + dirs[k], j + dirs[k + 1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] == -1:
                    i, j = x, y
                    break
                k = (k + 1) % 4
        return matrix
