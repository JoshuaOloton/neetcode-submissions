class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        curr = [0] * 26
        s1_count = [0] * 26
        for c in s1:
            idx = ord(c) - ord('a')
            s1_count[idx] += 1

        for i in range(k):
            idx = ord(s2[i]) - ord('a')
            curr[idx] += 1
        if curr == s1_count:
            return True

        for i in range(k, len(s2)):
            add_idx = ord(s2[i]) - ord('a')
            sub_idx = ord(s2[i - k]) - ord('a')
            curr[add_idx] += 1
            curr[sub_idx] -= 1

            if curr == s1_count:
                return True

        return False
