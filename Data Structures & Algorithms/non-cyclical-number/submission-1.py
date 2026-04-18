class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            squares = 0
            for d in str(n):
                squares += (int(d) ** 2)
            if squares == 1:
                return True # non-cyclical
            if squares in seen:
                return False # cyclical
            seen.add(squares)
            n = squares

