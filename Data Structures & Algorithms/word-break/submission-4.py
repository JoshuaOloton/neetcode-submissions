class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i > len(s):
                return False
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            for word in wordDict:
                if word != s[i:i+len(word)]:
                    continue
                if dfs(i+len(word)):
                    return True 
            dp[i] = False     
            return False
        
        return dfs(0)