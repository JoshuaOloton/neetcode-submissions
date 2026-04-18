class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr, postfix_arr = [1] * len(nums), [1] * len(nums)
        prefix_prod, postfix_prod = 1, 1
        res = []

        for i in range(1, len(nums)):
            prefix_prod *= nums[i-1]
            prefix_arr[i] = prefix_prod
        
        for i in range(len(nums)-2, -1, -1):
            postfix_prod *= nums[i+1]
            postfix_arr[i] = postfix_prod
        
        for i in range(len(nums)):
            res.append(prefix_arr[i] * postfix_arr[i])
        
        return res
        