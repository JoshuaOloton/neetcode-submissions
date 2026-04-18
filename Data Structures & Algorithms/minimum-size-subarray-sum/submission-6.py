class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curr = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target and l <= r:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
            
        return res if res < float('inf') else 0
            