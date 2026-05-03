class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        res = -float('inf')

        for num in nums:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            
            cur_max = max(cur_max * num, num)
            cur_min = min(cur_min * num, num)
        
            res = max(res, cur_max)
        return res