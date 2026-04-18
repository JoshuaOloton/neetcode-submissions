class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        canComplete = set() # processed nodes without cycles
        
        preqMap = defaultdict(list)
        for crs, pre in prerequisites:
            preqMap[crs].append(pre)

        def dfs(crs):
            if crs in visited: # cycle exists
                return False
            if preqMap[crs] == [] or crs in canComplete:
                return True
                
            visited.add(crs)

            for p in preqMap[crs]:
                if not dfs(p):
                    return False
            canComplete.add(crs)

            visited.remove(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True