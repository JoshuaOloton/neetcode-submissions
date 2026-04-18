class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = {}
        def dfs(i):
            if i == len(nums) - 1:
                return True
            if i >= len(nums):
                return False

            if i in seen:
                return seen[i]

            for j in range(1, nums[i] + 1):
                if i + j in seen and seen[i + j]:
                    return seen[i + j]
                if dfs(i + j):
                    seen[i + j] = True
                    return True
            seen[i] = False
            return False
        
        return dfs(0)