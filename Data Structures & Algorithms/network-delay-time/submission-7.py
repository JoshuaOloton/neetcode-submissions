class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]
        while pq:
            curr_dist, u = heapq.heappop(pq)
            
            for v, w in adj[u]:
                new_dist = curr_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
            
        result = max(dist[1:]) # index 0 is unused, will remain float('inf')
        return result if result < float('inf') else -1
