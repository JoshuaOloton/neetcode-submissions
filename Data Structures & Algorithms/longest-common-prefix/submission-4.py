class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(strs[0])
        res = strs[0]
        for string in strs:
            if len(string) < shortest:
                shortest = len(string)
                res = string

        i = 0
        prev = ""

        while i <= shortest:
            for string in strs:
                if string[0:i+1] != prev and len(prev) > 0:
                    return string[0:i] 
                if len(prev) == 0:
                    prev = string[0:i+1]
            prev = ""
            i += 1
        
        return res