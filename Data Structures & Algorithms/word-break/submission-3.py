class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(seq):
            if seq != s[:len(seq)] or len(seq) > len(s):
                return False
            if len(seq) == len(s):
                return True

            if seq in dp:
                return dp[seq]

            for word in wordDict:
                if dfs(seq+word):
                    return True 
            dp[seq] = False     
            return False
        
        return dfs("")