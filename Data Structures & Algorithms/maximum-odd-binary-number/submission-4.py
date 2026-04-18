class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        map_s = Counter(s)
        no_ones = map_s.get('1')
        no_zeros = len(s) - no_ones
        res = ""

        res += '1' * (no_ones - 1)
        res += '0' * no_zeros
        res += '1'

        return res