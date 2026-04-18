class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operatorsMap = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operatorsMap:
                second = stack.pop()
                first = stack.pop()

                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                elif token == '/':
                    result = int(first / second)
                
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
