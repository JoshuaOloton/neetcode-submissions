class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        mapped = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            mapped[num] = mapped.get(num,0)+1
        for n, count in mapped.items():
            freq[count].append(n)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        