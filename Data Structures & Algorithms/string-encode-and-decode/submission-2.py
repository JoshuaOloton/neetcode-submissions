class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s))+'#'+s)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        i, count = 0, 0
        nums, word, result = [], [], []
        while i < len(s):
            if s[i].isnumeric() and count == 0:
                nums.append(s[i])
                if s[i+1] == '#':
                    count = int(''.join(nums))
                    nums = []
                    i+=1
                    if count == 0:
                        result.append('')
            else:
                word.append(s[i])
                count -= 1
                if count == 0:
                    result.append(''.join(word))
                    word = []
            i+=1
        return result