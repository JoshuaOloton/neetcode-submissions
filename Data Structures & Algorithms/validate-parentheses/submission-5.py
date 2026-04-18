class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        bracketMap = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char not in bracketMap:
                stack.append(char)
                continue

            if not stack or bracketMap[char] != stack[-1]:
                return False
            stack.pop()

        return not stack
