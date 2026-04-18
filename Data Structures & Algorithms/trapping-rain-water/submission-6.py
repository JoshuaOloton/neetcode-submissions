class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        n = len(height)
        maxLeft, maxRight = [0] * len(height), [0] * len(height)

        maxLeft[1] = height[0]
        for i in range(2, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
            
        maxRight[-2] = height[n - 1]
        for i in range(n - 3, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])

        print(maxLeft)
        print(maxRight)
        res = 0
        for i in range(n):
            if min(maxLeft[i], maxRight[i]) >= height[i]:
                res += min(maxLeft[i], maxRight[i]) - height[i]

        return res
