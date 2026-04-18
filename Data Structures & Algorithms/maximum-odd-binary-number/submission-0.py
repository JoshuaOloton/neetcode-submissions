class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        map_s = Counter(s)
        no_ones = map_s.get('1')
        total = 0
        n = len(s)

        for i in range(1, no_ones):
            total += 1 << (n - i)
        total += 1
        
        res = bin(total)[2:]
        return ((n - len(res)) * '0') + res
