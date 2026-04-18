"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(n):
            if not n:
                return None
            if n in oldToNew:
                return oldToNew[n]
            oldToNew[n] = Node(n.val)
            for nei in n.neighbors:
                oldToNew[n].neighbors.append(dfs(nei))

            return oldToNew[n]
        
        return dfs(node)