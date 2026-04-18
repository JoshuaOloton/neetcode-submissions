class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for crs, pre in prerequisites:
            adjMap[pre].append(crs)

        visiting = set()
        visited = set()
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in adjMap[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True