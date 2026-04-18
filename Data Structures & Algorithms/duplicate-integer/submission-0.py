class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if map.get(num):
                return True
            map[num] = True
        return False