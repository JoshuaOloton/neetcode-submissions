class Solution:
    def isPalindrome(self, s: str) -> bool:
        original = []
        for i in range(len(s)):
            c = s[i].lower()
            if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'):
                original.append(c)
        return original == original[::-1]