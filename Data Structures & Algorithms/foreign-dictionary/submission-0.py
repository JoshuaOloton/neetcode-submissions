class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return ""
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break 

        res = []
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            visiting.remove(node)
            visited.add(node)
            return True

        allChars = set()
        for word in words:
            for char in word:
                allChars.add(char)

        for char in allChars:
            if not dfs(char):
                return ""
        
        print(res)
        res = ''.join(res)
        return res[::-1]