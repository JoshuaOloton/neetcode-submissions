class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curSum = -float('inf'), 0
        for i in range(len(nums)):
            curSum += nums[i]
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
        return res 