class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_count = 0
        count = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev+1:
                count += 1
                print(count, nums[i], prev)
            elif nums[i] != prev:
                if count > max_count:
                    max_count = count
                count = 1
            prev = nums[i]
        if count > max_count:
            max_count = count
        return max_count
        