class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        freqTable = {}

        for r in range(len(s)):
            freqTable[s[r]] = freqTable.get(s[r], 0) + 1
            while (r-l+1) - max(freqTable.values()) > k:
                freqTable[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res
