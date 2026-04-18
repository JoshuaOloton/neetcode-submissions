class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        length, max_length = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                length += 1
                max_length = max(length, max_length)
            else:
                length = 1
        
        return max_length