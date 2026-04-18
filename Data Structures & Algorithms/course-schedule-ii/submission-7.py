class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        visiting = [0] * numCourses
        visited = [0] * numCourses
        stack = []
        
        def dfs(node):
            if visited[node]:
                return True
            if visiting[node]:
                return False

            visiting[node] = 1

            for nei in adjList[node]:
                if not visited[nei]:
                    if not dfs(nei):
                        return False
            stack.append(node)

            visiting[node] = 0
            visited[node] = 1
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []

        return stack