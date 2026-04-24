class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1] and j - i > resLen:
                    resLen = j - i
                    res = substr

        return res