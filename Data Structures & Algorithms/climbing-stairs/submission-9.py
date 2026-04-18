class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            res = 0
            res += dfs(i+1)
            res += dfs(i+2)
        
            return res

        return dfs(0)