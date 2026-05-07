class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        visiting = set()

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)

            for nei in adj[node]:
                if nei != parent and not dfs(nei, node):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True

        return dfs(0, -1) and len(visited) == n
