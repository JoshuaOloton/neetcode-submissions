class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = "", 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > resLen:
                resLen = r - l - 1
                resIdx = l + 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > resLen:
                resLen = r - l - 1
                resIdx = l + 1
    
        return s[resIdx : resIdx + resLen]