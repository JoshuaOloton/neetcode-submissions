class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        curr = [0] * 26
        s1_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        for i in range(k):
            curr[ord(s2[i]) - ord('a')] += 1
        if curr == s1_count:
            return True

        for i in range(k, len(s2)):
            curr[ord(s2[i]) - ord('a')] += 1
            curr[ord(s2[i - k]) - ord('a')] -= 1

            if curr == s1_count:
                return True

        return False
