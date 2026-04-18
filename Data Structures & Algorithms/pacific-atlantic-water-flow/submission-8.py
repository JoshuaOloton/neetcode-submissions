class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        NEIGBHORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))

            for dr, dc in NEIGBHORS:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or 
                    nc < 0 or nc >= COLS
                ):
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, visited)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        
        return list(pacific & atlantic)
