class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0

        def dfs(r, c):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in seen and
                    grid[nr][nc] == "1"
                ):
                    seen.add((nr, nc))
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1

        return islands