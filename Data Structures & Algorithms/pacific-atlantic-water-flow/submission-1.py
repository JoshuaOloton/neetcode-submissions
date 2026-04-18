class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable, atlantic_reachable = set(), set()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(r, c, visited, height):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS
                or (r, c) in visited or
                heights[r][c] < height):
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS-1])

        return list(atlantic_reachable & pacific_reachable)
