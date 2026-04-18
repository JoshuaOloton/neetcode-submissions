class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr, postfix_arr = [1] * len(nums), [1] * len(nums)
        prefix_prod, postfix_prod = 1, 1
        res = []

        for i in range(1, len(nums)):
            prefix_prod *= nums[i-1]
            prefix_arr[i] = prefix_prod
        
        for j in range(len(nums)-2, -1, -1):
            postfix_prod *= nums[j+1]
            postfix_arr[j] = postfix_prod
        
        for idx in range(len(nums)):
            res.append(prefix_arr[idx] * postfix_arr[idx])
        
        return res
        