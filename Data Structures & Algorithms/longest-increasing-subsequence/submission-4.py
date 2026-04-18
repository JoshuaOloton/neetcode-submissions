class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1)] * (n + 1)
        def dfs(i, j):
            if i == len(nums):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            res = dfs(i + 1, j)
            if nums[i] > nums[j] or j == -1:
                res = max(res, 1 + dfs(i + 1, i))

            dp[i][j] = res
            return res

        return dfs(0, -1)