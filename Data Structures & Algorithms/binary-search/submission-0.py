class Solution:
    def recursive_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1

        mid = (start+end)//2

        if nums[mid] > target:     # search lower half
            return self.recursive_search(nums, target, start, mid-1)
        elif nums[mid] < target:   # search upper half
            return self.recursive_search(nums, target, mid+1, end)
        else:
            return mid

    def search(self, nums: List[int], target: int) -> int:
        return self.recursive_search(nums, target, 0, len(nums)-1)

