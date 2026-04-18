class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, postf = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]
        for j in reversed(range(len(nums) - 1)):
            postf[j] = postf[j + 1] * nums[j + 1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pref[i] * postf[i]

        return res        
        