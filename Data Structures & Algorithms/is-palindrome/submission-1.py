class Solution:
    def isAlphaNumeric(self, c: str) -> bool:
        return (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l < r and not self.isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
