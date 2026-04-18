class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * n
        outdegree = [0] * n
        for u, v in trust:
            indegree[v - 1] += 1
            outdegree[u - 1] += 1

        for i, out in enumerate(outdegree):
            if out == 0 and indegree[i] == n - 1:
                return i + 1
        return -1
