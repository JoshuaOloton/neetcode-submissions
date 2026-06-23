class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_seen = min_seen = 1
        res = -float('inf')

        for num in nums:
            temp = num * max_seen
            max_seen = max(num * max_seen, num * min_seen, num)
            min_seen = min(temp, num * min_seen, num)

            res = max(res, max_seen, min_seen)
        return res