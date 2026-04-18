class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for orderIdx, c in enumerate(order):
            orderMap[c] = orderIdx
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    if orderMap[w1[j]] > orderMap[w2[j]]:
                        return False
                    break
                j += 1
            if j < len(w1) and j == len(w2): # w1(word 1 is longer)
                return False
        
        return True
