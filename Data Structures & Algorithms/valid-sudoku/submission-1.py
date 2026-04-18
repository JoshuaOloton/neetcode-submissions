class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_seen, row_seen = set(), set()
        for i in range(len(board)):
            row_seen.clear()
            col_seen.clear()
            for j in range(len(board[0])):
                if board[i][j] in row_seen and board[i][j] != '.':
                    return False
                row_seen.add(board[i][j])
                if board[j][i] in col_seen and board[j][i] != '.':
                    print(2)
                    return False
                col_seen.add(board[j][i])
        
        box_seen = set()
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(3)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(0, 3):
            for j in range(3, 6):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(4)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(0, 3):
            for j in range(6, 9):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(5)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(3, 6):
            for j in range(0, 3):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(6)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(7)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(8)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(9)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(10)
                    return False
                box_seen.add(board[i][j])

        box_seen.clear()
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] in box_seen and board[i][j] != '.':
                    print(11)
                    return False
                box_seen.add(board[i][j])
        
        return True
        