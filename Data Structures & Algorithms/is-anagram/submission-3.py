class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if count.get(c, 0) == 0:
                return False
            count[c] -= 1

        return not any(count.values())
        
        