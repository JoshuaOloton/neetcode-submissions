class Solution:
    def countBits(self, n: int) -> List[int]:
        if not n:
            return [0]
        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 1]

        res = [0] * (n + 1)
        res[0], res[1], res[2] = [0, 1, 1]
        for i in range(3, n + 1):
            res[i] = res[i // 2]
            if i % 2:
                res[i] += 1
        return res