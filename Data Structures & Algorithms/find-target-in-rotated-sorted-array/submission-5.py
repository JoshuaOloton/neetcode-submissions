class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[start]:    # left subarray
                if (target < nums[mid] and target < nums[start]) or target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:   # right subarray
                if target < nums[mid] or (target > nums[mid] and target > nums[end]):
                    end = mid - 1
                else:
                    start = mid + 1

        return -1
