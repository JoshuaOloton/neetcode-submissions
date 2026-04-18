class Solution:

    #BRUTE FORCE
    def maxArea2(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0

        while r > 0:
            while l < r:
                area = (r-l) * min(heights[l], heights[r])
                max_area = max(area, max_area)
                l += 1
            l, r = 0, r - 1
        
        return max_area

    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1
        
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
