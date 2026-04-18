class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapped = {}
        for num in nums:
            mapped[num] = 1 + mapped.get(num, 0)

        count = [[k, n] for n, k in mapped.items()]
        count.sort()

        res = []
        for i in range(len(count)-1, -1, -1):
            res.append(count[i][1])
            k -= 1
            if k == 0:
                return res