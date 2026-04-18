class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [[] for _ in range(len(strs))]
        mapped = {}
        for i, s in enumerate(strs):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in mapped:
                key = mapped[tuple(count)]
                res[key].append(s)
            else:
                res[i].append(s)
                mapped[tuple(count)] = i
                
        return list(filter(lambda x: x, res))
