class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in mapped:
                return [mapped[complement], i]
            if not nums[i] in mapped:
                mapped[nums[i]] = i
        return []
        