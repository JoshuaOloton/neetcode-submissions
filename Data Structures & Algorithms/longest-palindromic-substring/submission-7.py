class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        def count_dromes(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            odd_drome = count_dromes(i, i)
            if len(odd_drome) > resLen:
                resLen = len(odd_drome)
                res = odd_drome
            even_drome = count_dromes(i, i + 1)
            if len(even_drome) > resLen:
                resLen = len(even_drome)
                res = even_drome
        
        return res