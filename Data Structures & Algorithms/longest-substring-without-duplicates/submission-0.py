class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mappedSet = set()
        res, left = 0, 0

        for right in range(len(s)):
            while s[right] in mappedSet:
                # shrink the window from the left until we remove the duplicate
                mappedSet.remove(s[left])
                left += 1
            mappedSet.add(s[right])
            res = max(res, right-left+1)

        return res