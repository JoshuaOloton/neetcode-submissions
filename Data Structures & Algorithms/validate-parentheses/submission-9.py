class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')': '(', '}': '{', ']': '['}

        stack = []
        for c in s:
            if c not in bracketMap:
                stack.append(c)
                continue
            if not stack or bracketMap[c] != stack.pop():
                return False
        
        return not stack