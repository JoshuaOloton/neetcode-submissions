class Solution:
    def isValid(self, s: str) -> bool:
        open = { '(', '{', '[' }
        close = { ')', '}', ']' }
        map = {')': '(', '}': '{', ']': '['}

        stack = []
        for c in s:
            if c in open:
                stack.append(c)
                continue
            if not stack or map[c] != stack[-1]:
                return False
            stack.pop()
        
        return not stack