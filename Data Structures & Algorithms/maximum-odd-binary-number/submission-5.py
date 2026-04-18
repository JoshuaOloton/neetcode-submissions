class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        map_s = Counter(s)
        no_ones = map_s.get('1')
        no_zeros = len(s) - no_ones

        res = []
        res.extend(['1'] * (no_ones - 1))
        res.extend(['0'] * no_zeros)
        res.append('1')

        return ''.join(res)