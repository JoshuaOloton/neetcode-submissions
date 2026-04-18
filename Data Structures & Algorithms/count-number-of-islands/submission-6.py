class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        no_islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= ROWS or \
                col < 0 or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    no_islands += 1
        
        return no_islands
