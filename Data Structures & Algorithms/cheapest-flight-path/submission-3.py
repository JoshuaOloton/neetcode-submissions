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
            cost, city, stops = heapq.heappop(pq)
            if stops > k:
                continue
            if cost <= dist[city]:
                dist[city] = cost
            new_stops = stops + 1
            for nei, w in adj[city]:
                new_cost = cost + w
                if new_cost > dist[nei]:
                    continue
                heapq.heappush(pq, (new_cost, nei, new_stops))
        
        print(dist)
        return dist[dst] if dist[dst] < INF else -1