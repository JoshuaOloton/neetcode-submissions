class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> List[int]:
        cur_max = max(nums[:k])
        res = [cur_max]
        l = 0
        for r in range(k, len(nums)):
            if nums[r] > cur_max:
                cur_max = nums[r]
            elif nums[l] == cur_max:
                    cur_max = nums[l + 1]
                    for i in range(l + 1, l + 1 + k):
                        cur_max = max(cur_max, nums[i])
            
            res.append(cur_max)
            l += 1

        return res
