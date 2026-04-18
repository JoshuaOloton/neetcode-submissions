class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for crs, pre in prerequisites:
            adjMap[pre].append(crs)

        visiting = set()
        visited = set()
        def dfs(crs):
            if crs in visited or adjMap[crs] == []:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for nei in adjMap[crs]:
                if not dfs(nei):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True