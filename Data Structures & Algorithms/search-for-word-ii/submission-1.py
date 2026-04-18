class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        seen = set()

        def dfs(r, c, index):
            if index == len(word):
                return True

            if (r < 0 or r == len(board) or 
                c < 0 or c == len(board[0]) or 
                board[r][c] != word[index] or (r,c) in seen):
                return False

            # board[r][c] = '*'
            seen.add((r,c))

            ret = (
                dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or
                dfs(r,c+1,index+1) or dfs(r,c-1,index+1)
            )

            # board[r][c] = word[index]
            seen.remove((r,c))
            
            return ret


        for word in words:
            flag = False
            for r in range(len(board)):
                if flag:
                    break
                for c in range(len(board[0])):
                    if board[r][c] != word[0]:
                        continue
                    if dfs(r,c,0):
                        flag = True
                        res.append(word)
                        break
        
        return res

