class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(len(nums) - 2):
            dp[i + 2] = max(nums[i + 2] + dp[i], dp[i + 1])
        return dp[-1]
        