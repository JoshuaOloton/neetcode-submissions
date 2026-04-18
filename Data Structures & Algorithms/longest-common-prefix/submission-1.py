class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lowest = len(strs[0])
        res = strs[0]
        for string in strs:
            if len(string) < lowest:
                lowest = len(string)
                res = string

        pos = 0
        prev = ""

        while pos < lowest:
            for string in strs:
                if pos > len(string):
                    return string
                if string[0:pos+1] != prev and len(prev) > 0:
                    return string[0:pos] 
                if len(prev) == 0:
                    prev = string[0:pos+1]
            prev = ""
            pos += 1
        
        return res