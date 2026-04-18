class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        init_set = set(nums)
        seen = set()
        res = 0
        length = 0
        for n in nums:
            if n in seen:
                continue
            if n - 1 not in init_set: # beginning of sequence
                curr = n
                while curr in init_set:
                    curr += 1
                    length += 1
                    seen.add(curr)
                res = max(res, length)
                length = 0
        
        return res