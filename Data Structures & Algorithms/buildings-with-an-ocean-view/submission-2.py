class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # decreasing monotonic stack
        stack = [0]
        for i in range(1, len(heights)):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack
