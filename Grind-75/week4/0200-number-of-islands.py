class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # traverse the grid until we found a 1
        # once we found a 1, then it's like flood-fill question
        # we mark it into 0 (in-place modification) or use a visited matrix

        # this can be solved via dfs or bfs, but bfs is giving MLE because of big queue

        rows, cols = len(grid), len(grid[0])
        count = 0
        # directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        # def dfs(r, c):
        #     if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
        #         return
        #     grid[r][c] = "0"
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)

        # the following implementation can call dfs() less
        def dfs(i, j):
            grid[i][j] = "0"

            if i + 1 < rows and grid[i + 1][j] == "1":
                dfs(i + 1, j)
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                dfs(i - 1, j)
            if j + 1 < cols and grid[i][j + 1] == "1":
                dfs(i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == "1":
                dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count
