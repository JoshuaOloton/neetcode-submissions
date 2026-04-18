class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visiting = set()
        completed = set()

        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, parent):
            if node in visiting:
                return False
            if node in completed:
                return True
            
            visiting.add(node)

            for adj in adjList[node]:
                if adj != parent and not dfs(adj, node):
                    return False
            
            visiting.remove(node)
            completed.add(node)
            return True
        
        return dfs(0, None) and len(completed) == n
