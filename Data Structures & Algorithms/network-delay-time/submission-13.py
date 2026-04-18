class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        dist = {i: INF for i in range(1, n + 1)}
        dist[k] = 0

        adjMap = defaultdict(list)
        for u, v, t in times:
            adjMap[u].append((v, t))

        pq = [(0, k)]
        while pq:
            weight, node = heapq.heappop(pq)
            if weight > dist[node]:
                continue

            for nei, w in adjMap[node]:
                new_dist = weight + w
                if new_dist < dist[nei]:
                    heapq.heappush(pq, (new_dist, nei))
                    dist[nei] = new_dist

        res = max(dist.values())
        return -1 if res == INF else res