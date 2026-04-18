class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            # Check for odd-length palindromes
            res += self.countPalindromes(s, i, i)
            # Check for even-length palindromes
            res += self.countPalindromes(s, i, i+1)
            
        return res

    def countPalindromes(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res