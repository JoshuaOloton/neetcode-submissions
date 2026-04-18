class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = defaultdict(list)
        heap1 = []

        for n in arr:
            offset = abs(n - x)
            diff[offset].append(n)
            if len(diff[offset]) == 1:
                heapq.heappush(heap1, offset)

        heap2 = []
        i = 0
        while i < k:
            t = heapq.heappop(heap1)
            for s in diff[t]:
                heapq.heappush(heap2, s)
                i += 1
                if i >= k:
                    break
        
        res = []
        while len(heap2):
            res.append(heapq.heappop(heap2))
        
        return res
