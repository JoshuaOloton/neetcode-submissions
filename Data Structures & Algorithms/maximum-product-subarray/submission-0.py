class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                prod = 1
                for n in nums[i:j]:
                    prod *= n
                res = max(res, prod)
    
        return res