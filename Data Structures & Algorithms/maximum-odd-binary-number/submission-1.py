class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        map_s = Counter(s)
        no_ones = map_s.get('1')
        res = ''

        for i in range(len(s) - 1):
            if no_ones > 1:
                res += '1'
            else:
                res +='0'
            no_ones -= 1
        
        res += '1'
        return res