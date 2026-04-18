class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        no_ones = 0
        for c in s:
            if c == '1':
                no_ones += 1

        res = '1' * (no_ones - 1) + '0' * (len(s) - no_ones) + '1'
        return res