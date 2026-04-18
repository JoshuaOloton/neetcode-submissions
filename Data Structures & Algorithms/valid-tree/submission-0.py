class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list) # build adjancecy list for undirected graph
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def has_cycle(node, parent):
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if has_cycle(nei, node):
                    return True
            return False

        return not has_cycle(0, -1) and len(visited) == n
        