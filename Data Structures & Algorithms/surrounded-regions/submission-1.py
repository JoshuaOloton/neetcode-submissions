class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        is_border = False
        region, is_valid = [], [] 

        def dfs(r, c):
            nonlocal is_border
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] == "X" or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            region.append((r, c))

            if (
                r == 0 or r == ROWS - 1 or
                c == 0 or c == COLS - 1
            ):
                is_border = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
                if not is_border and region:
                    is_valid.append(region)
                region = []
                is_border = False
        
        for v in is_valid:
            for r, c in v:
                board[r][c] = "X"
