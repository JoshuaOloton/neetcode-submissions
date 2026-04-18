class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-Source BFS

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        no_new_rottens, no_initial_fresh = 0, 0
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    no_initial_fresh += 1
        
        dist = 0
        is_added = False
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        q.append([nr, nc])
                        grid[nr][nc] = 2
                        no_new_rottens += 1
                        is_added = True
                
            if is_added:
                dist += 1
            is_added = False
            
        return dist if no_new_rottens == no_initial_fresh else -1



