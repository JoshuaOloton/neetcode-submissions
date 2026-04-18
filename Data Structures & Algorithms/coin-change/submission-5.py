class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        def dfs(i):
            if i == amount:
                return 0
            if dp[i] != -1:
                return dp[i]

            res = float('inf')
            for coin in coins:
                if i+coin <= amount:
                    res = min(res, 1+dfs(i+coin))
            
            dp[i] = res
            return res
        
        result = dfs(0)
        return -1 if result == float('inf') else result