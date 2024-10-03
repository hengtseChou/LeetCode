from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # ref: https://www.quora.com/How-do-I-implement-flood-fill-using-BFS-Would-the-algorithm-be-faster
        # code below is a bfs implementation
        if image[sr][sc] == color:
            return image

        original_color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        queue = deque([(sr, sc)])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while queue:
            r, c = queue.popleft()
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    queue.append((nr, nc))
        return image
