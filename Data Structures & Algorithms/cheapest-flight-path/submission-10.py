class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        tmp = dist.copy()

        for _ in range(k + 1):
            for u, v, w in flights:
                if dist[u] == float('inf'):
                    continue
                if dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
            dist = tmp.copy()
        
        return -1 if dist[dst] == float('inf') else dist[dst]