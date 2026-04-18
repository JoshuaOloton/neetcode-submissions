class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        times = {node: float('inf') for node in range(1, n + 1)}
        times[k] = 0

        pq = [(0, k)]
        while pq:
            t, u = heapq.heappop(pq)
            for v, w in adj[u]:
                new_t = t + w
                if new_t > times[v]:
                    continue
                heapq.heappush(pq, (new_t, v))
                times[v] = new_t
        
        res = max(times.values())
        return res if res < float('inf') else -1