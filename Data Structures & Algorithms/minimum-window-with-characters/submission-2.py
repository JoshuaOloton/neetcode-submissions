class Solution:
    def isValidSubstr(self, s: str, t: str) -> bool:
        for c in t:
            if c not in s or t[c] > s[c]:
                return False
        return True

    def minWindow(self, s: dict, t: dict) -> str:
        count_t = Counter(t)
        count_s = {}

        l = 0
        res = float('inf')
        st = ""
        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1
            print(count_s)
            while self.isValidSubstr(count_s, count_t):
                if r - l + 1 < res:
                    res = r - l + 1
                    st = s[l : r + 1]
                count_s[s[l]] -= 1
                l += 1

        return st
                
