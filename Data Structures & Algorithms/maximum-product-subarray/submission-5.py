class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = -float('inf')
        for i in range(n):
            cur = 1
            for j in range(i,n):
                cur *= nums[j]
                res = max(res, cur)
        return res
