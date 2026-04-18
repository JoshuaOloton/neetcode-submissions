class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        curr = defaultdict(int)
        k = len(s1)
        if k > len(s2):
            return False

        for i in range(k):
            curr[s2[i]] += 1
        if curr == s1_count:
            return True

        for i in range(k, len(s2)):
            curr[s2[i]] += 1

            curr[s2[i - k]] -= 1
            if curr[s2[i - k]] == 0:
                del curr[s2[i - k]]

            if curr == s1_count:
                return True

        return False
