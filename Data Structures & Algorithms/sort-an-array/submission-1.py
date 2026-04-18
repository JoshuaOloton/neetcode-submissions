class Solution:
    def merge(self, nums: List[int], l: int, r: int):
        m = (l + r) // 2
        left = nums[l : m]
        right = nums[m : r]
        i, j, k = 0, 0, l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        def split(nums, l, r):
            if l + 1 == r:
                return
            
            m = (l + r) // 2
            split(nums, l, m)
            split(nums, m, r)

            self.merge(nums, l, r)

            return

    
        split(nums, 0, len(nums))
        return nums