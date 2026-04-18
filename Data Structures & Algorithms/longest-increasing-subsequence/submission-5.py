class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            j = i + 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                j += 1
        
        return max(dp)