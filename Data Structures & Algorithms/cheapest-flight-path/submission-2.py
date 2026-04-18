class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        pq = [(0, src, -1)] # (weight, node, stops)

        # build adj map
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        while pq:
            w, n, stops = heapq.heappop(pq)
            if stops > k:
                continue
            if w <= dist[n]:
                dist[n] = w
            new_stops = stops + 1
            for n1, w1 in adj[n]:
                new_dist = w + w1
                if new_dist > dist[n1]:
                    continue
                heapq.heappush(pq, (new_dist, n1, new_stops))
        
        print(dist)
        return dist[dst] if dist[dst] < INF else -1