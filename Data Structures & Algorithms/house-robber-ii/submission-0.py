class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        one, two = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            one, two = two, max(nums[i]+one, two)

        three, four = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            three, four = four, max(nums[i]+three, four)

        return max(two, four)
        