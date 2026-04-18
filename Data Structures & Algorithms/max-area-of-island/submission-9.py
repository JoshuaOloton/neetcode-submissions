class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0
            or r >= ROWS or c >= COLS):
                return 0

            if (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            
            area = (dfs(r+1, c) +
            dfs(r-1, c) + 
            dfs(r, c+1) + dfs(r, c-1)) + 1

            return area


        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r, c)
                max_area = max(area, max_area)

        return max_area
        