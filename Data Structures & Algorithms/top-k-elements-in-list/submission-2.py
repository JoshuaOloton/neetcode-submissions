class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        res = sorted(freq_map, reverse=True, key=lambda num: freq_map[num])
        return res[:k]
        