class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = sorted(s)
        res.reverse()

        i = len(res) - 1
        while res[i] == '0':
            i -= 1
        res[i], res[len(res) - 1] = res[len(res) - 1], res[i]
    
        return ''.join(res)
