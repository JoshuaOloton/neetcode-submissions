class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(strs[0])
        res = strs[0]
        for s in strs:
            if len(s) < shortest:
                shortest = len(s)
                res = s

        i = 0
        prev = ""

        while i < len(strs[0]):
            for s in strs:
                if i > len(s):
                    return s
                if s[0:i+1] != prev and len(prev) > 0:
                    return s[0:i] 
                if len(prev) == 0:
                    prev = s[0:i+1]
            prev = ""
            i += 1
        
        return res