class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for n, f in count.items():
            heapq.heappush(heap, (-f, n))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res