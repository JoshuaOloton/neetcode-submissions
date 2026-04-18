class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, max_prod, min_prod = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(nums[i], max_prod*nums[i])
            min_prod = min(nums[i], min_prod*nums[i])
            
            res = max(res, max_prod)
        
        return res
