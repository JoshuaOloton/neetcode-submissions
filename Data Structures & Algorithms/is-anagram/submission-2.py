class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        print(count)
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        return not list(filter(lambda x: x != 0, count.values()))
