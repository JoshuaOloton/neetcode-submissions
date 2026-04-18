class Solution:
    def findCheapestPrice(self, n: int, flights, src, dst, k):
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))

        pq = [(0, src, 0)]  # (cost, node, stops)

        while pq:
            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > k:
                continue

            for nei, price in graph[node]:
                heapq.heappush(pq, (cost + price, nei, stops + 1))

        return -1