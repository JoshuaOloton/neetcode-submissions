class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0 for _ in range(n + 1)]
        res = []

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            else:
                parent[pu] = pv
                if rank[pu] == rank[pv]:
                    rank[pv] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                res.append([u, v])
        
        return res[-1]