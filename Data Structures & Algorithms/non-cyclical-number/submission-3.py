class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False # cyclical
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True # non-cyclical
    
    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            output += (n % 10) ** 2
            n //= 10
        print(output)
        return output