class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        diff, max_diff = 0, 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right    # since right is all time low, update left with right pointer
            else:
                diff = prices[right] - prices[left]
                max_diff = max(diff, max_diff)
                
            right += 1

        return max_diff
