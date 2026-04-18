class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, limit = 0, 0
        l, r = 0, 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                limit = max(limit, i + nums[i])
            steps += 1
            l, r = r + 1, limit
        
        return steps
        