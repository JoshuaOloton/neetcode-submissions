class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        no_islands = 0
        neigbhors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                grid[row][col] = "0"
                for dr, dc in neigbhors:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    no_islands += 1
        
        return no_islands
        