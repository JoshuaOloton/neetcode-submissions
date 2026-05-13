class Solution:
    def isValid(self, s: str) -> bool:
        open = { '(', '{', '[' }
        map = {')': '(', '}': '{', ']': '['}

        stack = []
        for c in s:
            if c in open:
                stack.append(c)
                continue
            if not stack or map[c] != stack.pop():
                return False
            # stack.pop()
        
        return not stack