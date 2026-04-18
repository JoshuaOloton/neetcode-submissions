class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        while i > 0:
            j = i - 1
            while j + nums[j] < i:
                j -= 1
                if j < 0:
                    return False
            i = j
    
        return True