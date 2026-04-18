class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        top = set(sorted(count.values())[-k:])
        # print(top, count)
        for n, f in count.items():
            if f in top:
                res.append(n)
            if len(res) == k:
                break
        
        return res
