class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        NEIGBHORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def p_dfs(r, c):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                (r, c) in pacific
            ):
                return
            
            pacific.add((r, c))
            for dr, dc in NEIGBHORS:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or 
                    nc < 0 or nc >= COLS
                ):
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                p_dfs(nr, nc)

        
        def a_dfs(r, c):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                (r, c) in atlantic
            ):
                return
            
            atlantic.add((r, c))
            for dr, dc in NEIGBHORS:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or 
                    nc < 0 or nc >= COLS
                ):
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                a_dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    p_dfs(r, c)
                if r == ROWS - 1 or c == COLS - 1:
                    a_dfs(r, c)
        
        print(pacific)
        print(atlantic)
        return list(pacific & atlantic)
