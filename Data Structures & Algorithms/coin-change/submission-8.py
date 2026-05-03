class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {amount: 0}
        def dfs(sum):
            if sum in dp:
                return dp[sum]

            res = float('inf')
            for coin in coins:
                if sum + coin > amount:
                    continue
                res = min(res, 1 + dfs(sum + coin))
            dp[sum] = res

            return dp[sum]

        answer = dfs(0)
        return -1 if answer == float('inf') else answer 