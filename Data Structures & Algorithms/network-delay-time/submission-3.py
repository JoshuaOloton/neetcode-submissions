class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = defaultdict(list)
        for u, v, w in times:
            adjMap[u].append((v, w))
        
        res = 0
        visited = set()
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)

            res = max(res, w1)

            for n2, w2 in adjMap[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, (w1 + w2, n2))

        return res if len(visited) == n else -1
