class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            j = i
            while j < n:
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                j += 1

        return max(dp)