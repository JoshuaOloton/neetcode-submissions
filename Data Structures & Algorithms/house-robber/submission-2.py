class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        one, two = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            one, two = two, max(nums[i] + one, two)

        return two
