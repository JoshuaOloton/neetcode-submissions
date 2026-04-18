class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[-1] = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            if dp[i] == -1:
                dp[i] = 1
        
        return max(dp)