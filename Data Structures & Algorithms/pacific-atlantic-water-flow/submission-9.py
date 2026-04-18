class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        NEIGHBORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited, prev=0):
            if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS or
            (r, c) in visited or 
            heights[r][c] < prev):
                return

            visited.add((r, c))
            curr = heights[r][c]

            dfs(r + 1, c, visited, curr)
            dfs(r - 1, c, visited, curr)
            dfs(r, c + 1, visited, curr)
            dfs(r, c - 1, visited, curr)
        
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        return list(atlantic & pacific)