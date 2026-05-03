class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        res = -float('inf')

        for num in nums:
            temp = cur_max * num
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(temp, cur_min * num, num)
        
            res = max(res, cur_max)
        return res