class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dist = -1
        q = deque()
        children = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        rotten = set()
        num_fresh = 0
        num_rotten = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                if grid[r][c] == 2:
                    num_rotten += 1

        if num_fresh == 0:
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    rotten.add((r, c))

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in children:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 1 and (nr, nc) not in rotten
                    ):
                        q.append([nr, nc])
                        rotten.add((nr, nc))
            dist += 1

        print(num_fresh, num_rotten, len(rotten))
        if num_fresh + num_rotten > len(rotten):
            return -1

        return dist 
