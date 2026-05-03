class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        def dfs(change):
            if change in memo:
                return memo[change]

            res = float('inf')
            for coin in coins:
                if change - coin >= 0:
                    res = min(res, 1 + dfs(change - coin))
            
            memo[change] = res
            return memo[change]

        ans = dfs(amount)
        return -1 if ans == float('inf') else ans 