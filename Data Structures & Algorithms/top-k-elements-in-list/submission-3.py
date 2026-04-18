class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapped = {}
        for num in nums:
            mapped[num] = 1 + mapped.get(num, 0)

        min_heap = []
        for n, count in mapped.items():
            heapq.heappush(min_heap, [-count, n])
        
        res = []
        while k > 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1

        return res
         