class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                res = max(res, prod)
        return res