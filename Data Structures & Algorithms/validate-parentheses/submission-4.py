class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False


        stack = []
        bracketMap = {'(':')', '{':'}', '[':']'}
        
        for i in range(len(s)):
            if s[i] in bracketMap:
                stack.append(s[i])
            elif len(stack) > 0:
                popValue = stack.pop()
                if bracketMap[popValue] != s[i]:
                    return False
            else: # stack is empty, likely more closing than opening brackets
                return False

        if len(stack)> 0: 
            # stack is still populated, more opening than closing brackets
            return False
        return True
