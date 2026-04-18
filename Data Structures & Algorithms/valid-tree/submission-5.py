class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        completed = set()
        visiting = set()
        adjMap = defaultdict(list)

        for u, v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)

        def dfs(node, parent):
            if node in visiting:
                return False
            if node in completed:
                return True
            
            visiting.add(node)

            for ne in adjMap[node]:
                if ne is parent:
                    continue
                if not dfs(ne, node):
                    return False
            
            visiting.remove(node)
            completed.add(node)
            return True
        
        return dfs(0, None) and len(completed) == n