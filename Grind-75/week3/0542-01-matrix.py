class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # ref 1: https://www.youtube.com/watch?v=2c7veIUvWNE
        # ref 2: https://lenchen.medium.com/leetcode-542-01-matrix-b85e06193ec8

        from collections import deque

        m = len(mat)
        n = len(mat[0])

        queue = deque()

        for i, row in enumerate(mat):
            for j, ele in enumerate(row):
                if ele:
                    mat[i][j] = float("inf")
                else:
                    queue.append((i, j))

        dirs = (0, 1, 0, -1, 0)
        while queue:
            i, j = queue.popleft()
            for k in range(4):
                x, y = i + dirs[k], j + dirs[k + 1]
                if -1 < x < m and -1 < y < n and mat[x][y] > mat[i][j] + 1:
                    mat[x][y] = mat[i][j] + 1
                    queue.append((x, y))
        return mat
