class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        p_diag = set()
        n_diag = set()
        col = set()
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if (c in col or
                    r+c in p_diag or
                    r-c in n_diag):
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                p_diag.add(r+c)
                n_diag.add(r-c)

                dfs(r+1)

                board[r][c] = '.'
                col.remove(c)
                p_diag.remove(r+c)
                n_diag.remove(r-c)  

        dfs(0)
        return res              
                