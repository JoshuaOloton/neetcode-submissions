class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        start, end = 0, len(nums)-1

        while start <= end:
            if nums[end] > nums[start]:
                res = min(nums[start], res)
                break

            mid = (start+end) // 2
            res = min(nums[mid], res)

            if nums[mid] >= nums[start]: # left subsequence, search right
                start = mid + 1
            else:   # right subsequence, search left
                end = mid - 1

        return res