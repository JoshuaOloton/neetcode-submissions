class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        cache1 = [-1] * len(nums)
        cache2 = [-1] * len(nums)

        def dfs(i, dp, nos):
            if i >= len(nos):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(
                nos[i] + dfs(i + 2, dp, nos), 
                dfs(i + 1, dp, nos))
            return dp[i]
        
        return max(
            dfs(0, cache1, nums[:n-1]),
            dfs(0, cache2, nums[1:n]),
        )
