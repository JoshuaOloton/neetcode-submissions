class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        visiting = set()

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(course):
            if course in visiting:
                return False
            
            visiting.add(course)
            
            for pre in prereq[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True