class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        print(n, res)
        for _ in range(32):
            if n & 1:
                res += "1"
            else:
                res += "0"
            n >>= 1
        return int(res, 2)