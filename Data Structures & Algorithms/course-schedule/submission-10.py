class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = [0] * numCourses
        completed = [0] * numCourses
        adjMap = defaultdict(list)

        for crs, pre in prerequisites:
            adjMap[crs].append(pre)

        def dfs(course):
            if visiting[course]:
                return False
            if completed[course]:
                return True
            
            visiting[course] = 1
            for pre in adjMap[course]:
                if not dfs(pre):
                    return False
                
            visiting[course] = 0
            completed[course] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True