class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        def count(l, r):
            nonlocal resLen, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            count(i, i) # even length palindrome 
            count(i, i + 1) # odd length palindrome
        
        return res
            