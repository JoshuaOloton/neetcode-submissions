class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapped = {}
        for num in nums:
            mapped[num] = 1 + mapped.get(num, 0)

        count = [[] for _ in range(len(nums) + 1)]
        for n, f in mapped.items():
             count[f].append(n)

        i = 0
        res = []
        for a in range(len(count)-1, -1, -1):
            for c in count[a]:
                res.append(c)
                i += 1
                if i == k:
                    return res
