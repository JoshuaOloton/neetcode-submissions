class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f'{len(s)}#{s}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while i < len(s):
            while s[j] != '#':
                j += 1
            skip = int(s[i : j])
            res.append(s[j + 1 : j + 1 + skip])
            j += (1 + skip)
            i = j
        
        return res
