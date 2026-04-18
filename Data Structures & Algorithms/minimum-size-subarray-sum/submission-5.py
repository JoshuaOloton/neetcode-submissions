class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                if cur >= target:
                    res = min(res, j - i + 1)
                    break
                
        return res if res < float('inf') else 0