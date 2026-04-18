class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)

        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
        
        return res
