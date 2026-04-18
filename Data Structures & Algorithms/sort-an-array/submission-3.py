class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, r):
            m = (l + r) // 2
            left = nums[l : m + 1]
            right = nums[m + 1 : r + 1]

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

        def mergeSort(l, r):
            if l == r:
                return
            
            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m + 1, r)

            merge(l, r)
        
        mergeSort(0, len(nums) - 1)
        return nums
        