class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        drome = ""

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]
                if substr == substr[::-1] and len(substr) > 1 and len(substr) > len(drome):
                    drome = substr

        return drome if drome != "" else s[0]