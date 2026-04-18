class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        cur = 1
        for _ in range(32):
            if cur & n:
                res += 1
            cur = (cur << 1)
            
        return res