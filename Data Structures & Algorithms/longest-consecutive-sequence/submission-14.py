class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak, res = 0, 0
        store = set(nums)

        for n in nums:
            while n in store:
                streak += 1
                n += 1
            res = max(res, streak)
            streak = 0
        
        return res