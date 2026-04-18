class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        no_components = 0
        visited = set()
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for adj in adjList[node]:
                dfs(adj)
            
        
        for i in range(n):
            if i not in visited:
                no_components += 1
                dfs(i)
        return no_components