class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable, atlantic_reachable = set(), set()

        def dfs(r, c, visited, lastHeight):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS
                or (r, c) in visited or
                heights[r][c] < lastHeight):
                return
            
            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS-1])

        return list(atlantic_reachable & pacific_reachable)
