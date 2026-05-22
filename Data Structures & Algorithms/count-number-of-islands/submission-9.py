class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] == "0"
                    ):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    no_islands += 1
        
        return no_islands
