class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        box_seen = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row_seen[r]:
                    return False
                row_seen[r].add(board[r][c])

                if board[r][c] in col_seen[c]:
                    print(2)
                    return False
                col_seen[c].add(board[r][c])

                if board[r][c] in box_seen[(r // 3, c // 3)]:
                    print(3)
                    return False
                box_seen[(r // 3, c // 3)].add(board[r][c])

        return True