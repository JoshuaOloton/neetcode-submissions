class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[k] = 0
        visited = set()

        adjMap = defaultdict(list)
        for u, v, t in times:
            adjMap[u].append((v, t))

        pq = [(0, k)]
        while pq:
            weight, node = heapq.heappop(pq)
            if node in visited:
                continue
            if weight < dist[node]:
                dist[node] = weight
            visited.add(node)

            for nei, w in adjMap[node]:
                heapq.heappush(pq, (weight + w, nei))
                
        dist = dist[1:] # index 0 is redundant (1->n)
        return -1 if max(dist) == INF else max(dist)
