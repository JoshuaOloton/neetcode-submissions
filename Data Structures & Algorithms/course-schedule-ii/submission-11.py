class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        indegree = [0] * numCourses
        for nodes in adjList:
            for node in nodes:
                indegree[node] += 1
        
        res = []
        q = deque()
        for n, deg in enumerate(indegree):
            if not deg:
                q.append(n)
        
        while q:
            n = q.popleft()
            res.append(n)
            for nei in adjList[n]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)

        return res[::-1] if len(res) == numCourses else []