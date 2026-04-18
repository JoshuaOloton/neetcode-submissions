class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for l in range(len(s) // 2):
            r = (len(s) - 1) - l
            s[l], s[r] = s[r], s[l]
        
        