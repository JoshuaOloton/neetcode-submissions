class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, cur = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target and l <= r:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1

        return res if res < float('inf') else 0
