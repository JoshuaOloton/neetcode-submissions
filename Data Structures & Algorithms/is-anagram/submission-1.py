class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapped = {}
        for i in range(len(s)):
            if not mapped.get(s[i]):
                mapped[s[i]]=1
            else:
                mapped[s[i]]+=1
        print(mapped)
        for j in range(len(t)):
            if not mapped.get(t[j]):
                return False
            else:
                if mapped.get(t[j]) == 1:
                    mapped.pop(t[j])
                else:
                    mapped[t[j]]-=1
        return len(mapped) == 0
