class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        def dfs(i):
            if i not in dp:
                if s[i] == "0":
                    return 0
                res = dfs(i + 1) # take one, move to next index
                if (i + 1) < len(s) and int(s[i : i + 2]) <= 26:
                    # take two, jump two index
                    res += dfs(i + 2)
                
                dp[i] = res
            return dp[i]
        
        return dfs(0)