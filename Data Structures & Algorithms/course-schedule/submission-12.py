class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visiting = set()
        visited = set()

        for u, v in prerequisites:
            adjList[u].append(v)
        
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
                    
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True