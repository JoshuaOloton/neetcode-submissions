class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0] * len(height), [0] * len(height)
        currLeft, currRight = 0, 0

        for i in range(len(height)):
            maxLeft[i] = currLeft
            currLeft =  max(currLeft, height[i])

        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = currRight
            currRight = max(currRight, height[i])

        print(maxLeft)
        print(maxRight)
        res = 0
        for i in range(len(height)):
            if min(maxLeft[i], maxRight[i]) < height[i]:
                continue
            res += min(maxLeft[i], maxRight[i]) - height[i]

        return res
