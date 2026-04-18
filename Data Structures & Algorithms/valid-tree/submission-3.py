class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n