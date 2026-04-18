class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        count_s1 = Counter(s1)
        window = Counter(s2[:k])
        if count_s1 == window:
            return True
        
        l = 0
        for r in range(k, len(s2)):
            window[s2[r]] += 1
            window[s2[l]] -= 1
            l += 1
            if count_s1 == window:
                return True

        return False