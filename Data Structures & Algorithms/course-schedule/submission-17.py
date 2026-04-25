class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        

        visited = set()
        visiting = set()
        def dfs(node):
            if node in visiting:
                return False
            if node in visited or adj[node] == []:
                return True
            
            visiting.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True