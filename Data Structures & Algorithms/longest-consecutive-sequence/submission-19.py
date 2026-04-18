class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res, length = 0, 0
        
        for n in numset:
            if n - 1 not in numset: # beginning of sequence
                cur = n
                while cur in numset:
                    cur += 1
                    length += 1
                res = max(res, length)
                length = 0
                
        return res