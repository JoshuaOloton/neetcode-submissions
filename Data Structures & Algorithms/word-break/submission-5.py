class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            for w in wordDict:
                if w != s[i:i+len(w)] or i+len(w) > len(s):
                    continue
                if dfs(i+len(w)):
                    return True 
            dp[i] = False     
            return False
        
        return dfs(0)