# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []
        top = -float('inf')
        def dfs(node):
            nonlocal top
            if not node:
                return True
            
            if not dfs(node.left):
                return False
            if nodes and node.val <= top:
                return False
            top = max(top, node.val)
            nodes.append(node.val)
            print(nodes)
            if not dfs(node.right):
                return False

            return True
        
        return dfs(root)