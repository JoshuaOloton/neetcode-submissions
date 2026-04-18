class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for n in arr:
            diff = abs(x - n)
            heapq.heappush(heap, (diff, n))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[-1])
        
        return sorted(res)