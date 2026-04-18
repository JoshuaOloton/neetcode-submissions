class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set(nums)
        count, max_count = (1, 0)
        for n in hashset:
            if n-1 not in hashset: # Start of sequence
                # Find all elements of consecutive sequence
                largest = 1
                while n+largest in hashset:
                    count += 1
                    largest += 1
                if count > max_count:
                    max_count = count
                count = 1
        return max_count