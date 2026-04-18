class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashset = set(nums)
        max_length = 0

        for n in hashset:
            if n-1 not in hashset: # Start of sequence
                # Find all elements of consecutive sequence
                length = 0

                # Continue checking for consecutive numbers (n+1, n+2, etc.)
                while n+length in hashset:
                    length += 1

                if length > max_length:
                    max_length = length

        return max_length