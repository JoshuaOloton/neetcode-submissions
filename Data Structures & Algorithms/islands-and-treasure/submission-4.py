class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        children = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    visited.add((row, col))
                    if grid[row][col] == 0:
                        return steps

                    for dr, dc in children:
                        nr, nc = row+dr, col+dc
                        if (nr < 0 or nc < 0 or nr == ROWS or 
                            nc == COLS or (nr, nc) in visited or
                            grid[row][col] == -1
                        ):
                            continue

                        q.append((nr, nc))

                steps += 1

            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != INF:
                    continue
                visited = set()
                grid[r][c] = bfs(r, c)
        