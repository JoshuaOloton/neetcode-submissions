class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        fmap = defaultdict(list)
        res = []

        for n, f in count.items():
            fmap[f].append(n)
        
        for f in sorted(fmap)[::-1]:
            for n in fmap[f]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []
