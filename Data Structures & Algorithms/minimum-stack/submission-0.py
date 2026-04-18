class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return float('inf')
        

    def getMin(self) -> int:
        minValue = float('inf')

        for element in self.stack:
            minValue = min(element, minValue)
        
        return minValue
        
