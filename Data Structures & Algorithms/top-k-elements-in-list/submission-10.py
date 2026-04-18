class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = heapq.nlargest(k, count.keys(), key=count.get)
        return res