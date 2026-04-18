class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(k):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s2_count == s1_count:
            return True

        for i in range(k, len(s2)):
            add_idx = ord(s2[i]) - ord('a')
            sub_idx = ord(s2[i - k]) - ord('a')
            s2_count[add_idx] += 1
            s2_count[sub_idx] -= 1

            if s2_count == s1_count:
                return True

        return False
