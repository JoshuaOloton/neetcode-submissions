class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(points)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        min_cost = 0
        visited = set()
        pq = [(0, 0)]
        while pq:
            w, n = heapq.heappop(pq)
            if n in visited:
                continue
            visited.add(n)
            min_cost += w
            for n1, w1 in adj[n]:
                if n1 in visited:
                    continue
                heapq.heappush(pq, (w1, n1))
        
        return min_cost
