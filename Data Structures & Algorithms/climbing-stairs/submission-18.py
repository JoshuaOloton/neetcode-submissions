class Solution:
    def climbStairs(self, n: int) -> int:
        one, two, three = 1, 1, 1

        for _ in range(n - 1):
            three = one + two
            temp = one
            one = three
            two = temp
        
        return three
