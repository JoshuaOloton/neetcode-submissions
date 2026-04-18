class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = cost.copy()
        for i in range(len(cost)-3, -1, -1):
            cache[i] = min(
                cost[i]+cache[i+1],
                cost[i]+cache[i+2]
            )
        
        print(cache)
        return min(cache[0], cache[1])