class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        no_islands = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()

        def bfs(r, c):
            q = deque([(r,c)])
            while q:
                row,col = q.popleft()
                seen.add((row,col))
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    
                    if (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        (nr, nc) in seen or
                        grid[nr][nc] == "0"):
                        continue
                        
                    q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0" or (r,c) in seen:
                    continue
                bfs(r, c)
                no_islands += 1

        return no_islands 
        