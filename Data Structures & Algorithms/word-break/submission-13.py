class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i : i + len(w)] == w and dfs(i + len(w))):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]

        return dfs(0)