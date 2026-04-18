class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, postf, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in reversed(range(len(nums) - 1)):
            postf[i] = postf[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            res[i] = pref[i] * postf[i]

        return res        
        