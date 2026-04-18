class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -float('inf')
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                res = max(res, area)
            
        return res