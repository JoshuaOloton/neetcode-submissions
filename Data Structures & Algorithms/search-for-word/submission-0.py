class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(r,c,found):
            if found >= len(word):
                return True
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                board[r][c] != word[found] or 
                (r,c) in seen):
                return False 
            
            seen.add((r,c))
            res = (dfs(r,c-1,found+1) or
                dfs(r,c+1,found+1) or
                dfs(r-1,c,found+1) or
                dfs(r+1,c,found+1)) 
            seen.remove((r,c))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False
