class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            if nums[r] >= nums[l]:  # perfectly sorted subarray
                res = min(nums[l], res)
            
            mid = (l + r) // 2
            res = min(nums[mid], res)

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                if nums[mid] < nums[mid-1]:
                    return nums[mid] 
                r = mid - 1

        return res