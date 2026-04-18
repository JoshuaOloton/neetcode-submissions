class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen, res = {}, []

        i = 0
        for idx, string in enumerate(strs):
            sorted_str = ''.join(sorted(string))
            if sorted_str not in seen:
                seen[sorted_str] = i
                res.append([string])
                i += 1
            else:
                res[seen[sorted_str]].append(string)
        print(seen)
        return res