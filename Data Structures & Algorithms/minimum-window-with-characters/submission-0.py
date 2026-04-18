class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, window = {}, {}

        for c in t:
            count[c] = count.get(c, 0) + 1

        l, res = 0, float('inf')
        have, need = 0, len(count)
        resRange = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in count and window[c] == count[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < res:
                    res = r-l+1
                    resRange = [l, r]
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1 
                l += 1 

        if resRange == [-1, -1]:
            return ""
        start, end = resRange
        return s[start:end+1]
