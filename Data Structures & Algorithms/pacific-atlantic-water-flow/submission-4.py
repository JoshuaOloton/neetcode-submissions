class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        NEIGBHORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                (r, c) in visited
            ):
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
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r, c, pacific)
                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r, c, atlantic)
        
        return list(pacific & atlantic)
