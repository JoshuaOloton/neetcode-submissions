class Solution:
    def countBits(self, n: int) -> List[int]:
        start = [0, 1, 1]
        if n < 3:
            return start[:n+1]

        res = [0] * (n + 1)
        res[0], res[1], res[2] = start
        for i in range(3, n + 1):
            res[i] = res[i // 2]
            if i % 2:
                res[i] += 1
        return res