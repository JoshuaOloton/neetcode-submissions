"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        oldToNew = {}

        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            
            newNode = Node(n.val)
            oldToNew[n] = newNode

            for ne in n.neighbors:
                newNode.neighbors.append(dfs(ne))

            return oldToNew[n]

        return dfs(node)