class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position_map = {}
        for idx, num in enumerate(nums):
            if (target - num) in position_map:
                return [position_map[target-num], idx]
            position_map[num] = idx
    
        return [-1, -1]