class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        store = set(nums)
        res = 0

        for n in nums:
            streak = 0
            if (n - 1) not in store:
                curr = n
                while curr in store:
                    seen.add(curr)
                    curr += 1
                    streak += 1
                    res = max(res, streak)
         
        return res
        