class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i, n):
                l, r = i, j
                while l <= r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l > r:
                    res += 1
        
        return res